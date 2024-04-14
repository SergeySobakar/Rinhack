from typing import Sequence

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.security_data_model import SecurityDataModel
from src.schemas.data_mapper import to_pydantic_model
from src.schemas.security_data_schemas import SDataGet


class SecurityDataRepository:
    @staticmethod
    async def create(data: dict, session: AsyncSession) -> SDataGet:
        """SQLAlchemy statement"""
        statement = insert(SecurityDataModel).values(**data).returning(SecurityDataModel)
        result = (await session.execute(statement)).scalar_one()
        return await to_pydantic_model(result.__dict__)

    @staticmethod
    async def find_all(limit: int, offset: int, session: AsyncSession) -> list[SDataGet]:
        """SQLAlchemy statement"""
        statement = select(SecurityDataModel).limit(limit).offset(offset)
        result = (await session.execute(statement)).scalars().all()
        return [await to_pydantic_model(r.__dict__) for r in result]

    @staticmethod
    async def find_by_id(id: int, session: AsyncSession) -> SDataGet | None:
        """SQLAlchemy statement"""
        statement = select(SecurityDataModel).where(SecurityDataModel.id == id)
        result = (await session.execute(statement)).scalar_one_or_none()
        if result is None:
            return None
        return await to_pydantic_model(result.__dict__)
