import streamlit as st

def show():
    st.header("Chips")
    
    chips = ["Wildcard", "Benchboost", "Triple Captain", "Free Hit"]
    
    for chip in chips:
        st.subheader(chip)
        # Add your logic here for each chip strategy