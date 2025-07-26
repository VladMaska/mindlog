# mindlog.py
import json
from datetime import datetime

DB_PATH = "mindlog.json"

def load_entries():
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_entries(entries):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

def add_entry(thought, mood):
    entries = load_entries()
    entries.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "thought": thought,
        "mood": mood
    })
    save_entries(entries)
