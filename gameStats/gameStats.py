from gameStats.gameStatsType import MinutesPlayed, \
    Goals, \
    OwnGoals, \
    GoalsConceded, \
    GoalAssists, \
    OffTargetAttemptAssists, \
    PenaltyAreaEntries, \
    PenaltyWon, \
    PenaltySaves, \
    PenaltyConceded, \
    PenaltyFailed, \
    Saves, EffectiveClearances, \
    YellowCard, \
    SecondYellowCard, \
    RedCard, \
    TotalScoringAttempts, \
    WonContest, \
    BallRecovery, \
    PossessionLost, \
    PlayerGameStats


def get_minutes_played(game_stats: dict) -> MinutesPlayed:
    return MinutesPlayed(
        minutes=game_stats['mins_played'][0],
        points=game_stats['mins_played'][1]
    )


def get_goals(game_stats: dict) -> Goals:
    return Goals(
        goals=game_stats['goals'][0],
        points=game_stats['goals'][1]
    )


def get_own_goals(game_stats: dict) -> OwnGoals:
    return OwnGoals(
        goals=game_stats['own_goals'][0],
        points=game_stats['own_goals'][1]
    )


def get_goals_conceded(game_stats: dict) -> GoalsConceded:
    return  GoalsConceded(
        goals=game_stats['goals_conceded'][0],
        points=game_stats['goals_conceded'][1]
    )


def get_goals_assists(game_stats: dict) -> GoalAssists:
    return GoalAssists(
        assists=game_stats['goal_assist'][0],
        points=game_stats['goal_assist'][1]
    )


def get_off_target_attempts_assists(game_stats: dict) -> OffTargetAttemptAssists:
    return OffTargetAttemptAssists(
        assists=game_stats['offtarget_att_assist'][0],
        points=game_stats['offtarget_att_assist'][1]
    )


def get_penalty_area_entries(game_stats: dict) -> PenaltyAreaEntries:
    return PenaltyAreaEntries(
        entries=game_stats['pen_area_entries'][0],
        points=game_stats['pen_area_entries'][1]
    )


def get_penalty_won(game_stats: dict) -> PenaltyWon:
    return PenaltyWon(
        penalty=game_stats['penalty_won'][0],
        points=game_stats['penalty_won'][1]
    )


def get_penalty_saves(game_stats: dict) -> PenaltySaves:
    return PenaltySaves(
        penalty=game_stats['penalty_save'][0],
        points=game_stats['penalty_save'][1]
    )


def get_penalty_failed(game_stats: dict) -> PenaltyFailed:
    return PenaltyFailed(
        penalty=game_stats['penalty_failed'][0],
        points=game_stats['penalty_failed'][1]
    )


def get_penalty_conceded(game_stats: dict) -> PenaltyConceded:
    return PenaltyConceded(
        penalty=game_stats['penalty_conceded'][0],
        points=game_stats['penalty_conceded'][1]
    )


def get_saves(game_stats: dict) -> Saves:
    return Saves(
        saves=game_stats['saves'][0],
        points=game_stats['saves'][1]
    )


def get_effective_clearances(game_stats: dict) -> EffectiveClearances:
    return EffectiveClearances(
        clearances=game_stats['effective_clearance'][0],
        points=game_stats['effective_clearance'][1]
    )


def get_yellow_card(game_stats: dict) -> YellowCard:
    return YellowCard(
        card=game_stats['yellow_card'][0],
        points=game_stats['yellow_card'][1]
    )


def get_second_yellow_card(game_stats: dict) -> SecondYellowCard:
    return SecondYellowCard(
        card=game_stats['second_yellow_card'][0],
        points=game_stats['second_yellow_card'][1]
    )


def get_red_card(game_stats: dict) -> RedCard:
    return RedCard(
        card=game_stats['red_card'][0],
        points=game_stats['red_card'][1]
    )


def get_total_scoring_attempts(game_stats: dict) -> TotalScoringAttempts:
    return TotalScoringAttempts(
        attempts=game_stats['total_scoring_att'][0],
        points=game_stats['total_scoring_att'][1]
    )


def get_won_contest(game_stats: dict) -> WonContest:
    return WonContest(
        contest=game_stats['won_contest'][0],
        points=game_stats['won_contest'][1]
    )


def get_ball_recovery(game_stats: dict) -> BallRecovery:
    return BallRecovery(
        recovery=game_stats['ball_recovery'][0],
        points=game_stats['ball_recovery'][1]
    )


def get_possession_lost(game_stats: dict) -> PossessionLost:
    return PossessionLost(
        lost=game_stats['poss_lost_all'][0],
        points=game_stats['poss_lost_all'][1]
    )


def get_game_stats(current_game: dict) -> PlayerGameStats:
    game_stats = current_game['stats']
    return PlayerGameStats(
        week=current_game['weekNumber'],
        totalPoints=current_game['totalPoints'],
        minutesPlayed=get_minutes_played(game_stats),
        goals=get_goals(game_stats),
        ownGoals=get_own_goals(game_stats),
        goalsConceded=get_goals_conceded(game_stats),
        goalsAssists=get_goals_assists(game_stats),
        offTargetAttemptAssists=get_off_target_attempts_assists(game_stats),
        penaltyAreaEntries=get_penalty_area_entries(game_stats),
        penaltyWon=get_penalty_won(game_stats),
        penaltySaves=get_penalty_saves(game_stats),
        penaltyFailed=get_penalty_failed(game_stats),
        penaltyConceded=get_penalty_conceded(game_stats),
        saves=get_saves(game_stats),
        effectiveClearances=get_effective_clearances(game_stats),
        yellowCard=get_yellow_card(game_stats),
        secondYellowCard=get_second_yellow_card(game_stats),
        redCard=get_red_card(game_stats),
        totalScoringAttempts=get_total_scoring_attempts(game_stats),
        wonContests=get_won_contest(game_stats),
        ballRecovery=get_ball_recovery(game_stats),
        possessionLost=get_possession_lost(game_stats),
        marcaPoints=game_stats['marca_points'][1]
    )
