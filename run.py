from src.scraper import (
    get_player_by_nickname,
    get_player_stats,
    get_match_history,
    get_match_details
)

def main():
    nickname = "ooyan"

    player = get_player_by_nickname(nickname)
    print(f"Player ID: {player['player_id']}")

    stats = get_player_stats(player["player_id"])
    print(f"Lifetime Stats: {stats.get('lifetime', {})}")

    matches = get_match_history(player["player_id"])
    for match in matches["items"]:
        print(f"Match ID: {match['match_id']}")
        details = get_match_details(match["match_id"])
        print(f"Map: {details['match']['game_map']}, Teams: {details['teams'].keys()}")

if __name__ == "__main__":
    main()
