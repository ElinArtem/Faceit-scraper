import json
from typing import Any, Dict, List, Optional
from pathlib import Path


def read_json(file_path: str | Path) -> Optional[Dict | List]:
    """
    Read and parse a JSON file.
    
    Args:
        file_path (str | Path): Path to the JSON file
        
    Returns:
        Optional[Dict | List]: Parsed JSON data as dictionary or list, None if error occurs
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file {file_path}: {str(e)}")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return None


def read_json_safe(file_path: str | Path, default: Any = None) -> Any:
    """
    Safely read and parse a JSON file with a default value if reading fails.
    
    Args:
        file_path (str | Path): Path to the JSON file
        default (Any, optional): Default value to return if reading fails. Defaults to None.
        
    Returns:
        Any: Parsed JSON data or default value if reading fails
    """
    result = read_json(file_path)
    return result if result is not None else default
