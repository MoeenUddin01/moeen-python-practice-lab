import jose
import json
import os


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            data = json.load(file)
            return data
    else:
        return []


def save_data(filepath, data):
    if os.path.exists(filepath):
        with open(filepath, "w") as file:
            save_data = json.dump(data, indent=4)
