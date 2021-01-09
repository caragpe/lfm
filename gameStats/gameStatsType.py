from typing import TypedDict


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