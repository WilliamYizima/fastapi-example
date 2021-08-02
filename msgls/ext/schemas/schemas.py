
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

class Message(BaseModel):
    id: int
    created_at: date
    name_template: str
    id_status: int

    class Config:
        orm_mode = True

class Segmentation(BaseModel):
    id: int
    name_segmentation: str
    updated_at: date

    class Config:
        orm_mode = True

class Entrepreneur(BaseModel):
    id: int
    name_entrepreneur: str
    phone_number: str

    class Config:
        orm_mode = True

class Historic(BaseModel):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True
