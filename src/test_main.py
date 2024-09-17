import pytest
from httpx import AsyncClient
from unittest.mock import AsyncMock

from src.application.adapter.EventsMashupTaskAdapter import EventsMashupTaskAdapter
from src.application.port.input.EventsMashupTaskPort import EventsMashupTaskPort
from src.application.port.out.ScoreBoardServicePort import ScoreBoardServicePort
from src.application.port.out.TeamRanksServicePort import TeamRanksServicePort
from src.domain.model.League import League
from src.main import app


async def events_mashup_task_port_run_empty(league: League, startDate, endDate):
    return []


@pytest.mark.asyncio
async def test_empty_ok():
    app.dependency_overrides[EventsMashupTaskPort] = lambda: AsyncMock(run=events_mashup_task_port_run_empty)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/events", json={"league": "NFL"})
    assert response.status_code == 200
    assert response.json() == []
    app.dependency_overrides = {}


async def events_mashup_task_port_run_data(league: League, start_date, end_date):
    return [{
        "event_id": "5055c2a2-af68-4082-9834-ceb36dd0a807",
        "event_date": "2023-01-11",
        "event_time": "14:00:00",
        "home_team_id": "8da0c96d-7b3d-41f3-9e68-29607f3babcf",
        "home_team_nick_name": "Atlanta Falcons",
        "home_team_city": "Atlanta",
        "home_team_rank": 3,
        "home_team_rank_points": 33.4,
        "away_team_id": "ae5132a4-e4b2-4bda-9933-b75c542b8d35",
        "away_team_nick_name": "Arizona Cardinals",
        "away_team_city": "Arizona",
        "away_team_rank": 1,
        "away_team_rank_points": 100.3
    }]


@pytest.mark.asyncio
async def test_data_ok():
    app.dependency_overrides[EventsMashupTaskPort] = lambda: AsyncMock(run=events_mashup_task_port_run_data)
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/events", json={"league": "NFL"})
    assert response.status_code == 200
    assert response.json() == [{
        "event_id": "5055c2a2-af68-4082-9834-ceb36dd0a807",
        "event_date": "2023-01-11",
        "event_time": "14:00:00",
        "home_team_id": "8da0c96d-7b3d-41f3-9e68-29607f3babcf",
        "home_team_nick_name": "Atlanta Falcons",
        "home_team_city": "Atlanta",
        "home_team_rank": 3,
        "home_team_rank_points": 33.4,
        "away_team_id": "ae5132a4-e4b2-4bda-9933-b75c542b8d35",
        "away_team_nick_name": "Arizona Cardinals",
        "away_team_city": "Arizona",
        "away_team_rank": 1,
        "away_team_rank_points": 100.3
    }]
    app.dependency_overrides = {}


async def scoreboard_service_port_run_empty(league: League):
    return []


async def team_ranks_service_port_run_empty(league: League):
    return []


@pytest.mark.asyncio
async def test_injection_empty_ok():
    app.dependency_overrides[ScoreBoardServicePort] = lambda: AsyncMock(run=scoreboard_service_port_run_empty)
    app.dependency_overrides[TeamRanksServicePort] = lambda: AsyncMock(run=team_ranks_service_port_run_empty)
    app.dependency_overrides[EventsMashupTaskPort] = EventsMashupTaskAdapter
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/events", json={"league": "NFL"})
    assert response.status_code == 200
    assert response.json() == []
    app.dependency_overrides = {}


