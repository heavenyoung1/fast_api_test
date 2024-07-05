# Описание моделей SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    desc = Column(String)
    link = Column(String, unique=True)
    pic = Column(String)

class ProjectPlate(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255))
    skills: Mapped[str] = mapped_column(String(255))
    link: Mapped[str] = mapped_column(String(255))

class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, unique=True, index=True)
    position = Column(String)
    link_job = Column(String)
    period = Column(String)
    function = relationship("FunctionJob", back_populates="company", cascade="all, delete-orphan")

class FunctionJob(Base):
    __tablename__ = "functions_in_company"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("company.id"))
    description = Column(String)
    company = relationship("Company", back_populates="function")




