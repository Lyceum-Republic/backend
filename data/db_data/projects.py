import sqlalchemy as sql
import sqlalchemy.orm as orm
from .db_initialize import DataBase
from datetime import datetime as dt


class Project(DataBase):
    __tablename__ = 'projects'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    author_id = sql.Column(sql.Integer, sql.ForeignKey('users.id'), nullable=False)
    name = sql.Column(sql.String, nullable=False, unique=True)
    creation_date = sql.Column(sql.TIMESTAMP, default=dt.timestamp(dt.now()), nullable=False)
    milestones = orm.relation('Milestone', back_populates='project')
    user = orm.relation('User')
    # TODO: сделать что-то с пользователями проекта, пока что только автор есть