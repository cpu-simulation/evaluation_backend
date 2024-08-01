from sqlalchemy.orm import Session
from .queue_handler import AbstractQueueHandler


class DependencyContainer:
    db: Session
    queue_handler: AbstractQueueHandler