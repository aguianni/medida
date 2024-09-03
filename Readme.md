# Medida

### For this project, I used a hexagonal (ports and adapters) architecture you can see the diagram on: 
    architecture.pdf

#### Domain: Here we have our business classes:

- Event
- League
- Scoreboard
- TeamInfo
- TeamRanking

#### Application: We define our tasks (adapters), input ports, and output ports:
- Adapter
    - EventsMashupTaskAdapter (EventsMashupTaskPort)
- Port
    - In
        - EventsMashupTaskPort
    - Out
        - ScoreBoardServicePort
        - TeamRanksServicePort

#### Infrastructure: We define our inputs and adapters for our output ports:
- In
    - EventController
- Out
    - ScoreBoardServiceAdapter (ScoreBoardServicePort)
    - TeamRanksServiceAdapter (TeamRanksServicePort)

## FastAPI
For the implementation, I used FastAPI (https://fastapi.tiangolo.com), utilizing dependency injection. 
Calls to external dependencies were made asynchronously to achieve better response times.

For testing, I used: pytest, AsyncClient and AsyncMock. You can test it with:

    src > pytest