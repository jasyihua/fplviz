import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

def show():
    st.title("FPL Data Visualization")
    
    data = load_data()
    
    st.header("Player Value (Points per Million) vs Total Points")
    fig = px.scatter(data, x='Total_Points', y='Value', color='Position', 
                     hover_name='Player', hover_data=['Team', 'Price'],
                     labels={'Total_Points': 'Total Points', 'Value': 'Value (Points per Million)'},
                     title='Player Value vs Total Points')
    st.plotly_chart(fig)

    st.header("Top 20 Players by Total Points")
    top_20 = data.nlargest(20, 'Total_Points')
    fig = px.bar(top_20, x='Player', y='Total_Points', color='Team',
                 hover_data=['Position', 'Price'],
                 labels={'Total_Points': 'Total Points'},
                 title='Top 20 Players by Total Points')
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig)

    st.header("Goals Distribution by Position")
    fig = px.box(data, x='Position', y='Goals', points="all",
                 labels={'Goals': 'Number of Goals'},
                 title='Goals Distribution by Position')
    st.plotly_chart(fig)

    st.header("Raw Data")
    st.dataframe(data)

if __name__ == "__main__":
    show()