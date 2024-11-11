import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the GEMINI_API_KEY from environment variables
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Use the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)
