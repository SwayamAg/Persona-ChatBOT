from dotenv import load_dotenv
import os

from personas import career_coach, friend, tech_mentor

load_dotenv()  

print("Select a Persona:")
print("1 - Career Coach")
print("2 - Friend")
print("3 - Tech Mentor")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    chat = career_coach.get_chain()
    prompt_path = "prompts/career_coach_prompt.txt"
elif choice == "2":
    chat = friend.get_chain()
    prompt_path = "prompts/friend_prompt.txt"
elif choice == "3":
    chat = tech_mentor.get_chain()
    prompt_path = "prompts/tech_mentor_prompt.txt"
else:
    print("Invalid choice.")
    exit()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Load persona prompt template
    template = open(prompt_path).read().strip() + "\n\nUser: {user_input}"
    final_prompt = template.format(user_input=user_input)

    # Send prompt to Gemini
    response = chat.send_message(final_prompt)
    print(f"Bot: {response.text}\n")
