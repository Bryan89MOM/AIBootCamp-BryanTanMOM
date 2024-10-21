import streamlit as st
import openai
import hmac

# Streamlit UI
st.title("HDB Resale Chatbot 🤖")
st.image("assets/hdb_logo.png", width=50)
st.write("""
    Hello! I am your assistant. If you have any queries about buying a resale flat, feel free to ask me!
""")

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

# Set up your OpenAI API key
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Function to generate the chatbot response
def generate_response(query):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Ensure this is a valid model for your API key
            messages=[
                {"role": "system", "content": "You are an HDB expert assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# User input
query = st.text_input("Ask the chatbot about HDB resale:")
if st.button("Get Answer"):
    if query:
        with st.spinner("Generating response..."):
            response = generate_response(query)
            st.success("Answer:")
            st.write(response)
    else:
        st.warning("Please enter a question.")
