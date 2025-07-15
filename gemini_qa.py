import os  # For accessing environment variables
import google.generativeai as genai  # Google Gemini API client
from dotenv import load_dotenv  # For loading environment variables from a .env file and store securely

# import google.api_core.exceptions
# import time  # For handling API exceptions and implementing retry logic

load_dotenv()  # Load environment variables from .env file into the environment
api_key = os.getenv("GOOGLE_API_KEY")  # Get the Gemini API key from environment variables
genai.configure(api_key=api_key)  # Configure the Gemini client with the API key

# # List available models
# for m in genai.list_models():
#     print(m.name)


# model = genai.GenerativeModel("models/gemini-1.5-pro-latest")  # Create a model object for Gemini Pro -upgrade to Pro for better performance
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")




def get_gemini_response(text, question):
    
    # Build a prompt that includes the PDF content and the user's question
    prompt = f"""Here is the content of a PDF:\n\n{text}\n\nNow answer this question:\n{question}"""
    response = model.generate_content(prompt)  # Send the prompt to Gemini and get a response
    return response.text  # Return the generated answer as text

def summarize_answer(answer_text):
    # Build a prompt to summarize the answer in 3–4 bullet points
    prompt = f"""Summarize the following answer in 3–4 short bullet points:\n\n{answer_text}"""
    response = model.generate_content(prompt)  # Get the summary from Gemini
    return response.text  # Return the summary text

def get_pdf_summary(text):
    # Build a prompt to summarize the PDF content in 5–7 bullet points
    prompt = f"""Summarize this PDF content in 5–7 bullet points:\n\n{text}"""
    response = model.generate_content(prompt)  # Get the summary from Gemini
    return response.text  # Return
#new
def chunk_text(text, chunk_size=1500):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

