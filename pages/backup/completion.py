import streamlit as st
import json
from streamlit_lottie import st_lottie
import time

# Streamlit page configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="Charging Complete", page_icon="✅")

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
st.markdown("<h1 class='center-header'>Charging Complete!</h1>", unsafe_allow_html=True)

# Load the Lottie animations
def load_lottieurl(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        st.error(f"Error loading Lottie animation: {str(e)}")
        return None

# Load your Lottie animations
lottie_credit_conversion = load_lottieurl("payment.json")  # Replace with your file path

if lottie_credit_conversion is None:
    st.warning("Credit conversion animation could not be loaded. Proceeding without animation.")

# Get final charge level and initial charge level from session state
if "initial_level" in st.session_state and "final_level" in st.session_state:
    initial_level = st.session_state.initial_level
    final_level = st.session_state.final_level
    
    # Display the final charge level
    st.subheader(f"Your vehicle is charged to {final_level}%.")
    
    # Display some important details
    st.write("Important Details:")
    st.write(f"Charge Level: {final_level}%")
    
    # Convert charge to credits (dummy calculation for demo purposes)
    credits = final_level * 0.1
    st.write(f"Converted to Credits: {credits:.2f} credits")

    # Calculate the total cost
    cost_per_percent = 0.50  # Example cost per percent
    total_cost = (final_level - initial_level) * cost_per_percent
    st.write(f"Total Cost: RM {total_cost:.2f}")

    # Display payment method and amount paid (auto payment for demo)
    payment_method = "Credit Card"  # Preset method of payment
    st.write(f"Payment Method: {payment_method}")
    st.write(f"Amount Paid: RM {total_cost:.2f}")

    # Display credit conversion animation
    if lottie_credit_conversion:
        st_lottie(lottie_credit_conversion, key="credit_animation", height=400)
        
    # Optional: Add a delay before showing the completion message
    time.sleep(3)
    
    st.success(f"Conversion complete! You now have {credits:.2f} credits.")
    
    # Finish and return to home
    if st.button("Finish and Return to Home"):
        st.session_state.clear()
        st.switch_page("main.py")
else:
    st.error("No final charge level found. Please go back to the charging process.")
    if st.button("Return to Charging Process"):
        st.switch_page("pages/charging_process.py")

# Add some space at the bottom
st.write("")
st.write("")

# Display a footer
st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")
