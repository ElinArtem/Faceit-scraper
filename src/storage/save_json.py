import json
import os

def save_to_json(data, filename: str, folder: str = "data"):
    """Save data to a JSON file."""
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{filename}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return path
