from dataclasses import dataclass


@dataclass
class RequestBodyOptionRaw:
    language: str


@dataclass
class RequestBodyOption:
    raw: RequestBodyOptionRaw


@dataclass
class RequestBody:
    mode: str
    raw: str
    options: RequestBodyOption
