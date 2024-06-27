from sqlalchemy.orm import Session
from .models import Product, Job

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
    db_job = models.Job(id = job.id,
                        name = job.name,
                        link = job.link_job,
                        period = job.period,
                        function = job.function)

def get_all_jobs(db: Session, skip: int = 0, limit: int = 100) -> list[Job]:
    """Получение списка работ"""
    return db.query(models.Job).offset(skip),limit(limit).all()

def get_job(db: Session, job_id: int) -> Job | None:
    """Получить Job по id"""
    return db.query(models.Job).filter(models.Job.id == job_id).first()
