from pydantic import BaseModel, EmailStr
from typing import Annotated
from fastapi import FastAPI, Body, Path


class CreateUser(BaseModel):
    username: Annotated[str, Path(min_length=5, max_length=20)]
    email: EmailStr 