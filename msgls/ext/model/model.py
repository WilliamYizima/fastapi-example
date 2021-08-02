
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer, String, ForeignKey
from sqlalchemy.types import Date
from msgls.ext.db import Base

class StatusMessage(Base):
    __tablename__ = "status_message"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(Date)
    updated_at = Column(Date)
    status = Column(String)

    status_message = relationship("Message", back_populates="status")

class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(Date)
    name_template = Column(String)
    id_status = Column(Integer, ForeignKey("status_message.id"))

    status = relationship("StatusMessage", back_populates="status_message")
    # TODO implementar segmentação-id - for. key

class Segmentation(Base):
    __tablename__ = "segmentation"

    id = Column(Integer, primary_key=True, index=True)
    name_segmentation = Column(String)
    updated_at = Column(Date)

class Entrepreneur(Base):
    __tablename__ = "entrepreneur"

    id = Column(Integer, primary_key=True, index=True)
    name_entrepreneur = Column(String)
    phone_number = Column(String)
    #TODO implementar segmentação-id
    #TODO implementar histórico

class Historic(Base):
    __tablename__ = "historic"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(Date)
    updated_at = Column(Date)
    #TODO implementar message-id
    #TODO implementar entrepreneur-id



