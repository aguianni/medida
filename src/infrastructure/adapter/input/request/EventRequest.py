from pydantic import BaseModel
from typing import Optional

from src.domain.model.League import League


class EventRequest(BaseModel):
    league: League
    start_date: Optional[str] = None
    end_date: Optional[str] = None
