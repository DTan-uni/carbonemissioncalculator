import streamlit as st
import time
import random
from streamlit_lottie import st_lottie

# Streamlit page configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="EV Charging Station", page_icon="🔋")

# Custom CSS to style the header and center-align it
style = """
    <style>
        .row-widget.stButton {text-align: center;}
        header {visibility: hidden;}
        .center-header {text-align: center; font-size: 2em;}
    </style>
"""
st.markdown(style, unsafe_allow_html=True)

# Center-aligned header
st.markdown("<h1 class='center-header'>EV Charging Station Setup</h1>", unsafe_allow_html=True)

# Initialize session state
if "charging_complete" not in st.session_state:
    st.session_state.charging_complete = False

# Function to calculate estimated time and cost
def calculate_estimates(initial_level, target_level):
    charge_difference = target_level - initial_level
    estimated_time = charge_difference  # 1 minute per 1%
    estimated_cost = charge_difference * 0.50  # RM0.50 per 1%
    return estimated_time, estimated_cost

# Main app logic
if "user_info" in st.session_state and "qr_result" in st.session_state:
    user_info = st.session_state.user_info
    qr_data = st.session_state.qr_result
    
    st.write(f"Welcome, {user_info.get('username', 'User')}!")
    st.write(f"Vehicle: {user_info.get('car_model', 'Unknown Model')}")
    
    initial_battery_level = qr_data.get("battery_level", 0)
    st.write(f"Initial Battery Level: {initial_battery_level}%")
    
    target_level = st.slider("Select target battery level", 
                             min_value=initial_battery_level, 
                             max_value=100, 
                             value=min(initial_battery_level + 20, 100))
    
    estimated_time, estimated_cost = calculate_estimates(initial_battery_level, target_level)
    
    st.write(f"Estimated Charging Time: {estimated_time} minutes")
    st.write(f"Estimated Charging Cost: RM {estimated_cost:.2f} (Auto-linked to your preset payment method)")
    
    if st.button("Start Charging"):
        st.session_state.initial_level = initial_battery_level
        st.session_state.target_level = target_level
        st.switch_page("pages/charging_process.py")

else:
    st.error("No vehicle information available. Please scan your QR code first.")
    if st.button("Return to Home"):
        st.switch_page("mainpage.py")

# Add some space at the bottom
st.write("")
st.write("")

# Display a footer
st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")