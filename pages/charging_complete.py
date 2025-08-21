import streamlit as st
from streamlit_lottie import st_lottie
import time
import json

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="Charging Complete", page_icon="✅")

st.title("Charging Complete!")

def load_lottieurl(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_credit_conversion = load_lottieurl("animations/charge_complete.json")  # Make sure this file exists

if "initial_level" in st.session_state and "final_level" in st.session_state:
    initial_level = st.session_state.initial_level
    final_level = st.session_state.final_level
    
    st.subheader(f"Your vehicle is charged from {initial_level}% to {final_level}%.")
       
    # Display credit conversion animation
    if lottie_credit_conversion:
        st_lottie(lottie_credit_conversion, key="credit_animation", height=400)
    else:
        st.warning("Credit conversion animation could not be loaded.")

    time.sleep(2)  # Simulate a short delay
    
    # Center the button and make it bigger
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Convert to Carbon Credits", key="convert_button", use_container_width=True):
            st.switch_page("pages/credit_conversion.py")

else:
    st.error("No charging data found. Please start a new charging session.")
    if st.button("Return to Charging Process"):
        st.switch_page("pages/charging_process.py")

st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")