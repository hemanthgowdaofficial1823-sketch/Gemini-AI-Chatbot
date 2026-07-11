from google import genai
from config import API_KEY

try:
    client = genai.Client(api_key=API_KEY)

    print("=" * 45)
    print("🤖 Google Gemini AI Chatbot")
    print("Type 'exit' to quit")
    print("=" * 45)

    while True:

        user = input("\nYou: ")

        if user.lower() == "exit":
            print("Goodbye!")
            break

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=user
        )

        print("\nGemini:", response.text)

except Exception as e:
    print("\nError:")
    print(e)
