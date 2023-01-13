from dataclasses import dataclass
from typing import Optional

from palourde.request_body import RequestBody
from palourde.request_url import RequestUrl


@dataclass
class BearerToken:
    key: str
    value: str


@dataclass
class RequestAuth:
    type: str
    bearer: Optional[list[BearerToken]]


@dataclass
class CollectionItemRequest:
    auth: Optional[RequestAuth]
    method: str
    header: list
    body: Optional[RequestBody]
    url: Optional[RequestUrl]
