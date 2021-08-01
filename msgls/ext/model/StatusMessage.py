
from sqlalchemy import Column,Integer, String
from sqlalchemy.types import Date
from msgls.ext.db import Base

class StatusMessage(Base):
    __tablename__ = "status_message"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(Date)
    updated_at = Column(Date)
    status = Column(String)