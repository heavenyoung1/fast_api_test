# Описание моделей Pydantic

from pydantic import BaseModel

class ElementItem(BaseModel):
    id: int
    name: str
    desc: str
    link: str
    pic: str


class ElementItem(Base):
    """Представляет собой элемент портфолио"""
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    desc = Column(String)
    link = Column(String, unique=True)
    pic = Column(String)
