from dataclasses import dataclass


@dataclass
class RequestUrl:
    raw: str
    protocol: str
    host: list[str]
    path: list[str]