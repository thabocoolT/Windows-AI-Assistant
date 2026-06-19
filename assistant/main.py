import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from listener import listen
from speaker import speak
from commands import execute
from config import GREETING

def run_assistant():
    speak(GREETING)
    while True:
        command=listen()
        if command:
            execute(command)

if __name__ == "__main__":
    run_assistant()