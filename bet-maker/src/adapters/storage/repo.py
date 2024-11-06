from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.adapters.storage.models import Bet
from src.application.interface import IRepository


class BetRepository(IRepository[Bet]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, **kwargs) -> Bet:
        """Создает новое событие и сохраняет его в базе данных."""
        bet = Bet(id=None, **kwargs)
        self.session.add(bet)
        return bet

    async def get_by_id(self, id: int) -> Optional[Bet]:
        """Возвращает событие по его идентификатору."""
        result = await self.session.execute(select(Bet).where(Bet.id == id))
        return result.scalars().first()

    async def filter_by(self, **kwargs) -> List[Bet]:
        result = await self.session.execute(select(Bet).filter_by(**kwargs))
        return result.scalars().all()

    async def update(self, id: str, **kwargs) -> Optional[Bet]:
        """Обновляет статус события по его идентификатору."""
        query = update(Bet).where(Bet.id == id).values(**kwargs).returning(Bet)
        res = await self.session.execute(query)

        return res.first()

    async def delete(self, id: int) -> None:
        """Удаляет событие по его идентификатору."""
        bet = await self.get_by_id(id)

        if bet:
            await self.session.delete(bet)

    async def update_many(self, *args, **kwargs) -> List[Bet]:
        query = update(Bet).where(*args).values(**kwargs).returning(Bet)
        res = await self.session.execute(query)
        return res.scalars().all()
