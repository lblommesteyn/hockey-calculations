# Hockey Gap Analysis Package

## Overview

The Hockey Gap Analysis package offers a sophisticated toolkit for analyzing gap control strategies in hockey. Leveraging spatial indexing, advanced analytics, and visualizations, it provides deep insights into player positioning, movement dynamics, and defensive effectiveness throughout a game.

## Key Features

### Spatial Analysis Improvements
- **Efficient Player Tracking**: Utilizes `KDTree` from `scipy.spatial` for rapid nearest-neighbor searches, optimizing the identification of the closest player to the puck and facilitating dynamic gap analysis.
- **Advanced Gap Measurement**: Incorporates calculations for optimal gap distances between players, enabling a detailed examination of defensive strategies across different zones on the ice.

### Analytics Module
- **Player Velocity and Acceleration**: Calculates player velocities and accelerations, offering insights into player dynamics and responsiveness.
- **Team and Player Efficiency**: Analyzes team velocity patterns and individual player efficiencies, providing a comprehensive view of performance and strategy.
- **Distance Covered**: Calculates the total distance covered by each player.
- **Player Speed**: Calculates the speed of each player.
- **Team Coverage Area**: Calculates the area covered by a team at each timestamp using the Convex Hull method.

### Visualization Enhancements
- **Interactive Gap Control Visualization**: Features advanced plotting capabilities, including player movement vectors and gap distances, to visually represent strategic dynamics on the ice.

### Modular and Scalable Design
- Organized into modular components for easy maintenance and scalability, allowing for the integration of new analysis methods and data sources.

## Installation

1. Clone this repository or download the package.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Import the package in your Python scripts or Jupyter notebooks:

```python
from hockey_gap_analysis import spatial_analysis, analytics, visualization
```

## Usage

The package is structured to facilitate easy access to its functionalities, divided among different modules for spatial analysis, player analytics, and visualization. Example usage can be found in the included Jupyter notebook (`ExampleUsage.ipynb`), demonstrating how to load data, perform gap control analysis, and visualize the results.

## Testing

Comprehensive unit tests are included in the `tests/` directory, ensuring the reliability and accuracy of the package's functionalities. To run the tests:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions to the Hockey Gap Analysis package are welcome. Please feel free to submit pull requests or open issues to discuss proposed changes or report bugs.

## Future Directions

- **Dynamic Zone Analysis**: Further refine the dynamic definitions of play areas based on the evolving context of the game.
- **Machine Learning Models**: Integrate predictive modeling to forecast play outcomes or player performance based on spatial and temporal data.
- **Real-Time Analysis**: Explore the feasibility of adapting the package for real-time data analysis during games.

## License

This project is licensed under the GNU General Public License.

---

\
