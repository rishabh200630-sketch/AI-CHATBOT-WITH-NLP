# AI-CHATBOT-WITH-NLP
COMPANY: CODTECH IT SOLUTIONS NAME: Rishabh Ramesh Singh INTERN ID: CTO8DZ264 DOMAIN: PYTHON DURATION: 8 WEEK MENTOR: NEELA SANTOSH


Here’s a professional and clear README description for your GitHub project based on the uploaded script and weather plot:



# 🗨️ Python NLTK Chatbot

## 📌 Overview

This is a simple **rule-based chatbot** built using Python's **NLTK (Natural Language Toolkit)** library.
It uses predefined patterns and responses to simulate a conversation with the user.

The chatbot can handle greetings, basic questions, and some casual conversation.

---

## 🗂 Project Structure

```
.
├── chatbot.py       # Main chatbot script
└── README.md        # Project documentation
```

---

## ⚙️ How It Works

1. **Pattern Matching**

   * Uses **regular expressions** to identify user inputs.
   * Matches the input to predefined response patterns stored in `pairs`.

2. **Conversation Handling**

   * Uses `nltk.chat.util.Chat` and `reflections` for dynamic responses.
   * Example: If the user says `"my name is John"`, the bot replies `"Hello John, How are you today?"`.

3. **NLTK Data**

   * Downloads essential NLTK datasets (`punkt`, `wordnet`, and POS tagger) if not already installed.

---

## 💬 Example Chat

```
Hi, I'm Chatbot! Type 'quit' to exit.
You: hello
Bot: Hello

You: my name is Satish
Bot: Hello Satish, How are you today?

You: how are you?
Bot: I'm doing good
How about You ?

You: quit
Bot: Bye, take care. See you soon :)
```

---

## 🚀 How to Run

1. **Install Dependencies**

   ```bash
   pip install nltk
   ```
2. **Run the Chatbot**

   ```bash
   python chatbot.py
   ```
3. **Start Chatting!**

   * Type messages and get replies.
   * Type `quit` to exit the conversation.

---

## ✨ Features

* Rule-based responses using regex patterns.
* Friendly and interactive conversation.
* Easy to customize with new patterns and replies.

---

## 📌 Customization

To add new conversation rules:

1. Open `chatbot.py`.
2. In the `pairs` list, add a new pattern and response:

   ```python
   [
       r"do you like music?",
       ["Yes, I enjoy music! Especially coding soundtracks."]
   ]
   ```
3. Run the script again and test it.

---

If you want, I can also **add a section in the README with a table of all available commands and their responses** so users know exactly what they can ask your chatbot. That would make it look more professional. Would you like me to add that?
