# Notion API ![auth](https://img.shields.io/badge/auth-token-brightgreen)

<br>

Hello and welcome!

To make use of this API collection collection as it's written, please duplicate [this database template](https://www.notion.so/8e2c2b769e1d47d287b9ed3035d607ae?v=dc1b92875fb94f10834ba8d36549bd2a).

[Create an integration](https://www.notion.so/my-integrations) to retrieve an API token, add your database and page ID's as variables in the collection, and start making your requests!

For our full documentation, including sample integrations and guides, visit [developers.notion.com](developers.notion.com)

Need more help? Join our [developer community on Slack](https://join.slack.com/t/notiondevs/shared_invite/zt-lkrnk74h-YmPRroySRFGiqgjI193AqA/)

<br>

## Requests

<br>

### Retrieve a user 

---
> Request

```
GET https://api.notion.com/v1/users/:id
```


> Response

*200 Success - Retrieve a user*
```json
{
    "object": "user",
    "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a",
    "name": "Aman Gupta",
    "avatar_url": null,
    "type": "person",
    "person": {
        "email": "XXXXXXXXXXX"
    }
}
```

<br>

### List all users 

---
> Request

```
GET https://api.notion.com/v1/users
```


> Response

*200 Success - List all users*
```json
{
    "object": "list",
    "results": [
        {
            "object": "user",
            "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a",
            "name": "Aman Gupta",
            "avatar_url": null,
            "type": "person",
            "person": {
                "email": "XXXXXXXXXX"
            }
        },
        {
            "object": "user",
            "id": "92a680bb-6970-4726-952b-4f4c03bff617",
            "name": "Leotastic",
            "avatar_url": null,
            "type": "bot",
            "bot": {
                "owner": {
                    "type": "workspace",
                    "workspace": true
                }
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

<br>

### Retrieve bot's user info 

---
> Request

```
GET https://api.notion.com/v1/users/me
```


> Response

*200 Success - Retrieve bot's user info*
```json
{
    "object": "user",
    "id": "92a680bb-6970-4726-952b-4f4c03bff617",
    "name": "Leotastic",
    "avatar_url": null,
    "type": "bot",
    "bot": {
        "owner": {
            "type": "workspace",
            "workspace": true
        }
    }
}
```

<br>

### Retrieve a database 

---
> Request

```
GET https://api.notion.com/v1/databases/:id
```


> Response

*200 Success - Retrieve a Database*
```json
{
    "object": "database",
    "id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae",
    "cover": null,
    "icon": null,
    "created_time": "2021-04-27T20:38:00.000Z",
    "created_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
    },
    "last_edited_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
    },
    "last_edited_time": "2022-02-24T22:14:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Ever Better Reading List Title",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Ever Better Reading List Title",
            "href": null
        }
    ],
    "properties": {
        "Score /5": {
            "id": ")Y7%22",
            "name": "Score /5",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "b7307e35-c80a-4cb5-bb6b-6054523b394a",
                        "name": "⭐️⭐️⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "9b1e1349-8e24-40ba-bbca-84a61296bc81",
                        "name": "⭐️⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "66d3d050-086c-4a91-8c56-d55dc67e7789",
                        "name": "⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "d3782c76-0396-467f-928e-46bf0c9d5fba",
                        "name": "⭐️",
                        "color": "default"
                    }
                ]
            }
        },
        "Type": {
            "id": "%2F7eo",
            "name": "Type",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    },
                    {
                        "id": "4ac85597-5db1-4e0a-9c02-445575c38f76",
                        "name": "TV Series",
                        "color": "default"
                    },
                    {
                        "id": "2991748a-5745-4c3b-9c9b-2d6846a6fa1f",
                        "name": "Film",
                        "color": "default"
                    },
                    {
                        "id": "82f3bace-be25-410d-87fe-561c9c22492f",
                        "name": "Podcast",
                        "color": "default"
                    },
                    {
                        "id": "861f1076-1cc4-429a-a781-54947d727a4a",
                        "name": "Academic Journal",
                        "color": "default"
                    },
                    {
                        "id": "9cc30548-59d6-4cd3-94bc-d234081525c4",
                        "name": "Essay Resource",
                        "color": "default"
                    }
                ]
            }
        },
        "Publisher": {
            "id": "%3E%24Pb",
            "name": "Publisher",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
                        "name": "NYT",
                        "color": "default"
                    },
                    {
                        "id": "1b9b0c0c-17b0-4292-ad12-1364a51849de",
                        "name": "Netflix",
                        "color": "blue"
                    },
                    {
                        "id": "f3533637-278f-4501-b394-d9753bf3c101",
                        "name": "Indie",
                        "color": "brown"
                    },
                    {
                        "id": "e70d713c-4be4-4b40-a44d-fb413c8b9d7e",
                        "name": "Bon Appetit",
                        "color": "yellow"
                    },
                    {
                        "id": "9c2bd667-0a10-4be4-a044-35a537a14ab9",
                        "name": "Franklin Institute",
                        "color": "pink"
                    },
                    {
                        "id": "6849b5f0-e641-4ec5-83cb-1ffe23011060",
                        "name": "Springer",
                        "color": "orange"
                    },
                    {
                        "id": "6a5bff63-a72d-4464-a5d0-1a601af2adf6",
                        "name": "Emerald Group",
                        "color": "gray"
                    },
                    {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                ]
            }
        },
        "Summary": {
            "id": "%3F%5C25",
            "name": "Summary",
            "type": "rich_text",
            "rich_text": {}
        },
        "Publishing/Release Date": {
            "id": "%3Fex%2B",
            "name": "Publishing/Release Date",
            "type": "date",
            "date": {}
        },
        "Link": {
            "id": "VVMi",
            "name": "Link",
            "type": "url",
            "url": {}
        },
        "Read": {
            "id": "_MWJ",
            "name": "Read",
            "type": "checkbox",
            "checkbox": {}
        },
        "Status": {
            "id": "%60zz5",
            "name": "Status",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    },
                    {
                        "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
                        "name": "Reading",
                        "color": "red"
                    },
                    {
                        "id": "59aa9043-07b4-4bf4-8734-3164b13af44a",
                        "name": "Finished",
                        "color": "blue"
                    },
                    {
                        "id": "f961978d-02eb-4998-933a-33c2ec378564",
                        "name": "Listening",
                        "color": "red"
                    },
                    {
                        "id": "1d450853-b27a-45e2-979f-448aa1bd35de",
                        "name": "Watching",
                        "color": "red"
                    }
                ]
            }
        },
        "Author": {
            "id": "qNw_",
            "name": "Author",
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "id": "15592971-7b30-43d5-9406-2eb69b13fcae",
                        "name": "Spencer Greenberg",
                        "color": "default"
                    },
                    {
                        "id": "b80a988e-dccf-4f74-b764-6ca0e49ed1b8",
                        "name": "Seth Stephens-Davidowitz",
                        "color": "default"
                    },
                    {
                        "id": "0e71ee06-199d-46a4-834c-01084c8f76cb",
                        "name": "Andrew Russell",
                        "color": "default"
                    },
                    {
                        "id": "5807ec38-4879-4455-9f30-5352e90e8b79",
                        "name": "Lee Vinsel",
                        "color": "default"
                    },
                    {
                        "id": "4cf10a64-f3da-449c-8e04-ce6e338bbdbd",
                        "name": "Megan Greenwell",
                        "color": "default"
                    },
                    {
                        "id": "833e2c78-35ed-4601-badc-50c323341d76",
                        "name": "Kara Swisher",
                        "color": "default"
                    },
                    {
                        "id": "82e594e2-b1c5-4271-ac19-1a723a94a533",
                        "name": "Paul Romer",
                        "color": "default"
                    },
                    {
                        "id": "ae3a2cbe-1fc9-4376-be35-331628b34623",
                        "name": "Karen Swallow Prior",
                        "color": "default"
                    },
                    {
                        "id": "da068e78-dfe2-4434-9fd7-b7450b3e5830",
                        "name": "Judith Shulevitz",
                        "color": "default"
                    }
                ]
            }
        },
        "Name": {
            "id": "title",
            "name": "Name",
            "type": "title",
            "title": {}
        }
    },
    "parent": {
        "type": "page_id",
        "page_id": "c4d39556-6364-46a1-8a61-ebbb668f7445"
    },
    "url": "https://www.notion.so/8e2c2b769e1d47d287b9ed3035d607ae",
    "archived": false
}
```

<br>

### Query a database 

---
> Request

```
POST https://api.notion.com/v1/databases/:id/query
```


> Body

```json
{
    "filter": {
        "property": "Status",
        "select": {
            "equals": "Reading"
        }
    }
}
```


> Responses

*200 Success - Query a Database (OR)*
```json
{
    "object": "list",
    "results": [
        {
            "object": "page",
            "id": "a1712d54-53e4-4893-a69d-4d581cd2c845",
            "created_time": "2021-04-27T20:38:00.000Z",
            "last_edited_time": "2021-05-12T06:07:00.000Z",
            "created_by": {
                "object": "user",
                "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "b7307e35-c80a-4cb5-bb6b-6054523b394a",
                        "name": "⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
                        "name": "NYT",
                        "color": "default"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2018-10-21",
                        "end": null,
                        "time_zone": null
                    }
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": true
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
                        "name": "Reading",
                        "color": "red"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": "833e2c78-35ed-4601-badc-50c323341d76",
                            "name": "Kara Swisher",
                            "color": "default"
                        }
                    ]
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Who Will Teach Silicon Valley to Be Ethical? ",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Who Will Teach Silicon Valley to Be Ethical? ",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/Who-Will-Teach-Silicon-Valley-to-Be-Ethical-a1712d5453e44893a69d4d581cd2c845"
        },
        {
            "object": "page",
            "id": "557ef501-bfdb-4586-918e-4434f31bca8c",
            "created_time": "2021-04-27T20:38:00.000Z",
            "last_edited_time": "2021-04-27T20:38:00.000Z",
            "created_by": {
                "object": "user",
                "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
            },
            "last_edited_by": {
                "object": "user",
                "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "66d3d050-086c-4a91-8c56-d55dc67e7789",
                        "name": "⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "9cc30548-59d6-4cd3-94bc-d234081525c4",
                        "name": "Essay Resource",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2016-10-03",
                        "end": null,
                        "time_zone": null
                    }
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.theatlantic.com/entertainment/archive/2016/03/how-jane-eyre-created-the-modern-self/460461/"
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
                        "name": "Reading",
                        "color": "red"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": "ae3a2cbe-1fc9-4376-be35-331628b34623",
                            "name": "Karen Swallow Prior",
                            "color": "default"
                        }
                    ]
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Jane Eyre",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": true,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Jane Eyre",
                            "href": null
                        },
                        {
                            "type": "text",
                            "text": {
                                "content": " and the Invention of Self",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": " and the Invention of Self",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/Jane-Eyre-and-the-Invention-of-Self-557ef501bfdb4586918e4434f31bca8c"
        },
        {
            "object": "page",
            "id": "7ea694fa-93bb-43ba-b342-90a7706e55aa",
            "created_time": "2021-04-27T20:38:00.000Z",
            "last_edited_time": "2021-04-27T20:38:00.000Z",
            "created_by": {
                "object": "user",
                "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
            },
            "last_edited_by": {
                "object": "user",
                "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": null
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
                        "name": "NYT",
                        "color": "default"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Putting a levy on targeted ad revenue would give Facebook and Google a real incentive to change their dangerous business models.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Putting a levy on targeted ad revenue would give Facebook and Google a real incentive to change their dangerous business models.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2019-10-06",
                        "end": null,
                        "time_zone": null
                    }
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2019/05/06/opinion/tax-facebook-google.html"
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": "82e594e2-b1c5-4271-ac19-1a723a94a533",
                            "name": "Paul Romer",
                            "color": "default"
                        }
                    ]
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "A Tax That Could Fix Big Tech ",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "A Tax That Could Fix Big Tech ",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/A-Tax-That-Could-Fix-Big-Tech-7ea694fa93bb43bab34290a7706e55aa"
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

