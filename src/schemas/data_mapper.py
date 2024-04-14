from src.schemas.security_data_schemas import SDataGet


async def to_pydantic_model(data: dict) -> SDataGet:
    return SDataGet(
        id=data["id"],
        timestamp=data["timestamp"],
        source_ip=data["source_ip"],
        destination_ip=data["destination_ip"],
        protocol=data["protocol"],
        source_port=data["source_port"],
        destination_port=data["destination_port"],
        packet_length=data["packet_length"],
        flags=data["flags"],
        threat=data["threat"],
        created_at=data["created_at"]
    )