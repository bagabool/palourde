from dataclasses import dataclass
from typing import Optional

from palourde.request_body import RequestBody
from palourde.request_url import RequestUrl


@dataclass
class RequestAuth:
    type: str


@dataclass
class CollectionItemRequest:
    auth: Optional[RequestAuth]
    method: str
    header: list
    body: RequestBody | None
    url: RequestUrl | None
