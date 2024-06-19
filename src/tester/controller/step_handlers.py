from abc import ABC, abstractmethod
from ..models.models import ScenarioStep
import requests
from datetime import datetime
from core.exceptions import MyBaseException as SysException

class AbstractStepHandler(ABC):

    def __init__(self, step: ScenarioStep) -> None: ...

    @abstractmethod
    def check(self) -> None: ...

    @abstractmethod
    def validate(self) -> None: ...

    @abstractmethod
    def pre_request(self) -> None: ...

    @abstractmethod
    def send_req(self) -> None: ...

    @property
    @abstractmethod
    def report(self) -> tuple[bool, int]: ...


class BaseHandler(AbstractStepHandler):

    def __init__(self, step: ScenarioStep, url: str, status_code=200) -> None:
        if not isinstance(step, ScenarioStep):
            raise SysException(
                level=40,
                msg=f"models.step_handler.BaseHandler {step} is not a step instance"
                )
        self.__step_input = step.input
        self.__step_exp_output = step.output
        self.__step_name = step.name
        self.__step_type = step.type
        self.url = url
        self.__exp_status_code = status_code

    def check(self) -> None:
        self.__check_host()

    def __check_host(self):
        try:
            requests.head(self.url)
        except:
            raise SysException(
                level=30,
                msg=f"[HostNotReachable]: cant reach host: {self.url}"
            )

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
        response = self.method(self.url + self.endpoint, **self.data)
        self.response_time = datetime.now() - start_time
        self.response: requests.Response = response

    def validate(self) -> bool:
        a = self.__validate_output()
        b = self.__validate_status_code()
        self.__is_valid = a and b

    def __validate_output(self) -> bool:
        response = self.response.json()
        if response != self.__step_exp_output:
            return False
        return True

    def __validate_status_code(self) -> bool:
        if self.response.status_code != self.__exp_status_code:
            return False
        return True

    @property
    def report(self) -> tuple[bool, int]:
        return self.__is_valid, self.response_time

    def run(self) -> tuple[bool, int]:
        self.check()
        self.pre_request()
        self.send_req()
        self.validate()
        return self.report


class Handler(
    BaseHandler,
):
    def __init__(self, step: ScenarioStep, url: str) -> None:
        super().__init__(step, url)
