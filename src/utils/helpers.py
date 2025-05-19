from datetime import datetime

def format_date(iso_date: str) -> str:
    """Convert ISO string to readable date."""
    try:
        return datetime.fromisoformat(iso_date).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return iso_date

def safe_get(data: dict, *keys):
    """Safely get nested data without KeyError."""
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data
