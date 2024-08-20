import os
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import pytest
from uuid import uuid4

from dependency import DependencyContainer
from models.models import Base
from models.schema import QueueMessage
from core.queue_handler import MockQueueHandler
from models.models import Team, Scenario
from core.pod_handler import MockPodHandler
from main import main


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


@pytest.fixture(scope="function")
def mock_di_container(mock_db):
    dic = DependencyContainer(
        db=mock_db,
        queue_handler=MockQueueHandler(),
        pod_handler=MockPodHandler
    )
    
    yield dic

    del dic




class TestClass:
    def setuper(self, mock_di_container) -> None:
        id=uuid4()
        team = Team(
            members=[],
            name="test",
            id=id
        )
        sc = Scenario(
            id=1,
            name="test_sc",
            weight=1
        )

        sessionmaker_obj: sessionmaker = mock_di_container.db
        
        with sessionmaker_obj.begin() as Session:
            Session.add(team)
            Session.add(sc)
            Session.commit()
        self.id = id

    def test_imp(self, mock_di_container):
        self.setuper(mock_di_container)
        msg = QueueMessage(
            host="pass",
            team_id=self.id
        )
        mock_di_container.queue_handler.some_data = [
        msg.model_dump_json()
        ]
        try:
            main(mock_di_container)
        except NotImplementedError:
            assert True
        except Exception as e:
            raise e