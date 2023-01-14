import json
import pathlib
import sys

import dacite

from palourde.classes import Collection


def flatten(root: dict, out: list) -> None:
    """
    Flatten the root dict into a list of requests with a recursive exploration
    :param root: The postman collection
    :param out: The list of request
    :return: None
    """
    for data in root.get("item"):
        if data.get("request") is None:
            flatten(data, out)
        else:
            out.append(data)


def execute():
    postman_collection = sys.argv[1].strip()

    doc = pathlib.Path(postman_collection)
    with open(doc, 'r+') as json_coll:
        decoded = json.load(json_coll)
        items = []
        flatten(decoded, items)
        # Flatten the requests, ignoring the folder structure
        decoded["item"] = items

    collection = dacite.from_dict(data_class=Collection, data=decoded)
    collection.to_markdown()


if __name__ == '__main__':
    execute()
