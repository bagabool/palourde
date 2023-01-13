from dataclasses import dataclass
from palourde.collection_item import CollectionItem


@dataclass
class CollectionInfo:
    _postman_id: str
    name: str
    schema: str


@dataclass
class Collection:
    info: CollectionInfo
    item: list[CollectionItem]
