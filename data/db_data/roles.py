import sqlalchemy as sql
import sqlalchemy.orm as orm
from .db_initialize import DataBase

# У каждого пользователя может быть несколько ролей, а каждая роль относится
# к определённому проекту
user_to_roles = sql.Table(
    'user_to_roles',
    DataBase.metadata,
    sql.Column('user', sql.Integer, sql.ForeignKey('users.id')),
    sql.Column('role', sql.Integer, sql.ForeignKey('roles.id'))
)


class Role(DataBase):
    """
    Обозначает роль участника в проекте. Сама роль задаётся создаётся
    автором проекта, куда позже добавляется человек
    """
    __tablename__ = 'roles'
    id = sql.Column(sql.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True, index=True)
    project_id = sql.Column(sql.Integer, nullable=False)
    role_name = sql.Column(sql.String, nullable=False, unique=False)
    tags = orm.relation("Tag", secondary="role_to_tag", backref="roles")
    tasks = orm.relation("Taks", secondary="roles_to_task", backref="roles")
