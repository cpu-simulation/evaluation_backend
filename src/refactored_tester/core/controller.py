import json
from typing import Any
from sqlalchemy.orm import Session

from models.models import Scenario
from models.schema import QueueMessage
from models.db_interface import DataBaseInterface

from .pod_handler import AbstractPodHandler


class Controller:
    def __init__(self, db: Session, pod_handler: AbstractPodHandler) -> None:
        self.db = db
        self.pod_handler = pod_handler

    def __call__(self, body) -> Any:
        # [x] decode q msg
        msg = QueueMessage(**json.loads(body))

        # [TODO] query db for team and scenario and scenario_steps
        team = DataBaseInterface.find_team_by_id(session=self.db, team_id=msg.team_id)
        assert team is not None

        ...

        #[x]: init pod handler and check connection
        # FIXME: NOTICE: pod hostname base on name
        self.pod_handler.host = msg.host or f"http://{team.name}:8000"
        pod_handler = self.pod_handler
        # check if available
        pod_handler.connect()

        scenarios = DataBaseInterface.find_scenarios(session=self.db)
        for scenario in scenarios:
            pod_handler.test(scenario)
        # test each scenario
        # append to results
        # save all results
    def test(self, scenario: Scenario, pod_handler: AbstractPodHandler):
        steps = DataBaseInterface.find_scenario_steps(session=self.db, scenario_id=scenario.id)
        for step in steps:
            ...