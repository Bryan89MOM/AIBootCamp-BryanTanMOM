import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if the API key is read correctly
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("Success! API key read correctly:")
    print(api_key)
else:
    print("Error! Failed to read API key. Check your .env file.")