*200 Success - Query a Database (AND)*
```json
{
    "object": "list",
    "results": [
        {
            "object": "page",
            "id": "a1712d54-53e4-4893-a69d-4d581cd2c845",
            "created_time": "2021-04-27T20:38:00.000Z",
            "last_edited_time": "2021-05-12T06:07:00.000Z",
            "created_by": {
                "object": "user",
                "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "b7307e35-c80a-4cb5-bb6b-6054523b394a",
                        "name": "⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
                        "name": "NYT",
                        "color": "default"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2018-10-21",
                        "end": null,
                        "time_zone": null
                    }
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": true
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
                        "name": "Reading",
                        "color": "red"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": "833e2c78-35ed-4601-badc-50c323341d76",
                            "name": "Kara Swisher",
                            "color": "default"
                        }
                    ]
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Who Will Teach Silicon Valley to Be Ethical? ",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Who Will Teach Silicon Valley to Be Ethical? ",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/Who-Will-Teach-Silicon-Valley-to-Be-Ethical-a1712d5453e44893a69d4d581cd2c845"
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

*200 Success - Query a Database (Single Filter)*
```json
{
    "object": "list",
    "results": [
        {
            "object": "page",
            "id": "557ef501-bfdb-4586-918e-4434f31bca8c",
            "created_time": "2021-04-27T20:38:00.000Z",
            "last_edited_time": "2021-04-27T20:38:00.000Z",
            "created_by": {
                "object": "user",
                "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
            },
            "last_edited_by": {
                "object": "user",
                "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "66d3d050-086c-4a91-8c56-d55dc67e7789",
                        "name": "⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "9cc30548-59d6-4cd3-94bc-d234081525c4",
                        "name": "Essay Resource",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2016-10-03",
                        "end": null,
                        "time_zone": null
                    }
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.theatlantic.com/entertainment/archive/2016/03/how-jane-eyre-created-the-modern-self/460461/"
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
                        "name": "Reading",
                        "color": "red"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": "ae3a2cbe-1fc9-4376-be35-331628b34623",
                            "name": "Karen Swallow Prior",
                            "color": "default"
                        }
                    ]
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Jane Eyre",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": true,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Jane Eyre",
                            "href": null
                        },
                        {
                            "type": "text",
                            "text": {
                                "content": " and the Invention of Self",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": " and the Invention of Self",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/Jane-Eyre-and-the-Invention-of-Self-557ef501bfdb4586918e4434f31bca8c"
        },
        {
            "object": "page",
            "id": "a1712d54-53e4-4893-a69d-4d581cd2c845",
            "created_time": "2021-04-27T20:38:00.000Z",
            "last_edited_time": "2021-05-12T06:07:00.000Z",
            "created_by": {
                "object": "user",
                "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "b7307e35-c80a-4cb5-bb6b-6054523b394a",
                        "name": "⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
                        "name": "NYT",
                        "color": "default"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2018-10-21",
                        "end": null,
                        "time_zone": null
                    }
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": true
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
                        "name": "Reading",
                        "color": "red"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": "833e2c78-35ed-4601-badc-50c323341d76",
                            "name": "Kara Swisher",
                            "color": "default"
                        }
                    ]
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Who Will Teach Silicon Valley to Be Ethical? ",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Who Will Teach Silicon Valley to Be Ethical? ",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/Who-Will-Teach-Silicon-Valley-to-Be-Ethical-a1712d5453e44893a69d4d581cd2c845"
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

<br>

### Create a database 

---
> Request

```
POST https://api.notion.com/v1/databases/
```


> Body

```json
{
    "parent": {
        "type": "page_id",
        "page_id": "{{PAGE_ID}}"
    },
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            }
        }
    ],
    "properties": {
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
            "checkbox": {}
        },
        "Food group": {
            "select": {
                "options": [
                    {
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Price": {
            "number": {
                "format": "dollar"
            }
        },
        "Last ordered": {
            "date": {}
        },
        "Store availability": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "name": "Gus's Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "+1": {
            "people": {}
        },
        "Photo": {
            "files": {}
        }
    }
}
```


> Response

*200 Success - Create a database*
```json
{
    "object": "database",
    "id": "23cde96c-0ad8-41d8-bfa2-b477c63dd52a",
    "cover": null,
    "icon": null,
    "created_time": "2022-02-24T22:06:00.000Z",
    "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "last_edited_time": "2022-02-24T22:06:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Grocery List",
            "href": null
        }
    ],
    "properties": {
        "Description": {
            "id": "%3EWW~",
            "name": "Description",
            "type": "rich_text",
            "rich_text": {}
        },
        "Last ordered": {
            "id": "O%5C%3BK",
            "name": "Last ordered",
            "type": "date",
            "date": {}
        },
        "In stock": {
            "id": "Pya%5C",
            "name": "In stock",
            "type": "checkbox",
            "checkbox": {}
        },
        "+1": {
            "id": "%5CSky",
            "name": "+1",
            "type": "people",
            "people": {}
        },
        "Photo": {
            "id": "dSrT",
            "name": "Photo",
            "type": "files",
            "files": {}
        },
        "Store availability": {
            "id": "jRd%3E",
            "name": "Store availability",
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "id": "8e6441ee-8f17-4833-a2fe-68af5dced24f",
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "id": "64a9da77-9805-461f-9773-1e176fdbd203",
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "id": "012d0436-66a1-4613-a1bd-314b1d1d059b",
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "id": "63ab31f9-8cbd-4d02-8688-752376f455ea",
                        "name": "Gus's Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Food group": {
            "id": "q%5DO%5B",
            "name": "Food group",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "392af858-f42f-43ea-a171-7c0ca5c0a683",
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "id": "df461a24-14c6-494a-8c61-55775fedbdcd",
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "id": "0ff22aaa-348e-4194-83c2-67a76dfb10fc",
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Price": {
            "id": "t%60jj",
            "name": "Price",
            "type": "number",
            "number": {
                "format": "dollar"
            }
        },
        "Name": {
            "id": "title",
            "name": "Name",
            "type": "title",
            "title": {}
        }
    },
    "parent": {
        "type": "page_id",
        "page_id": "c4d39556-6364-46a1-8a61-ebbb668f7445"
    },
    "url": "https://www.notion.so/23cde96c0ad841d8bfa2b477c63dd52a",
    "archived": false
}
```

