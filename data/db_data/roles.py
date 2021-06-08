import sqlalchemy as sql
import sqlalchemy.orm as orm
from .db_initialize import DataBase


roles_to_users = sql.Table(
    'roles_to_users',
    DataBase.metadata,
    sql.Column('users', sql.Integer, sql.ForeignKey('users.id')),
    sql.Column('role', sql.Integer, sql.ForeignKey('roles.id'))
)


class Role(DataBase):
    __tablename__ = 'roles'
    id = sql.Column(sql.Integer, primary_key=True, nullable=False, unique=True, index=True)
    project_id = sql.Column(sql.Integer, nullable=False)
    role_name = sql.Column(sql.String, nullable=False, unique=False)


