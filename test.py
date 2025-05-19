import requests
import json

API_KEY = 'f57d591e-0f6c-4da9-b34f-edf6894d7751'  # Replace with your actual key
BASE_URL = 'https://open.faceit.com/data/v4'

headers = {
    'Authorization': f'Bearer {API_KEY}'
}


def save_json(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
    

def get_player_id(nickname):
    url = f'https://open.faceit.com/data/v4/players?nickname={nickname}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('player_id')
    else:
        print(response.text)
        return None

def get_match_history(player_id, game='cs2', offset=0, limit=20):
    url = f'https://open.faceit.com/data/v4/players/{player_id}/history'
    params = {
        'game': game,
        'offset': offset,
        'limit': limit  # Max 100 per request
    }
    response = requests.get(url, headers=headers, params=params)
    result = []
    if response.status_code == 200:
        for r in response:
            result.append(r.get("match_id"))
        return result
    else:
        print(response.text)
        return []


def get_full_match_history(nickname):
    player_id = get_player_id(nickname)
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

# Example usage
all_matches = get_full_match_history('ooyan')
save_json(all_matches, "test.json")
print(f"Total matches found: {len(all_matches)}")

