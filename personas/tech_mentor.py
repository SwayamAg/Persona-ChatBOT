import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_chain():
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    chat = model.start_chat(history=[])
    return chat
