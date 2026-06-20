import subprocess
import json
import os
import glob


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

with open(os.path.join(BASE_DIR, "data", "apps.json"), "r") as file:
    apps=json.load(file)

def open_application(app):
    app=app.lower().strip()

    if app in apps:
        try:
            path=apps[app]
            #handles speacial Windows URI schemes
            if path.startswith("ms-"):
                os.startfile(path)
            else:
                subprocess.Popen(path)
            return True
        except Exception as e:
            print(f"Error opening {app}: {e}")
            return False
    
    #Auto search common install locations
    search_paths=[
        f"C:\\Program Files\\**\\{app}.exe",
        f"C:\\Program Files (x86)\\**\\{app}.exe",
        f"C:\\Users\\thabo\\AppData\\Roaming\\**\\{app}.exe",
        f"C:\\Users\\thabo\\AppData\\Local\\**\\{app}.exe",
    ]

    for pattern in search_paths:
        results=glob.glob(pattern,recursive=True)
        if results:
            try:
                subprocess.Popen(results[0])
                return True
            except Exception as e:
                print(f"Error opening {app}: {e}")
                return False
    return False