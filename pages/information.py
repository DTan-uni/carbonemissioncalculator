# information.py

import streamlit as st

# Set page configuration with title and icon
st.set_page_config(
    page_title="EV Carbon Counting and Credit System",
    page_icon="ℹ️",  # You can use any emoji or URL to an image
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



# Define the introduction content
intro_content = """
### Introduction to Carbon Accounting in EV Chargers: Baseline and Project Emissions

Carbon Accounting System in EV Chargers:

The integration of electric vehicle (EV) chargers into carbon accounting systems is vital for assessing and managing the environmental impact of EV infrastructure.
A carbon accounting system tracks the greenhouse gas (GHG) emissions associated with the production, installation, and operation of EV chargers. This system helps organizations and governments measure progress towards reducing carbon footprints and achieving sustainability goals.

Baseline Emissions:

Baseline emissions refer to the amount of GHGs emitted under normal or business-as-usual scenarios, without the implementation of any emission reduction projects. For EV chargers, baseline emissions might include:

- Electricity Source: The emissions associated with the electricity used by the chargers, which depends on the energy mix of the grid (e.g., coal, natural gas, renewable sources).
- Operational Efficiency: The energy efficiency of the charging equipment and potential losses during the charging process.
Baseline emission can be quantified as below:
"""
project_content = """ 
Project Emissions:

Project emissions are the GHG emissions after the implementation of a specific emission reduction project. In this scenario, the electric vehicle acts as a project for the carbon reduction. These emissions typically include:

- Reduced Grid Emissions: Lower emissions due to a higher proportion of renewable energy used in the electricity supplied to EV chargers.
- Improved Efficiency: Emissions saved by using more efficient charging technologies that reduce energy consumption and losses.
"""

reduction_content = """
Emissions Reduction:

By comparing baseline and project emissions, organizations can quantify the GHG reductions achieved and make informed decisions to further optimize their carbon footprint.
The leakage emissions is assumed to be zero. 
"""
# Display the introduction content in Streamlit
def show_information():
    st.markdown(intro_content)
    with st.expander('Formula for baseline emission 💡'):
        st.write("""
        𝐵𝐸𝑦 = ∑𝐸𝐹𝐵𝐿,𝑘𝑚,𝑖
        ×
        𝐸𝐶𝑃𝐽,𝑖,𝑦
        𝑆𝐸𝐶𝑃𝐽,𝑘𝑚,𝑖,𝑦
        × 10^{-6}
        """)
        st.write("""
        Parameters:
        - 𝐸𝐹𝐵𝐿,𝑘𝑚,𝑖: Emission factor for baseline vehicle category i (g CO2/km)
        - 𝐸𝐶𝑃𝐽,𝑖,𝑦: Electricity consumed for charging project vehicles category i at the charging stations/points in year y (kWh)
        - 𝑆𝐸𝐶𝑃𝐽,𝑘𝑚,𝑖,𝑦: Specific electricity consumption per km per project vehicle category i in year y (kWh/km)
        """)
    
    st.markdown(project_content)
    with st.expander('Formula for project emission 💡'):
        st.write("""
        𝑃𝐸𝑦 = ∑𝐸𝐹𝑃𝐽,𝑘𝑚,𝑖
        ×
        𝐸𝐶𝑃𝐽,𝑖,𝑦
        𝑆𝐸𝐶𝑃𝐽,𝑘𝑚,𝑖,𝑦
        """)
        st.write("""
        Parameters Sources:
        - 𝐸𝐹𝑃𝐽,𝑘𝑚,𝑖: Emission factor by the project vehicle type i (t CO2/km)
        - 𝐸𝐶𝑃𝐽,𝑖,𝑦: Electricity consumed for charging project vehicles category i at the charging stations/points in year y (kWh)
        - 𝑆𝐸𝐶𝑃𝐽,𝑘𝑚,𝑖,𝑦: Specific electricity consumption per km per project vehicle category i in year y (kWh/km)
        """)
        
    st.markdown(reduction_content)
    with st.expander('Formula for emission reduction 💡'):
        st.write("""
        𝐸𝑅𝑦 = 𝐵𝐸𝑦 - 𝑃𝐸𝑦 - 𝐿𝐸𝑦
        """)
        st.write("""
        Parameters:
        - 𝐸𝑅𝑦: Emission reductions in year y (t CO2e)
        - 𝐵𝐸𝑦: Baseline emissions in year y (t CO2e)
        - 𝑃𝐸𝑦: Project emissions in year y (t CO2e)
        - 𝐿𝐸𝑦: Leakage reductions in year y (t CO2e)
        """)

# Example usage in Streamlit app (main.py or another script)
if __name__ == "__main__":
    show_information()

if st.button("Back to Homepage", type="primary"):
    st.switch_page("mainpage.py")