from abc import ABC, abstractmethod
from .models import ScenarioStep
import requests
from datetime import datetime

class AbstractStepHandler(ABC):
    
    def __init__(self, step:ScenarioStep) -> None:
        ...
    
    @abstractmethod
    def check(self) -> None:
        ...

    @abstractmethod
    def validate(self) -> None:
        ...

    @abstractmethod
    def pre_request(self) -> None:
        ...

    @abstractmethod
    def send_req(self) -> None:
        ...

    @property
    @abstractmethod
    def report(self) -> tuple[bool, int]:
        ...


class BaseHandler(AbstractStepHandler):
    
    def __init__(self, step: ScenarioStep, url:str) -> None:
        if  not isinstance(step, ScenarioStep):
            raise Exception #TODO: Need a error handler and error class
        self.__step_input = step.input
        self.__step_exp_output = step.output
        self.__step_name = step.name
        self.__step_type = step.type
        self.url = url


    def check(self) -> None:
        self.__check_host()        

    def __check_host(self):
        try:
            requests.head(self.url)
        except:
            raise Exception #FIXME: valid error\

    def pre_request(self):
        self.__provide_endpoint()
        self.__provide_data()

    def __provide_data(self):
        if self.method == requests.get:
            return
        self.data = {**self.__step_input}


    def __provide_endpoint(self):
        d = {
            "M_R": ("memory/read", requests.get),
            "M_W": ("memory/write", requests.post),
            "R_W": ("register/write", requests.post),
            "R_R": ("register/read", requests.get),
            "C_C": ("core/compile", requests.post),
            "C_E": ("core/execute", requests.post),
        }
        self.endpoint, self.method = d[self.__step_type]

    def send_req(self):
        start_time = datetime.now()
        response = self.method(self.url+self.endpoint, **self.data)
        self.response_time = datetime.now() - start_time
        self.response = response

    def validate(self) -> None:
        self.__validate_output()
        self.__validate_status_code()

    @property
    def report(self) -> tuple[bool, int]:
        return self.__is_valid , self.response_time

    def run(self) -> tuple[bool, int]:
        self.check()
        self.pre_request()
        self.send_req()
        # self.validate()
        return self.report

class Handler(
    BaseHandler,
    ):
    def __init__(self, step: ScenarioStep, url: str) -> None:
        super().__init__(step, url)
