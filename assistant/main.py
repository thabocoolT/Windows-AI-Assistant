from listener import listen
from speaker import speak
from commands import execute
from wake_word import wait_for_wake_word

speak("Nova online")

while True:
    wait_for_wake_word()
    

    # Stay awake for multiple commands
    while True:
        command = listen()

        if not command:
            speak("I did not hear anything, going back to sleep")
            break

        if "nova" in command:
            command = command.replace("nova", "").strip()

        should_close = execute(command)

        if should_close:
            print("Program closed")
            exit()

        # Go back to sleep after saying "sleep" or "nevermind"
        if any(word in command for word in ["sleep", "nevermind", "never mind", "go to sleep"]):
            speak("Going to sleep")
            break