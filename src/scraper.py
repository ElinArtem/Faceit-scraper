# faceit_scraper/scraper.py

import requests
from config import ENDPOINTS, HEADERS, DEFAULT_GAME, MAX_MATCHES
from storage import save_to_json

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


def get_match_details(match_id: str) -> dict:
    """
    Fetch details for a specific match.
    """
    url = ENDPOINTS["match_details"].format(match_id=match_id)
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

save_to_json(get_match_history("1e76eaf4-d549-4ab5-9e3e-041f02789828"), "test")