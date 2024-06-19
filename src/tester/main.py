import logging.config
import pika, os, sys
from test import *
from config import Base, DB, RABBIT, TEST_QUEUE, setup_logging
from mixin import ConsumerMixin
import json
import logging
MOCK = json.dumps({"team_id": "7c90d362-c443-40da-b428-fab41656dd0f"})  #FIXME
logger = logging.getLogger(__name__)

def main():
    try:
        Base.metadata.create_all(DB)
        consumer = Consumer(host=RABBIT, queue=TEST_QUEUE)
        consumer.callback(None, None, None, MOCK) #FIXME
        # consumer.start_consuming()

    except KeyboardInterrupt:
        logger.error("INTERRUPTED: keyboard interrupt")
        try:
            sys.exit(0)
        except:
            os._exit(0)
    except Exception as e:
        logger.error(e)
        raise e


class Consumer(ConsumerMixin):
    __connection_host: str
    __queue: str
    __inited = False

    def __init__(self, host, queue) -> None:
        self.__connection_host = host
        self.__queue = queue

    def connect(self):
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.__connection_host)
        )
        self.__channel = self.__connection.channel()
        self.__channel.basic_consume(
            queue=self.__queue, on_message_callback=self.callback
        )
        self.__inited = True

    def callback(self, ch, method, properties, body):
        return super().callback(body)

    def start_consuming(self):
        assert self.__inited, "Consumer not initialized"
        self.__channel.start_consuming()


if __name__ == "__main__":
    setup_logging()
    main()
