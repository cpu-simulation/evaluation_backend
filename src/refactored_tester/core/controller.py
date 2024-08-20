import json
from typing import Any
from sqlalchemy.orm import sessionmaker

from models.schema import QueueMessage
from models.db_interface import DataBaseInterface

from .pod_handler import AbstractPodHandler


class Controller:
    def __init__(self, db: sessionmaker, pod_handler_cls: type[AbstractPodHandler]) -> None:
        self.db = db
        self.pod_handler_cls = pod_handler_cls

    def __call__(self, body) -> Any:
        msg = QueueMessage(**json.loads(body))

        team = DataBaseInterface.find_team_by_id(Session=self.db, team_id=msg.team_id)
        assert team is not None

        pod_handler = self.pod_handler_cls()
        pod_handler.host = msg.host or f"{team.name}"
        pod_handler.connect()

        scenarios = DataBaseInterface.find_scenarios(Session=self.db)
        result = []

        for scenario in scenarios:
            result.append(self.test_scenario(scenario))
        
        self.save_results(result)

    def test_scenario(self, scenario):
        raise NotImplementedError("Test scenario has not been implemented")

    def save_result(self, result:list):
        raise NotImplementedError("save_result is not implemented")