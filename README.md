### Palourde
---

![version](https://img.shields.io/badge/version-1.0.0-blue)

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
palourde api_platform.postman_collection.json
```

This should a `demo.md` file in the same folder.

See [Demos](https://github.com/bagabool/palourde/tree/main/demo).