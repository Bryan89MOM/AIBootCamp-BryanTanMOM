import streamlit as st
import openai
import json
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Load the scraped data
with open('data/data.json', 'r') as fp:
    data = json.load(fp)

# Streamlit UI
st.title("HDB Resale Chatbot 🤖")
st.image("assets/hdb_logo.png", width=50)
st.write("""
    Hello! I am your assistant. If you have any queries about buying a resale flat, feel free to ask me!
""")

# Set up your OpenAI API key
client = openai(
    api_key=st.secrets["OPENAI_API_KEY"],
)

# Function to generate the chatbot response
def generate_response(query):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an HDB expert assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
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


