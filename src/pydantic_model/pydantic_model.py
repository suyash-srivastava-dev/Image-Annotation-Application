from typing import Optional, Union

from pydantic import BaseModel, Json
from pyparsing import Any
from sqlalchemy import JSON


class Create_Project(BaseModel):
    # id :str 
    name : str
    desc: str

class Create_Dataset(BaseModel):
    # id :str 
    description : str
    annotation_url :  Json[Any]
    project_id : str
    dataset_img_url: str
    annotation_img_url: str


class Update_Dataset(BaseModel):
    id :str 
    annotation_url :  Json[Any]
    annotation_img_url: str

  