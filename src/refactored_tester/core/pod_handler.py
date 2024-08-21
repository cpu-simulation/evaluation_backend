from abc import ABC, abstractmethod
import requests
import time


class AbstractPodHandler(ABC):
    host: str
    connection_checked:bool = False


    @abstractmethod
    def connect(self)->None:
        ...

class PodHandler(AbstractPodHandler):
    
    def connect(self):
        try:
            requests.head(f"http:/{self.host}:8000")
        except:
            time.sleep(5)
            raise Exception("host not reachable")
        else:
            self.connection_checked = True


class MockPodHandler(AbstractPodHandler):
    
    def connect(self) -> None:
        self.connection_checked = True