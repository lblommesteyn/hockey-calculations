import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from hockey_gap_analysis.analytics import calculate_velocity, calculate_acceleration, team_velocity
from hockey_gap_analysis.data_loading import load_player_data, load_puck_data
from hockey_gap_analysis.preprocessing import clean_data
from hockey_gap_analysis.spatial_analysis import (
    create_spatial_index, dynamic_gap_control_analysis, dynamic_gap_measurement
)
from hockey_gap_analysis.visualization import visualize_gap_control

def main():
    # Load your data
    player_data = load_player_data('path_to_player_data.csv')
    puck_data = load_puck_data('path_to_puck_data.csv')
    gap_control_df = pd.read_csv('path_to_gap_control_data.csv')
    
    # Preprocess data
    player_data = clean_data(player_data)
    puck_data = clean_data(puck_data)
    
    # Perform calculations
    player_data = calculate_velocity(player_data)
    player_data = calculate_acceleration(player_data)
    team_avg_velocity = team_velocity(player_data, team_id=1)
    
    # Create spatial index for player positions
    spatial_index = create_spatial_index(player_data)
    
    # Perform dynamic gap control analysis
    gap_control_data = dynamic_gap_control_analysis(player_data, puck_data)
    
    # Measure dynamic gaps
    gap_measurements = dynamic_gap_measurement(player_data, puck_data, spatial_index)
    
    # Visualize
    visualize_gap_control(gap_control_df, player_data, puck_data, timeStamp=1234567890)
    
    # Save or display results as needed
    player_data.to_csv('updated_player_data.csv', index=False)
    team_avg_velocity.to_csv('team_avg_velocity.csv', index=False)
    gap_control_data.to_csv('gap_control_data.csv', index=False)
    gap_measurements.to_csv('gap_measurements.csv', index=False)

if __name__ == "__main__":
    main()