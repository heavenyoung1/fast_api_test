from fastapi import FastAPI, Body, Path, HTTPException, Depends
from typing import Annotated
from app.models import CreateUser
import uvicorn
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import Sessionlocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI() #FastAPI - это класс, который наследуется от Starlette, app - это экземпляр класса.

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user





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
