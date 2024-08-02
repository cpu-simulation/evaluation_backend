import sqlalchemy as sa
from sqlalchemy import URL
from sqlalchemy.orm import Session, declarative_base

import os

Base = declarative_base()

def get_db():
    DB = sa.create_engine(URL.create(
        drivername="mysql+pymysql",
        database=os.environ.get("MYSQL_DB"),
        host=os.environ.get("DB_URL", "mysql"),
        password=os.environ.get("MYSQL_PASSWORD"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        username=os.environ.get("MYSQL_USER"),
        ))
    Base.metadata.create_all(DB)
    session = Session(DB)

    return session
