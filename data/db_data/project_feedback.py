import sqlalchemy as sql
import sqlalchemy.orm as orm
from .db_initialize import DataBase
from datetime import datetime as dt


class Feedback(DataBase):
    """Фидбек к проектам. Схожий принцип у комментариев на itch.io"""
    __tablename__ = 'projects_feedback'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False, index=True)
    author_id = sql.Column(sql.Integer, sql.ForeignKey('users.id'), nullable=False, unique=False)
    to_project_id = sql.Column(sql.Integer, sql.ForeignKey('projects.id'), nullable=False)
    content = sql.Column(sql.String, nullable=True)
    like_or_not = sql.Column(sql.Boolean, nullable=False)
    wrote_date = sql.Column(sql.DateTime, default=dt.now(), nullable=False)
    user = orm.relation('User')
    project = orm.relation('Project')
