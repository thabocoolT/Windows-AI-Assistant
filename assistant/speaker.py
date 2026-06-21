import pyttsx3
import threading
import time

gui = None

def set_gui(window):
    global gui
    gui = window

def speak(text):
    print(f"Nova: {text}")

    if gui:
        gui.signals.update_status.emit("Speaking...")
        gui.signals.update_text.emit(text)

    def _speak():
        engine = pyttsx3.init()
        engine.setProperty("rate", 165)
        engine.setProperty("volume", 1.0)
        voices = engine.getProperty("voices")
        if len(voices) > 1:
            engine.setProperty("voice", voices[1].id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

        if gui:
            gui.signals.update_status.emit("Sleeping...")

    t = threading.Thread(target=_speak)
    t.start()
    t.join()