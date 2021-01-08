import json
import requests
import pprint
import json
from typing import TypedDict, Union, List


API_URL_BASE = 'api.laligafantasymarca.com/api/v3'

TEAMS = {
    'atletico-de-madrid': 2,
    # 'athletic-club': 3,
    # 'fc-barcelona': 4,
    # 'real-betis': 5,
    # 'rc-celta': 6,
    # 'elche-c-f': 7,
    # 'getafe-cf': 9,
    # 'granada-cf': 10,
    # 'levante-ud': 11,
    # 'c-a-osasuna': 13,
    # 'real-madrid': 15,
    # 'real-sociedad': 16,
    # 'sevilla-fc': 17,
    # 'valencia-cf': 18,
    # 'r-valladolid-cf': 19,
    # 'villareal-cf': 20,
    # 'd-alaves': 21,
    # 'sd-eibar': 27,
    # 'sd-huesca': 63,
    # 'cadiz-cf': 162
}


class Player(TypedDict):
    playerID: int
    playerSlug: str
    isGoalkeeper: bool


class MinutesPlayed(TypedDict):
    minutes: int
    points: int

class Goals(TypedDict):
    goals: int
    points: int

class OwnGoals(TypedDict):
    goals: int
    points: int

class GoalsConceded(TypedDict):
    goals: int
    points: int

class GoalAssists(TypedDict):
    assists: int
    points: int

class OffTargetAttemptAssists(TypedDict):
    assists: int
    points: int

class PenaltyAreaEntries(TypedDict):
    entries: int
    points: int

class PenaltyWon(TypedDict):
    penalty: int
    points: int

class PenaltySaves(TypedDict):
    penalty: int
    points: int

class PenaltyFailed(TypedDict):
    penalty: int
    points: int

class PenaltyConceded(TypedDict):
    penalty: int
    points: int

class Saves(TypedDict):
    saves: int
    points: int

class EffectiveClearances(TypedDict):
    clearances: int
    points: int

class YellowCard(TypedDict):
    card: int
    points: int


class SecondYellowCard(TypedDict):
    card: int
    points: int


class RedCard(TypedDict):
    card: int
    points: int

class TotalScoringAttempts(TypedDict):
    attempts: int
    points: int

class WonContest(TypedDict):
    contest: int
    points: int

class BallRecovery(TypedDict):
    recovery: int
    points: int

class PossessionLost(TypedDict):
    lost: int
    points: int


class PlayerGameStats(TypedDict):
    week: int
    totalPoints: int
    minutesPlayed: MinutesPlayed
    goals: Goals
    ownGoals: OwnGoals
    goalsConceded: GoalsConceded
    goalsAssists: GoalAssists
    offTargetAttemptAssists: OffTargetAttemptAssists
    penaltyAreaEntries: PenaltyAreaEntries
    penaltyWon: PenaltyWon
    penaltySaves: PenaltySaves
    penaltyFailed: PenaltyFailed
    penaltyConceded: PenaltyConceded
    saves: Saves
    effectiveClearances: EffectiveClearances
    yellowCard: YellowCard
    secondYellowCard: SecondYellowCard
    redCard: RedCard
    totalScoringAttempts: TotalScoringAttempts
    wonContests: WonContest
    ballRecovery: BallRecovery
    possessionLost: PossessionLost
    marcaPoints: int


def get_team_player(api: str, team_id: int) -> Union[List[Player], None]:
    headers = {}
    payload = {}
    url = 'https://{}/player/team/{}'.format(api, team_id)
    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        result = []
        players = json.loads(response.content.decode('utf-8'))['players']
        for player in players:
            result.append(extract_player(player))
        return result
    else:
        return None


def extract_player(player: dict) -> Player:
    goalkeeper_id = 1
    return Player(
        playerID=player['id'],
        playerSlug=player['slug'],
        isGoalkeeper=player['positionId'] == goalkeeper_id
    )


