from listener import listen
from commands import execute
from speaker import speak


speak("Nova online")

while True:

    command = listen()

    if command:

        if "nova" in command:
            command = command.replace("nova", "").strip()

        execute(command)