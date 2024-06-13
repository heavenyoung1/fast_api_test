from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr
from typing import Annotated
from fastapi import FastAPI, Body, Path
from .database import Base #Из нашего файла импортируем 

class CreateUser(BaseModel):
    username: Annotated[str, Path(min_length=5, max_length=20)]
    email: EmailStr 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner") #Вместо back_populates можно использовать backref, разобраться!!!!

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True) #Индексы нужны для ускорения выполнения запросов
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="itrems") #"Волшебный" атрибут, содержащий значения других таблиц, связанных с этой