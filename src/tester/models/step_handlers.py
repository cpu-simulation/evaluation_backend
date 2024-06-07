from abc import ABC, abstractmethod
from .models import ScenarioStep
import json

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
    
    def __init__(self, step: ScenarioStep) -> None:
        __step_input = json.loads(step.input)
        __step_exp_output = json.loads(step.output)
        __step_name = step.name
        __step_type = step.type

    def check(self) -> None:
        self.__check_input()
        self.__check_host()

    def pre_request(self):
        self.__provide_endpoint()
        self.__provide_data()
        

    def send_req(self):
        #TODO: send request to foo
        raise NotImplementedError()

    def validate(self) -> None:
        self.__validate_output()
        self.__validate_status_code()

    @property
    def report(self) -> tuple[bool, int]:
        #TODO: Not Implemented
        raise NotImplementedError()

    def run(self) -> tuple[bool, int]:
        self.check()
        self.pre_request()
        self.send_req()
        self.validate()
        return self.report

class Handler(BaseHandler):
    
    def __provide_endpoint(self):
        #TODO: Not Implemented
        raise NotImplementedError()
    
    def __provide_data(self):
        #TODO: Not Implemented
        raise NotADirectoryError()
    
    def __validate_output(self):
        #TODO: Not Implemented
        raise NotImplementedError()
    
    def __validate_status_code(self):
        #TODO: Not Implemented
        raise NotImplementedError()
