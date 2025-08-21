import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO
import os

# Streamlit page configuration
st.set_page_config(layout="centered", initial_sidebar_state="collapsed", page_title="User Access", page_icon="👤")

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
st.markdown("<h1 class='center-header'>User Access</h1>", unsafe_allow_html=True)

# Function to generate PDF
def generate_pdf(data_frame, total_credits, user_specific=True):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Add logo
    logo_path = "images/idpmainlogo.png"  # Replace with your logo file path
    logo = ImageReader(logo_path)
    logo_width = 100
    logo_height = 50
    c.drawImage(logo, (width - logo_width) / 2, height - logo_height - 20, width=logo_width, height=logo_height, preserveAspectRatio=True, mask='auto')

    # Add title
    title = "User Charging Log" if user_specific else "Admin Charging Log"
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - logo_height - 60, title)

    # Set font size for table headers
    c.setFont("Helvetica-Bold", 6)
    y = height - logo_height - 100

    # Add table header
    x = 50
    col_widths = [50, 50, 50, 40, 50, 60, 60, 60, 60, 60]  # Adjust column widths as needed
    for i, col in enumerate(data_frame.columns):
        c.drawString(x, y, col)
        x += col_widths[i]
    y -= 20

    # Add table rows
    c.setFont("Helvetica", 7)  # Reduced font size for table rows
    for index, row in data_frame.iterrows():
        x = 50
        for i, (col, val) in enumerate(row.items()):
            c.drawString(x, y, str(val))
            x += col_widths[i]
        y -= 20
        if y < 40:  # Add a new page if we reach the bottom
            c.showPage()
            c.setFont("Helvetica", 7)
            y = height - 40

    # Add total credits
    c.setFont("Helvetica-Bold", 10)
    y -= 20
    c.drawString(50, y, f"Total Carbon Credits Earned: {total_credits}")
    
    # Add footer
    c.setFont("Helvetica", 10)
    c.drawCentredString(width / 2, 30, "© 2024 EV Charging Station. All rights reserved.")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# Initialize session state
if "user_info" not in st.session_state:
    st.session_state["user_info"] = None

if st.session_state["user_info"]:
    user_info = st.session_state["user_info"]

    # Load user-specific log from Excel
    file_name = 'charging_station_details.xlsx'
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
        user_df = df[df["Username"] == user_info["username"]]

        if not user_df.empty:
            st.subheader("Charging Log")
            
            st.write("")
            st.table(user_df)

            total_credits = user_df["Credits Earned"].sum()
            st.write(f"Total Carbon Credits Earned: {total_credits}")

            # Generate PDF
            buffer = generate_pdf(user_df, total_credits, user_specific=True)
            st.download_button(label="Download Log as PDF", data=buffer, file_name="user_charging_log.pdf", mime="application/pdf")
        else:
            st.warning("No charging log found for this user.")

if st.button("Back to Homepage", type="primary"):
    st.session_state.clear()
    st.switch_page("mainpage.py")

# Add some space at the bottom
st.write("")
st.write("")

# Display a footer
st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")
