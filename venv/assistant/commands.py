from speaker import speak
from modules.open_app import open_application

def execute(command):
    if "open chrome" in command:
        open_application(
            "chrome"
        )
        speak("Opening Chrome")

    elif "time" in command:
        from datetime import datetime
        current=(
            datetime.now()
            .strftime("%H:%M")
        )
        speak(current)
    
    elif "exit" in command:
        speak("Goodbye!")
        exit()

        exit()

    else:
        speak("Command not recognized")