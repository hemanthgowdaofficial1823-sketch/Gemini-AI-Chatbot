from google import genai
import json
import os

API_KEY = "YOUR_API_KEY"

client = genai.Client(api_key=API_KEY)

HISTORY_FILE = "chat_history.json"

# Load previous history
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)
else:
    history = []

print("=" * 50)
print("🤖 Google Gemini AI Chatbot")
print("Conversation History Enabled")
print("History Auto Save Enabled")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        print("Conversation saved.")
        print("Goodbye!")
        break

    history.append({
        "role": "user",
        "text": user
    })

    prompt = ""

    for message in history:
        prompt += f"{message['role']}: {message['text']}\n"

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        reply = response.text

        print("\nGemini:", reply)

        history.append({
            "role": "Gemini",
            "text": reply
        })

        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)

    except Exception as e:
        print("\nError:")
        print(e)
