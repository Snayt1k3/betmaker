from datetime import datetime
from typing import List, Optional

from src.adapters.storage.models import Bet
from src.application.dto.bet import BetCreate
from src.application.enum import EventStatus
from src.application.interface import IUnitOfWork


class BetService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def create_bet(self, bet_data: BetCreate) -> Bet:
        """Создает новую ставку на событие."""
        async with self.uow:

            # Создаем ставку
            bet = await self.uow.bets.add(
                event_id=bet_data.event_id,
                amount=bet_data.amount,
                status=EventStatus.UNFINISHED,
                created_at=datetime.utcnow(),
            )
            return bet

    async def get_bet_by_id(self, bet_id: int) -> Optional[Bet]:
        """Возвращает ставку по её идентификатору."""
        async with self.uow:
            bet = await self.uow.bets.get_by_id(bet_id)
            if bet:
                return bet
            return None

    async def update_bet_status(self, bet_id: int, status: EventStatus) -> Bet:
        """Обновляет статус ставки."""
        async with self.uow:
            bet = await self.uow.bets.get_by_id(bet_id)
            if not bet:
                raise ValueError("Ставка не найдена")

            # Обновляем статус
            updated_bet = await self.uow.bets.update(bet_id, status=status)

            return updated_bet

    async def list_bets_by_event(self, event_id: int) -> List[Bet]:
        """Возвращает список ставок для конкретного события."""
        async with self.uow:
            bets = await self.uow.bets.filter_by(event_id=event_id)
            return bets

    async def get_all_bets(self):
        async with self.uow as uow:
            bets = await uow.bets.filter_by()
        return bets

    async def update_bets_by_event(
        self, event_id: int, status: EventStatus
    ) -> List[Bet]:
        async with self.uow as uow:
            bets = await uow.bets.update_many(Bet.event_id == event_id, status=status)
        return bets
