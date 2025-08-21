#Initialization
#1. Vehicle Identity & Model Showcase
#2. Plug in status

import streamlit as st
import pandas as pd

# Ensure this script only runs when the session state "page" is "initialize"
if st.session_state.get("page") != "initialize":
    st.stop()

# Your initialize.py logic here
st.title("Initialize Page")
st.write("This is the initialize page content.")

# Simulate the plug status
def is_plugged_in():
    return st.session_state.get('plug_status', False)

# Simulate authentication status
def is_authenticated():
    return st.session_state.get('auth_status', False)

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'initial'

    if st.session_state.page == 'initial':
        st.write("Please connect the charging cable to the vehicle")
        plug_status_input = st.text_input("Enter 'plugged in' to connect the cable:")
        if plug_status_input.lower() == 'plugged in':
            st.session_state.plug_status = True
            st.session_state.page = 'auth'
            st.rerun()

    elif st.session_state.page == 'auth':
        st.write("Please authenticate to start charging")
        auth_input = st.text_input("Enter 'authenticated' to authenticate:")
        if auth_input.lower() == 'authenticated':
            st.session_state.auth_status = True
            st.session_state.page = 'charging'
            st.rerun()

    elif st.session_state.page == 'charging':
        st.write("Charging in progress...")
        plug_status_input = st.text_input("Enter 'disconnected' to disconnect the cable:")
        if plug_status_input.lower() == 'disconnected':
            st.session_state.plug_status = False
            st.session_state.auth_status = False
            st.session_state.page = 'initial'
            st.rerun()

if __name__ == "__main__":
    main()

