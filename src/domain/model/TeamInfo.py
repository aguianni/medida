import dataclasses


@dataclasses.dataclass(init=True)
class TeamInfo:
    id: str
    nick_name: str
    city: str
