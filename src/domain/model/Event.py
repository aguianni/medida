import dataclasses


@dataclasses.dataclass(init=True)
class Event:
    event_id: str
    event_date: str
    event_time: str
    home_team_id: str
    home_team_nick_name: str
    home_team_city: str
    home_team_rank: str
    home_team_rank_points: str
    away_team_id: str
    away_team_nick_name: str
    away_team_city: str
    away_team_rank: str
    away_team_rank_points: str
