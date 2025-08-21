import streamlit as st

st.header('Explanation on the carbon accounting system')

# Define the introduction content
intro_content = """
### Introduction to Carbon Accounting in EV Chargers: Baseline and Project Emissions

*Carbon Accounting System in EV Chargers:*

The integration of electric vehicle (EV) chargers into carbon accounting systems is vital for assessing and managing the environmental impact of EV infrastructure.
A carbon accounting system tracks the greenhouse gas (GHG) emissions associated with the production, installation, and operation of EV chargers. This system helps organizations and governments measure progress towards reducing carbon footprints and achieving sustainability goals.

*Baseline Emissions:*

Baseline emissions refer to the amount of GHGs emitted under normal or business-as-usual scenarios, without the implementation of any emission reduction projects. For EV chargers, baseline emissions might include:

- *Electricity Source:* The emissions associated with the electricity used by the chargers, which depends on the energy mix of the grid (e.g., coal, natural gas, renewable sources).
- *Operational Efficiency:* The energy efficiency of the charging equipment and potential losses during the charging process.
Baseline emission can be quantified as below:
"""
project_content = """ 
*Project Emissions:*

Project emissions are the GHG emissions after the implementation of a specific emission reduction project, such as the installation of more efficient EV chargers or the use of renewable energy sources. These emissions typically include:

- *Reduced Grid Emissions:* Lower emissions due to a higher proportion of renewable energy used in the electricity supplied to EV chargers.
- *Improved Efficiency:* Emissions saved by using more efficient charging technologies that reduce energy consumption and losses.
- *Lifecycle Emissions:* Reduced emissions from the production and deployment of chargers with lower carbon footprints.

By comparing baseline and project emissions, organizations can quantify the GHG reductions achieved and make informed decisions to further optimize their carbon footprint in the context of EV infrastructure.
"""
# Display the introduction content in Streamlit
def information():
    st.markdown(intro_content)
    with st.expander('Formula for baseline emission'):
        st.write("""
        𝐵𝐸𝑦 = ∑𝐸𝐹𝐵𝐿,𝑘𝑚,𝑖
        ×
        𝐸𝐶𝑃𝐽,𝑖,𝑦
        𝑆𝐸𝐶𝑃𝐽,𝑘𝑚,𝑖,𝑦
        × 10^{-6}
        """)
    
    st.markdown(project_content)
    with st.expander('Formula for project emission'):
        st.write("""
        𝑃𝐸𝑦 = ∑𝐸𝐹𝑃𝐽,𝑘𝑚,𝑖
        ×
        𝐸𝐶𝑃𝐽,𝑖,𝑦
        𝑆𝐸𝐶𝑃𝐽,𝑘𝑚,𝑖,𝑦
        """)      

information()