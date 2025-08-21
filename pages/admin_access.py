import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO
import os

# Streamlit page configuration
st.set_page_config(layout="centered", initial_sidebar_state="collapsed", page_title="Admin Access", page_icon="🔑")

# Custom CSS to style the header and center-align content
style = """
    <style>
        .center-header {text-align: center; font-size: 2em; margin-top: 20px;}
        .center-content {text-align: center; font-size: 1.2em; margin-top: 10px;}
        .admin-form {text-align: center; margin-top: 20px;}
    </style>
"""
st.markdown(style, unsafe_allow_html=True)

# Center-aligned header
st.markdown("<h1 class='center-header'>Admin Access</h1>", unsafe_allow_html=True)

# Define credentials directly in the code (for testing purposes)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

# Admin login form
with st.form(key='admin_login_form', clear_on_submit=True):
    st.markdown("<div class='admin-form'><p>Enter your username and password to access admin features:</p></div>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Login")

# Dummy authentication
def authenticate(username, password):
    # Replace with your actual authentication logic
    return username == ADMIN_USERNAME  and password == ADMIN_PASSWORD

# Function to generate PDF
def generate_pdf(df, total_credits):
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
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - logo_height - 60, "Admin Charging Log")

    # Set font size for table headers
    c.setFont("Helvetica-Bold", 6)
    y = height - logo_height - 100

    # Add table header
    x = 50
    col_widths = [50, 50, 50, 50, 50, 60, 60, 60, 60, 60]
    for i, col in enumerate(df.columns):
        c.drawString(x, y, col)
        x += col_widths[i]
    y -= 20

    # Add table rows
    c.setFont("Helvetica", 6)
    for index, row in df.iterrows():
        x = 50
        for i, (col, val) in enumerate(row.items()):
            c.drawString(x, y, str(val))
            x += col_widths[i]
        y -= 20
        if y < 40:  # Add a new page if we reach the bottom
            c.showPage()
            c.setFont("Helvetica", 6)
            y = height - 40

    # Add total credits
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y - 20, f"Total Carbon Credits Earned: {total_credits}")

    # Add footer
    c.setFont("Helvetica", 10)
    c.drawCentredString(width / 2, 30, "© 2024 EV Charging Station. All rights reserved.")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# Process login
if submit_button:
    if authenticate(username, password):
        # Load all charging logs from Excel
        file_name = 'charging_station_details.xlsx'
        if os.path.exists(file_name):
            df = pd.read_excel(file_name)

            # Display all charging logs
            st.subheader("Charging Logs")
            st.write(df)

            # Calculate total carbon credits
            total_credits = df["Credits Earned"].sum()
            st.write(f"Total Carbon Credits Earned: {total_credits}")

            # Generate PDF
            buffer = generate_pdf(df, total_credits)
            st.download_button(label="Download Log as PDF", data=buffer, file_name="admin_charging_log.pdf", mime="application/pdf")
        else:
            st.warning("No charging logs found.")
    else:
        st.error("Invalid username or password.")

# Button to go back to the homepage
if st.button("Back to Homepage"):
    st.session_state.clear()
    st.switch_page("mainpage.py")

# Add some space at the bottom
st.write("")
st.write("")

# Display a footer
st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")
