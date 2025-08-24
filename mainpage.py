import streamlit as st
import json
from streamlit_lottie import st_lottie
# Configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="EV Charging Station Hub", page_icon="images/idplogo.png")
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
        text-shadow: 2px 2px 4px #000000; /* Dark outline for text */
    }
    .stButton > button {
        width: 100%;
        font-size: 20px;
        padding: 15px 32px;
        border: none;
        cursor: pointer;
        color: white;
        height: 150px;
        background-color: #2E7D32;
        transition: background-color 0.3s, transform 0.2s;
        margin-bottom: 10px;
    }
    .stButton > button:nth-of-type(3) {
        background-color: #FFD700; /* Yellow color for Start Charging button */
        height: 300px;
    }
    .stButton > button:hover {
        background-color: #1B5E20;
        transform: scale(1.05);
    }
    .stButton > button:nth-of-type(3):hover {
        background-color: #FFC107; /* Darker shade of yellow on hover */
        transform: scale(1.05);
    }
    .footer {
        text-align: center;
        padding: 10px 0;
        background-color: #1f4037;
        color: white;
        margin-top: 20px;
    }
    h2 {
        font-size: 40px; /*Welcome */
        color: #55e6e1;
        font-family: "Times New Roman", Times, serif;
        text-shadow: 2px 2px 4px #000000; /* Dark outline for h2 */
    }
    p {
        font-size: 28px; /*Button Labels */
        font-family: "Times New Roman", Times, serif;
        text-shadow: 1px 1px 3px #000000; /* Dark outline for paragraphs */
    }
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# Functions
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        print(filepath)
        return json.load(f)

st.write("")
st.write("")

# Load the Lottie animation
lottie_coding = load_lottiefile("animations/homepage1.0.json") # Replace with your Lottie animation file path or URL
#/home/yz/main_code/animations/homepage1.0.json
def create_buttons(row_no):
    button_labels = ["Information ", "Summary ", "Start Charging ", "Nearby Stations ", "Help "]
    page_paths = ["pages/information.py", "pages/summary.py", "pages/scanner.py", "pages/nearby_stations.py", "pages/help.py"]
    if row_no < len(button_labels):
        if st.button(button_labels[row_no], key=f"button_{row_no}"):
            st.switch_page(page_paths[row_no])
def create_layout():
    col1, col2 = st.columns([1, 1])
    with col1:
        if lottie_coding:
            st_lottie(
                lottie_coding,
                height=330, # Increased height
                width=680, # Added width
            )
    with col2:
        col3, col4 = st.columns([1, 1])
    with col3:
        create_buttons(0)
    with col4:
        create_buttons(1)
        create_buttons(2)
    colA, colB = st.columns([1, 1])
    with colA:
        st.header("Welcome to EV Charging Station Hub")
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

# Adding Side Tab UTAR Logo

with st.sidebar:
    #Adding Company Logo at Side Tab
    st.logo(image="images/idpmainlogo.png",icon_image=r"images/idplogo.png")
    st.image("images/idpmainlogo.png")
    st.image("https://www.utar.edu.my/main2014/utar-logo.png")

# Display a footer
footer = """
    <div class="footer">
        <p>� 2024 EV Charging Station. All rights reserved.</p>
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