async def scoreboard_service_port_run_data(league: League):
    return [
        {
            "away": {
                "city": "Arizona",
                "id": "ae5132a4-e4b2-4bda-9933-b75c542b8d35",
                "nickName": "Arizona Cardinals"
            },
            "home": {
                "city": "Atlanta",
                "id": "8da0c96d-7b3d-41f3-9e68-29607f3babcf",
                "nickName": "Atlanta Falcons"
            },
            "id": "5055c2a2-af68-4082-9834-ceb36dd0a807",
            "timestamp": "2023-01-11T14:00:00Z"
        },
        {
            "away": {
                "city": "Atlanta",
                "id": "8da0c96d-7b3d-41f3-9e68-29607f3babcf",
                "nickName": "Atlanta Falcons"
            },
            "home": {
                "city": "Carolina",
                "id": "9ebdd9c1-b445-4076-afe1-5463cacc9138",
                "nickName": "Carolina Panthers"
            },
            "id": "d9c18865-f89d-41de-a42e-5e4bdc2b305a",
            "timestamp": "2023-02-28T21:30:00Z"
        },
        {
            "away": {
                "city": "Chicago",
                "id": "59a25bfb-e316-42c1-ac75-fc62aa34df48",
                "nickName": "Chicago Bears"
            },
            "home": {
                "city": "Detroit",
                "id": "28851743-d1b5-4653-9f25-bda3a386c825",
                "nickName": "Detroit Lions"
            },
            "id": "bf436983-3c42-4e45-893d-3f89d0ef3451",
            "timestamp": "2023-01-30T16:30:00Z"
        },
        {
            "away": {
                "city": "Carolina",
                "id": "9ebdd9c1-b445-4076-afe1-5463cacc9138",
                "nickName": "Carolina Panthers"
            },
            "home": {
                "city": "Dallas",
                "id": "2f784ca2-9964-4d95-8d0d-67e553a70c40",
                "nickName": "Dallas Cowboys"
            },
            "id": "7d6e1536-231a-4451-b40a-6bf0bcd2e7c3",
            "timestamp": "2023-03-08T18:30:00Z"
        },
        {
            "away": {
                "city": "Dallas",
                "id": "2f784ca2-9964-4d95-8d0d-67e553a70c40",
                "nickName": "Dallas Cowboys"
            },
            "home": {
                "city": "Chicago",
                "id": "59a25bfb-e316-42c1-ac75-fc62aa34df48",
                "nickName": "Chicago Bears"
            },
            "id": "2d98e984-1197-42c5-80a0-083667891f51",
            "timestamp": "2023-05-24T22:00:00Z"
        }
    ]


async def team_ranks_service_port_run_data(league: League):
    return [
        {
            "rank": 1,
            "rankPoints": 100.3,
            "teamId": "ae5132a4-e4b2-4bda-9933-b75c542b8d35"
        },
        {
            "rank": 3,
            "rankPoints": 33.4,
            "teamId": "8da0c96d-7b3d-41f3-9e68-29607f3babcf"
        },
        {
            "rank": 2,
            "rankPoints": 63.9,
            "teamId": "9ebdd9c1-b445-4076-afe1-5463cacc9138"
        },
        {
            "rank": 5,
            "rankPoints": 10.2,
            "teamId": "28851743-d1b5-4653-9f25-bda3a386c825"
        },
        {
            "rank": 4,
            "rankPoints": 18.76,
            "teamId": "59a25bfb-e316-42c1-ac75-fc62aa34df48"
        },
        {
            "rank": 6,
            "rankPoints": 11.01,
            "teamId": "2f784ca2-9964-4d95-8d0d-67e553a70c40"
        }
    ]