<br>

### Update a database 

---
> Request

```
PATCH https://api.notion.com/v1/databases/:id
```


> Body

```json
{
    "title": [
        {
            "text": {
                "content": "Ever Better Reading List Title"
            }
        }
    ],
    "properties":{
        "Wine Pairing": { "rich_text": {} } 
    }
}
```


> Responses

*200 Success - Update a Database*
```json
{
    "object": "database",
    "id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae",
    "cover": null,
    "icon": null,
    "created_time": "2021-04-27T20:38:00.000Z",
    "created_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
    },
    "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "last_edited_time": "2022-02-24T22:08:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Ever Better Reading List Title",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Ever Better Reading List Title",
            "href": null
        }
    ],
    "properties": {
        "Score /5": {
            "id": ")Y7\"",
            "name": "Score /5",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "b7307e35-c80a-4cb5-bb6b-6054523b394a",
                        "name": "⭐️⭐️⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "9b1e1349-8e24-40ba-bbca-84a61296bc81",
                        "name": "⭐️⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "66d3d050-086c-4a91-8c56-d55dc67e7789",
                        "name": "⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "d3782c76-0396-467f-928e-46bf0c9d5fba",
                        "name": "⭐️",
                        "color": "default"
                    }
                ]
            }
        },
        "Type": {
            "id": "/7eo",
            "name": "Type",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    },
                    {
                        "id": "4ac85597-5db1-4e0a-9c02-445575c38f76",
                        "name": "TV Series",
                        "color": "default"
                    },
                    {
                        "id": "2991748a-5745-4c3b-9c9b-2d6846a6fa1f",
                        "name": "Film",
                        "color": "default"
                    },
                    {
                        "id": "82f3bace-be25-410d-87fe-561c9c22492f",
                        "name": "Podcast",
                        "color": "default"
                    },
                    {
                        "id": "861f1076-1cc4-429a-a781-54947d727a4a",
                        "name": "Academic Journal",
                        "color": "default"
                    },
                    {
                        "id": "9cc30548-59d6-4cd3-94bc-d234081525c4",
                        "name": "Essay Resource",
                        "color": "default"
                    }
                ]
            }
        },
        "Publisher": {
            "id": ">$Pb",
            "name": "Publisher",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
                        "name": "NYT",
                        "color": "default"
                    },
                    {
                        "id": "1b9b0c0c-17b0-4292-ad12-1364a51849de",
                        "name": "Netflix",
                        "color": "blue"
                    },
                    {
                        "id": "f3533637-278f-4501-b394-d9753bf3c101",
                        "name": "Indie",
                        "color": "brown"
                    },
                    {
                        "id": "e70d713c-4be4-4b40-a44d-fb413c8b9d7e",
                        "name": "Bon Appetit",
                        "color": "yellow"
                    },
                    {
                        "id": "9c2bd667-0a10-4be4-a044-35a537a14ab9",
                        "name": "Franklin Institute",
                        "color": "pink"
                    },
                    {
                        "id": "6849b5f0-e641-4ec5-83cb-1ffe23011060",
                        "name": "Springer",
                        "color": "orange"
                    },
                    {
                        "id": "6a5bff63-a72d-4464-a5d0-1a601af2adf6",
                        "name": "Emerald Group",
                        "color": "gray"
                    },
                    {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                ]
            }
        },
        "Summary": {
            "id": "?\\25",
            "name": "Summary",
            "type": "rich_text",
            "rich_text": {}
        },
        "Publishing/Release Date": {
            "id": "?ex+",
            "name": "Publishing/Release Date",
            "type": "date",
            "date": {}
        },
        "Link": {
            "id": "VVMi",
            "name": "Link",
            "type": "url",
            "url": {}
        },
        "Wine Pairing": {
            "id": "Y=H]",
            "name": "Wine Pairing",
            "type": "rich_text",
            "rich_text": {}
        },
        "Read": {
            "id": "_MWJ",
            "name": "Read",
            "type": "checkbox",
            "checkbox": {}
        },
        "Status": {
            "id": "`zz5",
            "name": "Status",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    },
                    {
                        "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
                        "name": "Reading",
                        "color": "red"
                    },
                    {
                        "id": "59aa9043-07b4-4bf4-8734-3164b13af44a",
                        "name": "Finished",
                        "color": "blue"
                    },
                    {
                        "id": "f961978d-02eb-4998-933a-33c2ec378564",
                        "name": "Listening",
                        "color": "red"
                    },
                    {
                        "id": "1d450853-b27a-45e2-979f-448aa1bd35de",
                        "name": "Watching",
                        "color": "red"
                    }
                ]
            }
        },
        "Author": {
            "id": "qNw_",
            "name": "Author",
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "id": "15592971-7b30-43d5-9406-2eb69b13fcae",
                        "name": "Spencer Greenberg",
                        "color": "default"
                    },
                    {
                        "id": "b80a988e-dccf-4f74-b764-6ca0e49ed1b8",
                        "name": "Seth Stephens-Davidowitz",
                        "color": "default"
                    },
                    {
                        "id": "0e71ee06-199d-46a4-834c-01084c8f76cb",
                        "name": "Andrew Russell",
                        "color": "default"
                    },
                    {
                        "id": "5807ec38-4879-4455-9f30-5352e90e8b79",
                        "name": "Lee Vinsel",
                        "color": "default"
                    },
                    {
                        "id": "4cf10a64-f3da-449c-8e04-ce6e338bbdbd",
                        "name": "Megan Greenwell",
                        "color": "default"
                    },
                    {
                        "id": "833e2c78-35ed-4601-badc-50c323341d76",
                        "name": "Kara Swisher",
                        "color": "default"
                    },
                    {
                        "id": "82e594e2-b1c5-4271-ac19-1a723a94a533",
                        "name": "Paul Romer",
                        "color": "default"
                    },
                    {
                        "id": "ae3a2cbe-1fc9-4376-be35-331628b34623",
                        "name": "Karen Swallow Prior",
                        "color": "default"
                    },
                    {
                        "id": "da068e78-dfe2-4434-9fd7-b7450b3e5830",
                        "name": "Judith Shulevitz",
                        "color": "default"
                    }
                ]
            }
        },
        "Name": {
            "id": "title",
            "name": "Name",
            "type": "title",
            "title": {}
        }
    },
    "parent": {
        "type": "page_id",
        "page_id": "c4d39556-6364-46a1-8a61-ebbb668f7445"
    },
    "url": "https://www.notion.so/8e2c2b769e1d47d287b9ed3035d607ae",
    "archived": false
}
```

*200 Success - Update a Database*
```json
{
    "object": "database",
    "id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae",
    "cover": null,
    "icon": null,
    "created_time": "2021-04-27T20:38:00.000Z",
    "created_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
    },
    "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "last_edited_time": "2022-02-24T22:08:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Ever Better Reading List Title",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Ever Better Reading List Title",
            "href": null
        }
    ],
    "properties": {
        "Score /5": {
            "id": ")Y7\"",
            "name": "Score /5",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "b7307e35-c80a-4cb5-bb6b-6054523b394a",
                        "name": "⭐️⭐️⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "9b1e1349-8e24-40ba-bbca-84a61296bc81",
                        "name": "⭐️⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "66d3d050-086c-4a91-8c56-d55dc67e7789",
                        "name": "⭐️⭐️",
                        "color": "default"
                    },
                    {
                        "id": "d3782c76-0396-467f-928e-46bf0c9d5fba",
                        "name": "⭐️",
                        "color": "default"
                    }
                ]
            }
        },
        "Type": {
            "id": "/7eo",
            "name": "Type",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    },
                    {
                        "id": "4ac85597-5db1-4e0a-9c02-445575c38f76",
                        "name": "TV Series",
                        "color": "default"
                    },
                    {
                        "id": "2991748a-5745-4c3b-9c9b-2d6846a6fa1f",
                        "name": "Film",
                        "color": "default"
                    },
                    {
                        "id": "82f3bace-be25-410d-87fe-561c9c22492f",
                        "name": "Podcast",
                        "color": "default"
                    },
                    {
                        "id": "861f1076-1cc4-429a-a781-54947d727a4a",
                        "name": "Academic Journal",
                        "color": "default"
                    },
                    {
                        "id": "9cc30548-59d6-4cd3-94bc-d234081525c4",
                        "name": "Essay Resource",
                        "color": "default"
                    }
                ]
            }
        },
        "Publisher": {
            "id": ">$Pb",
            "name": "Publisher",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
                        "name": "NYT",
                        "color": "default"
                    },
                    {
                        "id": "1b9b0c0c-17b0-4292-ad12-1364a51849de",
                        "name": "Netflix",
                        "color": "blue"
                    },
                    {
                        "id": "f3533637-278f-4501-b394-d9753bf3c101",
                        "name": "Indie",
                        "color": "brown"
                    },
                    {
                        "id": "e70d713c-4be4-4b40-a44d-fb413c8b9d7e",
                        "name": "Bon Appetit",
                        "color": "yellow"
                    },
                    {
                        "id": "9c2bd667-0a10-4be4-a044-35a537a14ab9",
                        "name": "Franklin Institute",
                        "color": "pink"
                    },
                    {
                        "id": "6849b5f0-e641-4ec5-83cb-1ffe23011060",
                        "name": "Springer",
                        "color": "orange"
                    },
                    {
                        "id": "6a5bff63-a72d-4464-a5d0-1a601af2adf6",
                        "name": "Emerald Group",
                        "color": "gray"
                    },
                    {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                ]
            }
        },
        "Summary": {
            "id": "?\\25",
            "name": "Summary",
            "type": "rich_text",
            "rich_text": {}
        },
        "Publishing/Release Date": {
            "id": "?ex+",
            "name": "Publishing/Release Date",
            "type": "date",
            "date": {}
        },
        "Link": {
            "id": "VVMi",
            "name": "Link",
            "type": "url",
            "url": {}
        },
        "Wine Pairing": {
            "id": "Y=H]",
            "name": "Wine Pairing",
            "type": "rich_text",
            "rich_text": {}
        },
        "Read": {
            "id": "_MWJ",
            "name": "Read",
            "type": "checkbox",
            "checkbox": {}
        },
        "Status": {
            "id": "`zz5",
            "name": "Status",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    },
                    {
                        "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
                        "name": "Reading",
                        "color": "red"
                    },
                    {
                        "id": "59aa9043-07b4-4bf4-8734-3164b13af44a",
                        "name": "Finished",
                        "color": "blue"
                    },
                    {
                        "id": "f961978d-02eb-4998-933a-33c2ec378564",
                        "name": "Listening",
                        "color": "red"
                    },
                    {
                        "id": "1d450853-b27a-45e2-979f-448aa1bd35de",
                        "name": "Watching",
                        "color": "red"
                    }
                ]
            }
        },
        "Author": {
            "id": "qNw_",
            "name": "Author",
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "id": "15592971-7b30-43d5-9406-2eb69b13fcae",
                        "name": "Spencer Greenberg",
                        "color": "default"
                    },
                    {
                        "id": "b80a988e-dccf-4f74-b764-6ca0e49ed1b8",
                        "name": "Seth Stephens-Davidowitz",
                        "color": "default"
                    },
                    {
                        "id": "0e71ee06-199d-46a4-834c-01084c8f76cb",
                        "name": "Andrew Russell",
                        "color": "default"
                    },
                    {
                        "id": "5807ec38-4879-4455-9f30-5352e90e8b79",
                        "name": "Lee Vinsel",
                        "color": "default"
                    },
                    {
                        "id": "4cf10a64-f3da-449c-8e04-ce6e338bbdbd",
                        "name": "Megan Greenwell",
                        "color": "default"
                    },
                    {
                        "id": "833e2c78-35ed-4601-badc-50c323341d76",
                        "name": "Kara Swisher",
                        "color": "default"
                    },
                    {
                        "id": "82e594e2-b1c5-4271-ac19-1a723a94a533",
                        "name": "Paul Romer",
                        "color": "default"
                    },
                    {
                        "id": "ae3a2cbe-1fc9-4376-be35-331628b34623",
                        "name": "Karen Swallow Prior",
                        "color": "default"
                    },
                    {
                        "id": "da068e78-dfe2-4434-9fd7-b7450b3e5830",
                        "name": "Judith Shulevitz",
                        "color": "default"
                    }
                ]
            }
        },
        "Name": {
            "id": "title",
            "name": "Name",
            "type": "title",
            "title": {}
        }
    },
    "parent": {
        "type": "page_id",
        "page_id": "c4d39556-6364-46a1-8a61-ebbb668f7445"
    },
    "url": "https://www.notion.so/8e2c2b769e1d47d287b9ed3035d607ae",
    "archived": false
}
```

<br>

### Create a Page 

---
> Request

```
POST https://api.notion.com/v1/pages/
```


> Body

```json
{
    "parent": {
        "database_id": "{{DATABASE_ID}}"
    },
    "properties": {
        "Type": {
            "select": {
                "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                "name": "Article",
                "color": "default"
            }
        },
        "Score /5": {
            "select": {
                "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                "name": "⭐️⭐️⭐️⭐️⭐️",
                "color": "default"
            }
        },
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "New Media Article"
                    }
                }
            ]
        },
        "Status": {
            "select": {
                "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                "name": "Ready to Start",
                "color": "yellow"
            }
        },
        "Publisher": {
            "select": {
                "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                "name": "The Atlantic",
                "color": "red"
            }
        },
        "Publishing/Release Date": {
            "date": {
                "start": "2020-12-08T12:00:00Z",
                "end": null
            }
        },
        "Link": {
            "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Summary": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                    "href": null
                }
            ]
        },
        "Read": {
            "checkbox": false
        }
    }
}
```


> Response

*200 Success - Create a Page*
```json
{
    "object": "page",
    "id": "f3a1f364-6ca1-41d2-8986-552ae37c1bdf",
    "created_time": "2022-03-02T05:24:00.000Z",
    "last_edited_time": "2022-03-02T05:24:00.000Z",
    "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "cover": null,
    "icon": null,
    "parent": {
        "type": "database_id",
        "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
    },
    "archived": false,
    "properties": {
        "Score /5": {
            "id": ")Y7%22",
            "type": "select",
            "select": {
                "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                "name": "⭐️⭐️⭐️⭐️⭐️",
                "color": "default"
            }
        },
        "Type": {
            "id": "%2F7eo",
            "type": "select",
            "select": {
                "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                "name": "Article",
                "color": "default"
            }
        },
        "Publisher": {
            "id": "%3E%24Pb",
            "type": "select",
            "select": {
                "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                "name": "The Atlantic",
                "color": "red"
            }
        },
        "Summary": {
            "id": "%3F%5C25",
            "type": "rich_text",
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                    "href": null
                }
            ]
        },
        "Publishing/Release Date": {
            "id": "%3Fex%2B",
            "type": "date",
            "date": {
                "start": "2020-12-08T12:00:00.000+00:00",
                "end": null,
                "time_zone": null
            }
        },
        "Link": {
            "id": "VVMi",
            "type": "url",
            "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Read": {
            "id": "_MWJ",
            "type": "checkbox",
            "checkbox": false
        },
        "Status": {
            "id": "%60zz5",
            "type": "select",
            "select": {
                "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                "name": "Ready to Start",
                "color": "yellow"
            }
        },
        "Author": {
            "id": "qNw_",
            "type": "multi_select",
            "multi_select": []
        },
        "Name": {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "New Media Article",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "New Media Article",
                    "href": null
                }
            ]
        }
    },
    "url": "https://www.notion.so/New-Media-Article-f3a1f3646ca141d28986552ae37c1bdf"
}
```

<br>

### Create a Page with Content 

---
> Request

```
POST https://api.notion.com/v1/pages/
```


> Body

```json
{
    "parent": {
        "database_id": "{{DATABASE_ID}}"
    },
    "properties": {
        "Type": {
            "select": {
                "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                "name": "Article",
                "color": "default"
            }
        },
        "Score /5": {
            "select": {
                "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                "name": "⭐️⭐️⭐️⭐️⭐️",
                "color": "default"
            }
        },
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "New Media Article"
                    }
                }
            ]
        },
        "Status": {
            "select": {
                "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                "name": "Ready to Start",
                "color": "yellow"
            }
        },
        "Publisher": {
            "select": {
                "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                "name": "The Atlantic",
                "color": "red"
            }
        },
        "Publishing/Release Date": {
            "date": {
                "start": "2020-12-08T12:00:00Z",
                "end": null
            }
        },
        "Link": {
            "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Summary": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                    "href": null
                }
            ]
        },
        "Read": {
            "checkbox": false
        }
    },
    "children": [
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Lacinato kale"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                            "link": {
                                "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
                            }
                        }
                    }
                ]
            }
        }
    ]
}
```


> Response

*200 Success - Create a Page with Content*
```json
{
    "object": "page",
    "id": "672b014a-2626-4ada-9211-fb3613d07ae2",
    "created_time": "2022-03-02T05:24:00.000Z",
    "last_edited_time": "2022-03-02T05:24:00.000Z",
    "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "cover": null,
    "icon": null,
    "parent": {
        "type": "database_id",
        "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
    },
    "archived": false,
    "properties": {
        "Score /5": {
            "id": ")Y7%22",
            "type": "select",
            "select": {
                "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                "name": "⭐️⭐️⭐️⭐️⭐️",
                "color": "default"
            }
        },
        "Type": {
            "id": "%2F7eo",
            "type": "select",
            "select": {
                "id": "672b014a-2626-4ada-9211-fb3613d07ae2",
                "name": "Article",
                "color": "default"
            }
        },
        "Publisher": {
            "id": "%3E%24Pb",
            "type": "select",
            "select": {
                "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                "name": "The Atlantic",
                "color": "red"
            }
        },
        "Summary": {
            "id": "%3F%5C25",
            "type": "rich_text",
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                    "href": null
                }
            ]
        },
        "Publishing/Release Date": {
            "id": "%3Fex%2B",
            "type": "date",
            "date": {
                "start": "2020-12-08T12:00:00.000+00:00",
                "end": null,
                "time_zone": null
            }
        },
        "Link": {
            "id": "VVMi",
            "type": "url",
            "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Read": {
            "id": "_MWJ",
            "type": "checkbox",
            "checkbox": false
        },
        "Status": {
            "id": "%60zz5",
            "type": "select",
            "select": {
                "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                "name": "Ready to Start",
                "color": "yellow"
            }
        },
        "Author": {
            "id": "qNw_",
            "type": "multi_select",
            "multi_select": []
        },
        "Name": {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "New Media Article",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "New Media Article",
                    "href": null
                }
            ]
        }
    },
    "url": "https://www.notion.so/New-Media-Article-672b014a26264ada9211fb3613d07ae2"
}
```

<br>

### Retrieve a Page 

---
> Request

```
GET https://api.notion.com/v1/pages/:id
```


> Response

*200 Success - Retrieve a Page*
```json
{
    "object": "page",
    "id": "c4d39556-6364-46a1-8a61-ebbb668f7445",
    "created_time": "2021-04-27T20:38:00.000Z",
    "last_edited_time": "2022-03-02T05:22:00.000Z",
    "created_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
    },
    "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "cover": null,
    "icon": {
        "type": "emoji",
        "emoji": "📕"
    },
    "parent": {
        "type": "page_id",
        "page_id": "c1218692-102d-4b47-ab38-c21900b3557b"
    },
    "archived": false,
    "properties": {
        "title": {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Reading List",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "Reading List",
                    "href": null
                }
            ]
        }
    },
    "url": "https://www.notion.so/Reading-List-c4d39556636446a18a61ebbb668f7445"
}
```

<br>

### Update Page properties  

---
> Request

```
PATCH https://api.notion.com/v1/pages/:id
```


> Body

```json
{
    "properties": {
        "Status": {
            "select": {
                "name": "Reading"
            }
        }
    }
}
```


> Response

*200 Success - Update Page properties*
```json
{
    "object": "page",
    "id": "a1712d54-53e4-4893-a69d-4d581cd2c845",
    "created_time": "2021-04-27T20:38:19.437Z",
    "last_edited_time": "2021-04-28T23:12:53.160Z",
    "parent": {
        "type": "database_id",
        "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
    },
    "archived": false,
    "properties": {
        "Score /5": {
            "id": ")Y7\"",
            "type": "select",
            "select": {
                "id": "b7307e35-c80a-4cb5-bb6b-6054523b394a",
                "name": "⭐️⭐️⭐️⭐️",
                "color": "default"
            }
        },
        "Type": {
            "id": "/7eo",
            "type": "select",
            "select": {
                "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                "name": "Article",
                "color": "default"
            }
        },
        "Publisher": {
            "id": ">$Pb",
            "type": "select",
            "select": {
                "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
                "name": "NYT",
                "color": "default"
            }
        },
        "Summary": {
            "id": "?\\25",
            "type": "rich_text",
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                    "href": null
                }
            ]
        },
        "Publishing/Release Date": {
            "id": "?ex+",
            "type": "date",
            "date": {
                "start": "2018-10-21",
                "end": null
            }
        },
        "Link": {
            "id": "VVMi",
            "type": "url",
            "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Read": {
            "id": "_MWJ",
            "type": "checkbox",
            "checkbox": true
        },
        "Status": {
            "id": "`zz5",
            "type": "select",
            "select": {
                "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
                "name": "Reading",
                "color": "red"
            }
        },
        "Author": {
            "id": "qNw_",
            "type": "multi_select",
            "multi_select": [
                {
                    "id": "833e2c78-35ed-4601-badc-50c323341d76",
                    "name": "Kara Swisher",
                    "color": "default"
                }
            ]
        },
        "Name": {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Who Will Teach Silicon Valley to Be Ethical? ",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "Who Will Teach Silicon Valley to Be Ethical? ",
                    "href": null
                }
            ]
        }
    }
}
```

<br>

### Delete a Page 

---
> Request

```
DELETE https://api.notion.com/v1/blocks/:id
```


> Response

*200 Success - Delete a page*
```json
{
    "object": "block",
    "id": "2646ac0d-df90-4bab-bb4e-75e3cb972ed1",
    "created_time": "2022-02-24T22:14:00.000Z",
    "last_edited_time": "2022-02-24T22:15:00.000Z",
    "created_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
    },
    "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "has_children": false,
    "archived": true,
    "type": "child_page",
    "child_page": {
        "title": ""
    }
}
```

<br>

### Retrieve a Page Property Item 

---
> Request

```
GET https://api.notion.com/v1/pages/:page_id/properties/:property_id
```


> Response

*200 Success - Retrieve a Page Property Item*
```json
{
    "object": "property_item",
    "type": "select",
    "select": {
        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
        "name": "⭐️⭐️⭐️⭐️⭐️",
        "color": "default"
    }
}
```

<br>

### Retrieve block children 

---
> Request

```
GET https://api.notion.com/v1/blocks/:id/children?page_size=100
```

> Query parameters

**`page_size`**


> Response

*200 Success - Retrieve block children*
```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "48c1ffb5-2789-4025-937b-2c35eaaaab3f",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "unsupported",
            "unsupported": {}
        },
        {
            "object": "block",
            "id": "e381a0a3-4efb-4ba9-aa93-45b70fa9ce7f",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "I think we can all agree that Silicon Valley needs more adult supervision right about now.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "I think we can all agree that Silicon Valley needs more adult supervision right about now.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "ce5f79ac-8145-44ab-be3b-8ad143d6f8a7",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Is the solution for its companies to hire a chief ethics officer?",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Is the solution for its companies to hire a chief ethics officer?",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "0387b374-7847-4ddc-bc53-6b0813ce4ed4",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "While some tech companies like Google have top compliance officers and others turn to legal teams to police themselves, no big tech companies that I know of have yet taken this step. But a lot of them seem to be talking about it, and I’ve discussed the idea with several chief executives recently. Why? Because slowly, then all at once, it feels like too many digital leaders have lost their minds.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "While some tech companies like Google have top compliance officers and others turn to legal teams to police themselves, no big tech companies that I know of have yet taken this step. But a lot of them seem to be talking about it, and I’ve discussed the idea with several chief executives recently. Why? Because slowly, then all at once, it feels like too many digital leaders have lost their minds.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "da035311-5af3-48bc-8279-d28d9f4ef2e2",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "It’s probably no surprise, considering the complex problems the tech industry faces. As one ethical quandary after another has hit its profoundly ill-prepared executives, their once-pristine reputations have fallen like palm trees in a hurricane. These last two weeks alone show how tech is stumbling to react to big world issues armed with only bubble world skills:",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "It’s probably no surprise, considering the complex problems the tech industry faces. As one ethical quandary after another has hit its profoundly ill-prepared executives, their once-pristine reputations have fallen like palm trees in a hurricane. These last two weeks alone show how tech is stumbling to react to big world issues armed with only bubble world skills:",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "63a60fca-4a11-43eb-8773-c5f0164a3117",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "As a journalist is beheaded and dismembered at the direction of Saudi Arabian leaders (allegedly, but the killers did bring a bone saw), Silicon Valley is swimming in oceans of money from the kingdom’s Public Investment Fund. Saudi funding includes hundreds of millions for Magic Leap, and huge investments in hot public companies like Tesla. Most significantly: Saudis have invested about $45 billion in SoftBank’s giant Vision Fund, which has in turn doused the tech landscape — $4.4 billion to WeWork, $250 million to Slack, and $300 million to the dog-walking app Wag. In total Uber has gotten almost $14 billion, either through direct investments from the Public Investment Fund or through the Saudis’ funding of the Vision Fund. A billion here, a billion there and it all adds up.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "As a journalist is beheaded and dismembered at the direction of Saudi Arabian leaders (allegedly, but the killers did bring a bone saw), Silicon Valley is swimming in oceans of money from the kingdom’s Public Investment Fund. Saudi funding includes hundreds of millions for Magic Leap, and huge investments in hot public companies like Tesla. Most significantly: Saudis have invested about $45 billion in SoftBank’s giant Vision Fund, which has in turn doused the tech landscape — $4.4 billion to WeWork, $250 million to Slack, and $300 million to the dog-walking app Wag. In total Uber has gotten almost $14 billion, either through direct investments from the Public Investment Fund or through the Saudis’ funding of the Vision Fund. A billion here, a billion there and it all adds up.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "8c58c8f1-86ae-4a14-b6b9-74f5fa579620",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "[",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "[",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "Kara Swisher answered your questions about her column ",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Kara Swisher answered your questions about her column ",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "on Twitter",
                            "link": {
                                "url": "https://twitter.com/karaswisher/status/1054842303922298880"
                            }
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "on Twitter",
                        "href": "https://twitter.com/karaswisher/status/1054842303922298880"
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": ".",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": ".",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "]",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "]",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "875d3aff-086b-45da-9ed1-bc3ddb185229",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Facebook introduced a new home video device called Portal, and promised that what could be seen as a surveillance tool would not share data for the sake of ad targeting. Soon after, as ",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Facebook introduced a new home video device called Portal, and promised that what could be seen as a surveillance tool would not share data for the sake of ad targeting. Soon after, as ",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "reported by Recode",
                            "link": {
                                "url": "https://www.recode.net/2018/10/16/17966102/facebook-portal-ad-targeting-data-collection"
                            }
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "reported by Recode",
                        "href": "https://www.recode.net/2018/10/16/17966102/facebook-portal-ad-targeting-data-collection"
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": ", Facebook admitted that “data about who you call and data about which apps you use on Portal ",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": ", Facebook admitted that “data about who you call and data about which apps you use on Portal ",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "can",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "can",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": " be used to target you with ads on other Facebook-owned properties.” Oh. Um. That’s awkward.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": " be used to target you with ads on other Facebook-owned properties.” Oh. Um. That’s awkward.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "306ab0fb-6daa-4c5b-b1f7-f51a5f92b6ff",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "After agreeing to pay $20 million to the Securities and Exchange Commission for an ill-advised tweet about possible funding (from the Saudis, by the way), the Tesla co-founder Elon Musk proceeded to troll the regulatory agency on, you got it, Twitter. And even though the ",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "After agreeing to pay $20 million to the Securities and Exchange Commission for an ill-advised tweet about possible funding (from the Saudis, by the way), the Tesla co-founder Elon Musk proceeded to troll the regulatory agency on, you got it, Twitter. And even though the ",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "settlement called for some kind of control of his communications",
                            "link": {
                                "url": "https://www.sec.gov/news/press-release/2018-226"
                            }
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "settlement called for some kind of control of his communications",
                        "href": "https://www.sec.gov/news/press-release/2018-226"
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": ", it appears that Mr. Musk will continue tweeting until someone steals his phone.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": ", it appears that Mr. Musk will continue tweeting until someone steals his phone.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "122b1457-4129-4513-abaa-7cce7d66e4a1",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Finally, Google took six months to make public that user data on its social network, Google Plus, ",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Finally, Google took six months to make public that user data on its social network, Google Plus, ",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "had been exposed",
                            "link": {
                                "url": "https://www.nytimes.com/2018/10/08/technology/google-plus-security-disclosure.html?module=inline"
                            }
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "had been exposed",
                        "href": "https://www.nytimes.com/2018/10/08/technology/google-plus-security-disclosure.html?module=inline"
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": " and that profiles of up to 500,000 users may have been compromised. While the service failed long ago, because it was pretty much designed by antisocial people, this lack of concern for privacy was profound.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": " and that profiles of up to 500,000 users may have been compromised. While the service failed long ago, because it was pretty much designed by antisocial people, this lack of concern for privacy was profound.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "4d4af599-556f-4d8b-af8e-4d01ebe2aa27",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Grappling with what to say and do about the disasters they themselves create is only the beginning. Then there are the broader issues that the denizens of Silicon Valley expect their employers to have a stance on: immigration, income inequality, artificial intelligence, automation, transgender rights, climate change, privacy, data rights and whether tech companies should be helping the government do controversial things. It’s an ethical swamp out there.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Grappling with what to say and do about the disasters they themselves create is only the beginning. Then there are the broader issues that the denizens of Silicon Valley expect their employers to have a stance on: immigration, income inequality, artificial intelligence, automation, transgender rights, climate change, privacy, data rights and whether tech companies should be helping the government do controversial things. It’s an ethical swamp out there.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "f5775df5-59eb-4533-a2cb-e150412ec4f6",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "That’s why, in a recent interview, Marc Benioff, the co-chief executive and a founder of Salesforce, told me he was in the process of hiring a chief ethical officer to help anticipate and address any thorny conundrums it might encounter as a business — like the decision it had to make a few months back about whether it should stop providing recruitment software for Customs and Border Protection because of the government’s policy of separating immigrant families at the border.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "That’s why, in a recent interview, Marc Benioff, the co-chief executive and a founder of Salesforce, told me he was in the process of hiring a chief ethical officer to help anticipate and address any thorny conundrums it might encounter as a business — like the decision it had to make a few months back about whether it should stop providing recruitment software for Customs and Border Protection because of the government’s policy of separating immigrant families at the border.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "31405c6e-7ece-4667-8c4d-36c9d79a0bfa",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Amid much criticism, Mr. Benioff decided to keep the contract, but said he would focus more on social and political issues.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Amid much criticism, Mr. Benioff decided to keep the contract, but said he would focus more on social and political issues.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "a2ab7e8a-d521-401d-89ae-9eb27efb9990",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "At a recent company event, he elaborated: “We can have a structured conversation not just with our own employees myopically, but by bringing in the key advisers, supporters and pundits and philosophers and everybody necessary to ask the question if what we are doing today is ethical and humane.”",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "At a recent company event, he elaborated: “We can have a structured conversation not just with our own employees myopically, but by bringing in the key advisers, supporters and pundits and philosophers and everybody necessary to ask the question if what we are doing today is ethical and humane.”",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "a4498e1e-8b85-48d7-802a-db447ca7d1ac",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "23andMe has also toyed with the idea of hiring a chief ethics officer. In an interview I did this week with its chief executive, Anne Wojcicki, she said the genetics company had even interviewed candidates, but that many of them wanted to remain in academia to be freer to ponder these issues. She acknowledged that the collection of DNA data is rife with ethical considerations, but said, “I think it has to be our management and leaders who have to add this to our skill set, rather than just hire one person to determine this.”",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "23andMe has also toyed with the idea of hiring a chief ethics officer. In an interview I did this week with its chief executive, Anne Wojcicki, she said the genetics company had even interviewed candidates, but that many of them wanted to remain in academia to be freer to ponder these issues. She acknowledged that the collection of DNA data is rife with ethical considerations, but said, “I think it has to be our management and leaders who have to add this to our skill set, rather than just hire one person to determine this.”",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "cbf7e7e0-5552-4b3f-b09e-9dcca120931c",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "When asked about the idea of a single source of wisdom on ethics, some point out that legal or diversity/inclusion departments are designed for that purpose and that the ethics should really come from the top — the chief executive.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "When asked about the idea of a single source of wisdom on ethics, some point out that legal or diversity/inclusion departments are designed for that purpose and that the ethics should really come from the top — the chief executive.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "d24b2887-0f1f-4e91-99c1-c295bed8ad65",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Also of concern is the possibility that a single person would not get listened to or, worse, get steamrollered. And, if the person was bad at the job, of course, it could drag the whole thing down.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Also of concern is the possibility that a single person would not get listened to or, worse, get steamrollered. And, if the person was bad at the job, of course, it could drag the whole thing down.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "78c55f65-c8b8-4364-a369-c40699968e90",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Others are more worried that the move would be nothing but window dressing. One consultant who focuses on ethics, but did not want to be named, told me: “We haven’t even defined ethics, so what even is ethical use, especially for Silicon Valley companies that are babies in this game?”",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Others are more worried that the move would be nothing but window dressing. One consultant who focuses on ethics, but did not want to be named, told me: “We haven’t even defined ethics, so what even is ethical use, especially for Silicon Valley companies that are babies in this game?”",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "0b492111-1586-4a73-8848-04f0c391aadc",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "How can an industry that, unlike other business sectors, persistently promotes itself as doing good, learn to do that in reality? Do you want to not do harm, or do you want to do good? These are two totally different things.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "How can an industry that, unlike other business sectors, persistently promotes itself as doing good, learn to do that in reality? Do you want to not do harm, or do you want to do good? These are two totally different things.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "302f8229-2404-460b-8c3c-e7058b4365e5",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "And how do you put an official ethical system in place without it seeming like you’re telling everyone how to behave? Who gets to decide those rules anyway, setting a moral path for the industry and — considering tech companies’ enormous power — the world.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "And how do you put an official ethical system in place without it seeming like you’re telling everyone how to behave? Who gets to decide those rules anyway, setting a moral path for the industry and — considering tech companies’ enormous power — the world.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "8f9bc91c-5662-4b3f-a110-809f46b79f49",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Like I said, adult supervision. Or maybe, better still, Silicon Valley itself has to grow up.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Like I said, adult supervision. Or maybe, better still, Silicon Valley itself has to grow up.",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "7bea1831-a25c-4b3e-8c9b-b37de814f948",
            "created_time": "2021-04-27T20:38:19.437Z",
            "last_edited_time": "2021-04-27T20:38:19.437Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Follow The New York Times Opinion section on ",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Follow The New York Times Opinion section on ",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "Facebook",
                            "link": {
                                "url": "https://www.facebook.com/nytopinion"
                            }
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Facebook",
                        "href": "https://www.facebook.com/nytopinion"
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": ", ",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": ", ",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "Twitter (@NYTopinion)",
                            "link": {
                                "url": "http://twitter.com/NYTOpinion"
                            }
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Twitter (@NYTopinion)",
                        "href": "http://twitter.com/NYTOpinion"
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": " and ",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": " and ",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "Instagram",
                            "link": {
                                "url": "https://www.instagram.com/nytopinion/"
                            }
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Instagram",
                        "href": "https://www.instagram.com/nytopinion/"
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": ", and sign up for the ",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": ", and sign up for the ",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "Opinion Today newsletter",
                            "link": {
                                "url": "http://www.nytimes.com/newsletters/opiniontoday/"
                            }
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Opinion Today newsletter",
                        "href": "http://www.nytimes.com/newsletters/opiniontoday/"
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": ".",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": ".",
                        "href": null
                    }
                ]
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

