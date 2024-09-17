from fastapi import FastAPI

from src.application.adapter.EventsMashupTaskAdapter import EventsMashupTaskAdapter
from src.application.port.input.EventsMashupTaskPort import EventsMashupTaskPort
from src.application.port.out.ScoreBoardServicePort import ScoreBoardServicePort
from src.application.port.out.TeamRanksServicePort import TeamRanksServicePort
from src.infrastructure.adapter.input.EventControllerAdapter import router as event_router
from src.infrastructure.adapter.out.ScoreBoardServiceAdapter import ScoreBoardServiceAdapter
from src.infrastructure.adapter.out.TeamRanksServiceAdapter import TeamRanksServiceAdapter

app = FastAPI()


# Inyecta el servicio como dependencia
@app.on_event("startup")
def startup_event():
    app.dependency_overrides[ScoreBoardServicePort] = ScoreBoardServiceAdapter
    app.dependency_overrides[TeamRanksServicePort] = TeamRanksServiceAdapter
    app.dependency_overrides[EventsMashupTaskPort] = EventsMashupTaskAdapter


app.include_router(event_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
