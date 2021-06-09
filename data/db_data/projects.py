import sqlalchemy as sql
import sqlalchemy.orm as orm
from .db_initialize import DataBase
from datetime import datetime as dt

users_to_projects = sql.Table(
    DataBase.metadata,
    sql.Column('user_id', sql.ForeignKey('users.id')),
    sql.Column('project_id', sql.ForeignKey('projects.id'))
)


class Project(DataBase):
    __tablename__ = 'projects'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    author_id = sql.Column(sql.Integer, sql.ForeignKey('users.id'), nullable=False)
    name = sql.Column(sql.String, nullable=False, unique=True)
    creation_date = sql.Column(sql.TIMESTAMP, default=dt.timestamp(dt.now()), nullable=False)
    milestones = orm.relation('Milestone', back_populates='project')
    user = orm.relation('User', secondary='users_to_projects', backref="projects")
    # TODO: сделать что-то с пользователями проекта, пока что только автор есть