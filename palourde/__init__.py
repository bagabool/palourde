import pathlib
from dataclasses import dataclass
from typing import Optional

from slugify import slugify


@dataclass
class ResponseHeader:
    key: str
    value: str


@dataclass
class CollectionInfo: name: str


@dataclass
class BearerToken:
    key: str
    value: str


@dataclass
class RequestAuth:
    type: str
    bearer: Optional[list[BearerToken]]


@dataclass
class FormData:
    key: str
    type: str
    src: str


@dataclass
class RequestBodyOptionRaw: language: str


@dataclass
class RequestBodyOption: raw: RequestBodyOptionRaw


@dataclass
class RequestBody:
    mode: str
    formdata: Optional[list[FormData]]
    raw: Optional[str]
    options: Optional[RequestBodyOption]


@dataclass
class RequestQuery:
    key: str
    value: str


@dataclass
class RequestUrl:
    raw: str
    query: Optional[list[RequestQuery]]


@dataclass
class CollectionItemRequest:
    auth: Optional[RequestAuth]
    method: str
    header: list
    body: Optional[RequestBody]
    url: Optional[RequestUrl]


@dataclass
class CollectionItemResponse:
    name: str
    originalRequest: CollectionItemRequest
    status: str
    code: int
    _postman_previewlanguage: str
    body: str


@dataclass
class CollectionItem:
    name: str
    request: CollectionItemRequest
    response: CollectionItemResponse | list


@dataclass
class Collection:
    info: CollectionInfo
    item: list[CollectionItem]

    def __post_init__(self):
        self.file = pathlib.Path("demo").joinpath("Microsoft Graph API").joinpath(f"{slugify(self.info.name)}.md")
        self.file.touch(exist_ok=True)

    def to_markdown(self):
        with open(self.file, 'w') as markdown:

            # REQUEST NAME
            markdown.write(f"# {self.info.name}\n\n---\n\n<br>\n\n")
            for item in self.item:

                # REQUEST METHOD AND URL
                if item.request.__dict__.get("url") is not None:
                    markdown.write(
                        f"### {item.name}\n\n---\n> Request\n\n```\n{item.request.method} {item.request.url.raw}\n```\n\n"
                    )

                # REQUEST HEADERS AND BODY
                if item.request.body and item.request.body.raw:
                    options = item.request.body.options
                    language = options.raw.language if options is not None else item.request.body.mode
                    if bool(item.request.header):
                        for header in item.request.header:
                            if "application/json" in header.values():
                                language = "json"
                                break
                    markdown.write(
                        f"\n> Body\n\n```{language}\n{item.request.body.raw}\n```\n\n"
                    )

                # REQUEST RESPONSE
                if bool(item.response):
                    markdown.write(
                        f"\n> Response\n\n```{item.response[0].get('_postman_previewlanguage')}\n{item.response[0].get('body')}\n```\n\n"
                    )
