import pyttsx3
import time
from config import VOICE_RATE

def speak(text):
    print(f"Assistant: {text}")
    engine = pyttsx3.init()
    engine.setProperty("rate", VOICE_RATE)
    print(
        f"Nova: {text}"
    )

    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.5)