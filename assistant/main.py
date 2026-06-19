import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from listener import listen
from speaker import speak
from commands import execute

def run_assistant():
    speak("Assistant started")
    while True:
        command=listen()
        if command:
            execute(command)

if __name__ == "__main__":
    run_assistant()