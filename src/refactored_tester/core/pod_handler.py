from abc import ABC, abstractmethod
import requests
import time


class AbstractPodHandler(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        ...
    @abstractmethod
    def connect(self)->None:
        ...

class PodHandler(AbstractPodHandler):
    def __init__(self, host:str, *args, **kwargs) -> None:
        self.host = host
        self.connection_checked = False
    
    def connect(self):
        try:
            requests.head(f"http:/{self.host}:8000")
        except:
            time.sleep(5)
            raise Exception("host not reachable")
        else:
            self.connection_checked = True
