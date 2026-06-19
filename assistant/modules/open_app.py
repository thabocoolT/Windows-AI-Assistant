import subprocess
import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

json_path = os.path.join(
    BASE_DIR,
    "data",
    "apps.json"
)


with open(
    json_path,
    "r"
) as file:

    apps = json.load(file)


def open_application(app):

    app = app.lower()

    if app in apps:

        subprocess.Popen(
            apps[app]
        )

        return True

    return False