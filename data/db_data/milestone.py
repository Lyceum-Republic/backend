import sqlalchemy.orm as orm
from datetime import  datetime as dt
import sqlalchemy as sql
from .db_initialize import DataBase


class Milestone(DataBase):
    __tablename__ = 'milestones'

    id = sql.Column(sql.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    name = sql.Column(sql.String, nullable=False, unique=False)
    deadline_date = sql.Column(sql.Date, nullable=False)
    project_id = sql.Column(sql.Integer, sql.ForeignKey('projects.id'))
    project = orm.relation("Project")
    tasks = orm.relation('Task', back_populates='milestone')
