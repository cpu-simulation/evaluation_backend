import json
from typing import Any
from sqlalchemy.orm import Session

from models.schema import QueueMessage
from models.db_interface import DataBaseInterface

from .pod_handler import AbstractPodHandler


class Controller:
    def __init__(self, db: Session, pod_handler_cls: type[AbstractPodHandler]) -> None:
        self.db = db
        self.pod_handler_cls = pod_handler_cls

    def __call__(self, body) -> Any:
        # [x] decode q msg
        msg = QueueMessage(**json.loads(body))

        # [TODO] query db for team and scenario and scenario_steps
        team = DataBaseInterface.find_team_by_id(session=self.db, team_id=msg.team_id)
        assert team is not None

        ...

        # FIXME: NOTICE: pod hostname base on name
        pod_handler = self.pod_handler_cls(host=f"{team.name}")
        # check if available
        pod_handler.connect()

        # test each scenario
        # append to results
        # save all results
