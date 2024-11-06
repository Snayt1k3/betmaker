from sqlalchemy import Column, String, Float, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum
from datetime import datetime

Base = declarative_base()


class EventStatus(enum.Enum):
    UNFINISHED = "unfinished"
    WIN_FIRST_TEAM = "win_first_team"
    WIN_SECOND_TEAM = "win_second_team"


class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, unique=True, index=True)
    odds = Column(Float, nullable=False)
    deadline = Column(DateTime, nullable=False)
    status = Column(Enum(EventStatus), default=EventStatus.UNFINISHED)

    def is_active(self) -> bool:
        """Check if the event is still open for betting (deadline not passed)."""
        return self.deadline > datetime.utcnow()
