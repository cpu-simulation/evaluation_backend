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
    controller = Controller(
        db=dp_container.db,
        pod_handler=dp_container.pod_handler
    )

    queue_handler = PikaQueueHandler(
        host=dp_container.RABBITMQ_URL,
        queue=dp_container.TEST_QUEUE,
        callback=controller
    )
    queue_handler.connect()
    queue_handler.start_consuming()
    

if __name__=="__main__":
    dp_container = DependencyContainer()
    dp_container.db = get_db()
    dp_container.pod_handler = PodHandler
    dp_container.TEST_QUEUE = os.environ.get("TEST_QUEUE", "Test_Queue")
    dp_container.RABBITMQ_URL = os.environ.get("RABBITMQ_URL", "rabbitmq")
    main(dp_container)