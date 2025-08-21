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
            background: linear-gradient(135deg, #1f4037, #99f2c8);
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        h1, h2, h3, h4, h5, h6, p {
            color: white;
        }
        .stButton > button {
            width: 100%;
            font-size: 24px;
            padding: 15px 32px;
            border: none;
            cursor: pointer;
            color: white;
            height: 150px; /* Default height for most buttons */
            background-color: #2E7D32; /* Dark green for all buttons */
            transition: background-color 0.3s, transform 0.2s;
        }
        .stButton > button:nth-child(3) {
            background-color: #4CAF50; /* Lighter green for the "Start Charging" button */
            height: 300px; /* Height for "Start Charging" button */
        }
        .stButton > button:hover {
            background-color: #1B5E20; /* Darker green on hover */
            transform: scale(1.05);
        }
        .stButton > button:nth-child(3):hover {
            background-color: #45a049; /* Slightly darker green for "Start Charging" on hover */
        }
        .footer {
            text-align: center;
            padding: 10px 0;
            background-color: #1f4037;
            color: white;
            margin-top: 20px;
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
    page_paths = ["pages/information.py", "pages/summary.py", "pages/scanner.py", "pages/nearby_stations.py", "pages/help.py"]
    
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
footer = """
    <div class="footer">
        <p>© 2024 EV Charging Station. All rights reserved.</p>
        <p>
            <a href="https://twitter.com" target="_blank" style="color: white; text-decoration: none; margin: 0 10px;">
                <i class="fab fa-twitter"></i> Twitter
            </a>
            <a href="https://facebook.com" target="_blank" style="color: white; text-decoration: none; margin: 0 10px;">
                <i class="fab fa-facebook-f"></i> Facebook
            </a>
            <a href="https://instagram.com" target="_blank" style="color: white; text-decoration: none; margin: 0 10px;">
                <i class="fab fa-instagram"></i> Instagram
            </a>
        </p>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)
