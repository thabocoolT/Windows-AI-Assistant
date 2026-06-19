import pyttsx3

def speak(message):
    print(f"Assistant: {message}")
    engine = pyttsx3.init()
    engine.setProperty("rate", 180)
    engine.say(message)
    engine.runAndWait()
    engine.stop()