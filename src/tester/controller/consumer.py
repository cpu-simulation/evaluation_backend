import pika

from core.exceptions import MyBaseException
from .mixin import ConsumerMixin
import time
import logging

logger = logging.getLogger(__name__)


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
        assert self.__inited, "Consumer not initialized"
        err = super().callback(body)
        if err is None:
            self.__channel.basic_ack(delivery_tag=method.delivery_tag)
            return
        elif isinstance(err, MyBaseException):
            logger.warning("[FAILED_TO_TEST] failed to test. %s", err)
        elif isinstance(err, Exception):
            logger.error(f"[SystemError]: {err}")
        logger.info("sleep after failed")
        time.sleep(1.0)
        self.__channel.basic_nack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        assert self.__inited, "Consumer not initialized"
        self.__channel.start_consuming()
