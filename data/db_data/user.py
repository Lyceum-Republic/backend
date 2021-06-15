from datetime import datetime
import sqlalchemy as sql
import sqlalchemy.orm as orm
from .db_initialize import DataBase


class User(DataBase):
    """Пользователь сайта"""
    __tablename__ = 'users'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True, index=True)
    name = sql.Column(sql.String, nullable=False)
    email = sql.Column(sql.String, nullable=False, unique=True, index=True)
    about = sql.Column(sql.String, nullable=True, default=None)
    created_date = sql.Column(sql.TIMESTAMP, default=datetime.timestamp(datetime.now()),
                              nullable=False)
    path_to_avatar = sql.Column(sql.String, default='img/default_avatar.jpg', nullable=False)
    # Тэги, обозначающие умения пользователей
    tags = orm.relation("Tag", secondary="user_to_tags", backref="users")
    roles = orm.relation("Role", secondary="user_to_roles", backref="users")
    # тут именно те проекты, где пользователь - автор.
    # (потому что если мы добавляем проект в это поле, то у нас в таблице
    # проектов author_id становится id этого юзера)
    leading_projects = orm.relation("Project", back_populates="user")
    written_comments = orm.relation("Feedback", back_populates="user")
    notifications = orm.relation("Notification", back_populates="user")
