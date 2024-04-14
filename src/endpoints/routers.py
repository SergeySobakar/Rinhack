from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from http import HTTPStatus

from src.database.config import get_async_session
from src.schemas.security_data_schemas import SDataCreate, SDataGet, SDataList, SEmail
from src.services.email_service import EmailService
from src.services.security_service import SecurityDataService


routers = APIRouter(prefix="/api/security-data")


@routers.post("/", response_model=SDataGet)
async def create_security_data(form_data: SDataCreate, session: AsyncSession = Depends(get_async_session)) -> SDataGet:
    request = await SecurityDataService().create(data=form_data, session=session)
    return request


@routers.get("/", response_model=SDataList)
async def get_all_security_data(limit: int = 20, offset: int = 0, session: AsyncSession = Depends(get_async_session)) -> SDataList:
    request = await SecurityDataService().find_all(limit, offset, session)
    return request


@routers.get("/{id}", response_model=SDataGet)
async def get_current_security_data(id: int, session: AsyncSession = Depends(get_async_session)) -> SDataGet:
    request = await SecurityDataService().find_by_id(id, session)
    if request is None:
        raise HTTPException(detail="Not found", status_code=HTTPStatus.NOT_FOUND)
    return request


@routers.post("/send-email")
async def send_email(data: SEmail):
    await EmailService().send(recipients_emails=data.to_email, msg_text="Выявлена угроза")
    return {"status": "successfully sent"}