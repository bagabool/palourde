import pathlib
import json

import dacite

import palourde


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


doc = pathlib.Path("demo").joinpath("Google Analytics API").joinpath("Google Analytics API.postman_collection.json")
with open(doc, 'r+') as json_coll:
    decoded = json.load(json_coll)
    items = []
    flatten(decoded, items)
    # Flatten the requests, ignoring the folder structure
    decoded["item"] = items

collection = dacite.from_dict(data_class=palourde.Collection, data=decoded)
collection.to_markdown()
