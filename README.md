
# Persona Chatbot 🤖✨

A simple Python chatbot system that uses the **Gemini Pro API** and prompt engineering to simulate conversations with multiple personas:
- 🎓 **Career Coach**
- 🫶 **Friend**
- 👨‍💻 **Tech Mentor**

## 📌 How it works
- Choose a persona when you run the app.
- The app loads the relevant prompt template.
- Your input is dynamically added to the prompt.
- The prompt is sent to the Gemini Pro API to generate a response.
- Chat continues until you type `exit` or `quit`.

---

## 🚀 Tech Stack

- **Python**
- **LangChain / Gemini Pro API**
- `.env` for secure API key storage

---

## 🗂️ Project Structure

```
persona_bot/
 ├── personas/
 │   ├── career_coach.py
 │   ├── friend.py
 │   ├── tech_mentor.py
 ├── prompts/
 │   ├── career_coach_prompt.txt
 │   ├── friend_prompt.txt
 │   ├── tech_mentor_prompt.txt
 ├── main.py
 ├── app.py
 ├── requirements.txt
 ├── .env
```

---

## ⚙️ Setup Instructions

1. **Clone this repo**
   ```bash
   git clone https://github.com/yourusername/persona_chatbot.git
   cd persona_chatbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Gemini API key**
   - Create a `.env` file and add:
     ```
     GEMINI_API_KEY="your_api_key_here"
     ```

5. **Run the chatbot**
   ```bash
   python main.py
   ```

---

## 📌 Example

```
Select a Persona:
1 - Career Coach
2 - Friend
3 - Tech Mentor

You: How can I grow in my career?
Gemini: Here’s what I recommend...
```

---

## 📜 License

MIT License — free to use for learning and open-source contributions.

---

## 🤝 Contributing

PRs and feedback welcome! Feel free to fork and build your own persona chatbot ideas 🚀

**Connect:**  
[LinkedIn](https://linkedin.com/in/swayam-agarwal) | [GitHub](https://github.com/SwayamAg)
