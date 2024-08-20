from abc import ABC, abstractmethod
import pika
import json
class AbstractQueueHandler(ABC):
    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def start_consuming(self):
        ...

    @abstractmethod
    def callback(self, ch, method, properties, body):
        ...

class PikaQueueHandler(AbstractQueueHandler):
    def __init__(self, host:str, queue:str, callback_func: callable = None) -> None:
        self.__connection_host = host
        self.__queue = queue
        self.callback_func = callback_func

    def connect(self):
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.__connection_host)
        )
        self.__channel = self.__connection.channel()
        self.__channel.basic_consume(
            queue=self.__queue, on_message_callback=self.callback
        )
        self.__inited = True

    def start_consuming(self):
        assert self.__inited, "Consumer not initialized"
        self.__channel.start_consuming()

    def callback(self, ch, method, properties, body):
        assert self.__inited, "Consumer not initialized"
        self.callback_func(body)


class MockQueueHandler(AbstractQueueHandler):
    some_data: list

    def __init__(self, callback_func: callable = None, *args, **kwargs) -> None:
        self.callback_func = callback_func
        self.__inited = False
        
    def connect(self):
        self.__inited = True
    

    def callback(self, ch=None, method=None, properties=None, body=None):
        assert self.__inited, "Consumer not initialized"
        self.callback_func(body)

    def start_consuming(self):
        for data in self.some_data:
            self.callback(body=data)