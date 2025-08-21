import streamlit as st

# Set page configuration with title and icon
st.set_page_config(
    page_title="Help Page",
    page_icon="❓",  # You can use any emoji or URL to an image
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit decoration bar and change the background color of elements with class 'st-at'
hide_decoration_bar_style = """
    <style>
        header {visibility: hidden;}
        .st-at {
            background-color: rgb(120, 254, 113);
        }
    </style>
"""
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# Content for the help section
st.header("Help ❓")
st.write("Help and support information will be displayed here.")
st.write("For assistance, please contact support@ultraev.com.")
st.write(" ")

if st.button("Back to Homepage", type="primary"):
    st.switch_page("mainpage.py")
    
# Add some space at the bottom
st.write("")
st.write("")

# Display a footer
st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")