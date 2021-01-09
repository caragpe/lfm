from typing import TypedDict


class Team(TypedDict):
    teamID: int
    teamSlug: str


class Player(TypedDict):
    playerID: int
    playerSlug: str
    team: Team
