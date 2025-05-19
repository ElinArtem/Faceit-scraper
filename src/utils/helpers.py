from datetime import datetime

def get_matchs_id(matchs_history):
    result = []
    for match in matchs_history:
        result.append(match.get('match_id'))
    return result

def format_date(date_str: str | int) -> str:
    """
    Convert date string or Unix timestamp to readable date format.
    
    Args:
        date_str (str | int): Date in ISO format or Unix timestamp
        
    Returns:
        str: Formatted date string (YYYY-MM-DD HH:MM) or original string if conversion fails
    """
    
    try:
        # Handle Unix timestamp
        if isinstance(date_str, (int, str)) and str(date_str).isdigit():
            return datetime.fromtimestamp(int(date_str)).strftime("%Y-%m-%d %H:%M")
        
        # Handle ISO format
        return datetime.fromisoformat(str(date_str)).strftime("%Y-%m-%d %H:%M")
    except Exception as e:
        print(f"Error formatting date {date_str}: {e}")
        return str(date_str)

def safe_get(data: dict, *keys):
    """Safely get nested data without KeyError."""
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data
