import csv
import os
from typing import List, Dict

def save_to_csv(data: List[Dict], filename: str, folder: str = "data"):
    """Save a list of dictionaries to a CSV file."""
    if not data:
        return None

    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{filename}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return path
