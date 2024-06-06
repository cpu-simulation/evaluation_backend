from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable, Literal
import requests
from requests import Response
import time


class AbstractEngine(ABC):
    __func_dict: dict[str, Callable[[any], Response]]
    def __init__(
        self, action: Literal["Read", "Write"], _input: dict, output: dict, url: str
    ) -> None:
        assert action in self.__func_dict.keys
        self.__action = action
        self.__method = self.__func_dict.get(action)
        self.__input = _input
        self.__expected_output = output
        self.url = url

    @abstractmethod
    def check(self): ...

    def call_api(self, *args, **kwargs)-> Response:
        real_output = self.__method(url=f"{self.url}/{self.__endpoint}", *args, **kwargs)
        return real_output

    def __test(self, *args, **kwargs):
        start = time.time()        
        r = self.call_api(*args, **kwargs)
        end = time.time()
        self.response = r
        return (end - start) *1000

class MemoryEngine(AbstractEngine):
    __func_dict = {"Read": requests.get, "Write": requests.post}

    def __init__(self, action: Literal['Read', 'Write'], _input: dict, output: dict, url: str) -> None:
        super().__init__(action, _input, output, url)
        self.__endpoint = "memory/" + "read" if action == "Read" else "write" #FIXME: Bulk read and bulk write :(

    def __test(self, *args, **kwargs):
        return super().__test(*args, **kwargs)

    def __validate(self, content_check=False, raise_exception=False, response=200):
        self.errors = []
        try:
            content = self.response.json()
            if content_check:
                assert content == self.__expected_output
            assert response == self.response.status_code

        except Exception as exc:
            self.errors.append(exc)

        if self.errors and raise_exception:
            raise AssertionError(exc.__str__())

    def check(self):
        if self.__action == "Write":
            kwargs = {"data": input}
        token_time = self.__test(**kwargs)
        content_check = self.__action == "Read"
        self.__validate(raise_exception=True,
                        content_check=content_check
                        )
        return token_time