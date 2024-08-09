import streamlit as st
import pandas as pd
from utils.data_loader import load_player_data

def show():
    st.header("Player Data")
    
    # Load data
    df = load_player_data()
    
    # Create tabs
    tabs = st.tabs(["Overview", "FWD", "MID", "DEF", "GK", "Bench"])
    
    with tabs[0]:
        st.subheader("Overview")
        st.dataframe(df)
    
    positions = ["FWD", "MID", "DEF", "GK"]
    for i, pos in enumerate(positions, start=1):
        with tabs[i]:
            st.subheader(pos)
            st.dataframe(df[df['position'] == pos])
    
    with tabs[5]:
        st.subheader("Bench")
        st.dataframe(df[df['is_bench'] == True])