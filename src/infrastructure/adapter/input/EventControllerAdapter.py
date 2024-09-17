import logging

from fastapi import APIRouter, Depends

from src.application.port.input.EventsMashupTaskPort import EventsMashupTaskPort
from src.infrastructure.adapter.input.request.EventRequest import EventRequest

router = APIRouter()

LOG = logging.getLogger(__name__)
LOG.info("API is starting up")


@router.post("/events")
async def events_mashup(request: EventRequest, events_mashup_task: EventsMashupTaskPort = Depends()):
    LOG.info('Doing something')
    events = events_mashup_task.run(request.league, request.start_date, request.end_date)
    return await events
