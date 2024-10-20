from dotenv import load_dotenv
import os

# Specify the path to the .env file using a raw string
dotenv_path = r'C:\Users\tan_p\venv\.env'
load_dotenv(dotenv_path=dotenv_path)

# Check if the environment variable is loaded
openai_api_key = os.getenv('OPENAI_API_KEY')
print(f"Your OpenAI API key is: {openai_api_key}")