<br>

### Append block children 

---
> Request

```
PATCH https://api.notion.com/v1/blocks/:id/children
```


> Body

```json
{
	"children": [
		{
			"object": "block",
			"type": "heading_2",
			"heading_2": {
				"text": [{ "type": "text", "text": { "content": "Lacinato kale" } }]
			}
		},
		{
			"object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
							"link": { "url": "https://en.wikipedia.org/wiki/Lacinato_kale" }
						}
					}
				]
			}
		}
	]
}
```


> Response

*200 Success - Append block children*
```json
{
    "object": "block",
    "id": "a1712d54-53e4-4893-a69d-4d581cd2c845",
    "created_time": "2021-04-27T20:38:19.437Z",
    "last_edited_time": "2021-05-12T06:07:37.724Z",
    "has_children": true,
    "type": "child_page",
    "child_page": {
        "title": "Who Will Teach Silicon Valley to Be Ethical? "
    }
}
```

<br>

### Update a block 

---
> Request

```
PATCH https://api.notion.com/v1/blocks/:id
```


> Body

```json
{
    "paragraph": {
        "rich_text": [{
            "type": "text", 
            "text": { "content": "hello to you"}
        }]
    }
}
```


> Response

*200 Success - Update a block*
```json
{
    "object": "block",
    "id": "4868767d-9029-4b9d-a41b-652ef4c9c7b9",
    "created_time": "2021-08-06T17:46:00.000Z",
    "last_edited_time": "2021-08-12T00:12:00.000Z",
    "has_children": false,
    "type": "paragraph",
    "paragraph": {
        "text": [
            {
                "type": "text",
                "text": {
                    "content": "hello to you",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "hello to you",
                "href": null
            }
        ]
    }
}
```

