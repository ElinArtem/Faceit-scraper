from src.scraper import (
    get_player_by_nickname,
    get_player_stats,
    get_match_history,
    get_match_details
)
from src.history import (get_full_match_history, get_match_stats)
from src.utils import format_date
from src.storage import save_to_json
from time import sleep

def main():
    nickname = "NICKNAME"

    player = get_player_by_nickname(nickname)
    print(f'Found player: {nickname} ({player['player_id']})')

    stats = get_player_stats(player["player_id"])
    print(f"Lifetime Stats: {stats.get('lifetime', {})}")

    history = get_full_match_history(nickname)
    print(f"Total match in history: {len(history)}")

    history_stats = []
    for match in history:
        print(f'Fetching of match *{match['match_id']}* started!')

        stats = get_match_stats(match['match_id'], player['player_id'])
        stats['started_at'] = format_date(match.get("started_at"))
        stats['finished_at'] = format_date(match.get("finished_at"))

        history_stats.append(stats)

        sleep(0.5)

    save_to_json(history_stats, f"{nickname}_history_stats")

    



    

    

if __name__ == "__main__":
    main()
