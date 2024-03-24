import matplotlib.pyplot as plt
import numpy as np

def visualize_gap_control(gap_control_df, player_data, puck_data, timeStamp):
    """
    Visualize player positions, puck position, and gap control for a given timestamp.
    
    Parameters:
    - gap_control_df: DataFrame containing gap control measurements.
    - player_data: DataFrame with player positions and velocities.
    - puck_data: DataFrame with puck positions.
    - timeStamp: Specific timestamp to visualize.
    """
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Filter data for the given timestamp
    players_at_timestamp = player_data[player_data['timeStamp'] == timeStamp]
    puck_position = puck_data[puck_data['timeStamp'] == timeStamp].iloc[0]
    
    # Plot players by team
    for team in players_at_timestamp['team'].unique():
        team_players = players_at_timestamp[players_at_timestamp['team'] == team]
        ax.scatter(team_players['position_x'], team_players['position_y'], label=f'Team {team}', s=100)
        
        # Optionally, add velocity vectors for players
        for _, player in team_players.iterrows():
            ax.arrow(player['position_x'], player['position_y'], 
                     player['velocity_x']*10, player['velocity_y']*10, 
                     head_width=1, head_length=1, fc='k', ec='k')
    
    # Plot puck position
    ax.scatter(puck_position['position_x'], puck_position['position_y'], color='black', label='Puck', s=100, zorder=5)
    
    # Highlight the player with the puck and closest opponent if available in gap_control_df
    if not gap_control_df[gap_control_df['timeStamp'] == timeStamp].empty:
        gap_info = gap_control_df[gap_control_df['timeStamp'] == timeStamp].iloc[0]
        player_with_puck = players_at_timestamp[players_at_timestamp['entityId'] == gap_info['player_with_puck']].iloc[0]
        closest_opponent = players_at_timestamp[players_at_timestamp['entityId'] == gap_info['closest_opponent']].iloc[0]
        
        # Draw a line representing the gap
        ax.plot([player_with_puck['position_x'], closest_opponent['position_x']], 
                [player_with_puck['position_y'], closest_opponent['position_y']], 
                'r--', label='Gap')
        
        # Highlight player with puck and closest opponent
        ax.scatter(player_with_puck['position_x'], player_with_puck['position_y'], s=200, facecolors='none', edgecolors='r', label='Player with Puck', zorder=10)
        ax.scatter(closest_opponent['position_x'], closest_opponent['position_y'], s=200, facecolors='none', edgecolors='blue', label='Closest Opponent', zorder=10)
    
    ax.set_xlabel('Position X')
    ax.set_ylabel('Position Y')
    ax.set_title(f'Gap Control Visualization at Timestamp {timeStamp}')
    ax.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()
