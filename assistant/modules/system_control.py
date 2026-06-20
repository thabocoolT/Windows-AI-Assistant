import os
import pyautogui
from datetime import datetime
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

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

def set_volume(level):
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(level / 100, None)
        return True
    except Exception:
        # Fallback method using pyautogui keypresses
        try:
            # Reset to 0 first then press up to desired level
            for _ in range(50):
                pyautogui.press("volumedown")
            presses = int(level / 2)
            for _ in range(presses):
                pyautogui.press("volumeup")
            return True
        except Exception as e:
            print(f"Volume error: {e}")
            return False

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

def shutdown_pc():
    os.system("shutdown /s /t 5")
    return True

def restart_pc():
    os.system("shutdown /r /t 5")
    return True