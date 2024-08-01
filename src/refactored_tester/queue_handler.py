from abc import ABC, abstractmethod
import pika

class AbstractQueueHandler(ABC):
    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def start_consuming(self):
        ...


class PikaQueueHandler:
    def __init__(self, host, queue) -> None:
        self.__connection_host = host
        self.__queue = queue

    def connect(self):
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.__connection_host)
        )       # ---> dependency
        self.__channel = self.__connection.channel()
        self.__channel.basic_consume(
            queue=self.__queue, on_message_callback=self.callback
        )
        self.__inited = True

    def start_consuming(self):
        assert self.__inited, "Consumer not initialized"
        self.__channel.start_consuming()
