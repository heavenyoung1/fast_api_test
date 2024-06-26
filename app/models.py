# Описание моделей SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    """Представляет собой элемент портфолио"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    desc = Column(String)
    link = Column(String, unique=True)
    pic = Column(String)

class Job(Base):
    """Опыт работы в разных компаниях"""
    __tablename__ = "job"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    position = Column(String)
    link_job = Column(String)
    period = Column(String)
    function = relationship("FunctionJob", back_populates="description")

class FunctionJob(Base):
    """Функции для конкретного места работы"""
    __tablename__ = "description-job"

    id = Column(Integer, primary_key=True)
    description = relationship("Job", back_populates="function")