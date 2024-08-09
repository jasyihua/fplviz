import streamlit as st

def sidebar():
    with st.sidebar:
        st.title("FPL Data Viz")
        return st.radio("Navigate", ["Home", "Data Visualization", "Contact"])