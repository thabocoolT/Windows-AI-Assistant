import pyttsx3
import threading
import time

def speak(text):
    print(f"Nova: {text}")
    
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

    t = threading.Thread(target=_speak)
    t.start()
    t.join()