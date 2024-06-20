# Описание моделей Pydantic

from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    desc: str
    link: str
    pic: str

class ProductCreate(ProductBase):
    pass    

class Product(ProductBase):
    id: int 