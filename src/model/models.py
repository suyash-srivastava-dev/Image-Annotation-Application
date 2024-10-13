import uuid
from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(String,default=str(uuid.uuid4()), primary_key=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    
    datasets = relationship("Dataset", back_populates="projects")


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(String,default=str(uuid.uuid4()), primary_key=True)
    dataset_img_url=Column(String)
    annotation_url=Column(JSON)
    annotation_img_url = Column(String)
    description = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))

    projects = relationship("Project", back_populates="datasets")