<br>

### Retrieve a block 

---
> Request

```
GET https://api.notion.com/v1/blocks/:id
```


> Response

*200 Success - Retrieve a block*
```json
{
    "object": "block",
    "id": "4868767d-9029-4b9d-a41b-652ef4c9c7b9",
    "created_time": "2021-08-06T17:46:00.000Z",
    "last_edited_time": "2021-08-12T00:12:00.000Z",
    "has_children": false,
    "type": "paragraph",
    "paragraph": {
        "text": [
            {
                "type": "text",
                "text": {
                    "content": "hello to you",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "hello to you",
                "href": null
            }
        ]
    }
}
```

<br>

### Delete a block 

---
> Request

```
DELETE https://api.notion.com/v1/blocks/:id
```


> Response

*200 Success - Delete a block*
```json
{
    "object": "block",
    "id": "4868767d-9029-4b9d-a41b-652ef4c9c7b9",
    "created_time": "2021-08-06T17:46:00.000Z",
    "last_edited_time": "2022-02-24T22:26:00.000Z",
    "created_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
    },
    "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
    },
    "has_children": false,
    "archived": true,
    "type": "paragraph",
    "paragraph": {
        "text": [
            {
                "type": "text",
                "text": {
                    "content": "hello to you",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "hello to you",
                "href": null
            }
        ]
    }
}
```

