import logging
from fastapi import APIRouter, Depends, HTTPException

from src.application.port.input.EventsMashupTaskPort import EventsMashupTaskPort
from src.domain.model.League import League
from src.infrastructure.input.request.EventRequest import EventRequest

router = APIRouter()

LOG = logging.getLogger(__name__)
LOG.info("API is starting up")


@router.post("/events")
async def events_mashup(request: EventRequest, events_mashup_task: EventsMashupTaskPort = Depends()):
    LOG.info('Doing something')
    try:
        League[request.league]
    except:
        raise HTTPException(
            status_code=404,
            detail="League not found"
        )
    events = events_mashup_task.run(League[request.league], request.startDate, request.endDate)
    return await events
