import pathlib
from slugify import slugify

author = "bagabool"
version = "1.0"

from dataclasses import dataclass
from palourde.collection_item import CollectionItem


@dataclass
class CollectionInfo:
    name: str
    schema: str


@dataclass
class Collection:
    info: CollectionInfo
    item: list[CollectionItem]

    def to_markdown(self):
        file = pathlib.Path(f"{slugify(self.info.name)}.md")
        file.touch(exist_ok=True)
        with open(file, 'w') as markdown:
            markdown.write(f"# {self.info.name}\n\n<br>\n\n")
            for item in self.item:
                markdown.write(f"### {item.name}")
                markdown.write(f"""
                    ### {item.name}
                    > Request
                    ```
                    {item.request.method} {item.request.url.raw}
                    ```
                """)
