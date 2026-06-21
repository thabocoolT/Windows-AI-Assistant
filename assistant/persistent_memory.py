import json
import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE=os.path.join(BASE_DIR,"..", "data", "memory.json")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return{
            "user_name": "Prince Motau",
            "nichname": "Cool Tee",
            "preferences":{},
            "habits":[]
        }
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dumb(data, f, indent=4)

def get_user_name():
    return load_memory().get("user_name", "Prince")

def get_nickname():
    return load_memory().get("nickname", "Cool Tee")

def add_habit(habit):
    data = load_memory()
    if habit not in data["habits"]:
        data["habits"].append(habit)
        save_memory(data)

def set_preference(key, value):
    data = load_memory()
    data["preferences"][key] = value
    save_memory(data)

def get_preference(key):
    return load_memory()["preferences"].get(key)