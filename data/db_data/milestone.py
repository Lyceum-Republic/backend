import sqlalchemy.orm as orm
from datetime import datetime as dt
import sqlalchemy as sql
from .db_initialize import DataBase


class Milestone(DataBase):
    """
    Отметка с несколькими задачами, которые относятся к проекту.
    Можно сравнить с релизом, имеющим свой дедлайн и задачи, относящиеся к нему
    """
    __tablename__ = 'milestones'

    id = sql.Column(sql.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True, index=True)
    name = sql.Column(sql.String, nullable=False, unique=False)
    deadline_date = sql.Column(sql.Date, nullable=False)
    project_id = sql.Column(sql.Integer, sql.ForeignKey('projects.id'))
    project = orm.relation("Project")
    tasks = orm.relation('Task', back_populates='milestone')
