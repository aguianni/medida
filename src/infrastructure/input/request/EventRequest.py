from pydantic import BaseModel
from typing import Optional


class EventRequest(BaseModel):
    league: Optional[str]
    startDate: Optional[str] = None
    endDate: Optional[str] = None
