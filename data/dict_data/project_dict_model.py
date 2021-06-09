from datetime import datetime
import pydantic
import typing


class ProjectBaseModel(pydantic.BaseModel):
    name: str
    creation_date: datetime


class Project(ProjectBaseModel):
    id: int
    author_id: int

    class Config:
        orm_mode = True
