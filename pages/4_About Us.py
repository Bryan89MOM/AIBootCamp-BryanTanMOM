import streamlit as st
import hmac

# Streamlit About Us page setup
st.set_page_config(
    page_title="About Us - HDB Resale Guru",
    page_icon=":information_source:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Title for the About Us page
st.title("About Us")

# Function to check password (same as in main.py)
def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False
            
    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True
    
    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
        
    return False

# Check password for this page
if not check_password():
    st.stop()  # Stop if password check fails

# Project Overview
st.markdown(
    """
    Welcome to **HDB Resale Guru**, an interactive web-based application designed to assist individuals interested in the HDB resale market in Singapore. 
    Our mission is to simplify the process of understanding HDB resale procedures, grants, policies, and market trends.
    """
)

# Project Objectives
st.subheader("Objectives")
st.markdown(
    """
    Our key objectives include:
    - Providing a user-friendly platform for querying past HDB resale transactions.
    - Analyzing market trends and offering data-driven insights to potential buyers.
    - Through the integrated AI chatbot, deliver instant, accurate answers to users' queries about HDB resale flats, eligibility, pricing, and grants, enhancing user experience and reducing response time.
    """
)

# Data Sources
st.subheader("Data Sources")
st.markdown(
    """
    To ensure accuracy and relevance, our application utilizes the following reliable data sources:
    - **HDB Transaction Data**: Resale prices and property details are sourced from HDB's publicly available datasets, accessible at [data.gov.sg](https://data.gov.sg/).
    - **Official HDB Information**: We scrape information regarding the resale HDB process, grants, and policies from the official HDB website. The following URLs were scraped as of **October 18, 2024**:
    
    - [Buying Procedure for Resale Flats](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats)
    - [Planning, Sourcing, and Contracting](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract)
    - [Overview of Buying Procedure](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/overview)
    - [Planning Considerations](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations)
    - [Managing the Flat Purchase](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/managing-the-flat-purchase)
    - [EIP and SPR Quota](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/planning-considerations/eip-spr-quota)
    - [Mode of Financing](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/mode-of-financing)
    - [Option to Purchase](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/option-to-purchase)
    - [Request for Value](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/plan-source-and-contract/request-for-value)
    """
)

# Features
st.subheader("Features")
st.markdown(
    """
    Our application offers a variety of features to enhance your experience:
    - **Chatbot Assistance**: An AI-powered chatbot that answers queries related to HDB resale processes and guidelines.
    - **Resale Market Analysis Tool**: Analyze historical transaction data, visualize price trends, and gain insights on market performance.
    """
)

# Conclusion
st.markdown(
    """
    We are committed to empowering individuals with the information needed to navigate the HDB resale market effectively. 
    Enjoy exploring your options with **HDB Resale Guru**!
    """
)
