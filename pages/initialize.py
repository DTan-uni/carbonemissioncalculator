import streamlit as st
import pandas as pd
from PIL import Image
import time
import plotly.graph_objects as go

# Configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="Vehicle Details", page_icon="👤")

# Helper function to create donut chart with reduced size
def create_donut_chart(title, value, max_value, chart_width=100, chart_height=100):
    fig = go.Figure(data=[go.Pie(
        values=[value, max_value - value],
        hole=0.6,
        marker_colors=['orange', 'lightgray'],
        textinfo='none'
    )])
    fig.update_layout(
        title=title,
        showlegend=False,
        margin=dict(t=0, b=0, l=0, r=0),
        annotations=[dict(text=f"{value:.1f}", x=0.5, y=0.5, font_size=16, showarrow=False)],  # Adjust font size
        width=chart_width,  # Adjust width of the chart
        height=chart_height  # Adjust height of the chart
    )
    return fig

# Function to capitalize and remove underscores
def format_text(text):
    words = text.split('_')
    for i, word in enumerate(words):
        if word.lower() == 'suv':
            words[i] = 'SUV'
        else:
            words[i] = word.capitalize()
    return ' '.join(words)

# Ensure this script only runs when the session state "page" is "initialize"
if st.session_state.get("page") != "initialize":
    st.stop()

# Access user_info from session state
user_info = st.session_state.get("user_info")

if user_info:
    st.title("Vehicle Information")
    
    # Warning message about personal information
    st.warning("The following information is sensitive and personal. Please ensure you are authorized to view this data.")

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("General Information")
        username = user_info.get("username", "Unknown")
        phone_no = user_info.get("phone_number", "Unknown")
        category = user_info.get("car_category", "Unknown")
        car_category = format_text(user_info.get("car_category", "Unknown"))
        car_model = user_info.get("car_model", "Unknown")
        
        st.write(f"Username       : **{username}**")
        st.write(f"Phone Number   : **{phone_no}**")
        st.write(f"Car Model      : **{car_model}**")
        st.write(f"Car Category   : **{car_category}**")
        payment_methods = ["Credit Card", "Debit Card", "PayPal", "Google Pay", "Apple Pay"]
        selected_method = st.selectbox("Payment Method", payment_methods)
        st.write("Last Charge Date: **17/7/2024**")
        
        user_info["payment_method"] = selected_method

        # Convert user_info to DataFrame and display it
        df = pd.DataFrame([user_info]).reset_index(drop=True)
        #st.dataframe(df)

        # Performance metrics section below vehicle image
        st.subheader("Performance Metrics")
                
        #Performance Metrics
        acceleration = float(user_info.get("acceleration", "Unknown"))
        top_speed = float(user_info.get("top_speed", "Unknown"))
        range_km = float(user_info.get("range", "Unknown"))
        
        colA, colB, colC = st.columns([1, 1, 1])
        
        # Display donut charts in a row
        with colA:
            st.write(f"**Acceleration:** {acceleration} seconds (0-100 km/h)")
            fig1 = create_donut_chart("Acceleration (s)", acceleration, 30, chart_height=200, chart_width=10)
            st.plotly_chart(fig1, use_container_width=False)

        with colB:
            st.write(f"**Top Speed:** {top_speed} km/h")
            st.write(" ")
            fig2 = create_donut_chart("Top Speed (km/h)", top_speed, 1000, chart_height=200, chart_width=10)
            st.plotly_chart(fig2, use_container_width=False)

        with colC:
            st.write(f"**Range:** {range_km} km")
            st.write(" ")
            fig3 = create_donut_chart("Range (km)", range_km, 1000, chart_height=200, chart_width=10)
            st.plotly_chart(fig3, use_container_width=False)

    with col2:
        #Display image of car_category
        st.subheader("Vehicle Image")
        image_path = f"images/{category}.jpg"
        try:
            image = Image.open(image_path)
            st.image(image, caption=f"Example {car_category} Vehicle: {car_model}")  # Adjust width of the image
        except FileNotFoundError:
            st.error(f"No image found for {car_category}")
    
    st.write("")
    st.info("Please connect the charging cable to the vehicle.")

    # Cancel Charging button
    if st.button("Cancel Charging"):
        st.write("Charging process canceled.")
        st.session_state.clear()
        st.switch_page("mainpage.py")
        
    if st.button("Jump to Next Page"):
        st.switch_page("pages/charging_setup.py")

    # Example: Add a warning message based on some condition
    if car_category == "Unknown":
        st.warning("Warning: Car category is not recognized. Please check your information.")

    # Display detailed vehicle information if available
    if "vehicle_details" in user_info:
        st.subheader("Detailed Vehicle Information")
        vehicle_details = user_info["vehicle_details"]
        for key, value in vehicle_details.items():
            st.write(f"**{key}:** {value}")
else:
    st.error("No user information available.")

# Add some space at the bottom
st.write("")
st.write("")

# Display a footer
st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")

