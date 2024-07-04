from static.text import dict_skills, list_skills

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from pathlib import Path
from starlette.responses import HTMLResponse, FileResponse
from sqlalchemy.orm import Session

from app.models import Product, Company, FunctionJob#, ProjectPlate
from app import crud, models, schemas
from app.database import SessionLocal, Base, engine

from typing import Optional

Base.metadata.create_all(bind=engine)

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

#------------------------POST-REQUESTS---------------------------------------------------

@app.post("/products", response_model=schemas.ProductCreate)
def create_product(product: schemas.Product, db: Session = Depends(get_db)) -> Product:
    """POST-запрос на отправку продукта в БД"""
    db_product = crud.get_product(db, product_id=product.id)
    if db_product:
        raise HTTPException(status_code=400, detail="ID already existed")
    return crud.create_product(db=db, product=product)

@app.post("/jobs", response_model=schemas.JobCreate)
def create_job(job: schemas.Job, db: Session = Depends(get_db)) -> Company:
    """POST-запрос на отправку компании в БД"""
    db_job = crud.get_job(db, job_id=job.id)
    if db_job:
        raise HTTPException(status_code=400, detail="ID already existed")
    return crud.create_job(db=db, job=job)

@app.post("/job-description", response_model=schemas.FunctionJob)
def create_job_func(function_job: schemas.FunctionJob, db: Session = Depends(get_db)) -> FunctionJob:
    """POST-запрос на отправку продукта в Описания Функций для Компании по её ID в БД"""
    db_func_job = crud.get_desc(db, func_job=function_job)
    if db_func_job: 
            raise HTTPException(status_code=400, detail="ID already existed")
    return crud.create_desc

@app.post("/projects/", response_model=schemas.ProjectCreate)
def create_project(project: schemas.Project, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project.id)
    if db_project:  
        raise HTTPException(status_code=400, detail="ID already existed")
    return crud.create_project


#------------------------GET-REQUEST---------------------------------------------------

@app.get("/")
def root():
    """GET-запрос на получение корневой страницы"""
    return{"message": "Hello World!"}

@app.get("/products", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[Product]:
    """GET-запрос на получение списка продуктов"""
    products = crud.get_all_products(db, skip=skip, limit=limit)
    return products

@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    """GET-запрос на получение продукта по ID"""
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product



@app.get("/person")
def get_image():
    """GET-запрос (Тестовый эндпоинт для получения изображения)"""
    image_path = Path("static/image_1.jpg")
    return FileResponse(image_path)

@app.get("/resume")
def redirect_to_resume():
    """GET-запрос на получение Резюме лежащего на GitHub"""
    return RedirectResponse("https://github.com/heavenyoung1/heavenyoung1/blob/main/Резюме.pdf")


#---------------------НИЖЕ ДОРАБОТКИ------------------------#

@app.get("/home", response_class=HTMLResponse)
def read_companies(request: Request, selected_company_id: int = None, db: Session = Depends(get_db)):
    companies = crud.get_companies(db)
    selected_company = None
    functions = []
    if selected_company_id:
        selected_company = crud.get_company_by_id(db, selected_company_id)
        functions = crud.get_functions_by_company_id(db, selected_company_id)

    skills = list_skills
    companies_item = crud.get_companies(db)
    #projects = db.query(ProjectPlate).all()

    return templates.TemplateResponse("index.html", {"request": request, 
                                                     "companies": companies, 
                                                     "selected_company": selected_company, 
                                                     "functions": functions,
                                                     "skills": skills,
                                                     "items": companies_item,
                                                     }) #"projects": projects

# ------------------------------------ На всякий случай ------------------------------------ #

# @app.get("/home", response_class=HTMLResponse)
# def root(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
#     """Прошлый метод получения главной страницы HOME"""
#     skills = list_skills
#     companies_item = crud.get_companies(db)
#     return templates.TemplateResponse("index.html", {"request": request, 
#                                                      "items": companies_item, 
#                                                      "skills": skills})