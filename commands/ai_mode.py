import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_ai_command(command, speak):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant named Light. Keep answers short and clear."},
                {"role": "user", "content": command}
            ],
            max_tokens=150
        )

        reply = response.choices[0].message.content
        speak(reply)
        return True

    except Exception as e:
        speak("There was an error with AI mode.")
        print("AI error:", e)
        return False