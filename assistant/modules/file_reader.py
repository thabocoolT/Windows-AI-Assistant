import os
from speaker import speak

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SEARCH_PATHS = [
    BASE_DIR,
    os.path.join(BASE_DIR, "assistant"),
    os.path.expanduser("~\\Documents"),
    os.path.expanduser("~\\Desktop"),
]

def read_file(filename):
    try:
        # Check if full path was given
        if os.path.exists(filename):
            filepath = filename
        else:
            # Search known locations
            filepath = None
            for folder in SEARCH_PATHS:
                candidate = os.path.join(folder, filename)
                if os.path.exists(candidate):
                    filepath = candidate
                    break

        if not filepath:
            speak(f"I could not find {filename}")
            return False

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.strip():
            speak("That file is empty")
            return False

        if len(content) > 500:
            content = content[:500]
            speak("The file is long, I will read the first part")

        speak(content)
        return True

    except Exception as e:
        print(f"File read error: {e}")
        speak("I could not read that file")
        return False