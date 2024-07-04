from sqlalchemy.orm import Session
from .models import Product, Company, ProjectPlate

from . import models, schemas

from app.schemas import ProjectCreate

def get_product(db: Session, product_id: int) -> Product | None:
    """получить products по id"""
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_all_products(db: Session, skip: int = 0, limit: int = 100) -> list[Product]:
    """получение всех products"""
    return db.query(models.Product).offset(skip).limit(limit).all()

#---------------------------------------------------------------------------------------
def create_product(db: Session, product: schemas.Product):
    """Фунция для отправки ПРОДУКТА в БД, нужно избавиться от введения ID!!!"""
    db_product = models.Product(id = product.id,
                                name = product.name,
                                desc = product.desc,
                                link = product.link,
                                pic = product.pic)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_job(db: Session, job: schemas.Job):
    """Фунция для отправки КОМПАНИИ в БД, нужно избавиться от введения ID!!!"""
    db_job = models.Company(#id = job.id,
                        name = job.name,
                        position=job.position,
                        link_job = job.link_job,
                        period = job.period,
                        ) #function = job.function
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def create_desc(db: Session, func_job: schemas.FunctionJob):
    """Фунция для отправки ОПИСАНИЯ ФУНКЦИИ ВЫПОЛНЯЕМОЙ В КОМПАНИИ в БД"""
    db_func_job = models.FunctionJob(job_id = func_job.job_id,
                                     description = func_job.description)
    db.add(db_func_job)
    db.commit()
    db.refresh(db_func_job)
    return db_func_job

def create_project(db: Session, project: schemas.Project):
    db_project = models.ProjectPlate(name = project.name,
                                     description = project.description,
                                     skills = project.skills,
                                     link = project.link)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

#---------------------------------------------------------------------------------------

def get_desc(db: Session, job_id: int):
    """Получить Job по id"""
    return db.query(models.FunctionJob).filter(models.FunctionJob.id == job_id).first()

def get_all_jobs(db: Session, skip: int = 0, limit: int = 100) -> list[Company]:
    """Получение списка работ"""
    return db.query(models.Company).offset(skip),limit(limit).all()

def get_job(db: Session, job_id: int) -> Company | None:
    """Получить Job по id"""
    return db.query(models.Company).filter(models.Company.id == job_id).first()

def get_company_by_id(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()

def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Company).offset(skip).limit(limit).all()

def get_functions_by_company_id(db: Session, company_id: int):
    return db.query(models.FunctionJob).filter(models.FunctionJob.job_id == company_id).all()

#---------------------------------------------------------------------------------------

def get_project(db: Session, project_id: int) -> models.ProjectPlate | None:
    return db.query(models.ProjectPlate).filter(models.ProjectPlate.id == project_id).first()

def get_projects(db: Session):
    return db.query(models.ProjectPlate).all()

def update_project(db: Session, project_id: int, project: schemas.ProjectCreate):
    db_project = db.query(models.ProjectPlate).filter(models.ProjectPlate.id == project_id).first()
    if db_project is None:
        return None
    db_project.name = project.name
    db_project.description = project.description
    db_project.skills = project.skills
    db_project.link = project.link
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = db.query(models.ProjectPlate).filter(models.ProjectPlate.id == project_id).first()
    if db_project is None:
        return None
    db.delete(db_project)
    db.commit()
    return db_project