from dataclasses import dataclass

from palourde.collection_item_request import CollectionItemRequest
from palourde.collection_item_response import CollectionItemResponse


@dataclass
class CollectionItem:
    name: str
    request: CollectionItemRequest
    response: CollectionItemResponse | list
