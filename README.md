### Palourde
---

|Python Version| |PyPI version|

Palourde converts **a v2.1 Postman collection**,  into a **markdown file**, shareable on Github or in Obsidian.

[How to export your postman collection](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#exporting-collections)

Be aware, palourde will explore recursively all your folders and subfolders to get to the requests, so **the end result won't display your folder structure**.

Note that palourde has only been tested on version **2.1** postman collections and on Python **3.10**.

<br>

### Installation
---

```shell
pip install palourde
```

<br>

### Usage
---

```shell
palourde demo.postman_collection.json > demo.md
```

See [Demos](https://github.com/bagabool/palourde/tree/main/demo).