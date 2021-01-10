import requests
import json
from typing import Union, List
from players.playerTypes import Player, Team
from gameStats.gameStats import get_game_stats

HEADERS = {}
PAYLOAD = {}


def get_team_player(api: str, team: Team) -> Union[List[Player], None]:
    url = 'https://{}/player/team/{}'.format(api, team['teamID'])
    response = requests.get(url, headers=HEADERS, data=PAYLOAD)
    if response.status_code == 200:
        result = []
        players = json.loads(response.content.decode('utf-8'))['players']
        for player in players:
            result.append(create_player(player, team))
        return result
    else:
        return None


def create_player(player: dict, team: Team) -> Player:
    return Player(
        playerID=player['id'],
        playerSlug=player['slug'],
        team=team
    )


def get_player_stats(api: str, player: Player):
    player_slug = player['playerSlug']
    print('\nExtracting game stats for {}'.format(player_slug))
    url = 'https://{}/player/{}'.format(api, player['playerID'])
    response = requests.get(url, headers=HEADERS, data=PAYLOAD)
    if response.status_code == 200:
        full_player_stats = []
        player_stats = json.loads(response.content.decode('utf-8'))['playerStats']
        for stats in player_stats:
            full_player_stats.append(get_game_stats(stats))
        # print(json.dumps(full_player_stats, indent=4, sort_keys=False))
        return full_player_stats
    else:
        return None

