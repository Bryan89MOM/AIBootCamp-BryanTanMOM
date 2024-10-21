import streamlit as st
import hmac

# Methodology Page
st.title("Methodology")

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

# Explanation of Data Flows
st.header("Data Flows")
st.write("""
This section outlines the data flows in the HDB Resale Guru application. The flowcharts below visually represent how data is processed in two key components of the application: the HDB Resale Chatbot and the HDB Resale Market Analysis Tool.
""")

# Expander for HDB Resale Chatbot Flowchart
with st.expander("HDB Resale Chatbot Flowchart"):
    st.image("assets/HDB_Resale_Chatbot.png")

# Expander for HDB Resale Market Analysis Tool Flowchart
with st.expander("HDB Resale Market Analysis Tool Flowchart"):
    st.image("assets/HDB_Resale_Market_Analysis_Tool.png")
