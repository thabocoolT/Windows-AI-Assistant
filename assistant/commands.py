from speaker import speak
from modules.open_app import open_application
from config import ASSISTANT_NAME
from datetime import datetime

def execute(command):
    command=command.lower()

    if "hello" in command:
        speak("Hello. How can I assist you?")

    elif "how are you" in command:
        speak("I am functioning properly.")

    elif(
        "your name" in command or
        "who are you" in command
    ):
        speak(f"My name is {ASSISTANT_NAME}.")

    elif "open" in command:
        app=(command .replace("open", "")).strip()

        opened=(open_application(app))

        if opened:
            speak(f"Opening {app}.")
        else:
            speak("I couldn't find that application.")

    elif "exit" in command:
        speak("Goodbye.")
        exit()

    else:
        speak(
            "I did not understand that command."
        )