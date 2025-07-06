import streamlit as st
from dotenv import load_dotenv
import os

from personas import career_coach, friend, tech_mentor

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.title("🤖 Persona Bot")

# Sidebar for persona selection
persona = st.sidebar.selectbox(
    "Choose a Persona",
    ("Career Coach", "Friend", "Tech Mentor")
)

# Load the right chain
if persona == "Career Coach":
    chain = career_coach.get_chain(api_key)
elif persona == "Friend":
    chain = friend.get_chain(api_key)
elif persona == "Tech Mentor":
    chain = tech_mentor.get_chain(api_key)

# Chat input
user_input = st.text_input("You:", "")

# If there's input, run the chain
if user_input:
    response = chain.run({"user_input": user_input})
    st.write(f"**{persona}:** {response}")
