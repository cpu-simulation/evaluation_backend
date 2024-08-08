import json
from typing import Any
from sqlalchemy.orm import Session

from models.schema import QueueMessage

class Controller:
    def __init__(self, db: Session, pod_handler) -> None:
        self.db = db
        self.pod_handler = pod_handler


    def __call__(self, body) -> Any:
        msg = QueueMessage(**json.loads(body))

