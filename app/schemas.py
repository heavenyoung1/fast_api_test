# Описание моделей Pydantic

from pydantic import BaseModel

# --------------- ПРОДУКТ --------------- #

class ProductBase(BaseModel):
    name: str
    desc: str
    link: str
    pic: str

class ProductCreate(ProductBase):
    pass    

class Product(ProductBase):
    id: int 

# --------------- КОМПАНИЯ --------------- #

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

# --------------- ФУНКЦИИ РАБОТНИКА В КОМПАНИИ --------------- #

class FunctionJobBase(BaseModel):
    pass

class FunctionJob(FunctionJobBase):
    job_id: int
    description: str

# --------------- ПРОЕКТ --------------- #

class ProjectBase(BaseModel):
    name: str
    description: str
    skills: str
    link: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
