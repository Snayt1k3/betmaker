from pydantic import BaseModel

from src.application.enum import EventStatus


class EventDTO(BaseModel):
    odds: float
    id: int
    status: EventStatus
    deadline: int
