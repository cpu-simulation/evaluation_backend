import pika, os, sys
from test import *
from config import Base, DB, RABBIT, TEST_QUEUE, Session
from models import Team
from mixin import ConsumerMixin
import json

mock = json.dumps({"team_id": "5de00e9e-cc32-4e98-bb24-e289917f674e"})


def main():
    try:

        Base.metadata.create_all(DB)
        consumer = Consumer(host=RABBIT, queue=TEST_QUEUE)
        consumer.callback(None, None, None, mock)
        # consumer.start_consuming()

    except KeyboardInterrupt:
        print("[INTERRUPTED]: keyboard interrupt")
        try:
            sys.exit(0)
        except:
            os._exit(0)


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
    main()