<br>

### Search 

---
> Request

```
POST https://api.notion.com/v1/search
```


> Body

```json
{
    "query": "Media Article",
    "sort": {
        "direction": "ascending",
        "timestamp": "last_edited_time"
    }
}
```


> Responses

*200 Success - Search*
```json
{
    "object": "list",
    "results": [
        {
            "object": "page",
            "id": "ae1905c3-b77b-475b-b98f-7596c242137f",
            "created_time": "2021-05-21T16:41:00.000Z",
            "last_edited_time": "2021-05-21T16:41:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": true,
                                "italic": true,
                                "strikethrough": true,
                                "underline": true,
                                "code": true,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-ae1905c3b77b475bb98f7596c242137f"
        },
        {
            "object": "page",
            "id": "8f16061d-4b77-4dbc-bf04-e8b0b4319b5a",
            "created_time": "2021-05-21T16:42:00.000Z",
            "last_edited_time": "2021-05-21T16:42:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": true,
                                "italic": true,
                                "strikethrough": true,
                                "underline": true,
                                "code": true,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-8f16061d4b774dbcbf04e8b0b4319b5a"
        },
        {
            "object": "page",
            "id": "dc2a9117-163d-4075-907e-604b2f04c504",
            "created_time": "2021-06-15T17:23:00.000Z",
            "last_edited_time": "2021-06-15T17:23:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-dc2a9117163d4075907e604b2f04c504"
        },
        {
            "object": "page",
            "id": "c443c084-4637-4df2-ba37-b3c8a7e3d062",
            "created_time": "2021-06-15T17:23:00.000Z",
            "last_edited_time": "2021-06-15T17:23:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-c443c08446374df2ba37b3c8a7e3d062"
        },
        {
            "object": "page",
            "id": "0ac85319-05c5-4b5b-b812-7ea0f6476ea0",
            "created_time": "2021-06-15T17:23:00.000Z",
            "last_edited_time": "2021-06-15T17:23:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-0ac8531905c54b5bb8127ea0f6476ea0"
        },
        {
            "object": "page",
            "id": "794fc25a-7f59-419d-a6e5-d9f0b516ecc7",
            "created_time": "2021-06-15T17:24:00.000Z",
            "last_edited_time": "2021-06-15T17:24:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-794fc25a7f59419da6e5d9f0b516ecc7"
        },
        {
            "object": "page",
            "id": "41ad30b7-98e7-4c55-bf21-7ac7f09c2fd5",
            "created_time": "2021-06-15T17:24:00.000Z",
            "last_edited_time": "2021-06-15T17:24:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "b598e780-263b-4b02-862c-9bf7a91859ac",
                        "name": "New Option",
                        "color": "orange"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-41ad30b798e74c55bf217ac7f09c2fd5"
        },
        {
            "object": "page",
            "id": "6a313bae-fdd3-4617-9bd6-5b132f23be35",
            "created_time": "2021-06-15T17:24:00.000Z",
            "last_edited_time": "2021-06-15T17:24:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "ad038109-97d3-4b5d-a93a-3b88229b1b58",
                        "name": "New Option 3",
                        "color": "purple"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-6a313baefdd346179bd65b132f23be35"
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

*200 Success - Search*
```json
{
    "object": "list",
    "results": [
        {
            "object": "page",
            "id": "ae1905c3-b77b-475b-b98f-7596c242137f",
            "created_time": "2021-05-21T16:41:00.000Z",
            "last_edited_time": "2021-05-21T16:41:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": true,
                                "italic": true,
                                "strikethrough": true,
                                "underline": true,
                                "code": true,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-ae1905c3b77b475bb98f7596c242137f"
        },
        {
            "object": "page",
            "id": "8f16061d-4b77-4dbc-bf04-e8b0b4319b5a",
            "created_time": "2021-05-21T16:42:00.000Z",
            "last_edited_time": "2021-05-21T16:42:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": true,
                                "italic": true,
                                "strikethrough": true,
                                "underline": true,
                                "code": true,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-8f16061d4b774dbcbf04e8b0b4319b5a"
        },
        {
            "object": "page",
            "id": "dc2a9117-163d-4075-907e-604b2f04c504",
            "created_time": "2021-06-15T17:23:00.000Z",
            "last_edited_time": "2021-06-15T17:23:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-dc2a9117163d4075907e604b2f04c504"
        },
        {
            "object": "page",
            "id": "c443c084-4637-4df2-ba37-b3c8a7e3d062",
            "created_time": "2021-06-15T17:23:00.000Z",
            "last_edited_time": "2021-06-15T17:23:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-c443c08446374df2ba37b3c8a7e3d062"
        },
        {
            "object": "page",
            "id": "0ac85319-05c5-4b5b-b812-7ea0f6476ea0",
            "created_time": "2021-06-15T17:23:00.000Z",
            "last_edited_time": "2021-06-15T17:23:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-0ac8531905c54b5bb8127ea0f6476ea0"
        },
        {
            "object": "page",
            "id": "794fc25a-7f59-419d-a6e5-d9f0b516ecc7",
            "created_time": "2021-06-15T17:24:00.000Z",
            "last_edited_time": "2021-06-15T17:24:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                        "name": "Ready to Start",
                        "color": "yellow"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-794fc25a7f59419da6e5d9f0b516ecc7"
        },
        {
            "object": "page",
            "id": "41ad30b7-98e7-4c55-bf21-7ac7f09c2fd5",
            "created_time": "2021-06-15T17:24:00.000Z",
            "last_edited_time": "2021-06-15T17:24:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "b598e780-263b-4b02-862c-9bf7a91859ac",
                        "name": "New Option",
                        "color": "orange"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-41ad30b798e74c55bf217ac7f09c2fd5"
        },
        {
            "object": "page",
            "id": "6a313bae-fdd3-4617-9bd6-5b132f23be35",
            "created_time": "2021-06-15T17:24:00.000Z",
            "last_edited_time": "2021-06-15T17:24:00.000Z",
            "created_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "last_edited_by": {
                "object": "user",
                "id": "92a680bb-6970-4726-952b-4f4c03bff617"
            },
            "cover": null,
            "icon": null,
            "parent": {
                "type": "database_id",
                "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
            },
            "archived": false,
            "properties": {
                "Score /5": {
                    "id": ")Y7%22",
                    "type": "select",
                    "select": {
                        "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
                        "name": "⭐️⭐️⭐️⭐️⭐️",
                        "color": "default"
                    }
                },
                "Type": {
                    "id": "%2F7eo",
                    "type": "select",
                    "select": {
                        "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                        "name": "Article",
                        "color": "default"
                    }
                },
                "Publisher": {
                    "id": "%3E%24Pb",
                    "type": "select",
                    "select": {
                        "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                        "name": "The Atlantic",
                        "color": "red"
                    }
                },
                "Summary": {
                    "id": "%3F%5C25",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                            "href": null
                        }
                    ]
                },
                "Publishing/Release Date": {
                    "id": "%3Fex%2B",
                    "type": "date",
                    "date": {
                        "start": "2020-12-08T12:00:00.000+00:00",
                        "end": null,
                        "time_zone": null
                    }
                },
                "date": {
                    "id": "Lpwp",
                    "type": "date",
                    "date": null
                },
                "Link": {
                    "id": "VVMi",
                    "type": "url",
                    "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
                },
                "Wine Pairing": {
                    "id": "WO%40Z",
                    "type": "rich_text",
                    "rich_text": []
                },
                "Read": {
                    "id": "_MWJ",
                    "type": "checkbox",
                    "checkbox": false
                },
                "Status": {
                    "id": "%60zz5",
                    "type": "select",
                    "select": {
                        "id": "ad038109-97d3-4b5d-a93a-3b88229b1b58",
                        "name": "New Option 3",
                        "color": "purple"
                    }
                },
                "Author": {
                    "id": "qNw_",
                    "type": "multi_select",
                    "multi_select": []
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "New Media Article",
                                "link": null
                            },
                            "annotations": {
                                "bold": false,
                                "italic": false,
                                "strikethrough": false,
                                "underline": false,
                                "code": false,
                                "color": "default"
                            },
                            "plain_text": "New Media Article",
                            "href": null
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/New-Media-Article-6a313baefdd346179bd65b132f23be35"
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

<br>

### Retrieve comments 

---
> Request

```
GET https://api.notion.com/v1/comments?block_id={{BLOCK_ID}}&page_size=100
```

> Query parameters

**`block_id`**

**`page_size`**


> Response

*200 Success - Retrieve a comment*
```json
{
    "object": "list",
    "results": [
        {
            "object": "comment",
            "id": "ed4c62f2-c0ad-4081-b6b8-dad025637741",
            "parent": {
                "type": "block_id",
                "block_id": "5d4ca33c-d6b7-4675-93d9-84b70af45d1c"
            },
            "discussion_id": "ce18f8c6-ef2a-427f-b416-43531fc7c117",
            "created_time": "2022-07-15T21:38:00.000Z",
            "last_edited_time": "2022-07-15T21:38:00.000Z",
            "created_by": {
                "object": "user",
                "id": "952f41bb-da96-4d36-9c2e-74924eee8ef1"
            },
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Please cite your source",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "Please cite your source",
                    "href": null
                }
            ]
        },
        {
            "object": "comment",
            "id": "8949cb38-aee6-4c62-ba96-6ef7df9b4cf2",
            "parent": {
                "type": "block_id",
                "block_id": "5d4ca33c-d6b7-4675-93d9-84b70af45d1c"
            },
            "discussion_id": "e63f446f-a84a-4cab-8f5a-b9e7779ecb67",
            "created_time": "2022-07-15T21:38:00.000Z",
            "last_edited_time": "2022-07-15T21:38:00.000Z",
            "created_by": {
                "object": "user",
                "id": "952f41bb-da96-4d36-9c2e-74924eee8ef1"
            },
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "What other nutrients does kale have?",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "What other nutrients does kale have?",
                    "href": null
                }
            ]
        },
        {
            "object": "comment",
            "id": "6cd52483-6d55-4f8a-a724-4adb1c17ed43",
            "parent": {
                "type": "block_id",
                "block_id": "5d4ca33c-d6b7-4675-93d9-84b70af45d1c"
            },
            "discussion_id": "ce18f8c6-ef2a-427f-b416-43531fc7c117",
            "created_time": "2022-07-18T21:48:00.000Z",
            "last_edited_time": "2022-07-18T21:48:00.000Z",
            "created_by": {
                "object": "user",
                "id": "e450a39e-9051-4d36-bc4e-8581611fc592"
            },
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
                        "link": {
                            "url": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
                        }
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
                    "href": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
                }
            ]
        }
    ],
    "next_cursor": null,
    "has_more": false,
    "type": "comment",
    "comment": {}
}
```

<br>

### Add comment to page 

---
> Request

```
POST https://api.notion.com/v1/comments
```


> Body

```json
{
	"parent": {
		"page_id": "{{PAGE_ID}}"
	},
	"rich_text": [
		{
			"text": {
				"content": "Hello world"
			}
		}
	]
}
```


> Response

*200 Success - Add comment to page*
```json
{
    "object": "comment",
    "id": "be20daa4-31ed-45a2-9591-24f3dc3a61c2",
    "parent": {
        "type": "page_id",
        "page_id": "5c6a2821-6bb1-4a7e-b6e1-c50111515c3d"
    },
    "discussion_id": "cf4df352-6cc8-433c-9296-7f3550bfe421",
    "created_time": "2022-07-18T21:50:00.000Z",
    "last_edited_time": "2022-07-18T21:50:00.000Z",
    "created_by": {
        "object": "user",
        "id": "e450a39e-9051-4d36-bc4e-8581611fc592"
    },
    "rich_text": [
        {
            "type": "text",
            "text": {
                "content": "Hello world",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Hello world",
            "href": null
        }
    ]
}
```

<br>

### Add comment to discussion 

---
> Request

```
POST https://api.notion.com/v1/comments
```


> Body

```json
{
    "discussion_id": "{{DISCUSSION_ID}}",
    "rich_text": [
        {
            "text": {
                "content": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
                "link": {
                    "type": "url",
                    "url": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
                }
            }
        }
    ]
}
```


> Response

*200 Success - Add comment to page*
```json
{
    "object": "comment",
    "id": "6cd52483-6d55-4f8a-a724-4adb1c17ed43",
    "parent": {
        "type": "block_id",
        "block_id": "5d4ca33c-d6b7-4675-93d9-84b70af45d1c"
    },
    "discussion_id": "ce18f8c6-ef2a-427f-b416-43531fc7c117",
    "created_time": "2022-07-18T21:48:00.000Z",
    "last_edited_time": "2022-07-18T21:48:00.000Z",
    "created_by": {
        "object": "user",
        "id": "e450a39e-9051-4d36-bc4e-8581611fc592"
    },
    "rich_text": [
        {
            "type": "text",
            "text": {
                "content": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
                "link": {
                    "url": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
                }
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
            "href": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
        }
    ]
}
```

<br>

Generated with [Palourde](https://github.com/bagabool/palourde)