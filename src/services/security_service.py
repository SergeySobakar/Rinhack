from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.security_data_repository import SecurityDataRepository
from src.schemas.security_data_schemas import SDataCreate, SDataGet, SDataList


class SecurityDataService:
    def __init__(self, repository=SecurityDataRepository):
        self.repository = repository

    async def create(self, data: SDataCreate, session: AsyncSession) -> SDataGet:
        data_dict = data.model_dump()
        sec_data = await self.repository.create(data_dict, session)
        await session.commit()
        return sec_data

    async def find_all(self, limit: int, offset: int, session: AsyncSession) -> SDataList:
        sec_data = await self.repository.find_all(limit, offset, session)
        return SDataList(items=sec_data, count=len(sec_data))

    async def find_by_id(self, id: int, session: AsyncSession) -> SDataGet | None:
        sec_data = await self.repository.find_by_id(id, session)
        return sec_data
