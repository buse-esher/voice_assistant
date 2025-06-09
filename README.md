# Basic Voice Assistant

This project is a simple voice-activated AI assistant called Arche. 
Arche listens to spoken commands, performs certain tasks, and responds with speech. 
The assistant uses PyQt5 for the GUI and neuralintents for natural language understanding.

## 🚀 Features
-Voice Command Recognition (via Google Speech Recognition)

-AI-Powered Response System (using neuralintents)

-Text-to-Speech Output (pyttsx3)

-GUI Interface (built with PyQt5)

-Automatic file creation via voice command ("create a file")

## 🧠 Training Data

The assistant is trained using an intents.json file, which contains different intent tags, user input patterns, and appropriate responses.

## 📂 Project Files

main.py: Main application and GUI logic.

intents.json: Contains training data (intents and responses).

basic_model.keras: Trained model weights.

basic_model_words.pkl & basic_model_intents.pkl: Preprocessing artifacts.

## 💬 Supported Commands

“Hey Arche” → Activates the assistant.

“What is your name?” → Replies with the assistant’s name.

“Create a file” → Creates a file named somefile.txt.

“What is Arche?” → Explains what Arche is.

“Stop” → Shuts down the assistant and closes the app.

## 📌 Notes

A quiet environment is recommended for better speech recognition.

On the first run, the model will be trained and saved as .keras and .pkl files.
