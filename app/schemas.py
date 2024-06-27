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

class JobBase(BaseModel):
    id: int

class Job(JobBase):
    name: str
    position: str
    link_job: str  
    period: str
    function: str