import pandas as pd

def load_player_data():
    # Replace this with your actual data loading logic
    # This is just a placeholder
    return pd.DataFrame({
        'name': ['Player 1', 'Player 2', 'Player 3'],
        'position': ['FWD', 'MID', 'DEF'],
        'price': [10.0, 8.5, 6.0],
        'points': [50, 45, 30],
        'is_bench': [False, False, True]
    })