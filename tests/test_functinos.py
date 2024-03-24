import unittest
from hockey_gap_analysis.spatial_analysis import calculate_2d_distance, create_spatial_index
from hockey_gap_analysis.analytics import calculate_velocity
# Import other functions you wish to test

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

# Add more test classes as needed for other modules

if __name__ == '__main__':
    unittest.main()

# to run unit tests "python -m unittest tests/test_functions.py"
