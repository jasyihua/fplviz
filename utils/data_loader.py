import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    # Generate fake data
    np.random.seed(42)  # For reproducibility
    
    n_players = 300  # Number of players to generate
    
    data = {
        'Player': [f'Player_{i}' for i in range(1, n_players + 1)],
        'Team': np.random.choice(['ARS', 'CHE', 'LIV', 'MCI', 'MUN', 'TOT', 'LEI', 'EVE', 'WHU', 'NEW'], n_players),
        'Position': np.random.choice(['GK', 'DEF', 'MID', 'FWD'], n_players, p=[0.1, 0.3, 0.4, 0.2]),
        'Price': np.round(np.random.uniform(4.0, 14.0, n_players), 1),
        'Total_Points': np.random.randint(0, 300, n_players),
        'Minutes': np.random.randint(0, 3420, n_players),  # Max 3420 minutes in a 38-game season
        'Goals': np.random.randint(0, 30, n_players),
        'Assists': np.random.randint(0, 20, n_players),
        'Clean_Sheets': np.random.randint(0, 20, n_players),
        'Goals_Conceded': np.random.randint(0, 60, n_players),
        'Own_Goals': np.random.randint(0, 3, n_players),
        'Penalties_Saved': np.random.randint(0, 5, n_players),
        'Penalties_Missed': np.random.randint(0, 3, n_players),
        'Yellow_Cards': np.random.randint(0, 10, n_players),
        'Red_Cards': np.random.randint(0, 2, n_players),
        'Saves': np.random.randint(0, 150, n_players),
        'Bonus': np.random.randint(0, 30, n_players),
        'BPS': np.random.randint(0, 1000, n_players),
        'Influence': np.round(np.random.uniform(0, 1500, n_players), 1),
        'Creativity': np.round(np.random.uniform(0, 1500, n_players), 1),
        'Threat': np.round(np.random.uniform(0, 1500, n_players), 1),
        'ICT_Index': np.round(np.random.uniform(0, 450, n_players), 1),
    }
    
    df = pd.DataFrame(data)
    
    # Adjust data based on position
    df.loc[df['Position'] == 'GK', 'Goals'] = np.random.randint(0, 2, sum(df['Position'] == 'GK'))
    df.loc[df['Position'] == 'GK', 'Assists'] = np.random.randint(0, 5, sum(df['Position'] == 'GK'))
    df.loc[df['Position'] != 'GK', 'Saves'] = 0
    df.loc[df['Position'] != 'GK', 'Penalties_Saved'] = 0
    
    # Calculate Points Per Game
    df['Points_Per_Game'] = np.round(df['Total_Points'] / 38, 2)
    
    # Calculate Value (Points per Million)
    df['Value'] = np.round(df['Total_Points'] / df['Price'], 1)
    
    return df

# Example usage
if __name__ == "__main__":
    data = load_data()
    print(data.head())
    print(data.describe())