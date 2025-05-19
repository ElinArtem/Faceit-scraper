# faceit_scraper/scraper.py

import requests
from .config import ENDPOINTS, HEADERS, DEFAULT_GAME, MAX_MATCHES
from .storage import save_to_json

def get_player_by_nickname(nickname: str) -> dict:
    """
    Fetch basic player info using FACEIT nickname.
    """
    url = ENDPOINTS["player_by_nickname"].format(nickname=nickname)
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()


def get_player_stats(player_id: str, game: str = DEFAULT_GAME) -> dict:
    """
    Fetch lifetime stats for a given player and game.
    """
    url = ENDPOINTS["player_stats"].format(player_id=player_id, game=game)
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()


def get_match_history(player_id: str, game: str = DEFAULT_GAME, limit: int = MAX_MATCHES) -> dict:
    """
    Fetch match history for a player.
    """
    url = ENDPOINTS["player_history"].format(player_id=player_id)
    params = {
        "game": game,
        "limit": limit
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def get_full_match_history(player_id: str):
    if not player_id:
        return []

    all_matches = []
    offset = 0
    limit = 100  # Max allowed per call

    while True:
        matches = get_match_history(player_id, offset=offset, limit=limit)
        if not matches:
            break
        all_matches.extend(matches)
        offset += limit

    return all_matches


def get_match_details(match_id: str) -> dict:
    """
    Fetch details for a specific match.
    """
    url = ENDPOINTS["match_details"].format(match_id=match_id)
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_match_stats(match_id: str, player_id: str) -> dict | None:
    """
    Fetch detailed statistics for a specific player in a Faceit match.

    Args:
        match_id (str): Unique identifier of the match.
        player_id (str): Unique identifier of the player.

    Returns:
        dict | None: Dictionary with match info, team stats, and player stats,
                     or None if the player is not found or the match is unsupported.
    """
    url = ENDPOINTS["match_stats"].format(match_id=match_id)
    
    # Fetch match statistics
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        match_data = response.json()
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch match stats for {match_id}: {e}")
        return None
    except ValueError:
        print(f"[ERROR] Invalid JSON response for match {match_id}")
        return None

    rounds = match_data.get("rounds", [])
    if not rounds:
        print(f"[WARN] No rounds found for match {match_id}")
        return None

    # Use only the first round (standard format)
    round_data = rounds[0]
    match_stats = round_data.get("round_stats", {})

    # Search for player in both teams
    player_team_data = None
    player_stats = None
    teammates = []

    for team in round_data.get("teams", []):
        for player in team.get("players", []):
            if player.get("player_id") == player_id:
                player_team_data = team
                player_stats = player.get("player_stats", {})
                # Get teammates (excluding the main player)
                teammates = [
                    p for p in team["players"] if p["player_id"] != player_id
                ]
                break
        if player_team_data:
            break

    if not player_team_data or not player_stats:
        print(f"[INFO] Player {player_id} not found in match {match_id}")
        return None

    # Build final result
    return {
        "match_id": match_id,
        "date": round_data.get("started_at", "N/A"),
        "map": match_stats.get("Map", "Unknown"),
        "result": player_team_data.get("team_stats", {}).get("Result"),
        "score": player_team_data.get("team_stats", {}).get("Final Score"),
        "player": {
            "player_id": player_id,
            "nickname": next((p.get("nickname") for p in player_team_data["players"] if p["player_id"] == player_id), None),
            "stats": {
                "kills": player_stats.get("Kills"),
                "deaths": player_stats.get("Deaths"),
                "kd": player_stats.get("K/D Ratio"),
                "headshots": player_stats.get("Headshots %"),
                "mvps": player_stats.get("MVPs"),
                "kr_ratio": player_stats.get("K/R Ratio")
            }
        },
        "teammates": [
            {
                "player_id": mate["player_id"],
                "nickname": mate["nickname"],
                "stats": mate.get("player_stats", {})
            } for mate in teammates
        ]
    }