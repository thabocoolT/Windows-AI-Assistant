import os
import pyautogui
from datetime import datetime

def volume_up():
    pyautogui.press(
        "volumeup"
    )

    return True

def volume_down():
    pyautogui.press(
        "volumedown"
    )

    return True

def mute():
    pyautogui.press(
        "volumemute"
    )

    return True

def screenshot():

    try:

        folder = "screenshots"

        os.makedirs(
            folder,
            exist_ok=True
        )

        filename = (
            f"screenshot_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ".png"
        )

        path = os.path.join(
            folder,
            filename
        )

        image = (
            pyautogui
            .screenshot()
        )

        image.save(
            path
        )

        print(
            f"Saved → {path}"
        )

        return True


    except Exception as e:

        print(
            "Screenshot Error:",
            e
        )

        return False

def lock_pc():
    os.system(
        "rundll32.exe user32.dll,LockWorkStation"
    )

    return True