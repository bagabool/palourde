from dataclasses import dataclass
from typing import Optional


@dataclass
class RequestQuery:
    key: str
    value: str

@dataclass
class RequestUrl:
    raw: str
    query: Optional[list[RequestQuery]]