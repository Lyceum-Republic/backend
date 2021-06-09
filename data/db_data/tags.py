import sqlalchemy.orm as orm
import sqlalchemy as sql
from .db_initialize import DataBase

user_to_tags = sql.Table(
    'user_to_tags',
    DataBase.metadata,
    sql.Column('user', sql.Integer, sql.ForeignKey('users.id')),
    sql.Column('tags', sql.Integer, sql.ForeignKey('tags.id'))
)
role_to_tag = sql.Table(
    'role_to_tag',
    DataBase.metadata,
    sql.Column('role_id', sql.Integer, sql.ForeignKey('roles.id')),
    sql.Column('tag_id', sql.Integer, sql.ForeignKey('tags.id'))
)


class Tag(DataBase):
    __tablename__ = 'tags'

    id = sql.Column(sql.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    parent_id = sql.Column(sql.Integer, sql.ForeignKey('roles.id'), nullable=True, unique=False)
    name = sql.Column(sql.String, nullable=False)
