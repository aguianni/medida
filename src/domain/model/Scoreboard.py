from src.domain.model.TeamInfo import TeamInfo


class Scoreboard:
    def __init__(self, id: str, timestamp: str, home: TeamInfo, away: TeamInfo):
        self.id = id
        self.timestamp = timestamp
        self.home = home
        self.away = away
