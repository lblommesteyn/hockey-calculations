import numpy as np
import pandas as pd
from scipy.spatial import KDTree

def calculate_2d_distance(point1, point2):
    """
    Calculate 2D distance between two points.
    """
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def create_spatial_index(player_data):
    """
    Create a spatial index (KDTree) for player positions.
    """
    spatial_index = {}
    for time_stamp in player_data['timeStamp'].unique():
        current_players = player_data[player_data['timeStamp'] == time_stamp]
        positions = current_players[['position_x', 'position_y']].values
        tree = KDTree(positions)
        spatial_index[time_stamp] = (tree, current_players)
    return spatial_index

def calculate_optimal_gap(player_data, puck_data):
    """
    Calculate the optimal gap based on player and puck positions, considering defensive strategies.
    This function will identify the defensemen and calculate the gap between them and the nearest opposing forward, aiming for an optimal gap.
    """
    optimal_gaps = []
    for time_stamp in sorted(player_data['timeStamp'].unique()):
        current_players = player_data[player_data['timeStamp'] == time_stamp]
        puck_position = puck_data[puck_data['timeStamp'] == time_stamp][['position_x', 'position_y']].iloc[0].values
        
        # Identifying defensemen and forwards
        defensemen = current_players[current_players['position'] == 'D']
        forwards = current_players[current_players['position'] == 'F']
        
        # Calculate gap for each defenseman to the nearest forward
        for _, defenseman in defensemen.iterrows():
            tree = KDTree(forwards[['position_x', 'position_y']])
            distance, index = tree.query([defenseman['position_x'], defenseman['position_y']])
            
            optimal_gaps.append({
                'timeStamp': time_stamp,
                'defenseman_id': defenseman['entityId'],
                'optimal_gap': distance,
                'puck_distance': calculate_2d_distance([defenseman['position_x'], defenseman['position_y']], puck_position)
            })
    
    return pd.DataFrame(optimal_gaps)

def dynamic_gap_control_analysis(player_data, puck_data):
    """
    Perform a dynamic gap control analysis to assess how effectively defensemen manage the gap over time, especially in relation to the puck's position.
    This includes identifying moments when the gap is too wide or too narrow and suggesting adjustments.
    """
    gap_control_data = calculate_optimal_gap(player_data, puck_data)
    
    # Analyze gap trends and suggest adjustments
    gap_control_data['gap_status'] = np.select(
        [
            gap_control_data['optimal_gap'] < 5,  # idk what the threshhold values should be - maybe should be relative to speed
            gap_control_data['optimal_gap'] > 15
        ], 
        [
            'Too Narrow', 
            'Too Wide'
        ], 
        default='Optimal'
    )
    
    return gap_control_data

def find_closest_player_to_puck_optimized(puck_position, spatial_index, players):
    """
    Find the closest player to the puck using the spatial index.
    """
    tree, players = spatial_index
    _, index = tree.query(puck_position)
    closest_player_id = players.iloc[index]['entityId']
    return closest_player_id

def find_closest_opponent(player_with_puck_id, player_data, puck_position, time_stamp):
    """
    Find the closest opponent to the puck carrier.
    """
    # Filter out the player with the puck and get opponent team players
    player_with_puck_team = player_data[player_data['entityId'] == player_with_puck_id]['team'].iloc[0]
    opponents = player_data[(player_data['timeStamp'] == time_stamp) & (player_data['team'] != player_with_puck_team)]

    if opponents.empty:
        return None

    positions = opponents[['position_x', 'position_y']].values
    puck_position = puck_position.values.flatten()
    tree = KDTree(positions)
    _, index = tree.query(puck_position)
    closest_opponent_id = opponents.iloc[index]['entityId']
    return closest_opponent_id

def dynamic_gap_measurement(player_data, puck_data, spatial_index):
    """
    Measure dynamic gaps between the puck carrier and closest opponent over time.
    """
    gap_measurements = []
    for time_stamp in sorted(puck_data['timeStamp'].unique()):
        puck_position = puck_data.loc[puck_data['timeStamp'] == time_stamp, ['position_x', 'position_y']].iloc[0]
        tree, current_players = spatial_index[time_stamp]
        player_with_puck_id = find_closest_player_to_puck_optimized((puck_position['position_x'], puck_position['position_y']), (tree, current_players), current_players)
        closest_opponent_id = find_closest_opponent(player_with_puck_id, player_data, puck_position, time_stamp)
        
        if closest_opponent_id is not None:
            player_with_puck = player_data[player_data['entityId'] == player_with_puck_id]
            closest_opponent = player_data[player_data['entityId'] == closest_opponent_id]
            
            gap_distance = calculate_2d_distance(
                [puck_position['position_x'], puck_position['position_y']], 
                [closest_opponent['position_x'].iloc[0], closest_opponent['position_y'].iloc[0]]
            )
            velocity_difference = np.linalg.norm(
                player_with_puck[['velocity_x', 'velocity_y']].values[0] - closest_opponent[['velocity_x', 'velocity_y']].values[0]
            )
            
            gap_measurements.append({
                'timeStamp': time_stamp,
                'gap_distance': gap_distance,
                'velocity_difference': velocity_difference
            })
    
    return pd.DataFrame(gap_measurements)
