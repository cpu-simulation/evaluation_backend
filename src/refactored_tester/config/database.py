import sqlalchemy as sa
from sqlalchemy import URL
from sqlalchemy.orm import Session
from models import Base
from functools import lru_cache
import os


@lru_cache
def get_db():
    DB_conf = {
        "drivername":"mysql+pymysql",
        "database": os.environ.get("MYSQL_DB"),
        "host":os.environ.get("DB_URL", "mysql"),
        "password":os.environ.get("MYSQL_PASSWORD"),
        "port":int(os.environ.get("MYSQL_PORT", "3306")),
        "username":os.environ.get("MYSQL_USER"),
        }
    DB = db_connection(**DB_conf)
    Base.metadata.create_all(DB)
    session = Session(DB)
    return session


def db_connection(**kwargs):
    return sa.create_engine(URL.create(
        **kwargs
    ))