import pandas as pd

def calculate_xg(last_n_games=5):
    # Replace this with your actual xG calculation logic
    # This is just a placeholder
    return pd.DataFrame({
        'name': ['Player 1', 'Player 2', 'Player 3'],
        'xG': [2.5, 1.8, 0.3]
    })

def compare_xg_actual(last_n_games=30):
    # Replace this with your actual comparison logic
    # This is just a placeholder
    return pd.DataFrame({
        'name': ['Player 1', 'Player 2', 'Player 3'],
        'xG': [10.0, 8.0, 1.5],
        'actual_goals': [12, 6, 2],
        'difference': [2.0, -2.0, 0.5]
    })