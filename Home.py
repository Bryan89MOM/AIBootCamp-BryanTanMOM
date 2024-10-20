import streamlit as st

# Streamlit home page setup
st.set_page_config(
    page_title="Welcome to the HDB Resale Guru",
    page_icon=":house:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Create a column layout to place the logo beside the title text
col1, col2 = st.columns([1, 5])

with col1:
    st.image("assets/hdb_logo.png", width=80)

with col2:
    st.title("HDB Resale Guru   ")

st.markdown(
    """
    ## Overview
    The Housing & Development Board (HDB) is Singapore's public housing authority.
    This chatbot focuses on answering questions related to HDB resale procedures, grants, and policies.

    ## How to Navigate
    - **Use the sidebar** to access different sections:
        - **Hello Chatbot**: Ask questions about HDB resale and get answers powered by OpenAI.
        - **Resale Market Analysis Tool**: Get insights on past transactions.
        - **About Us**: Project scope, objectives, data sources, and features.
        - **Methodology**: Comprehensive explanation of the data flows and implementation details
    
    ## Get Started
    - Simply type your questions in the chatbot section to get quick answers.
    - Explore the market analysis to stay informed about the latest trends and data in the resale flat market.
    

    Enjoy exploring and getting the information you need!
    """
)

# Add disclaimer using expander
with st.expander("DISCLAIMER", expanded=False):
    st.write(
        """
        **IMPORTANT NOTICE**: This web application is a prototype developed for educational purposes only. 
        The information provided here is NOT intended for real-world usage and should not be relied upon 
        for making any decisions, especially those related to financial, legal, or healthcare matters.

        Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. 
        You assume full responsibility for how you use any generated output.

        Always consult with qualified professionals for accurate and personalized advice.
        """
    )
