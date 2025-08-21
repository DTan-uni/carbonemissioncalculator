import streamlit as st
import json
from streamlit_lottie import st_lottie

# Configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="EV Charging Station Hub", page_icon="⚡")

# Custom CSS for dark background and styling
style = """
    <style>
        .row-widget.stButton {text-align: center;}
        header {visibility: hidden;}
        .st-at {
            background-color: rgb(120, 254, 113);
        }
        .stApp {
            background-color: #121212;
            color: white;
        }
        h1, h2, h3, h4, h5, h6, p {
            color: white;
        }
    </style>
"""
st.markdown(style, unsafe_allow_html=True)

# Functions
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load the Lottie animation
lottie_coding = load_lottiefile("homepage_transparent.json")  # Replace with your Lottie animation file path or URL

def create_buttons(row_no):
    button_labels = ["Information 📄", "Summary 🔗", "Start Charging 🚗", "Find Nearby Stations 📍", "Help ❓"]
    page_paths = ["pages/information1.py", "pages/summary.py", "pages/scanner.py", "pages/nearby_stations.py", "pages/help.py"]
    
    button_style = """
    <style>
    div.stButton > button {
        width: 100%;
        font-size: 24px;
        padding: 15px 32px;
        border: none;
        cursor: pointer;
        color: white;
        height: 150px; /* Default height for most buttons */
        background-color: #2E7D32; /* Dark green for all buttons */
        transition: background-color 0.3s;
    }
    div.stButton > button:nth-child(3) {
        background-color: #4CAF50; /* Lighter green for the "Start Charging" button */
        height: 300px; /* Height for "Start Charging" button */
    }
    div.stButton > button:hover {
        background-color: #1B5E20; /* Darker green on hover */
    }
    div.stButton > button:nth-child(3):hover {
        background-color: #45a049; /* Slightly darker green for "Start Charging" on hover */
    }
    </style>
    """

    st.markdown(button_style, unsafe_allow_html=True)
    if row_no < len(button_labels):
        if st.button(button_labels[row_no], key=f"button_{row_no}"):
            st.switch_page(page_paths[row_no])

def create_layout():
    col1, col2 = st.columns([1, 1])
    with col1:
        if lottie_coding:
            st_lottie(lottie_coding, height=350)
            
    with col2:
        col3, col4 = st.columns([1, 1])
        with col3:
            create_buttons(0)
        with col4:
            create_buttons(1)
            
        create_buttons(2)
        
    colA, colB = st.columns([1, 1])
    with colA:
        st.header("Welcome to the EV Charging Station Hub")
        st.write("Please select an option to proceed.")
        
    with colB:
        colC, colD = st.columns([1, 1])
        with colC:
            create_buttons(3)  
        with colD:
            create_buttons(4)  
            
create_layout()

# Add some space at the bottom
st.write("")
st.write("")

# Display a footer
st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")