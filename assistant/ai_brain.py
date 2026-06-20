import os
import json
import re

from groq import Groq
from dotenv import load_dotenv
from config import DEVELOPER

from memory import get_memory

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_intent(command):

    messages = [
        {
            "role": "system",
            "content": """
You are Nova, a Windows assistant created by {DEVELOPER['name']} (also known as {DEVELOPER['nickname']}) 
He is a final year BSc IT student at North West University.
You were developed in {DEVELOPER['created']}.

Return ONE JSON object ONLY. Never return multiple JSON objects.

Two modes:

1. ACTION MODE:
{
 "type":"action",
 "intent":"open_app|time|exit|greeting|unknown",
 "value":"..."
}

2. CHAT MODE:
{
 "type":"chat",
 "response":"natural reply"
}

Rules:
- If user requests system task → action
- If general question → chat
- If asked about your developer, Cool Tee, or Prince → chat, answer from the info above
- Always return ONE JSON object only
"""
        }
    ]

    messages.extend(get_memory())

    messages.append({
        "role": "user",
        "content": command
    })

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    output = response.choices[0].message.content.strip()
    output = output.replace("```json", "").replace("```", "").strip()

    # Extract only the first JSON object
   
    start = output.find("{")
    end = output.rfind("}") + 1
    if start != -1 and end > start:
        try:
            return json.loads(output[start:end])
        except json.JSONDecodeError:
            pass

    return {"type": "action", "intent": "unknown", "value": None}