def extract_player_stats(api: str, player: Player):
    player_slug = player['playerSlug']
    print('\nExtracting game stats for {}'.format(player_slug))
    headers = {}
    payload = {}
    url = 'https://{}/player/{}'.format(api, player['playerID'])
    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        full_player_stats = []
        player_stats = json.loads(response.content.decode('utf-8'))['playerStats']
        for stats in player_stats:
            full_player_stats.append(get_game_stats(stats))
        # pprint.pprint(full_player_stats)
        print(json.dumps(full_player_stats, indent=4, sort_keys=False))
        return full_player_stats
    else:
        return None


def get_game_stats(game_stats: dict) -> PlayerGameStats:
    stats = game_stats['stats']
    return PlayerGameStats(
        week=game_stats['weekNumber'],
        totalPoints=game_stats['totalPoints'],
        minutesPlayed=MinutesPlayed(
            minutes=stats['mins_played'][0],
            points=stats['mins_played'][1]
        ),
        goals=Goals(
            goals=stats['goals'][0],
            points=stats['goals'][1]
        ),
        ownGoals=OwnGoals(
            goals=stats['own_goals'][0],
            points=stats['own_goals'][1]
        ),
        goalsConceded=GoalsConceded(
            goals=stats['goals_conceded'][0],
            points=stats['goals_conceded'][1]
        ),
        goalsAssists=GoalAssists(
            assists=stats['goal_assist'][0],
            points=stats['goal_assist'][1]
        ),
        offTargetAttemptAssists=OffTargetAttemptAssists(
            assists=stats['offtarget_att_assist'][0],
            points=stats['offtarget_att_assist'][1]
        ),
        penaltyAreaEntries=PenaltyAreaEntries(
            entries=stats['pen_area_entries'][0],
            points=stats['pen_area_entries'][1]
        ),
        penaltyWon=PenaltyWon(
            penalty=stats['penalty_won'][0],
            points=stats['penalty_won'][1]
        ),
        penaltySaves=PenaltySaves(
            penalty=stats['penalty_save'][0],
            points=stats['penalty_save'][1]
        ),
        penaltyFailed=PenaltyFailed(
            penalty=stats['penalty_failed'][0],
            points=stats['penalty_failed'][1]
        ),
        penaltyConceded=PenaltyConceded(
            penalty=stats['penalty_conceded'][0],
            points=stats['penalty_conceded'][1]
        ),
        saves=Saves(
            saves=stats['saves'][0],
            points=stats['saves'][1]
        ),
        effectiveClearances=EffectiveClearances(
            clearances=stats['effective_clearance'][0],
            points=stats['effective_clearance'][1]
        ),
        yellowCard=YellowCard(
            card=stats['yellow_card'][0],
            points=stats['yellow_card'][1]
        ),
        secondYellowCard=SecondYellowCard(
            card=stats['second_yellow_card'][0],
            points=stats['second_yellow_card'][1]
        ),
        redCard=RedCard(
            card=stats['red_card'][0],
            points=stats['red_card'][1]
        ),
        totalScoringAttempts=TotalScoringAttempts(
            attempts=stats['total_scoring_att'][0],
            points=stats['total_scoring_att'][1]
        ),
        wonContests=WonContest(
            contest=stats['won_contest'][0],
            points=stats['won_contest'][1]
        ),
        ballRecovery=BallRecovery(
            recovery=stats['ball_recovery'][0],
            points=stats['ball_recovery'][1]
        ),
        possessionLost=PossessionLost(
            lost=stats['poss_lost_all'][0],
            points=stats['poss_lost_all'][1]
        ),
        marcaPoints=stats['marca_points'][1]
    )

def get_calendar(api: str, team_id: int):
    headers = {}
    payload = {}
    url = 'https://{}/calendar/team/{}'.format(api, team_id)
    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        print(response.content.decode('utf-8'))

playerListStats = []

for teamSlug, teamID in TEAMS.items():
    playerList = get_team_player(API_URL_BASE, teamID)
    get_calendar(API_URL_BASE, teamID)
    # for player in playerList:
    #     playerListStats.append(extract_player_stats(API_URL_BASE, player))
