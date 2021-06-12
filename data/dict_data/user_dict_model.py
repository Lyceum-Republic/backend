import pydantic
from project_dict_model import Project
from notification_dict_model import Notification
from typing import List, Optional
from datetime import datetime


class UserBaseModel(pydantic.BaseModel):
    name: str
    email: str
    about: Optional[str] = None
    creation_date: datetime  # timestamp


class UserCreateModel(UserBaseModel):
    hashed_password: str


class User(UserBaseModel):
    id: int
    leading_projects: List[Project] = []
    written_comments: List[Notification] = []

    class Config:
        orm_mode = True
