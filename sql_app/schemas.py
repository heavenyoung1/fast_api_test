from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None # = None - значение по умолчанию

class ItemCreate(ItemBase):         #Не запутаться в = и : при определении моделей
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

