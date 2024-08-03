from sqlalchemy.orm import Session

from core.controller import Controller
from core.pod_handler import AbstractPodHandler
from core.queue_handler import AbstractQueueHandler

class DependencyContainer:
    db: Session
    queue_handler: AbstractQueueHandler
    pod_handler: AbstractPodHandler
    controller: Controller