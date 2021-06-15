import sqlalchemy as sql
import sqlalchemy.orm as orm
from .db_initialize import DataBase

# Для каждой роли присутствуют свои задачи
roles_to_task = sql.Table(
    DataBase.metadata,
    sql.Column('role_id', sql.ForeignKey('roles.id')),
    sql.Column('task_id', sql.ForeignKey('tasks.id'))
)


class Task(DataBase):
    """
    Задачи, которые относятся к цели (см. документацию Milestone).
    Задачи не могут относится конкретно к проекту, а только к Mileston'у)
    """
    __tablename__ = 'tasks'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True, index=True)
    milestone_id = sql.Column(sql.Integer, sql.ForeignKey('milestones.id'), nullable=False)
    deadline = sql.Column(sql.Date, default=sql.ForeignKey('milestones.deadline_date'), nullable=False)
    name = sql.Column(sql.String, nullable=False, unique=False)
    is_public = sql.Column(sql.Boolean, default=True)
    is_completed = sql.Column(sql.Boolean, default=False)
    milestone = orm.relation('Milestone')