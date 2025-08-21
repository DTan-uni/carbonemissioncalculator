import streamlit as st
import json
from streamlit_lottie import st_lottie
import time
import toml

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="Credit Conversion", page_icon="💳")

st.title("Converting to Carbon Credits")

def load_lottieurl(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def calculate_emission_reduction(ec, user_info, config):
    ir = 0.99

    # Get car category from user_info
    car_category = user_info['car_category']
    
    # Determine the fuel type and get parameters from config file
    if car_category in config["fossil_fuel_type"]["diesel"]["car_category"]:
        fuel_type = "diesel"
    elif car_category in config["fossil_fuel_type"]["gasoline"]["car_category"]:
        fuel_type = "gasoline"
    else:
        raise ValueError(f"Unknown car category: {car_category}")

    sfc = config["car_category"][car_category]['sfc']
    ef = config["fossil_fuel_type"][fuel_type]['ef']
    ncv = config["fossil_fuel_type"][fuel_type]['ncv']

    b_efactor = sfc * ncv * ef * ir
    baseline_emit = b_efactor * (ec / 0.188) * 10e-6  # specific electricity consumption = 0.188kWh

    # Example values for project emissions calculation (constant)
    specific_electricity_consumption = 0.188  # kWh/km
    project_ef = 0.758  # t CO2/km, assuming project emission factor (electricity)
    project_leakage = 0.0776  # leakage factor
    
    project_emit = (specific_electricity_consumption * project_ef / (1 - project_leakage)) * 10e-3
    emission_reduction = baseline_emit - project_emit
    
    return emission_reduction, baseline_emit, project_emit
    
lottie_credit_conversion = load_lottieurl("animations/credit.json")  # Make sure this file exists

if "final_level" in st.session_state:
    final_level = st.session_state.final_level
    initial_level = st.session_state.initial_level
    user_info = st.session_state.user_info
    
    # Calculate electricity consumption in kWh
    electricity_consumed = (final_level - initial_level)  # 1% equals to 1 kWh

    # Load config file
    with open("config.toml", "r", encoding="utf-8") as f:
        config = toml.load(f)
    
    # Calculate emission reduction
    emission_reduction, baseline_emit, project_emit = calculate_emission_reduction(electricity_consumed, user_info, config)

    credits = emission_reduction # 1 ton CO2e equals 1 credit
    st.session_state.credits = credits
    st.session_state.emission_reduction = emission_reduction
    st.session_state.baseline_emit = baseline_emit
    st.session_state.project_emit = project_emit
    
    # Display credit conversion animation
    if lottie_credit_conversion:
        st_lottie(lottie_credit_conversion, key="credit_animation", height=400)
    else:
        st.warning("Credit conversion animation could not be loaded.")
    
    # Simulate conversion process
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i + 1)
    
    st.success(f"Conversion complete! You've earned {credits:.3f} credits.")
    
    st.info("Redirecting to Account Details...")
    time.sleep(3)  # 3-second delay before switching
    st.switch_page("pages/charging_details.py")
else:
    st.error("No charging data found. Please start a new charging session.")
    if st.button("Return to Charging Process"):
        st.switch_page("pages/charging_process.py")

st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")