from contextlib import asynccontextmanager
from src.application.services.event import EventService
from src.adapters.uow import UnitOfWork

class IoC:
    @asynccontextmanager
    async def event_service(self) -> EventService:
        uow = UnitOfWork()
        yield EventService(uow)
