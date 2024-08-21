from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

from core.pod_handler import AbstractPodHandler
from core.queue_handler import AbstractQueueHandler

class DependencyContainer(BaseModel):
    model_config = {"arbitrary_types_allowed":True}

    db: sessionmaker
    queue_handler: AbstractQueueHandler
    pod_handler: type[AbstractPodHandler]