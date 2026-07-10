import requests
import json
import os
from config import API_KEY
from search import search_google

MODEL = "gemini-3.5-flash"

URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY
}

HISTORY_FILE = "chat_history.json"

# Load previous chat history
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)
else:
    history = []

print("=" * 45)
print("🤖 Google Gemini AI Chatbot")
print("Conversation history enabled")
print("Type 'exit' to quit")
print("=" * 45)

while True:

    user_input = input("\nYou: ")
    if user_input.lower().startswith("search:"):

    query = user_input.replace("search:", "").strip()

    result = search_google(query)

    print("\nGoogle:", result)

    continue

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    history.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    payload = {
        "contents": history
    }

    try:

        response = requests.post(
            URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:

            data = response.json()

            reply = data["candidates"][0]["content"]["parts"][0]["text"]

            print("\nGemini:", reply)

            history.append({
                "role": "model",
                "parts": [{"text": reply}]
            })

            with open(HISTORY_FILE, "w") as file:
                json.dump(history, file, indent=4)

        else:

    print("\n❌ API Error:", response.status_code)

    if response.status_code == 429:
        print("Quota exceeded. Please check your Google AI Studio quota or try again later.")

    elif response.status_code == 503:
        print("Gemini server is busy. Please try again in a few minutes.")

    else:
        print(response.text)

    except Exception as e:

    print("\n⚠️ Unexpected Error")
    print(e)
