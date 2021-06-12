import pydantic
from datetime import datetime
import typing


class NotificationBaseModel(pydantic.BaseModel):
    content: str
    date: datetime


class Notification(NotificationBaseModel):
    id: int
    author_id: int

    class Config:
        orm_node = True
