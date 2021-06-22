import pydantic
from project_dict_model import Project
from notification_dict_model import Notification
from comment_dict_model import Comment
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
    written_comments: List[Comment] = []
    notifications: List[Notification] = ['Может быть какой-то вступительный текст']

    class Config:
        orm_mode = True
