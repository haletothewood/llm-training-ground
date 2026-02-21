"""
Persist tasks to a local JSON file.
"""

import json
import os

STORAGE_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if not os.path.exists(STORAGE_FILE):
        return []
    try:
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(STORAGE_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
