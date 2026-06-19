from datetime import datetime

from speaker import speak
from ai_brain import get_intent
from modules.open_app import open_application
from memory import add_memory

EXIT_COMMANDS = ["exit", "quit", "goodbye", "stop"]

def execute(command):
    command = command.lower().strip()

    add_memory("user", command)

    if command in EXIT_COMMANDS:
        speak("Goodbye")
        return True

    data = get_intent(command)
    print("AI:", data)

    if data.get("type") == "chat":
        response = data.get("response")
        speak(response)
        add_memory("assistant", response)
        return False

    intent = data.get("intent")
    value = data.get("value")

    if intent == "exit":          # ← AI may return exit intent
        speak("Goodbye")
        return True

    elif intent == "greeting":
        reply = "Hello, how can I help you?"
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "time":
        current = datetime.now().strftime("%H:%M")
        reply = f"It is {current}"  # ← added space
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "open_app":
        success = open_application(value)
        if success:
            reply = f"Opening {value}"  # ← added space
        else:
            reply = "I could not find that application"
        speak(reply)                    # ← was missing speak()
        add_memory("assistant", reply)

    else:
        reply = "I did not understand"
        speak(reply)
        add_memory("assistant", reply)

    return False