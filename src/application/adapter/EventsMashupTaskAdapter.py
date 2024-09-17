import asyncio
from fastapi import Depends

from src.application.port.input.EventsMashupTaskPort import EventsMashupTaskPort
from src.application.port.out.ScoreBoardServicePort import ScoreBoardServicePort
from src.application.port.out.TeamRanksServicePort import TeamRanksServicePort
from src.domain.model.Event import Event
from src.domain.model.League import League
from src.utils.Utils import to_date, to_time


def filter_by_date(event, start_date, end_date):
    if start_date is not None and end_date is not None:
        return start_date <= to_date(event["timestamp"]) <= end_date
    else:
        if start_date is not None:
            return start_date <= to_date(event["timestamp"])
        else:
            if end_date is not None:
                return to_date(event["timestamp"]) <= end_date
    return True


class EventsMashupTaskAdapter(EventsMashupTaskPort):
    def __init__(self, team_ranks_service: TeamRanksServicePort = Depends(),
                 score_board_service: ScoreBoardServicePort = Depends()):
        self.scoreBoardService = score_board_service
        self.teamRanksService = team_ranks_service

    async def run(self, league: League, start_date, end_date):

        rankings, scoreboards = await asyncio.gather(self.teamRanksService.run(league),
                                                     self.scoreBoardService.run(league))

        ranks = {}
        for ranking in rankings:
            ranks[ranking["teamId"]] = ranking

        li = []
        filtered = list(filter(lambda x: filter_by_date(x, start_date, end_date), scoreboards))
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
