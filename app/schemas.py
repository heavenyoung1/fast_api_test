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
    name: str
    position: str
    link_job: str  
    period: str
    function: list[str] #было list, так должно быть в pydantic

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    
class FunctionJob(BaseModel):
    id: int
    description: str

    class Config:
        orm_mode = True

