import speech_recognition as sr
from speaker import speak
recognizer=sr.Recognizer()

def wait_for_wake_word():
    print("Waiting for wake word 'Hey Nova'...")
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio=recognizer.listen(source, timeout=5, phrase_time_limit=3)
                text=recognizer.recognize_google(audio).lower()
                print(f"Heard: {text}")
                if "hey nova" in text or "nova" in text or "nov" in text:
                    speak("Yes, I am listening")
                    return
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except Exception as e:
                print(f"Wake word error: {e}")