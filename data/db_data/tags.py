import sqlalchemy.orm as orm
import sqlalchemy as sql
from .db_initialize import DataBase

# Пользователь указывает список тэгов, которые описывают его умения
user_to_tags = sql.Table(
    'user_to_tags',
    DataBase.metadata,
    sql.Column('user', sql.Integer, sql.ForeignKey('users.id')),
    sql.Column('tags', sql.Integer, sql.ForeignKey('tags.id'))
)
# Для роли указывается список тэгов, соответствующий ей
role_to_tag = sql.Table(
    'role_to_tag',
    DataBase.metadata,
    sql.Column('role_id', sql.Integer, sql.ForeignKey('roles.id')),
    sql.Column('tag_id', sql.Integer, sql.ForeignKey('tags.id'))
)


class Tag(DataBase):
    """
    Базовый элемент на сайте для поиска, разделения задач в проекте и
    обозначения навыков пользователя. Тэги представляют собой древовидную
    структуру, т.е. есть общий тэг родитель и дочерние тэги
    """
    __tablename__ = 'tags'

    id = sql.Column(sql.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True, index=True)
    parent_id = sql.Column(sql.Integer, sql.ForeignKey('roles.id'), nullable=True, unique=False)
    name = sql.Column(sql.String, nullable=False)
