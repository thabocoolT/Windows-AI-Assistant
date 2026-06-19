from datetime import datetime

from speaker import speak
from ai_brain import get_intent
from modules.open_app import open_application


def execute(command):

    try:

        data = get_intent(command)
        print(data)

        print("AI OUTPUT:", data)

        intent = (
            data.get(
                "intent",
                "unknown"
            )
            .lower()
        )

        value = (
            data.get(
                "value"
            )
        )

    except Exception as e:

        print(
            "AI ERROR:",
            e
        )

        speak(
            "AI processing failed"
        )

        return False


    if intent == "greeting":

        speak(
            "Hello, how can I help you?"
        )

        return False


    elif intent == "time":

        current = (
            datetime.now()
            .strftime(
                "%H:%M"
            )
        )

        speak(
            f"It is {current}"
        )

        return False


    elif intent == "open_app":

        success = (
            open_application(
                value
            )
        )

        if success:

            speak(
                f"Opening {value}"
            )

        else:

            speak(
                "I could not find that application"
            )

        return False


    elif intent == "exit":

        speak(
            "Goodbye"
        )

        return True


    else:

        speak(
            "I did not understand that command"
        )

        return False