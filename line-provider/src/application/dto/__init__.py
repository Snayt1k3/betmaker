from datetime import datetime

from pydantic import BaseModel

from src.adapters.storage.models import EventStatus


class EventDTO(BaseModel):
    odds: float
    id: int
    status: EventStatus
    deadline: datetime
