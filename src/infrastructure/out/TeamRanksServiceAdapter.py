import requests

from src.application.port.out.TeamRanksServicePort import TeamRanksServicePort
from src.domain.model.League import League


class TeamRanksServiceAdapter(TeamRanksServicePort):

    def __init__(self):
        self.base_url = "http://localhost:9000"

    async def run(self, league: League):
        response = requests.get(f"{self.base_url}/{league}/team-rankings")
        response.raise_for_status()
        return response.json()
