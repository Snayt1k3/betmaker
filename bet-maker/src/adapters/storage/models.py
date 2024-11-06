import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Numeric, Enum, Float
from sqlalchemy.ext.declarative import declarative_base

from src.application.enum import EventStatus


Base = declarative_base()


class Bet(Base):
    __tablename__ = "bets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    event_id = Column(Integer, nullable=False)  # Связь с событием
    amount = Column(Numeric(precision=10, scale=2), nullable=False)
    status = Column(Enum(EventStatus), default=EventStatus.UNFINISHED)    # Статус ставки (not_played, won, lost)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)  # Время создания ставки

    def __repr__(self):
        return f"<Bet(id={self.id}, event_id={self.event_id}, amount={self.amount}, status={self.status})>"
