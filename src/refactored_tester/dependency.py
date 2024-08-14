from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

from core.controller import Controller
from core.pod_handler import AbstractPodHandler
from core.queue_handler import AbstractQueueHandler

class DependencyContainer(BaseModel):
    model_config = {"arbitrary_types_allowed":True}

    TEST_QUEUE: str
    RABBITMQ_URL: str
    db: sessionmaker
    queue_handler: AbstractQueueHandler
    pod_handler: AbstractPodHandler