@pytest.mark.asyncio
async def test_injection_data_ok():
    app.dependency_overrides[ScoreBoardServicePort] = lambda: AsyncMock(run=scoreboard_service_port_run_data)
    app.dependency_overrides[TeamRanksServicePort] = lambda: AsyncMock(run=team_ranks_service_port_run_data)
    app.dependency_overrides[EventsMashupTaskPort] = EventsMashupTaskAdapter
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/events", json={"league": "NFL"})
    assert response.status_code == 200
    assert response.json() == [
        {
            "event_id": "5055c2a2-af68-4082-9834-ceb36dd0a807",
            "event_date": "2023-01-11",
            "event_time": "14:00:00",
            "home_team_id": "8da0c96d-7b3d-41f3-9e68-29607f3babcf",
            "home_team_nick_name": "Atlanta Falcons",
            "home_team_city": "Atlanta",
            "home_team_rank": 3,
            "home_team_rank_points": 33.4,
            "away_team_id": "ae5132a4-e4b2-4bda-9933-b75c542b8d35",
            "away_team_nick_name": "Arizona Cardinals",
            "away_team_city": "Arizona",
            "away_team_rank": 1,
            "away_team_rank_points": 100.3
        },
        {
            "event_id": "d9c18865-f89d-41de-a42e-5e4bdc2b305a",
            "event_date": "2023-02-28",
            "event_time": "21:30:00",
            "home_team_id": "9ebdd9c1-b445-4076-afe1-5463cacc9138",
            "home_team_nick_name": "Carolina Panthers",
            "home_team_city": "Carolina",
            "home_team_rank": 2,
            "home_team_rank_points": 63.9,
            "away_team_id": "8da0c96d-7b3d-41f3-9e68-29607f3babcf",
            "away_team_nick_name": "Atlanta Falcons",
            "away_team_city": "Atlanta",
            "away_team_rank": 3,
            "away_team_rank_points": 33.4
        },
        {
            "event_id": "bf436983-3c42-4e45-893d-3f89d0ef3451",
            "event_date": "2023-01-30",
            "event_time": "16:30:00",
            "home_team_id": "28851743-d1b5-4653-9f25-bda3a386c825",
            "home_team_nick_name": "Detroit Lions",
            "home_team_city": "Detroit",
            "home_team_rank": 5,
            "home_team_rank_points": 10.2,
            "away_team_id": "59a25bfb-e316-42c1-ac75-fc62aa34df48",
            "away_team_nick_name": "Chicago Bears",
            "away_team_city": "Chicago",
            "away_team_rank": 4,
            "away_team_rank_points": 18.76
        },
        {
            "event_id": "7d6e1536-231a-4451-b40a-6bf0bcd2e7c3",
            "event_date": "2023-03-08",
            "event_time": "18:30:00",
            "home_team_id": "2f784ca2-9964-4d95-8d0d-67e553a70c40",
            "home_team_nick_name": "Dallas Cowboys",
            "home_team_city": "Dallas",
            "home_team_rank": 6,
            "home_team_rank_points": 11.01,
            "away_team_id": "9ebdd9c1-b445-4076-afe1-5463cacc9138",
            "away_team_nick_name": "Carolina Panthers",
            "away_team_city": "Carolina",
            "away_team_rank": 2,
            "away_team_rank_points": 63.9
        },
        {
            "event_id": "2d98e984-1197-42c5-80a0-083667891f51",
            "event_date": "2023-05-24",
            "event_time": "22:00:00",
            "home_team_id": "59a25bfb-e316-42c1-ac75-fc62aa34df48",
            "home_team_nick_name": "Chicago Bears",
            "home_team_city": "Chicago",
            "home_team_rank": 4,
            "home_team_rank_points": 18.76,
            "away_team_id": "2f784ca2-9964-4d95-8d0d-67e553a70c40",
            "away_team_nick_name": "Dallas Cowboys",
            "away_team_city": "Dallas",
            "away_team_rank": 6,
            "away_team_rank_points": 11.01
        }
    ]
    app.dependency_overrides = {}


@pytest.mark.asyncio
async def test_injection_data_filter_ok():
    app.dependency_overrides[ScoreBoardServicePort] = lambda: AsyncMock(run=scoreboard_service_port_run_data)
    app.dependency_overrides[TeamRanksServicePort] = lambda: AsyncMock(run=team_ranks_service_port_run_data)
    app.dependency_overrides[EventsMashupTaskPort] = EventsMashupTaskAdapter
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/events", json={"league": "NFL",
                                                      "start_date": "2023-01-11",
                                                      "end_date": "2023-01-11"})
    assert response.status_code == 200
    assert response.json() == [
        {
            "event_id": "5055c2a2-af68-4082-9834-ceb36dd0a807",
            "event_date": "2023-01-11",
            "event_time": "14:00:00",
            "home_team_id": "8da0c96d-7b3d-41f3-9e68-29607f3babcf",
            "home_team_nick_name": "Atlanta Falcons",
            "home_team_city": "Atlanta",
            "home_team_rank": 3,
            "home_team_rank_points": 33.4,
            "away_team_id": "ae5132a4-e4b2-4bda-9933-b75c542b8d35",
            "away_team_nick_name": "Arizona Cardinals",
            "away_team_city": "Arizona",
            "away_team_rank": 1,
            "away_team_rank_points": 100.3
        }
    ]
    app.dependency_overrides = {}


@pytest.mark.asyncio
async def test_injection_data_bad_league_ok():
    app.dependency_overrides[ScoreBoardServicePort] = lambda: AsyncMock(run=scoreboard_service_port_run_data)
    app.dependency_overrides[TeamRanksServicePort] = lambda: AsyncMock(run=team_ranks_service_port_run_data)
    app.dependency_overrides[EventsMashupTaskPort] = EventsMashupTaskAdapter
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/events", json={"league": "NBA"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "enum",
                "loc": [
                    "body",
                    "league"
                ],
                "msg": "Input should be 'NFL'",
                "input": "NBA",
                "ctx": {
                    "expected": "'NFL'"
                }
            }
        ]
    }
    app.dependency_overrides = {}
