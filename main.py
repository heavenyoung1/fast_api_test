from fastapi import FastAPI, Body, Path
from typing import Annotated
from models import CreateUser
import uvicorn

from .sql_app import crud, models, schemas
from .sql_app.database import Sessionlocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI() #FastAPI - это класс, который наследуется от Starlette, app - это экземпляр класса.

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/hello/")
def get_name(name: str = "World"):
    name = name.title()
    return {"message": f"Hello, {name}"}

@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "suscess",
        "name": user.username.title(),
        "email": user.email,
    }

@app.get("/items/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, le=999_000)]): #В Документации: Path-параметры и валидация числовых данных, ge - "greather or equal", le - "lower or equal" (1 - 999000)
    return {
        "item": {
            "item_id": item_id,
        }
    }

#if __name__ == "__main__":
    #uvicorn.run("main:app", reload=True) #Такая конструкция нужна для автоматического рестарта сервера во время разработки
