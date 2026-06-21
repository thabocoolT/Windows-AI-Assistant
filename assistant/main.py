import os
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"

import time
import sys
import threading
from PySide6.QtWidgets import QApplication
from listener import listen
from speaker import speak
from commands import execute
from wake_word import wait_for_wake_word
from gui import NovaGUI

app = QApplication(sys.argv)
window = NovaGUI()
window.show()

def run_assistant():
    speak("Nova online")
    window.signals.update_text.emit("Nova online")

    while True:
        window.signals.update_status.emit("Sleeping...")
        wait_for_wake_word()

        window.signals.update_status.emit("Listening...")
        window.signals.update_text.emit("Listening...")

        command = listen()

        if not command:
            continue

        if "nova" in command:
            command = command.replace("nova", "").strip()

        if not command:
            continue

        window.signals.update_text.emit(f"You: {command}")
        window.signals.update_status.emit("Thinking...")

        should_close = execute(command)

        if should_close:

            window.signals.update_status.emit(
                "Shutting down..."
            )

            window.signals.update_text.emit(
                "Goodbye"
            )

            time.sleep(1)

            window.signals.close_app.emit()

            return

        # Ask if there is anything else
        speak("Is there anything else I can help you with?")
        window.signals.update_status.emit("Listening...")
        window.signals.update_text.emit("Anything else?")

        followup = listen()

        if not followup:
            speak("Okay, going back to sleep")
            continue

        negative = ["no", "nope", "nothing", "that's all", "that is all", "no thanks", "nah"]

        if any(word in followup.lower() for word in negative):
            speak("Okay, going back to sleep. Say Hey Nova when you need me")
            window.signals.update_status.emit("Sleeping...")
            window.signals.update_text.emit("Sleeping...")
            continue

        # They said something else - treat it as a new command
        if "nova" in followup:
            followup = followup.replace("nova", "").strip()

        window.signals.update_text.emit(f"You: {followup}")
        window.signals.update_status.emit("Thinking...")

        should_close = execute(followup)

        if should_close:
            window.signals.update_status.emit(
                "Shutting donw..."
            )

            window.signals.update_text.emit(
                "Goodbye"
            )
            time.sleep(1)
            window.signals.close_app.emit()
            return

thread = threading.Thread(target=run_assistant, daemon=True)
thread.start()

sys.exit(app.exec())