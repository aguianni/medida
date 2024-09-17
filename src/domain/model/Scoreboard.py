import dataclasses

from src.domain.model.TeamInfo import TeamInfo


@dataclasses.dataclass(init=True)
class Scoreboard:
    id: str
    timestamp: str
    home: TeamInfo
    away: TeamInfo
