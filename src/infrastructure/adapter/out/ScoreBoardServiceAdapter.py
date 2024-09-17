import requests

from src.application.port.out.ScoreBoardServicePort import ScoreBoardServicePort
from src.domain.model.League import League


class ScoreBoardServiceAdapter(ScoreBoardServicePort):

    def __init__(self):
        self.base_url = "http://localhost:9000"

    async def run(self, league: League):
        response = requests.get(f"{self.base_url}/{league}/scoreboard")
        response.raise_for_status()
        return response.json()
