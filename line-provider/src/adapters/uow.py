from src.adapters.storage.repo import EventRepository
from src.adapters.db import get_session
from src.application.interface import IUnitOfWork


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = await get_session().__aenter__()
        self.events = EventRepository(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    async def commit(self):
        """Подтверждение транзакции."""
        await self.session.commit()

    async def rollback(self):
        """Откат транзакции."""
        await self.session.rollback()
