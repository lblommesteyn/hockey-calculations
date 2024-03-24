import pandas as pd

def load_player_data(filepath):
    """Load player data from a given filepath."""
    return pd.read_csv(filepath)

def load_puck_data(filepath):
    """Load puck data from a given filepath."""
    return pd.read_csv(filepath)
