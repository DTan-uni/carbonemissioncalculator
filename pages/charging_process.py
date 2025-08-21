import streamlit as st
import time
import random
from streamlit_lottie import st_lottie
import json

# Streamlit page configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="EV Charging Process", page_icon="🔋")

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
st.markdown("<h1 class='center-header'>EV Charging Process</h1>", unsafe_allow_html=True)

# Load the Lottie animation
def load_lottieurl(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        st.error(f"Error loading Lottie animation: {str(e)}")
        return None

# Load your Lottie animation file
lottie_charging = load_lottieurl("animations/charge1.0.json")  # Replace with your file path
if lottie_charging is None:
    st.warning("Charging animation could not be loaded. Proceeding without animation.")

# Function to simulate charging
def charge_vehicle(initial_level, target_level):
    progress = st.progress(0)
    status_text = st.empty()
    cancel_button = st.empty()
    
    if lottie_charging:
        st_lottie(lottie_charging, key="charging_animation", height=400)
    
    charging = True
    final_level = initial_level
    
    while final_level < target_level and charging:
        cancel_pressed = cancel_button.button("Stop Charging", key=f"cancel_button_{final_level}")
        if cancel_pressed:
            charging = False
            st.warning("Charging stopped.")
        else:
            final_level += 1
            progress.progress(final_level)
            status_text.text(f"Charging: {final_level}%")
            time.sleep(random.uniform(0.1, 0.5))
    
    cancel_button.empty()
    return charging, final_level

# In the main app logic
if "initial_level" in st.session_state and "target_level" in st.session_state:
    initial_level = st.session_state.initial_level
    target_level = st.session_state.target_level
    
    charging_completed, final_level = charge_vehicle(initial_level, target_level)
    
    # Save final level in session state
    st.session_state.final_level = final_level
    
    if charging_completed:
        st.success(f"Charging Complete! Your vehicle is now charged to {final_level}%.")
    else:
        st.info(f"Charging was stopped. Your vehicle is charged to {final_level}%.")
    
    final_cost = (final_level - initial_level) * 0.50
    st.write(f"Total Cost: RM {final_cost:.2f}")

    # Delay before switching pages
    time.sleep(1)
    st.switch_page("pages/charging_complete.py")
    
else:
    st.error("No charging parameters set. Please go back to the setup page.")
    if st.button("Return to Setup"):
        st.switch_page("pages/charging_setup.py")

# Add some space at the bottom
st.write("")
st.write("")

# Display a footer
st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")
