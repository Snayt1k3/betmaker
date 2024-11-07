from contextlib import asynccontextmanager

from src.adapters.request import HttpClient
from src.application.services.event import EventService
from src.adapters.uow import UnitOfWork


class IoC:
    @asynccontextmanager
    async def event_service(self) -> EventService:
        req = HttpClient()
        uow = UnitOfWork()
        yield EventService(uow, req)
