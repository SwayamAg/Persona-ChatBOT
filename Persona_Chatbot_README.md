
# Persona Chatbot 🤖✨

A simple Python chatbot that uses the **Gemini Pro API** and prompt engineering to simulate conversations with different personas:
- 🎓 Career Coach
- 🫶 Friend
- 👨‍💻 Tech Mentor

## 📌 How it works
- Select a persona when you run the app.
- Your input is added to a prompt template for that persona.
- The prompt is sent to the Gemini Pro API to generate a response.
- The chat continues until you type `exit` or `quit`.

## 🚀 Tech Stack
- Python
- Gemini Pro API
- `.env` for secure API key storage

## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/yourusername/persona_chatbot.git
cd persona_chatbot
```

### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
# OR
.venv\Scripts\activate  # For Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add your Gemini API Key
Create a file named `.env` in the project root and add:

```
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
```

Replace `YOUR_GEMINI_API_KEY_HERE` with your actual Gemini API key.

### 5️⃣ Run the chatbot
```bash
python main.py
```

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

## ✅ Example
```
Select a Persona:
1 - Career Coach
2 - Friend
3 - Tech Mentor

You: How do I grow in my career?
Gemini: Here's my advice...
```

## 📜 License
MIT License

## 🤝 Contributing
Feel free to fork and improve it! PRs welcome.

**Connect:**  
[LinkedIn](https://linkedin.com/in/swayam-agarwal) | [GitHub](https://github.com/SwayamAg)
