from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from src.pydantic_model.pydantic_model import Create_Dataset, Create_Project, Update_Dataset

from src.services import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/projects")
def read_root(db: Session = Depends(get_db) ):
    '''
    Get all the Projects
    '''
    list_projects= crud.get_projects(db=db)
    return list_projects


@router.post("/createproject")
def create_project(user:Create_Project, db: Session=Depends(get_db)):
    '''
    Create a new project
    '''
    prj= crud.create_project(db,user)
    return prj

@router.get("/datasets/{project_id}")
def read_datasets_in_project(project_id:str,db: Session = Depends(get_db) ):
    '''
    Get all the Projects
    '''
    list_datasets= crud.get_datasets_in_project(project_id=project_id,db=db)
    return list_datasets

@router.get("/annotations/{project_id}")
def fetch_annotation_datasets_in_project(project_id:str,db: Session = Depends(get_db) ):
    '''
    Get all the Projects
    '''
    list_datasets= crud.download_annotations_project(project_id=project_id,db=db)
    return list_datasets



@router.post("/createdataset")
def create_dataset(dataset:Create_Dataset, db: Session=Depends(get_db)):
    '''
    Create a new dataset in a project
    '''
    dataset_created= crud.create_dataset(db,dataset)
    return dataset_created


@router.patch("/updateannotation")
def update_dataset(dataset:Update_Dataset, db: Session=Depends(get_db)):
    '''
    Create a new dataset in a project
    '''
    dataset_updated= crud.update_dataset(db,dataset)
    return dataset_updated

@router.get("/health")
def read_health():
   return {'status':'good'}
