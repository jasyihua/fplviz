import streamlit as st
from pages import data_view, stats, transfers, chips

def main():
    st.set_page_config(page_title="Fantasy Premier League Analysis", layout="wide")
    st.title("Fantasy Premier League Analysis")

    # Sidebar for navigation
    page = st.sidebar.selectbox("Choose a page", ["Data View", "Stats", "Transfers", "Chips"])

    if page == "Data View":
        data_view.show()
    elif page == "Stats":
        stats.show()
    elif page == "Transfers":
        transfers.show()
    elif page == "Chips":
        chips.show()

if __name__ == "__main__":
    main()