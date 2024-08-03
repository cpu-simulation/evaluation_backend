import os

from core.controller import Controller
from core.pod_handler import PodHandler
from .config.database import get_db
from .dependency import DependencyContainer
from .core.queue_handler import PikaQueueHandler


def main(dp_container: DependencyContainer) -> None:
    # logic:
    # setup controller with db-handler and pod-handler
    # connect it to queue handler
    
    ...

if __name__=="__main__":
    dp_container = DependencyContainer()
    dp_container.db = get_db()
    dp_container.pod_handler = PodHandler()
    dp_container.controller = Controller(
        db=dp_container.db,
        pod_handler=dp_container.pod_handler
        )
    dp_container.queue_handler = PikaQueueHandler(
        host=os.environ.get("RABBITMQ_URL", "rabbitmq"),
        queue=os.environ.get("TEST_QUEUE", "Test_Queue"),
        callback=dp_container.controller
    )
    main(dp_container)