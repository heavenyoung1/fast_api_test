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
