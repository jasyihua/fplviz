import streamlit as st
from pages import home, data_visualization, contact
from components.sidebar import sidebar

def main():
    st.set_page_config(page_title="FPL Data Viz", page_icon="⚽", layout="wide")
    
    page = sidebar()

    if page == "Home":
        home.show()
    elif page == "Data Visualization":
        data_visualization.show()
    elif page == "Contact":
        contact.show()

if __name__ == "__main__":
    main()