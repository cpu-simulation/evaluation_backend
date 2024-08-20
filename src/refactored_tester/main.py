#! python

import os

from core.controller import Controller
from core.pod_handler import PodHandler
from config.database import get_db
from dependency import DependencyContainer
from core.queue_handler import PikaQueueHandler

def main(dp_container: DependencyContainer) -> None:
    # logic:
    # setup controller with db-handler and pod-handler
    # connect it to queue handler
    controller = Controller(
        db=dp_container.db,
        pod_handler_cls=dp_container.pod_handler
    )

    queue_handler = dp_container.queue_handler
    queue_handler.callback_func=controller
    
    queue_handler.connect()
    queue_handler.start_consuming()
    

if __name__=="__main__":
    TEST_QUEUE = os.environ.get("TEST_QUEUE", "Test_Queue")
    RABBITMQ_URL = os.environ.get("RABBITMQ_URL", "rabbitmq")

    dp_container = DependencyContainer(
        db=get_db(debug=True),
        pod_handler=PodHandler,
        queue_handler=PikaQueueHandler(
            host=RABBITMQ_URL,
            queue=TEST_QUEUE,
        ),
    )
    # main(dp_container)