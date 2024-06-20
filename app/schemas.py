# Описание моделей Pydantic

from pydantic import BaseModel

class BaseProduct(BaseModel):
    id: int

class Product(BaseProduct):
    name: str
    desc: str
    link: str
    pic: str