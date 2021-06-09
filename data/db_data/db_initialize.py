import sqlalchemy as sql
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as dec
from sqlalchemy.orm import Session

DataBase = dec.declarative_base()
__factory = None


def global_init(db_file):  # тут пока что есть файл БД, потом будет url. Всё тестовое будет на sqlite
    global __factory
    if __factory:
        return
    if not db_file:
        raise Exception('No DB file specified')
    connection_string = f'sqlite:///{db_file}?check_same_thread=False'
    engine = sql.create_engine(connection_string, echo=False)
    __factory = orm.sessionmaker(bind=engine, autocommit=False, autoflush=False)
    from . import __all_models
    DataBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
