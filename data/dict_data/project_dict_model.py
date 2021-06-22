from datetime import datetime
from comment_dict_model import Comment
import pydantic
import typing


class ProjectBaseModel(pydantic.BaseModel):
    name: str
    creation_date: datetime


class Project(ProjectBaseModel):
    id: int
    author_id: int
    comments: typing.List[Comment] = []

    class Config:
        orm_mode = True
