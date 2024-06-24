from enum import Enum
from static.text import list_skills

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from pathlib import Path
from starlette.responses import HTMLResponse, FileResponse
from sqlalchemy.orm import Session

from app.models import Product
from app import crud, models, schemas
from app.database import SessionLocal, engine

class ModelName(str, Enum):
    about = "About"
    experience = "Experience"
    work = "work"
    contact = "Contact"
    resume = "Resume"

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My first test app made on FastAPI",
    description="Creator HeavenYoung",
    version="0.1",
)

app.mount("/static", StaticFiles(directory="static"), name="static") #Import Static Files (FastAPI | Starlette)
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products", response_model=schemas.ProductCreate)
def create_product(product: schemas.Product, db: Session = Depends(get_db)) -> Product:
    db_product = crud.get_product(db, product_id=product.id)
    if db_product:
        raise HTTPException(status_code=400, detail="ID already existed")
    return crud.create_product(db=db, product=product)

@app.get("/products", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[Product]:
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

@app.get("/home", response_class=HTMLResponse)
def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/person")
def get_image():
    image_path = Path("static/image_1.jpg")
    return FileResponse(image_path)

@app.get("/get_list_skills", response_class=HTMLResponse)
def get_list_skills(request: Request):
    return templates.TemplateResponse(request=Request, name="item.html")


@app.get("/resume")
def redirect_to_resume():
    return RedirectResponse("https://github.com/heavenyoung1/heavenyoung1/blob/main/Резюме.pdf")

