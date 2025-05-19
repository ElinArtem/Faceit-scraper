# ==== API SETTINGS ====
FACEIT_API_KEY = "YOUR_API_KEY"
if not FACEIT_API_KEY:
    raise ValueError("FACEIT_API_KEY not found in environment variables.")

HEADERS = {
    "Authorization": f"Bearer {FACEIT_API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

BASE_URL = "https://open.faceit.com/data/v4"

# ==== API ENDPOINTS ====
ENDPOINTS = {
    "player_by_nickname": f"{BASE_URL}/players?nickname={{nickname}}",
    "player_stats": f"{BASE_URL}/players/{{player_id}}/stats/{{game}}",
    "player_history": f"{BASE_URL}/players/{{player_id}}/history",
    "match_details": f"{BASE_URL}/matches/{{match_id}}",
    "match_stats": f"{BASE_URL}/matches/{{match_id}}/stats"
}

# ==== OTHER CONSTANTS ====
DEFAULT_GAME = "cs2"
DEFAULT_REGION = "EU"
MAX_MATCHES = 50  # max cell of param is 100 
