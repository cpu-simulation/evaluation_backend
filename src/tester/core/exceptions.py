from dataclasses import dataclass

@dataclass
class MyBaseException(Exception):
    level: int
    msg: str = "BaseException"

