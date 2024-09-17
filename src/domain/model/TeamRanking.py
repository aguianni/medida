import dataclasses


@dataclasses.dataclass(init=True)
class TeamRanking:
    team_id: str
    rank: str
    rank_points: str
