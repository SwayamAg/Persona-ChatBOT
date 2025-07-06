import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# a = "Gemini Pro API Key: " + os.getenv("GEMINI_API_KEY")
# print(a)
# b = genai.list_models()
# print(b)


def get_chain():
    # Create a Gemini Pro model instance
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    # Start a persistent chat session with it
    chat = model.start_chat(history=[])
    return chat
