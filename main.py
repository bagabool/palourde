import pathlib
import json

import dacite

import palourde

doc = pathlib.Path("assets").joinpath("hub3e.postman_collection.json")
with open(doc, 'r') as json_coll:
    decoded = json.load(json_coll)

collection = dacite.from_dict(data_class=palourde.Collection, data=decoded)

print(collection)
