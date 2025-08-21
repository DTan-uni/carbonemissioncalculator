import streamlit as st
import pandas as pd
from camera_input_live import camera_input_live  # Custom camera input module
from pyzbar.pyzbar import decode
from io import BytesIO
from PIL import Image
import json
import time
from streamlit_lottie import st_lottie
from firebase_mode.firebase_factory import initialize_db  # Custom Firebase initialization module

# Streamlit page configuration
st.set_page_config(layout="centered", initial_sidebar_state="collapsed", page_title="EV Charging Station Hub", page_icon="⚡")

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
st.markdown("<h1 class='center-header'>Please Scan Your Vehicle QR Code</h1>", unsafe_allow_html=True)

# Initialize session state
if "qr_result" not in st.session_state:
    st.session_state["qr_result"] = None
if "user_info" not in st.session_state:
    st.session_state["user_info"] = None

# Cached function to get user info from Firebase
@st.cache_data(ttl=30)
def get_all_user_info():
    db = initialize_db()
    return db.reference("User_Info").get()

# Function to display wrong input message and options

def wrong_input():
    if lottie_coding_false:
        st_lottie(lottie_coding_false, height=450)
    st.error("UUID NOT FOUND!")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button('Retry'):
            st.session_state["qr_result"] = None
            st.rerun()

    with col2:
        if st.button('Back to Homepage'):
            st.session_state["qr_result"] = None
            st.switch_page("mainpage.py")

def vehicle_data():
    st.session_state["user_info"] = user_info
    st.success("UUID SUCCESSFULLY FOUND!")
    st.write(f"Battery Level: {st.session_state['user_info']['battery_level']}%")
    df = pd.DataFrame([st.session_state["user_info"]]).reset_index(drop=True)
    time.sleep(3)

def correct_input(): 
    if lottie_coding_true:
        st_lottie(lottie_coding_true, height=450)
    vehicle_data()
    st.session_state["page"] = "initialize"
    
# Function to load Lottie animation from file or URL
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load the Lottie animation
lottie_coding_true = load_lottiefile("animations/tick.json")  # Replace with your Lottie animation file path or URL
lottie_coding_false = load_lottiefile("animations/cross.json")

if st.session_state["qr_result"] is None:
    col = st.columns([0.5, 2, 0.5])
    with col[1]:
        image = camera_input_live(
            show_controls=False,
            debounce=200,
        )
        if image:
            decocdeQR = decode(Image.open(BytesIO(image.read())).convert("RGB"))
            try:
                result = decocdeQR[0].data.decode("ascii")
                st.write("Raw QR code data:", result)  # Debug print
                try:
                    qr_data = json.loads(result)
                    st.session_state["qr_result"] = qr_data
                    st.write("Parsed QR data:", qr_data)  # Debug print
                except json.JSONDecodeError as e:
                    st.error(f"Invalid QR code format: {str(e)}")
                except Exception as e:
                    st.error(f"Error parsing QR code: {str(e)}")
            except IndexError:
                st.image(image)
                st.error("No QR code detected")
            except Exception as e:
                st.error(f"Error decoding QR code: {str(e)}")

# Display user information if QR code is scanned successfully
if st.session_state["qr_result"]:
    try:
        uuid = st.session_state["qr_result"]["uuid"]
        battery_level = st.session_state["qr_result"].get("battery_level")
        user_info = get_all_user_info().get(uuid)
        if user_info is None:
            wrong_input()
        else:
            st.session_state["user_info"] = user_info
            if battery_level is not None:
                st.session_state["user_info"]["battery_level"] = battery_level
            correct_input()
    except KeyError as e:
        st.error(f"Missing expected key in QR data: {str(e)}")
    except Exception as e:
        st.error(f"Error processing user info: {str(e)}")
        
if st.session_state.get("page") == "initialize":
    st.switch_page("pages/initialize.py")
    
# Add some space at the bottom
st.write("")
st.write("")

# Display a footer
st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")