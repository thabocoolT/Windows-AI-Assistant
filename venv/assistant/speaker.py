import pyttsx3


engine=pyttsx3.init()
engine.setProperty(
    "rate", 180
)


def speak(message):
    print(f"Assistant: {message}")
    engine.say(message)
    engine.runAndWait()