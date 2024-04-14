import datetime

from pydantic import BaseModel


class SDataCreate(BaseModel):
    """Security data create schema"""
    timestamp: datetime.datetime
    source_ip: str
    destination_ip: str
    protocol: str
    source_port: str
    destination_port: str
    packet_length: str
    flags: str
    threat: str

    class Config:
        from_attributes = True


class SDataGet(BaseModel):
    """Security data get schema"""
    id: int

    timestamp: datetime.datetime
    source_ip: str
    destination_ip: str
    protocol: str
    source_port: str
    destination_port: str
    packet_length: str
    flags: str
    threat: str

    created_at: datetime.datetime

    class Config:
        from_attributes = True


class SDataList(BaseModel):
    """Security data get list schema"""
    items:  list[SDataGet]
    count: int

    class Config:
        from_attributes = True


class SEmail(BaseModel):
    """Schema to send email"""
    to_email: list[str]
    data: SDataCreate
