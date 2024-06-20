from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import FileResponse

from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine, Base

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My first test app made on FastAPI",
    description="Author HeavenYoung",
    version="0.1",
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_all_products(db, skip=skip, limit=limit)
    return products

@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.get("/")
def root():
    return{"message": "Hello World!"}

@app.get("/home")
def get_home():
    return FileResponse("static/index.html")