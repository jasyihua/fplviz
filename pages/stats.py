import streamlit as st
from utils.calculations import calculate_xg, compare_xg_actual

def show():
    st.header("Stats")
    
    st.subheader("Expected Goals (xG) - Last 5 Games")
    xg_df = calculate_xg(last_n_games=5)
    st.dataframe(xg_df)
    
    st.subheader("Clinical/Underperformers (xG vs Actual Goals) - Last 30 Games")
    comparison_df = compare_xg_actual(last_n_games=30)
    st.dataframe(comparison_df)