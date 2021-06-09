from datetime import datetime
import sqlalchemy as sql
import sqlalchemy.orm as orm
from .db_initialize import DataBase


class User(DataBase):
    __tablename__ = 'users'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    name = sql.Column(sql.String, nullable=False)
    email = sql.Column(sql.String, nullable=False, unique=True, index=True)
    about = sql.Column(sql.String, nullable=True, default=None)
    created_date = sql.Column(sql.TIMESTAMP, default=datetime.timestamp(datetime.now()),
                              nullable=False)
    tags = orm.relation("Tag", secondary="user_to_tags", backref="users")
    roles = orm.relation("Role", secondary="user_to_roles", backref="users")
    leading_projects = orm.relation("Project", back_population="user")  # тут мы содержим именно
    # те проекты, где пользователь - автор.(потому что если мы добавляем проект в
    # это поле, то у нас в таблице проектов author_id становится id этого юзера
