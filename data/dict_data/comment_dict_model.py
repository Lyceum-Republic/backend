import pydantic
import datetime


class Comment(pydantic.BaseModel):
    id: int
    content: str
    author_id: int
    to_project_id: int
    like_or_not: bool
    date: datetime.datetime

    class Config:
        orm_mode = True
