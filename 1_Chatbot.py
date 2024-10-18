import streamlit as st
from openai import OpenAI
import json

# Load the scraped data
with open('data/data.json', 'r') as fp:
    data = json.load(fp)

# Streamlit UI
st.title("HDB Resale Chatbot :robot_face:")
st.image("assets/hdb_logo.png", width=50)
st.write("""
    Hello! I am your assistant. If you have any queries about buying a resale flat, feel free to ask me!
""")

# Set up your OpenAI API key
client = OpenAI(api_key = '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')

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

