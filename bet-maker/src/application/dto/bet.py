from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, condecimal

from src.application.enum import EventStatus


class BetCreate(BaseModel):
    event_id: int
    amount: condecimal(
        gt=0, max_digits=10, decimal_places=2
    )  # Проверка на положительное число с двумя знаками после запятой
    status: EventStatus = EventStatus.UNFINISHED  # Статус будет из Enum

    class Config:
        orm_mode = True


class BetRead(BaseModel):
    id: int
    event_id: int
    amount: Decimal
    status: EventStatus
    created_at: datetime

    class Config:
        orm_mode = True
