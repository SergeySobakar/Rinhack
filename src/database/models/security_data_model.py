import datetime

from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column

from src.database.config import Base, intpk, created_at


class SecurityDataModel(Base):
    __tablename__ = "modelname"

    id: Mapped[intpk]

    timestamp: Mapped[datetime.date] = mapped_column(Date)
    source_ip: Mapped[str]
    destination_ip: Mapped[str]
    protocol: Mapped[str]
    source_port: Mapped[str]
    destination_port: Mapped[str]
    packet_length: Mapped[str]
    flags: Mapped[str]
    threat: Mapped[str]

    created_at: Mapped[created_at]
