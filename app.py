import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Premier League Predictions", layout="wide")

# Custom CSS to style the app
st.markdown("""
<style>
    .main {background-color: #f0f2f6;}
    .stButton>button {
        color: #ff4b4b;
        border-color: #ff4b4b;
        border-radius: 20px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff4b4b;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # st.image("https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png", width=200)
    st.title("Premier League Analysis")
    
    st.button("Overview")
    
    st.subheader("Predictions League")
    st.button("Enter Predictions")
    st.button("Check Latest Points")
    st.button("Leaderboards")
    st.button("League Predictions")
    st.button("Strategy")
    
    st.subheader("Fantasy Football")
    st.button("Latest Team Points")
    st.button("Fixtures / Results")
    st.button("Fixture Difficulty Rating")
    st.button("Player Stats")
    st.button("Data Visualisation")

# Main content
st.title("Premier League Predictions")

# FPL Team Section
st.subheader("View my FPL Team")
col1, col2, col3, col4, col5 = st.columns(5)
players = [
    ("B.Fernandes", "WOL (H)", "https://resources.premierleague.com/premierleague/photos/players/110x140/p141746.png"),
    ("Saka", "NFO (H)", "https://resources.premierleague.com/premierleague/photos/players/110x140/p223340.png"),
    ("Mitoma", "LUT (H)", "https://resources.premierleague.com/premierleague/photos/players/110x140/p449792.png"),
    ("Rashford", "WOL (H)", "https://resources.premierleague.com/premierleague/photos/players/110x140/p176297.png"),
    ("Foden", "BUR (A)", "https://resources.premierleague.com/premierleague/photos/players/110x140/p209244.png")
]

for i, (name, fixture, image_url) in enumerate(players):
    with [col1, col2, col3, col4, col5][i]:
        st.image(image_url, width=100)
        st.write(f"**{name}**")
        st.write(fixture)

st.button("View Team")

# Predictions League Section
st.subheader("Predictions League")
st.write("View the current standings in the predictions league.")

# Sample data for predictions
predictions_data = {
    'Home': ['Brentford', 'Everton', 'Fulham', 'Newcastle', 'Nottm Forest'],
    'Home Score': [2, 1, 1, 2, 1],
    'Away Score': [1, 1, 1, 1, 2],
    'Away': ['Chelsea', 'West Ham', 'Brighton', 'Wolves', 'Liverpool']
}
df = pd.DataFrame(predictions_data)

# Display predictions in a styled table
st.dataframe(df.style.apply(lambda x: ['background-color: #9C27B0' for i in x], axis=1))

col1, col2 = st.columns(2)
with col1:
    st.button("View Latest Points")
with col2:
    st.button("Add Predictions")