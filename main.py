import os
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from src.pydantic_model.pydantic_model import Create_Project
from src.services import crud
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import src.model.models as models
from database import SessionLocal, engine
from src.controller import controllers



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# app.include_routeer(file_upload.router)
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




app.include_router(
  controllers.router, 
  prefix="/v2/project", 
  tags=["projects"]
)