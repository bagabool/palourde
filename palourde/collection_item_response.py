from dataclasses import dataclass
from palourde.collection_item_request import CollectionItemRequest


@dataclass
class ResponseHeader:
    key: str
    value: str


@dataclass
class CollectionItemResponse:
    name: str
    originalRequest: CollectionItemRequest
    status: str
    code: int
    postman_previewlanguage: str
    header: list[ResponseHeader]
    cookie: list
    body: str
