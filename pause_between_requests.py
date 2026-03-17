import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

questions = [
    "What is the capital of France?",
    "What is the largest mammal?",
    "What is the speed of light?"
]
for question in questions:
    response=client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role":"user","content":question}]
    )

print(response.choices[0].message.content)

time.sleep(2)