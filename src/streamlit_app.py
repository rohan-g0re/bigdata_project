import streamlit as st
from src.tabs.engagement_tab.ui import render_engagement_tab
from src.tabs.game_tab.ui import render_game_info_tab

def main():
    """Main function to run the Streamlit app"""
    st.set_page_config(page_title="Steam Reviews Analysis", layout="wide")
    
    st.title("Steam Game Reviews Analysis")
    
    # Create tabs
    tab1, tab2 = st.tabs(["Engagement", "Game Info"])
    
    with tab1:
        render_engagement_tab()
    
    with tab2:
        render_game_info_tab()

if __name__ == "__main__":
    main() 