import uuid
from sqlalchemy.orm import Session

from src.pydantic_model.pydantic_model import Create_Dataset, Create_Project, Update_Dataset

from src.model.models import Dataset, Project


# def get_user(db: Session, user_id: int):
#     return db.query(annotations_model.User).filter(annotations_model.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(annotations_model.User).filter(annotations_model.User.email == email).first()


def get_projects(db: Session):
    return db.query(Project).all()


def create_project(db: Session, proj: Create_Project):
    db_user = Project(id=str(uuid.uuid4()),name=proj.name,description=proj.desc)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_datasets_in_project(db: Session,project_id:str):
    return db.query(Dataset).filter(Dataset.project_id == project_id).all()

def create_dataset(db: Session, dataset: Create_Dataset):
    db_project =  db.query(Project).filter(Project.id == dataset.project_id).first()
    if(db_project):
        db_dataset = Dataset(id=str(uuid.uuid4()),description=dataset.description,annotation_url=dataset.annotation_url,project_id=db_project.id,dataset_img_url=dataset.dataset_img_url,annotation_img_url=dataset.annotation_img_url)
        db.add(db_dataset)
        db.commit()
        db.refresh(db_dataset)
        return db_dataset
    else:
        return []

def update_dataset(db: Session, dataset: Update_Dataset):
    db_project =  db.get(Dataset,dataset.id)
    if(db_project):
        # db_dataset = Dataset(id=db_project.id,annotation_url=dataset.annotation_url,annotation_img_url=dataset.annotation_img_url)
        # new_data=dataset. model_dump(exclude_unset=True)
        # db_project.sqlmodel_update(new_data)
        db_project.annotation_img_url=dataset.annotation_img_url
        db_project.annotation_url=dataset.annotation_url
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project
    else:
        return []

def download_annotations_project(db: Session,project_id:str):
   db_project =  db.query(Dataset).filter(Dataset.project_id == project_id).all()
   response=[]
   if(db_project):
    for dataset in db_project:
        annot=dataset.annotation_url
        img=dataset.dataset_img_url
        dataobject={
            'annotations':annot,
            'img':img
        }
        response.append(dataobject)


    return response


# def create_annotation_files(db: Session, dataset:list[annotations_pydantic.Annotations_Files]):
#     for instance in dataset:
#         db_ann_file=annotations_model.Annotations_Files(index=instance['index'],filename=instance['filename'],annotations=instance['annotations'],png_file_path=instance['png_file_path'],plan_file=instance['plan_file'],dcm_tags=instance['dcm_tags'])
#         db.add(db_ann_file)
#         db.commit()
#         db.refresh(db_ann_file)
    
#     return True


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(annotations_model.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: annotations_pydantic.ItemCreate, user_id: int):
#     db_item = annotations_model.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item