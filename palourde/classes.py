import pathlib
from dataclasses import dataclass
from typing import Optional

from slugify import slugify


@dataclass
class ResponseHeader:
    key: str
    value: str


@dataclass
class CollectionInfo:
    name: str
    description: Optional[str]


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


@dataclass
class RequestQuery:
    key: str
    value: Optional[str]
    description: Optional[str]


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
    status: str
    code: int
    _postman_previewlanguage: str
    body: str


@dataclass
class CollectionItem:
    name: str
    request: CollectionItemRequest
    response: list[CollectionItemResponse]


@dataclass
class Collection:
    info: CollectionInfo
    item: list[CollectionItem]

    def __post_init__(self):
        self.file = pathlib.Path(f"{slugify(self.info.name)}.md")
        self.file.touch(exist_ok=True)

    def to_markdown(self):
        with open(self.file, 'w') as markdown:

            # REQUEST NAME
            markdown.write(f"# {self.info.name}\n\n---\n\n<br>\n\n")

            # REQUEST DESCRIPTION
            if self.info.description:
                markdown.write(f"{self.info.description}\n\n")

            markdown.write(f"<br>\n\n## Requests\n\n")
            for item in self.item:

                # REQUEST METHOD AND URL
                if item.request.__dict__.get("url") is not None:
                    markdown.write(
                        f"### {item.name}\n\n---\n> Request\n\n```\n"
                        f"{item.request.method} {item.request.url.raw}\n```\n\n"
                    )

                # REQUEST URL PARAMETERS
                if item.request.url.query:
                    markdown.write(f"> Query parameters\n\n")
                    for param in item.request.url.query:
                        markdown.write(f"**`{param.key}`**\n\n")
                        if param.description:
                            markdown.write(param.description + "\n\n")

                # REQUEST HEADERS AND BODY
                if item.request.body and item.request.body.raw:
                    options = item.request.body.options

                    # LANGUAGE
                    language = options.raw.language if options is not None else item.request.body.mode
                    if bool(item.request.header):
                        for header in item.request.header:
                            if "application/json" in header.values():
                                language = "json"
                                break

                    markdown.write(
                        f"\n> Body\n\n```{language}\n{item.request.body.raw}\n```\n\n"
                    )

                # REQUEST RESPONSES
                if bool(item.response):
                    markdown.write(f"\n> Response{'s' if len(item.response) > 1 else ''}\n\n")
                    for response in item.response:
                        markdown.write(f"*{response.name}*")
                        if bool(response.body):
                            markdown.write(f"\n```{response._postman_previewlanguage}\n{response.body}\n```\n\n")
                        else:
                            markdown.write(": No response specified\n\n")

                markdown.write("<br>\n\n")

            markdown.write("Generated with [Palourde](https://github.com/bagabool/palourde)")
