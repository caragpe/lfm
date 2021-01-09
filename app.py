from players.playerTypes import Team
from players.player import get_team_player, get_player_stats

API_URL_BASE = 'api.laligafantasymarca.com/api/v3'


TEAMS = [
    Team(teamSlug='atletico-de-madrid', teamID=2),
    # Team(teamSlug='athletic-club', teamID=3),
    # Team(teamSlug='fc-barcelona', teamID=4),
    # Team(teamSlug='real-betis', teamID=5),
    # Team(teamSlug='rc-celta', teamID=6),
    # Team(teamSlug='elche-c-f', teamID=7),
    # Team(teamSlug='getafe-cf', teamID=9),
    # Team(teamSlug='granada-cf', teamID=10),
    # Team(teamSlug='levante-ud', teamID=11),
    # Team(teamSlug='c-a-osasuna', teamID=13),
    # Team(teamSlug='real-madrid', teamID=15),
    # Team(teamSlug='real-sociedad', teamID=16),
    # Team(teamSlug='sevilla-fc', teamID=17),
    # Team(teamSlug='valencia-cf', teamID=18),
    # Team(teamSlug='r-valladolid-cf', teamID=19),
    # Team(teamSlug='villareal-cf', teamID=20),
    # Team(teamSlug='d-alaves', teamID=21),
    # Team(teamSlug='sd-eibar', teamID=27),
    # Team(teamSlug='sd-huesca', teamID=63),
    # Team(teamSlug='cadiz-cf', teamID=162)
]

playerListStats = []

for lfmTeam in TEAMS:
    playerList = get_team_player(API_URL_BASE, lfmTeam)
    for player in playerList:
        playerListStats.append(get_player_stats(API_URL_BASE, player))
