import openai
import os
from load_dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_reply(user_message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        ai_reply = response.choices[0].text.strip()
        return ai_reply
    except Exception as e:
        print(f"Error generating AI reply: {e}")
        return "Sorry, I couldn't process your request at the moment."