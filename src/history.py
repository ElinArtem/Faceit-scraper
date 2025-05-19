import requests
from .config import ENDPOINTS, HEADERS, DEFAULT_GAME, MAX_MATCHES, BASE_URL
from .scraper import get_player_by_nickname

def get_match_history(player_id, game=DEFAULT_GAME, offset=0, limit=20):
    url = f'https://open.faceit.com/data/v4/players/{player_id}/history'
    params = {
        'game': game,
        'offset': offset,
        'limit': limit  # Max 100 per request
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        print(response.text)
        return []


def get_full_match_history(nickname):
    player_id = get_player_by_nickname(nickname).get('player_id')
    if not player_id:
        return []

    all_matches = []
    offset = 0
    limit = MAX_MATCHES  # Max allowed per call

    while True:
        matches = get_match_history(player_id, offset=offset, limit=limit)
        if not matches:
            break
        all_matches.extend(matches)
        offset += limit

    return all_matches

def get_match_stats(match_id, player_id):
    """
    Get match statistics for a specific player in a match.
    
    Args:
        match_id (str): The ID of the match
        player_id (str): The ID of the player to get stats for
        
    Returns:
        dict: Dictionary containing match stats, team stats, player stats, and teammate info
        None: If there's an error or player not found
    """
    url = f'{BASE_URL}/matches/{match_id}/stats'
    
    try:
        res = requests.get(url, headers=HEADERS)
        res.raise_for_status()  # Raise exception for bad status codes
    except requests.RequestException as e:
        print(f"Error fetching match {match_id}: {str(e)}")
        return {}

    try:
        match_data = res.json()
    except ValueError as e:
        print(f"Error parsing JSON for match {match_id}: {str(e)}")
        return {}

    # Get the first round data
    rounds = match_data.get('rounds', [])
    if not rounds:
        print(f"No rounds data found for match {match_id}")
        return {}
    
    round_data = rounds[0]
    match_stats = round_data.get('round_stats', {})
    
    # Find the player's team and stats
    player_team = None
    player_stats = None
    
    for team in round_data.get('teams', []):
        for player in team.get('players', []):
            if player.get('player_id') == player_id:
                player_team = team
                player_stats = player.get('player_stats', {})
                break
        if player_team:
            break
    
    if not player_team or not player_stats:
        print(f"Player {player_id} not found in match {match_id}")
        return {}
    
    # Get teammate information
    teammates = [
        player for player in player_team.get('players', [])
        if player.get('player_id') != player_id
    ]
    
    return {
        'player_id': player_id,
        'match_stats': match_stats,
        'team_stats': player_team.get('team_stats', {}),
        'player_stats': player_stats,
        'teammates': teammates
    }
