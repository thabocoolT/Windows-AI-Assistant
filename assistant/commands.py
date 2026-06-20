from datetime import datetime

from modules.file_reader import read_file
from speaker import speak
from ai_brain import get_intent
from modules.open_app import open_application
from modules.system_control import (
    volume_up,
    volume_down,
    mute,
    screenshot,
    lock_pc,
    shutdown_pc,
    restart_pc,
    set_volume
)
from modules.search import search_google, open_youtube
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

    if intent == "greeting":
        reply = "Hello, how can I help you?"
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "time":
        current = datetime.now().strftime("%H:%M")
        reply = f"It is {current}"
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "open_app":
        success = open_application(value)
        if success:
            reply = f"Opening {value}"
        else:
            reply = "I could not find that application"
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "volume_up":
        volume_up()
        reply = "Volume increased"
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "volume_down":
        volume_down()
        reply = "Volume decreased"
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "mute":
        mute()
        reply = "Muted"
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "screenshot":
        screenshot()
        reply = "Screenshot saved"
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "search":
        search_google(value)
        reply = f"Searching {value}"
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "search_youtube":
        open_youtube(value)
        reply = f"Searching {value} on YouTube"
        speak(reply)
        add_memory("assistant", reply)

    elif intent == "lock":
        reply = "Locking computer"
        speak(reply)
        add_memory("assistant", reply)
        lock_pc()

    elif intent == "shutdown":
        reply = "Shutting down in 5 seconds"
        speak(reply)
        add_memory("assistant", reply)
        shutdown_pc()

    elif intent == "restart":
        reply = "Restarting in 5 seconds"
        speak(reply)
        add_memory("assistant", reply)
        restart_pc()

    elif intent == "exit":
        speak("Goodbye")
        return True
    
    elif intent=="set_volume":
        try:
            level=int(value)
            set_volume(level)
            reply=f"Volume set to {level} percent"
        except:
            reply="Please say a number between 0 and 100"
        speak(reply)
        add_memory("assistant",reply)

    elif intent == "read_file":
        if value:
            read_file(value)
        else:
            speak("Please tell me the file name to read")

    else:
        reply = "I did not understand that command"
        speak(reply)
        add_memory("assistant", reply)

    return False