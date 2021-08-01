
from datetime import date
from pydantic import BaseModel
from enum import Enum

class StatusName(str, Enum):
    not_sended = "não enviado"
    sended = "enviado"
    delivered = "entregue"
    readed = "lido"

class StatusMessage(BaseModel):
    id: int
    created_at: date
    updated_at: date
    status: StatusName

    class Config:
        orm_mode = True