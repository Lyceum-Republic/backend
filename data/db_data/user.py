from datetime import datetime
import sqlalchemy as sql
import sqlalchemy.orm as orm
from .db_initialize import DataBase


class User(DataBase):
    __tablename__ = 'users'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    name = sql.Column(sql.String, nullable=False)
    email = sql.Column(sql.String, nullable=False, unique=True, index=True)
    about = sql.Column(sql.String, nullable=True)
    created_date = sql.Column(sql.TIMESTAMP, default=datetime.timestamp(datetime.now()),
                              nullable=False)
    tags = orm.relation("Tags", secondary="User_to_Tag", backref="user")
    roles = orm.relation("Roles", secondary="User_to_Role", backref="user")
    
