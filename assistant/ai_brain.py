import os
import json
import re
from persistent_memory import get_user_name, get_nickname

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
            "content": f"""
You are Nova, a Windows assistant created by {DEVELOPER['name']} (also known as {DEVELOPER['nickname']}).
He is a final year BSc IT student at North West University.
You were developed in {DEVELOPER['created']}.
You are currently talking to {get_user_name()}, also known as {get_nickname()}.
Address the user by name occasionally to make the conversation feel personal.
...rest of prompt stays the same...


Return ONE JSON object ONLY. Never return multiple JSON objects.

Two modes:

1. ACTION MODE:
{{
 "type":"action",
 "intent":"open_app|time|exit|greeting|volume_up|volume_down|set_volume|mute|screenshot|search|search_youtube|shutdown|restart|lock|read_file|unknown",
 "value":"extracted value or null"
}}

2. CHAT MODE:
{{
 "type":"chat",
 "response":"natural reply"
}}

Rules:
- open chrome/calculator/notepad → open_app, value=app name
- what time is it → time
- hello/hi → greeting
- exit/goodbye/quit → exit
- increase/raise volume → volume_up
- decrease/lower volume → volume_down
- mute → mute
- take screenshot → screenshot
- search [query] → search, value=query
- search youtube [query] → search_youtube, value=query
- lock computer → lock
- shutdown/turn off computer → shutdown
- restart computer → restart
- set volume to 50 → set_volume, value=50
- read file [filename] → read_file, value=filename
- general questions → chat
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