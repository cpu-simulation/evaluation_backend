import os
from models.models import Base
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import pytest


@pytest.fixture(scope="session")
def mock_db():

    MOCK_DB_URL = "sqlite:///./test_test.db"
    eng = sa.create_engine(MOCK_DB_URL)
    Base.metadata.create_all(eng)
    session = sessionmaker(eng)

    yield session

    Base.metadata.drop_all(eng)
    if os.path.exists("test_test.db"):
        os.remove("test_test.db")

