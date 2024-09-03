import asyncio
from fastapi import Depends

from src.application.port.input.EventsMashupTaskPort import EventsMashupTaskPort
from src.application.port.out.ScoreBoardServicePort import ScoreBoardServicePort
from src.application.port.out.TeamRanksServicePort import TeamRanksServicePort
from src.domain.model.Event import Event
from src.domain.model.League import League
from src.utils.Utils import to_date, to_time


def filter_by_date(event, startDate, endDate):
    if startDate is not None and endDate is not None:
        return startDate <= to_date(event["timestamp"]) <= endDate
    else:
        if startDate is not None:
            return startDate <= to_date(event["timestamp"])
        else:
            if endDate is not None:
                return to_date(event["timestamp"]) <= endDate
    return True


class EventsMashupTaskAdapter(EventsMashupTaskPort):
    def __init__(self, teamRanksService: TeamRanksServicePort = Depends(),
                 scoreBoardService: ScoreBoardServicePort = Depends()):
        self.scoreBoardService = scoreBoardService
        self.teamRanksService = teamRanksService

    async def run(self, league: League, startDate, endDate):

        rankings, scoreboards = await asyncio.gather(self.teamRanksService.run(league),
                                                     self.scoreBoardService.run(league))

        ranks = {}
        for ranking in rankings:
            ranks[ranking["teamId"]] = ranking

        li = []
        filtered = list(filter(lambda x: filter_by_date(x, startDate, endDate), scoreboards))
        for scoreboard in filtered:
            li.append(
                Event(scoreboard["id"], to_date(scoreboard["timestamp"]), to_time(scoreboard["timestamp"]),
                      scoreboard["home"]["id"],
                      scoreboard["home"]["nickName"], scoreboard["home"]["city"],
                      ranks[scoreboard["home"]["id"]]["rank"],
                      ranks[scoreboard["home"]["id"]]["rankPoints"], scoreboard["away"]["id"],
                      scoreboard["away"]["nickName"], scoreboard["away"]["city"],
                      ranks[scoreboard["away"]["id"]]["rank"],
                      ranks[scoreboard["away"]["id"]]["rankPoints"]))

        return li
