# Описание моделей SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class ElementItem(Base):
    """Представляет собой элемент портфолио"""
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    desc = Column(String)
    link = Column(String, unique=True)
    pic = Column(String)
