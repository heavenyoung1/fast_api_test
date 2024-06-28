from sqlalchemy.orm import Session
from .models import Product, Company

from . import models, schemas

def get_product(db: Session, product_id: int) -> Product | None:
    """получить products по id"""
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_all_products(db: Session, skip: int = 0, limit: int = 100) -> list[Product]:
    """получение всех products"""
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.Product):
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
    db_func_job = models.FunctionJob(job_id = func_job.id,
                                     description = func_job.description)
    db.add(db_func_job)
    db.commit()
    db.refresh(db_func_job)
    return db_func_job

def get_desc(db: Session, job_id: int):
    """Получить Job по id"""
    return db.query(models.FunctionJob).filter(models.FunctionJob.id == job_id).first()

def get_all_jobs(db: Session, skip: int = 0, limit: int = 100) -> list[Company]:
    """Получение списка работ"""
    return db.query(models.Company).offset(skip),limit(limit).all()

def get_job(db: Session, job_id: int) -> Company | None:
    """Получить Job по id"""
    return db.query(models.Company).filter(models.Company.id == job_id).first()
