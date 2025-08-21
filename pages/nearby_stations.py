import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration with title and icon
st.set_page_config(
    page_title="Find Nearby Stations",
    page_icon="📍",  # You can use any emoji or URL to an image
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit decoration bar and change the background color of elements with class 'st-at'
hide_decoration_bar_style = """
    <style>
        header {visibility: hidden;}
        .st-at {
            background-color: rgb(120, 254, 113);
        }
    </style>
"""
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

st.header("Find Nearby Stations 📍")
st.write("Map and list of nearby stations will be displayed here.")
# Defining Latitude and Longitude
locate_map = pd.DataFrame(
    np.random.randn(50, 2) / [10, 10]
    + [3.1390, 101.6869],  # Kuala Lumpur coordinates
    columns=["latitude", "longitude"],
)
# Map Function
st.map(locate_map)

if st.button("Back to Homepage", type="primary"):
    st.switch_page("mainpage.py")

    