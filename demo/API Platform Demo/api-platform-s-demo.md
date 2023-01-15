# API Platform's demo ![auth](https://img.shields.io/badge/auth-apikey-orange)

<br>

This is a demo application of the [API Platform](https://api-platform.com) framework.
[Its source code](https://github.com/api-platform/demo) includes various examples, check it out!
You may also be interested by [the GraphQL entrypoint](/graphql).
[A PWA](/) and [an admin](/admin) are consuming this API.

<br>

## Requests

<br>

### Retrieves a Book resource. 

---
> Request

```
GET {{baseUrl}}/books/:id
```


> Responses

*Book resource*
```json
{
  "title": "ex",
  "description": "voluptate nostrud ullamco",
  "author": "esse",
  "publicationDate": "1951-06-26T01:40:49.639Z",
  "@context": "dolor",
  "@id": "ut cupidatat dolore",
  "@type": "sunt consectetur do magna",
  "id": "e22a78a0-bed4-fee9-f9ee-04940de5f1c1",
  "isbn": "qui elit cupidatat",
  "reviews": [
    {
      "body": "minim pariatur fugiat esse",
      "@context": "conse",
      "@id": "deserunt",
      "@type": "velit ut",
      "id": "urn:uuid:cfb7face-828a-5d3d-f92d-92cfaeb6127b"
    },
    {
      "body": "magna commodo elit amet",
      "@context": "irure deserunt consequat cupidatat aliquip",
      "@id": "labore",
      "@type": "esse deserunt anim",
      "id": "urn:uuid:699b3ac3-b47a-b5b9-ef30-4d479734039e"
    }
  ]
}
```

*Resource not found*: No response specified

<br>

### Replaces the Book resource. 

---
> Request

```
PUT {{baseUrl}}/books/:id
```


> Body

```json
{
  "title": "esse quis officia consequat",
  "description": "fugiat Duis",
  "author": "ex adipisicing tempor",
  "publicationDate": "1999-04-17T00:30:55.199Z",
  "isbn": "Duis incididunt",
  "reviews": [
    "aliqua Lorem officia aliquip",
    "sint reprehenderit"
  ],
  "cover": "incidi",
  "archivedAt": "2016-09-24T23:11:55.744Z"
}
```


> Responses

*Book resource updated*
```json
{
  "title": "ex",
  "description": "voluptate nostrud ullamco",
  "author": "esse",
  "publicationDate": "1951-06-26T01:40:49.639Z",
  "@context": "dolor",
  "@id": "ut cupidatat dolore",
  "@type": "sunt consectetur do magna",
  "id": "e22a78a0-bed4-fee9-f9ee-04940de5f1c1",
  "isbn": "qui elit cupidatat",
  "reviews": [
    {
      "body": "minim pariatur fugiat esse",
      "@context": "conse",
      "@id": "deserunt",
      "@type": "velit ut",
      "id": "urn:uuid:cfb7face-828a-5d3d-f92d-92cfaeb6127b"
    },
    {
      "body": "magna commodo elit amet",
      "@context": "irure deserunt consequat cupidatat aliquip",
      "@id": "labore",
      "@type": "esse deserunt anim",
      "id": "urn:uuid:699b3ac3-b47a-b5b9-ef30-4d479734039e"
    }
  ]
}
```

*Invalid input*: No response specified

*Resource not found*: No response specified

*Unprocessable entity*: No response specified

<br>

### Removes the Book resource. 

---
> Request

```
DELETE {{baseUrl}}/books/:id
```


> Responses

*Book resource deleted*: No response specified

*Resource not found*: No response specified

<br>

### Updates the Book resource. 

---
> Request

```
PATCH {{baseUrl}}/books/:id
```


> Body

```json
[object Object]
```


> Responses

*Book resource updated*
```json
{
  "title": "ex",
  "description": "voluptate nostrud ullamco",
  "author": "esse",
  "publicationDate": "1951-06-26T01:40:49.639Z",
  "@context": "dolor",
  "@id": "ut cupidatat dolore",
  "@type": "sunt consectetur do magna",
  "id": "e22a78a0-bed4-fee9-f9ee-04940de5f1c1",
  "isbn": "qui elit cupidatat",
  "reviews": [
    {
      "body": "minim pariatur fugiat esse",
      "@context": "conse",
      "@id": "deserunt",
      "@type": "velit ut",
      "id": "urn:uuid:cfb7face-828a-5d3d-f92d-92cfaeb6127b"
    },
    {
      "body": "magna commodo elit amet",
      "@context": "irure deserunt consequat cupidatat aliquip",
      "@id": "labore",
      "@type": "esse deserunt anim",
      "id": "urn:uuid:699b3ac3-b47a-b5b9-ef30-4d479734039e"
    }
  ]
}
```

*Invalid input*: No response specified

*Resource not found*: No response specified

*Unprocessable entity*: No response specified

<br>

### Replaces the Book resource. 

---
> Request

```
PUT {{baseUrl}}/books/:id/generate-cover
```


> Body

```json
{
  "title": "esse quis officia consequat",
  "description": "fugiat Duis",
  "author": "ex adipisicing tempor",
  "publicationDate": "1999-04-17T00:30:55.199Z",
  "isbn": "Duis incididunt",
  "reviews": [
    "aliqua Lorem officia aliquip",
    "sint reprehenderit"
  ],
  "cover": "incidi",
  "archivedAt": "2016-09-24T23:11:55.744Z"
}
```


> Responses

*Book resource updated*
```json
{}
```

*Invalid input*: No response specified

*Resource not found*: No response specified

*Unprocessable entity*: No response specified

<br>

### Retrieves the collection of Book resources. 

---
> Request

```
GET {{baseUrl}}/books?page=1&itemsPerPage=30&archived=true&order[id]=asc&order[title]=asc&order[author]=asc&order[isbn]=asc&order[publicationDate]=asc&properties[]=est tempor et incididunt&properties[]=do culpa&title=eu&author=eu
```

> Query parameters

**`page`**

The collection page number

**`itemsPerPage`**

The number of items per page

**`archived`**

**`order[id]`**

**`order[title]`**

**`order[author]`**

**`order[isbn]`**

**`order[publicationDate]`**

**`properties[]`**

**`properties[]`**

**`title`**

**`author`**


> Response

*Book collection*
```json
{
  "hydra:member": [
    {
      "title": "in aute",
      "description": "et irure reprehenderit occaecat",
      "author": "adipisicing incididunt veniam",
      "publicationDate": "1958-07-08T20:18:32.329Z",
      "@context": "cillum",
      "@id": "eiusmod exercitation nostrud anim",
      "@type": "incididunt eu enim ex laboris",
      "id": "urn:uuid:d49da2a2-649f-423a-a631-2dd1aafb05ef",
      "isbn": "officia est ipsum n",
      "reviews": [
        {
          "body": "non do qui ut",
          "@context": "ea",
          "@id": "laboris cillum",
          "@type": "labore ",
          "id": "28767b1d-1c34-20c2-0d97-3861e21ecf4b"
        },
        {
          "body": "amet Ut Excepteur",
          "@context": "ut sint velit",
          "@id": "proide",
          "@type": "cillum eiusmod",
          "id": "aa3eabda-fcf5-6235-f51e-9b9939637697"
        }
      ]
    },
    {
      "title": "eu dolor",
      "description": "sunt m",
      "author": "sunt E",
      "publicationDate": "1980-11-14T07:01:17.267Z",
      "@context": "dolor in reprehenderit in",
      "@id": "ex labore",
      "@type": "nisi pariatur reprehenderit elit",
      "id": "d47c78b6-f2e8-588a-3164-f11e75b6fc56",
      "isbn": "culpa elit sun",
      "reviews": [
        {
          "body": "minim non",
          "@context": "consectetur ullamco incididunt id",
          "@id": "incididunt velit ut elit",
          "@type": "pariatur sit deserunt",
          "id": "8649e5c2-52dd-f5cc-f0b8-0bda9db74bb4"
        },
        {
          "body": "eiusmod consectetur irure labore quis",
          "@context": "nisi Lorem",
          "@id": "esse Ut cupidatat adipisicing",
          "@type": "anim magna Lorem",
          "id": "99a8f80c-0298-c78a-8fe1-6129c1cd5f6f"
        }
      ]
    }
  ],
  "hydra:totalItems": 77275772,
  "hydra:view": {
    "@id": "string",
    "type": "string",
    "hydra:first": "string",
    "hydra:last": "string",
    "hydra:previous": "string",
    "hydra:next": "string"
  },
  "hydra:search": {
    "@type": "sed consequat",
    "hydra:template": "proident",
    "hydra:variableRepresentation": "reprehenderit Duis",
    "hydra:mapping": [
      {
        "@type": "ea",
        "variable": "cupidatat anim irure tempor dolore",
        "property": "enim consequat",
        "required": true
      },
      {
        "@type": "est qui ut",
        "variable": "aliqua Duis dolor",
        "property": "anim amet",
        "required": true
      }
    ]
  }
}
```

<br>

### Creates a Book resource. 

---
> Request

```
POST {{baseUrl}}/books
```


> Body

```json
{
  "title": "pariatur et",
  "description": "nisi",
  "author": "veniam cillum",
  "publicationDate": "2022-04-09T21:49:17.479Z",
  "isbn": "Duis aliqua ut eu eius",
  "reviews": [
    "ipsum commodo",
    "magna deserunt dolor consequat"
  ],
  "cover": "enim n",
  "archivedAt": "1968-03-08T21:18:12.216Z"
}
```


> Responses

*Book resource created*
```json
{
  "title": "ex",
  "description": "voluptate nostrud ullamco",
  "author": "esse",
  "publicationDate": "1951-06-26T01:40:49.639Z",
  "@context": "dolor",
  "@id": "ut cupidatat dolore",
  "@type": "sunt consectetur do magna",
  "id": "e22a78a0-bed4-fee9-f9ee-04940de5f1c1",
  "isbn": "qui elit cupidatat",
  "reviews": [
    {
      "body": "minim pariatur fugiat esse",
      "@context": "conse",
      "@id": "deserunt",
      "@type": "velit ut",
      "id": "urn:uuid:cfb7face-828a-5d3d-f92d-92cfaeb6127b"
    },
    {
      "body": "magna commodo elit amet",
      "@context": "irure deserunt consequat cupidatat aliquip",
      "@id": "labore",
      "@type": "esse deserunt anim",
      "id": "urn:uuid:699b3ac3-b47a-b5b9-ef30-4d479734039e"
    }
  ]
}
```

*Invalid input*: No response specified

*Unprocessable entity*: No response specified

<br>

### Retrieves the collection of Review resources. 

---
> Request

```
GET {{baseUrl}}/books/:bookId/reviews?page=1&order[id]=asc&order[publicationDate]=asc&book=eu&book[]=est tempor et incididunt&book[]=do culpa
```

> Query parameters

**`page`**

The collection page number

**`order[id]`**

**`order[publicationDate]`**

**`book`**

**`book[]`**

**`book[]`**


> Response

*Review collection*
```json
{
  "hydra:member": [
    {
      "body": "aliquip dolore Lorem culpa ad",
      "rating": 0,
      "book": {
        "title": "esse elit Lorem Duis velit",
        "@context": "cupidatat tempor do",
        "@id": "in proident",
        "@type": "nisi aute eu est"
      },
      "@id": "officia quis cillum",
      "@type": "laborum enim aute elit",
      "@context": "fugiat velit est",
      "id": "13605898-d780-6728-af64-a3d96780caee",
      "letter": "b",
      "author": "ipsum Lorem mollit",
      "publicationDate": "1965-06-15T12:47:12.787Z"
    },
    {
      "body": "ut sed incididunt proident et",
      "rating": 0,
      "book": {
        "title": "labo",
        "@context": "cillum dolor ut",
        "@id": "aute cupidatat velit do aliquip",
        "@type": "ex qui"
      },
      "@id": "elit eiusmod fugiat occaecat dolor",
      "@type": "irure enim",
      "@context": "tempor incididunt do non",
      "id": "2b28f935-bea6-1683-3f16-eeaa67bf234c",
      "letter": "a",
      "author": "labore id aliquip minim",
      "publicationDate": "1947-10-13T02:25:52.503Z"
    }
  ],
  "hydra:totalItems": 9898490,
  "hydra:view": {
    "@id": "string",
    "type": "string",
    "hydra:first": "string",
    "hydra:last": "string",
    "hydra:previous": "string",
    "hydra:next": "string"
  },
  "hydra:search": {
    "@type": "Duis nisi",
    "hydra:template": "dolore est aute Duis",
    "hydra:variableRepresentation": "aute id ad",
    "hydra:mapping": [
      {
        "@type": "in exercitation ad esse",
        "variable": "deserunt laboris incididunt ut",
        "property": "eiusmod mi",
        "required": true
      },
      {
        "@type": "reprehenderit sit velit",
        "variable": "ea nisi aute aliq",
        "property": "quis ex Ut consectetur",
        "required": false
      }
    ]
  }
}
```

<br>

### Retrieves a Parchment resource. 

---
> Request

```
GET {{baseUrl}}/parchments/:id
```


> Responses

*Parchment resource*
```json
{
  "title": "occaecat proident aliqua incididunt ut",
  "description": "Duis minim eiusmod anim",
  "@context": "dolor sed",
  "@id": "in Ut ",
  "@type": "veniam eu",
  "id": "330a7855-e8cd-4e4f-29f9-d83ea7fecbc2"
}
```

*Resource not found*: No response specified

<br>

### Replaces the Parchment resource. 

---
> Request

```
PUT {{baseUrl}}/parchments/:id
```


> Body

```json
{
  "title": "ullamco elit",
  "description": "pariatur amet est"
}
```


> Responses

*Parchment resource updated*
```json
{
  "title": "occaecat proident aliqua incididunt ut",
  "description": "Duis minim eiusmod anim",
  "@context": "dolor sed",
  "@id": "in Ut ",
  "@type": "veniam eu",
  "id": "330a7855-e8cd-4e4f-29f9-d83ea7fecbc2"
}
```

*Invalid input*: No response specified

*Resource not found*: No response specified

*Unprocessable entity*: No response specified

<br>

### Removes the Parchment resource. 

---
> Request

```
DELETE {{baseUrl}}/parchments/:id
```


> Responses

*Parchment resource deleted*: No response specified

*Resource not found*: No response specified

<br>

### Updates the Parchment resource. 

---
> Request

```
PATCH {{baseUrl}}/parchments/:id
```


> Body

```json
[object Object]
```


> Responses

*Parchment resource updated*
```json
{
  "title": "occaecat proident aliqua incididunt ut",
  "description": "Duis minim eiusmod anim",
  "@context": "dolor sed",
  "@id": "in Ut ",
  "@type": "veniam eu",
  "id": "330a7855-e8cd-4e4f-29f9-d83ea7fecbc2"
}
```

*Invalid input*: No response specified

*Resource not found*: No response specified

*Unprocessable entity*: No response specified

<br>

### Retrieves the collection of Parchment resources. 

---
> Request

```
GET {{baseUrl}}/parchments?page=1
```

> Query parameters

**`page`**

The collection page number


> Response

*Parchment collection*
```json
{
  "hydra:member": [
    {
      "title": "eu",
      "description": "sed irure",
      "@context": "",
      "@id": "laboris sint nisi enim reprehenderit",
      "@type": "sed Duis voluptate",
      "id": "urn:uuid:9127d881-7103-9e16-6de6-2f6576b1cde1"
    },
    {
      "title": "velit",
      "description": "reprehenderit commodo",
      "@context": "laboris sunt esse consequat",
      "@id": "laborum in velit",
      "@type": "ex veniam pariatur dolor in",
      "id": "urn:uuid:66d14e31-ff67-0c60-e900-3bb44a2f2213"
    }
  ],
  "hydra:totalItems": 87267620,
  "hydra:view": {
    "@id": "string",
    "type": "string",
    "hydra:first": "string",
    "hydra:last": "string",
    "hydra:previous": "string",
    "hydra:next": "string"
  },
  "hydra:search": {
    "@type": "sunt ex",
    "hydra:template": "anim nostrud dolore occaecat ea",
    "hydra:variableRepresentation": "qui nost",
    "hydra:mapping": [
      {
        "@type": "esse sunt",
        "variable": "ad minim ex ",
        "property": "consequat labore dolor",
        "required": true
      },
      {
        "@type": "culpa elit",
        "variable": "veniam Lorem",
        "property": "aute nulla elit laborum",
        "required": false
      }
    ]
  }
}
```

<br>

### Creates a Parchment resource. 

---
> Request

```
POST {{baseUrl}}/parchments
```


> Body

```json
{
  "title": "ullamco elit",
  "description": "pariatur amet est"
}
```


> Responses

*Parchment resource created*
```json
{
  "title": "occaecat proident aliqua incididunt ut",
  "description": "Duis minim eiusmod anim",
  "@context": "dolor sed",
  "@id": "in Ut ",
  "@type": "veniam eu",
  "id": "330a7855-e8cd-4e4f-29f9-d83ea7fecbc2"
}
```

*Invalid input*: No response specified

*Unprocessable entity*: No response specified

<br>

### Retrieves a Review resource. 

---
> Request

```
GET {{baseUrl}}/reviews/:id
```


> Responses

*Review resource*
```json
{
  "body": "nulla m",
  "rating": 2,
  "book": {
    "title": "sit",
    "@context": "eu fugiat consequat cupidatat velit",
    "@id": "dolore nisi qui incidi",
    "@type": "Duis veniam"
  },
  "@id": "laborum",
  "@type": "mollit in",
  "@context": "enim mollit",
  "id": "0539f27a-d49c-e028-ef34-24382dde4429",
  "letter": "c",
  "author": "laborum",
  "publicationDate": "1973-01-02T11:01:32.600Z"
}
```

*Resource not found*: No response specified

<br>

### Replaces the Review resource. 

---
> Request

```
PUT {{baseUrl}}/reviews/:id
```


> Body

```json
{
  "body": "non sed",
  "rating": 1,
  "book": "ut a",
  "letter": "d",
  "author": "voluptate dolore proident aliqua",
  "publicationDate": "2011-10-17T15:25:47.262Z"
}
```


> Responses

*Review resource updated*
```json
{
  "body": "nulla m",
  "rating": 2,
  "book": {
    "title": "sit",
    "@context": "eu fugiat consequat cupidatat velit",
    "@id": "dolore nisi qui incidi",
    "@type": "Duis veniam"
  },
  "@id": "laborum",
  "@type": "mollit in",
  "@context": "enim mollit",
  "id": "0539f27a-d49c-e028-ef34-24382dde4429",
  "letter": "c",
  "author": "laborum",
  "publicationDate": "1973-01-02T11:01:32.600Z"
}
```

*Invalid input*: No response specified

*Resource not found*: No response specified

*Unprocessable entity*: No response specified

<br>

### Removes the Review resource. 

---
> Request

```
DELETE {{baseUrl}}/reviews/:id
```


> Responses

*Review resource deleted*: No response specified

*Resource not found*: No response specified

<br>

### Updates the Review resource. 

---
> Request

```
PATCH {{baseUrl}}/reviews/:id
```


> Body

```json
[object Object]
```


> Responses

*Review resource updated*
```json
{
  "body": "nulla m",
  "rating": 2,
  "book": {
    "title": "sit",
    "@context": "eu fugiat consequat cupidatat velit",
    "@id": "dolore nisi qui incidi",
    "@type": "Duis veniam"
  },
  "@id": "laborum",
  "@type": "mollit in",
  "@context": "enim mollit",
  "id": "0539f27a-d49c-e028-ef34-24382dde4429",
  "letter": "c",
  "author": "laborum",
  "publicationDate": "1973-01-02T11:01:32.600Z"
}
```

*Invalid input*: No response specified

*Resource not found*: No response specified

*Unprocessable entity*: No response specified

<br>

### Retrieves the collection of Review resources. 

---
> Request

```
GET {{baseUrl}}/reviews?page=1&itemsPerPage=30&order[id]=asc&order[publicationDate]=asc&book=eu&book[]=est tempor et incididunt&book[]=do culpa
```

> Query parameters

**`page`**

The collection page number

**`itemsPerPage`**

The number of items per page

**`order[id]`**

**`order[publicationDate]`**

**`book`**

**`book[]`**

**`book[]`**


> Response

*Review collection*
```json
{
  "hydra:member": [
    {
      "body": "aliquip dolore Lorem culpa ad",
      "rating": 0,
      "book": {
        "title": "esse elit Lorem Duis velit",
        "@context": "cupidatat tempor do",
        "@id": "in proident",
        "@type": "nisi aute eu est"
      },
      "@id": "officia quis cillum",
      "@type": "laborum enim aute elit",
      "@context": "fugiat velit est",
      "id": "13605898-d780-6728-af64-a3d96780caee",
      "letter": "b",
      "author": "ipsum Lorem mollit",
      "publicationDate": "1965-06-15T12:47:12.787Z"
    },
    {
      "body": "ut sed incididunt proident et",
      "rating": 0,
      "book": {
        "title": "labo",
        "@context": "cillum dolor ut",
        "@id": "aute cupidatat velit do aliquip",
        "@type": "ex qui"
      },
      "@id": "elit eiusmod fugiat occaecat dolor",
      "@type": "irure enim",
      "@context": "tempor incididunt do non",
      "id": "2b28f935-bea6-1683-3f16-eeaa67bf234c",
      "letter": "a",
      "author": "labore id aliquip minim",
      "publicationDate": "1947-10-13T02:25:52.503Z"
    }
  ],
  "hydra:totalItems": 9898490,
  "hydra:view": {
    "@id": "string",
    "type": "string",
    "hydra:first": "string",
    "hydra:last": "string",
    "hydra:previous": "string",
    "hydra:next": "string"
  },
  "hydra:search": {
    "@type": "Duis nisi",
    "hydra:template": "dolore est aute Duis",
    "hydra:variableRepresentation": "aute id ad",
    "hydra:mapping": [
      {
        "@type": "in exercitation ad esse",
        "variable": "deserunt laboris incididunt ut",
        "property": "eiusmod mi",
        "required": true
      },
      {
        "@type": "reprehenderit sit velit",
        "variable": "ea nisi aute aliq",
        "property": "quis ex Ut consectetur",
        "required": false
      }
    ]
  }
}
```

<br>

### Creates a Review resource. 

---
> Request

```
POST {{baseUrl}}/reviews
```


> Body

```json
{
  "body": "non sed",
  "rating": 1,
  "book": "ut a",
  "letter": "d",
  "author": "voluptate dolore proident aliqua",
  "publicationDate": "2011-10-17T15:25:47.262Z"
}
```


> Responses

*Review resource created*
```json
{
  "body": "nulla m",
  "rating": 2,
  "book": {
    "title": "sit",
    "@context": "eu fugiat consequat cupidatat velit",
    "@id": "dolore nisi qui incidi",
    "@type": "Duis veniam"
  },
  "@id": "laborum",
  "@type": "mollit in",
  "@context": "enim mollit",
  "id": "0539f27a-d49c-e028-ef34-24382dde4429",
  "letter": "c",
  "author": "laborum",
  "publicationDate": "1973-01-02T11:01:32.600Z"
}
```

*Invalid input*: No response specified

*Unprocessable entity*: No response specified

<br>

### Retrieves the collection of TopBook resources. 

---
> Request

```
GET {{baseUrl}}/top_books?page=1
```

> Query parameters

**`page`**

The collection page number


> Response

*TopBook collection*
```json
{
  "hydra:member": [
    {
      "@context": "minim",
      "@id": "incididunt dolor",
      "@type": "officia anim tempor incididunt eu",
      "id": -2505774,
      "title": "Ut ex Duis conse",
      "author": "non Lorem",
      "part": "id",
      "place": "sed laborum",
      "borrowCount": -35695914
    },
    {
      "@context": "veniam culpa dolore ",
      "@id": "consequat nisi in",
      "@type": "dolor do sit",
      "id": -68848204,
      "title": "exercitation minim incididunt",
      "author": "ea ut elit aliquip",
      "part": "proident non officia",
      "place": "est ad laborum adipisi",
      "borrowCount": 70707087
    }
  ],
  "hydra:totalItems": 93403241,
  "hydra:view": {
    "@id": "string",
    "type": "string",
    "hydra:first": "string",
    "hydra:last": "string",
    "hydra:previous": "string",
    "hydra:next": "string"
  },
  "hydra:search": {
    "@type": "exercitation sed eiusmod et",
    "hydra:template": "ullamco sunt Duis ut",
    "hydra:variableRepresentation": "labore do id",
    "hydra:mapping": [
      {
        "@type": "esse ex labore",
        "variable": "proident dolore quis",
        "property": "nisi dolore do magna",
        "required": true
      },
      {
        "@type": "nisi",
        "variable": "nostrud proident",
        "property": "qui proident aliqua",
        "required": false
      }
    ]
  }
}
```

<br>

### Retrieves a TopBook resource. 

---
> Request

```
GET {{baseUrl}}/top_books/:id
```


> Responses

*TopBook resource*
```json
{
  "@context": "exercitation laborum culpa",
  "@id": "ex ipsum pariatur aliqua Lorem",
  "@type": "reprehenderit proident velit do anim",
  "id": -1655768,
  "title": "pariatur",
  "author": "elit velit ullamco deserunt cupidatat",
  "part": "veniam pariatur sint",
  "place": "exercitation",
  "borrowCount": -49018559
}
```

*Resource not found*: No response specified

<br>

### Retrieves the number of books and top books (legacy endpoint). 

---
> Request

```
GET {{baseUrl}}/stats
```


> Response

*Untitled Response*
```json
{
  "books_count": 997,
  "topbooks_count": 101
}
```

<br>

Generated with [Palourde](https://github.com/bagabool/palourde)