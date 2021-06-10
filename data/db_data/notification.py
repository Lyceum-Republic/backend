import sqlalchemy as sql
import sqlalchemy.orm as orm
from datetime import datetime as dt
from .db_initialize import DataBase


class Notification(DataBase):
    __tablename__ = 'notifications'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True, nullable=False)
    to_user = sql.Column(sql.Integer, sql.ForeignKey('users.id'), nullable=False)
    content = sql.Column(sql.String, nullable=False)
    date = sql.Column(sql.DateTime, default=dt.now(), nullable=False)
    user = orm.relation('User')