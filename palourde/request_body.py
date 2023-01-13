from dataclasses import dataclass
from typing import Optional


@dataclass
class FormData:
    key: str
    type: str
    src: str


@dataclass
class RequestBodyOptionRaw:
    language: str


@dataclass
class RequestBodyOption:
    raw: RequestBodyOptionRaw


@dataclass
class RequestBody:
    mode: str
    formdata: Optional[list[FormData]]
    raw: Optional[str]
    options: Optional[RequestBodyOption]
