import streamlit as st
import pandas as pd
import os
import time
from openpyxl import load_workbook
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.utils import ImageReader
from datetime import datetime

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="Charging Details", page_icon="👤")

st.title("Charging Details")

def upload_to_excel(data_frame, file_name='charging_station_details.xlsx', max_attempts=20, delay=1):
    attempt = 0
    while attempt < max_attempts:
        try:
            if os.path.exists(file_name):
                # Read existing data
                existing_df = pd.read_excel(file_name, engine='openpyxl')
                
                # Combine new data with existing data
                combined_df = pd.concat([existing_df, data_frame], ignore_index=True)
                
                # Drop duplicates based on all columns
                combined_df = combined_df.drop_duplicates()
                
                # Write the updated DataFrame back to the Excel file
                with pd.ExcelWriter(file_name, mode='w', engine='openpyxl') as writer:
                    combined_df.to_excel(writer, index=False)
            else:
                # Write new file
                data_frame.to_excel(file_name, index=False)
                
            st.success(f"Data successfully appended to {file_name}")
            return
        except PermissionError:
            attempt += 1
            if attempt < max_attempts:
                st.warning(f"File is open. Retrying in {delay} seconds... (Attempt {attempt}/{max_attempts})")
                time.sleep(delay)
            else:
                st.error(f"Unable to write to file after {max_attempts} attempts. Please close the Excel file and try again.")
                return
        except Exception as e:
            st.error(f"An error occurred while writing to the file: {str(e)}")
            return

def generate_pdf(data_frame):
    buffer = BytesIO()
    try:
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        # Add logo
        logo_path = "images/idpmainlogo.png"  # Replace with your logo file path
        if os.path.exists(logo_path):
            logo = ImageReader(logo_path)
            logo_width = 100
            logo_height = 100
            c.drawImage(logo, (width - logo_width) / 2, height - logo_height - 20, width=logo_width, height=logo_height, preserveAspectRatio=True, mask='auto')
        else:
            st.warning(f"Logo file not found at {logo_path}")

        # Add title
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(width / 2, height - logo_height - 60, "Carbon Credit Certificate")

        c.setFont("Helvetica", 12)
        y = height - logo_height - 100
        for i, (col, val) in enumerate(data_frame.iloc[0].items()):
            if y < 40:  # Add a new page if we reach the bottom
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 40
            c.drawString(100, y, f"{col}: {val}")
            y -= 20

        # Add footer
        c.setFont("Helvetica", 10)
        c.drawCentredString(width / 2, 30, "© 2024 EV Charging Station. All rights reserved.")

        c.showPage()
        c.save()
        buffer.seek(0)
        return buffer
    except Exception as e:
        st.error(f"An error occurred while generating the PDF: {str(e)}")
        return None

if "user_info" in st.session_state:
    # Ensure user_info is present and initialize state flags
    if "data_saved" not in st.session_state:
        st.session_state.data_saved = False
    
    user_info = st.session_state.user_info.copy()
    credits = st.session_state.credits
    emission_reduction = st.session_state.emission_reduction
    baseline_emit = st.session_state.baseline_emit
    project_emit = st.session_state.project_emit

    # Add credits and emissions data to user_info
    user_info["credits_earned"] = f"{credits:.3f}"
    user_info["emission_reduction"] = f"{emission_reduction:.6f}"
    user_info["baseline_emit"] = f"{baseline_emit:.6f}"
    user_info["project_emit"] = f"{project_emit:.6f}"
    user_info["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Convert user_info to DataFrame
    df = pd.DataFrame([user_info])

    # Reorder and rename columns for Excel
    excel_columns_order = ["username", "phone_number", "car_model", "car_category", "credits_earned", "emission_reduction", "baseline_emit", "project_emit", "payment_method", "timestamp"]
    excel_df = pd.DataFrame(columns=excel_columns_order)

    for col in excel_columns_order:
        if col in df.columns:
            excel_df[col] = df[col]
        else:
            excel_df[col] = pd.Series(['-'] * len(df))

    excel_df.columns = ["Username", "Phone Number", "Car Model", "Car Category", "Credits Earned", "Emission Reduction", "Baseline Emission", "Project Emission", "Payment Method", "Timestamp"]

    # Format car_category
    excel_df["Car Category"] = excel_df["Car Category"].apply(lambda x: ' '.join(word.capitalize() for word in str(x).split('_')))

    # Save data to Excel file only if not already saved
    if not st.session_state.data_saved:
        upload_to_excel(excel_df)
        st.session_state.data_saved = True
    
    # Reorder and rename columns for Streamlit display (excluding baseline, project, and reduction)
    display_columns_order = ["username", "phone_number", "car_model", "car_category", "credits_earned", "payment_method"]
    display_df = pd.DataFrame(columns=display_columns_order)

    for col in display_columns_order:
        if col in df.columns:
            display_df[col] = df[col]
        else:
            display_df[col] = pd.Series(['-'] * len(df))

    display_df.columns = ["Username", "Phone Number", "Car Model", "Car Category", "Credits Earned", "Payment Method"]

    # Format car_category for display
    display_df["Car Category"] = display_df["Car Category"].apply(lambda x: ' '.join(word.capitalize() for word in str(x).split('_')))

    # Reset index to start from 1 and name it "No."
    display_df.index = range(1, len(display_df) + 1)
    display_df.index.name = "No."

    st.subheader("User Information")
    st.table(display_df)

    # Generate PDF
    buffer = generate_pdf(excel_df)
    if buffer:
        st.download_button(label="Download Credit Certificate as PDF", data=buffer, file_name="carbon_credit_certificate.pdf", mime="application/pdf")

    if st.button("Finish and Return to Home"):
        # Clear session state and flag
        st.session_state.clear()
        st.session_state.data_saved = False  # Reset the data saved flag for future use
        # Redirect to home page
        st.switch_page("mainpage.py")

st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")
