import subprocess

def open_appliaction(app):
    apps={
        "chrome":
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    }
    
    if app in apps:
        subprocess.Popen(apps[app])