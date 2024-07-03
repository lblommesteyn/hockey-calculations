import unittest
import pandas as pd
from hockey_gap_analysis.spatial_analysis import calculate_2d_distance, create_spatial_index
from hockey_gap_analysis.analytics import calculate_velocity, calculate_acceleration, calculate_distance_covered, calculate_speed, team_velocity

class TestSpatialAnalysisFunctions(unittest.TestCase):

    def test_calculate_2d_distance(self):
        # Test the distance calculation function
        point1 = (0, 0)
        point2 = (3, 4)
        expected_distance = 5
        calculated_distance = calculate_2d_distance(point1, point2)
        self.assertEqual(calculated_distance, expected_distance)

    def test_create_spatial_index(self):
        # Test the spatial index creation with a simple dataset
        player_data = {
            'entityId': [1, 2, 3],
            'team': ['A', 'A', 'B'],
            'position_x': [1, 2, 3],
            'position_y': [1, 2, 3],
            'timeStamp': [1, 1, 1]
        }
        # Convert to DataFrame if your function expects one
        player_data_df = pd.DataFrame(player_data)
        spatial_index = create_spatial_index(player_data_df)
        # Assert non-empty result, more specific tests can be added
        self.assertTrue(spatial_index)

class TestAnalyticsFunctions(unittest.TestCase):

    def test_calculate_velocity(self):
        # Test velocity calculation with a simple dataset
        player_data = {
            'entityId': [1, 1],
            'position_x': [0, 10],
            'position_y': [0, 0],
            'timeStamp': [1, 2]
        }
        # Convert to DataFrame if your function expects one
        player_data_df = pd.DataFrame(player_data)
        player_data_df_with_velocity = calculate_velocity(player_data_df)
        expected_velocity_x = [10.0]  # Assuming one unit of time between timestamps
        calculated_velocity_x = player_data_df_with_velocity['velocity_x'].tolist()[1:]  # Skip the first NaN value
        self.assertEqual(calculated_velocity_x, expected_velocity_x)

    def test_calculate_acceleration(self):
        # Test acceleration calculation with a simple dataset
        player_data = {
            'entityId': [1, 1],
            'velocity_x': [0, 10],
            'velocity_y': [0, 0],
            'timeStamp': [1, 2]
        }
        # Convert to DataFrame if your function expects one
        player_data_df = pd.DataFrame(player_data)
        player_data_df_with_acceleration = calculate_acceleration(player_data_df)
        expected_acceleration_x = [10.0]  # Assuming one unit of time between timestamps
        calculated_acceleration_x = player_data_df_with_acceleration['acceleration_x'].tolist()[1:]  # Skip the first NaN value
        self.assertEqual(calculated_acceleration_x, expected_acceleration_x)

    def test_calculate_distance_covered(self):
        # Test distance covered calculation with a simple dataset
        player_data = {
            'entityId': [1, 1, 1],
            'position_x': [0, 3, 6],
            'position_y': [0, 4, 8],
            'timeStamp': [1, 2, 3]
        }
        # Convert to DataFrame if your function expects one
        player_data_df = pd.DataFrame(player_data)
        distance_covered_df = calculate_distance_covered(player_data_df)
        expected_distance_covered = [10.0]  # 5 units between each point, total 10 units
        calculated_distance_covered = distance_covered_df['distance_covered'].tolist()
        self.assertEqual(calculated_distance_covered, expected_distance_covered)

    def test_calculate_speed(self):
        # Test speed calculation with a simple dataset
        player_data = {
            'entityId': [1, 1],
            'velocity_x': [3, 4],
            'velocity_y': [4, 3],
            'timeStamp': [1, 2]
        }
        # Convert to DataFrame if your function expects one
        player_data_df = pd.DataFrame(player_data)
        player_data_df_with_speed = calculate_speed(player_data_df)
        expected_speed = [5.0, 5.0]  # Speed is sqrt(3^2 + 4^2) = 5
        calculated_speed = player_data_df_with_speed['speed'].tolist()
        self.assertEqual(calculated_speed, expected_speed)

    def test_team_velocity(self):
        # Test team velocity calculation with a simple dataset
        player_data = {
            'entityId': [1, 2, 3],
            'team': [1, 1, 2],
            'velocity_x': [1, 2, 3],
            'velocity_y': [1, 2, 3],
            'timeStamp': [1, 1, 1]
        }
        # Convert to DataFrame if your function expects one
        player_data_df = pd.DataFrame(player_data)
        team_velocity_df = team_velocity(player_data_df, team_id=1)
        expected_avg_velocity_x = [1.5]  # Average of 1 and 2