import streamlit as st

# Streamlit page configuration
st.set_page_config(layout="centered", initial_sidebar_state="collapsed", page_title="Summary Page", page_icon="📊")

# Custom CSS 
style = """
    <style>
        .row-widget.stButton {text-align: center;}
        header {visibility: hidden;}
        .st-at {
            background-color: rgb(120, 254, 113);
        }
        h1, h2, h3, h4, h5, h6, p {
            color: white;
            text-shadow: 2px 2px 4px #000000; /* Dark outline for text */
        }
        .center-header {
            text-align: center;
            font-size: 36px; /* Reduced font size for header */
            text-shadow: 2px 2px 4px #000000; /* Dark outline for header text */
        }
        .stButton > button {
            width: 100%;
            font-size: 24px; /* Reduced font size for buttons */
            padding: 15px 32px;
            border: none;
            cursor: pointer;
            color: white;
            height: 100px;
            background-color: #00BCD4; /* Cyan color for buttons */
            transition: background-color 0.3s, transform 0.2s;
            margin-bottom: 10px;
        }
        .stButton > button:hover {
            background-color: #0097A7; /* Darker shade of cyan on hover */
            transform: scale(1.05);
        }
        .footer {
            text-align: center;
            padding: 10px 0;
            background-color: #1f4037;
            color: white;
            margin-top: 20px;
        }
        h2 {
            font-size: 40px; /* Reduced font size for h2 */
            color: #55e6e1; 
            font-family: "Times New Roman", Times, serif;   
            text-shadow: 2px 2px 4px #000000; /* Dark outline for h2 */
        }
        p {
            font-size: 30px; /* Reduced font size for paragraphs */
            font-family: "Times New Roman", Times, serif;
            text-shadow: 1px 1px 3px #000000; /* Dark outline for paragraphs */
        }
    </style>
"""
st.markdown(style, unsafe_allow_html=True)

# Center-aligned header
st.markdown("<h1 class='center-header'>Summary Page</h1>", unsafe_allow_html=True)

# Add some space 
st.write("")
st.write("")

st.markdown("<p class='center-content'>Please select an option to proceed.</p>", unsafe_allow_html=True)

# Add some space 
st.write("")
st.write("")

# Initialize session state
if "qr_result" not in st.session_state:
    st.session_state["qr_result"] = None
if "user_info" not in st.session_state:
    st.session_state["user_info"] = None

# Function to create the layout
def create_layout():
    # Create the User Access and Admin Access buttons side by side
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("User Access 👤", use_container_width=True):
            st.switch_page("pages/scanner_summary.py")
    with col2:
        if st.button("Admin Access 🔐", use_container_width=True):
            st.switch_page("pages/admin_access.py")

# Run the layout function
create_layout()

# Add the "Back to Homepage" button with default styling
if st.button("Back to Homepage", use_container_width=True):
    st.switch_page("mainpage.py")

# Add some space at the bottom
st.write("")
st.write("")

# Display a footer
st.markdown("---")
st.markdown("© 2024 EV Charging Station. All rights reserved.")
