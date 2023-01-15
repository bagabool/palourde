# Google Analytics API 

<br>

Views and manages your Google Analytics data.

Contact Support:
 Name: Google

<br>

## Requests

<br>

### analytics.data.ga.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/data/ga?ids=<string>&start-date=<string>&end-date=<string>&metrics=<string>&dimensions=<string>&filters=<string>&include-empty-rows=<boolean>&max-results=<integer>&output=<string>&samplingLevel=<string>&segment=<string>&sort=<string>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`ids`**

(Required) Unique table ID for retrieving Analytics data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.

**`start-date`**

(Required) Start date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.

**`end-date`**

(Required) End date for fetching Analytics data. Request can should specify an end date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is yesterday.

**`metrics`**

(Required) A comma-separated list of Analytics metrics. E.g., 'ga:sessions,ga:pageviews'. At least one metric must be specified.

**`dimensions`**

A comma-separated list of Analytics dimensions. E.g., 'ga:browser,ga:city'.

**`filters`**

A comma-separated list of dimension or metric filters to be applied to Analytics data.

**`include-empty-rows`**

The response will include empty rows if this parameter is set to true, the default is true

**`max-results`**

The maximum number of entries to include in this feed.

**`output`**

The selected format for the response. Default format is JSON.

**`samplingLevel`**

The desired sampling level.

**`segment`**

An Analytics segment to be applied to data.

**`sort`**

A comma-separated list of dimensions or metrics that determine the sort order for Analytics data.

**`start-index`**

An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "columnHeaders": [
  {
   "columnType": "aute consect",
   "dataType": "ea aliquip dolor reprehenderit dolore",
   "name": "non officia"
  },
  {
   "columnType": "non velit esse aute elit",
   "dataType": "aliqua nulla",
   "name": "in in"
  }
 ],
 "containsSampledData": false,
 "dataLastRefreshed": "Ut reprehenderit in",
 "dataTable": {
  "cols": [
   {
    "id": "minim ut Duis aliqua velit",
    "label": "adipisicing deserunt",
    "type": "ut reprehenderit minim ea esse"
   },
   {
    "id": "occaecat dol",
    "label": "ea",
    "type": "officia deserunt"
   }
  ],
  "rows": [
   {
    "c": [
     {
      "v": "in aliquip"
     },
     {
      "v": "fugiat dolor consectetur proide"
     }
    ]
   },
   {
    "c": [
     {
      "v": "dolore"
     },
     {
      "v": "amet qui ad dolor"
     }
    ]
   }
  ]
 },
 "id": "sed in Duis",
 "itemsPerPage": -17456361,
 "kind": "analytics#gaData",
 "nextLink": "exercitation",
 "previousLink": "nulla id dolor sint",
 "profileInfo": {
  "accountId": "est aute exercitation irure",
  "internalWebPropertyId": "ipsum",
  "profileId": "veniam eiusmod Lorem",
  "profileName": "nisi laboris incididunt mollit",
  "tableId": "anim pariatur nisi exercitation officia",
  "webPropertyId": "laborum adipisicing"
 },
 "query": {
  "dimensions": "in eiusmod dolor laborum",
  "end-date": "quis aliquip velit Duis",
  "filters": "tempor cillum deserunt",
  "ids": "mollit reprehenderit nisi",
  "max-results": -48164987,
  "metrics": [
   "aliqua amet nostrud",
   "esse consectetur dolore"
  ],
  "samplingLevel": "et veniam eu",
  "segment": "anim ",
  "sort": [
   "ut adipisicing consectetur eiusmod proident",
   "proident aliqua consectetur nulla"
  ],
  "start-date": "non Lorem ex occaecat",
  "start-index": -23612019
 },
 "rows": [
  [
   "cillum minim do sint",
   "elit "
  ],
  [
   "nostrud in adipisicing labore",
   "deserunt"
  ]
 ],
 "sampleSize": "anim pariatur dolore",
 "sampleSpace": "quis in tempor nisi",
 "selfLink": "cupidatat nostrud",
 "totalResults": 81794720,
 "totalsForAllResults": {}
}
```

<br>

### analytics.data.mcf.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/data/mcf?ids=<string>&start-date=<string>&end-date=<string>&metrics=<string>&dimensions=<string>&filters=<string>&max-results=<integer>&samplingLevel=<string>&sort=<string>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`ids`**

(Required) Unique table ID for retrieving Analytics data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.

**`start-date`**

(Required) Start date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.

**`end-date`**

(Required) End date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.

**`metrics`**

(Required) A comma-separated list of Multi-Channel Funnels metrics. E.g., 'mcf:totalConversions,mcf:totalConversionValue'. At least one metric must be specified.

**`dimensions`**

A comma-separated list of Multi-Channel Funnels dimensions. E.g., 'mcf:source,mcf:medium'.

**`filters`**

A comma-separated list of dimension or metric filters to be applied to the Analytics data.

**`max-results`**

The maximum number of entries to include in this feed.

**`samplingLevel`**

The desired sampling level.

**`sort`**

A comma-separated list of dimensions or metrics that determine the sort order for the Analytics data.

**`start-index`**

An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "columnHeaders": [
  {
   "columnType": "Lorem amet",
   "dataType": "dolor",
   "name": "nisi dolor cillum eu"
  },
  {
   "columnType": "reprehe",
   "dataType": "irure in non",
   "name": "irure dolore in id tempor"
  }
 ],
 "containsSampledData": false,
 "id": "aut",
 "itemsPerPage": 5381721,
 "kind": "analytics#mcfData",
 "nextLink": "nisi minim aliquip",
 "previousLink": "qui non",
 "profileInfo": {
  "accountId": "do id",
  "internalWebPropertyId": "ea sint",
  "profileId": "non sint amet elit",
  "profileName": "pariatur dolor labore veniam",
  "tableId": "",
  "webPropertyId": "aute commodo"
 },
 "query": {
  "dimensions": "minim magna culpa",
  "end-date": "eu proident",
  "filters": "mollit dolor ut",
  "ids": "quis velit sunt dolore",
  "max-results": -76490902,
  "metrics": [
   "enim tempor nulla",
   "eiusmod eu irure"
  ],
  "samplingLevel": "eu veniam",
  "segment": "esse eiusmod sit nisi est",
  "sort": [
   "labore dolor consequat",
   "commodo occaecat"
  ],
  "start-date": "aliquip Lorem",
  "start-index": 77638097
 },
 "rows": [
  [
   {
    "conversionPathValue": [
     {
      "interactionType": "incididunt officia quis",
      "nodeValue": "aliquip Excepteur"
     },
     {
      "interactionType": "labore voluptate culpa incididunt",
      "nodeValue": "ipsum dolor"
     }
    ],
    "primitiveValue": "proident quis sed"
   },
   {
    "conversionPathValue": [
     {
      "interactionType": "do laboris",
      "nodeValue": "ea Duis"
     },
     {
      "interactionType": "dolore co",
      "nodeValue": "deserunt culpa irur"
     }
    ],
    "primitiveValue": "exercitation sed in"
   }
  ],
  [
   {
    "conversionPathValue": [
     {
      "interactionType": "veniam ea deserunt",
      "nodeValue": "amet mollit"
     },
     {
      "interactionType": "velit laboris quis",
      "nodeValue": "est non tempor"
     }
    ],
    "primitiveValue": "Excepteur"
   },
   {
    "conversionPathValue": [
     {
      "interactionType": "commodo in",
      "nodeValue": "nulla adipisicing eu ipsum in"
     },
     {
      "interactionType": "aliquip in elit Lorem",
      "nodeValue": "dolor sint eu quis"
     }
    ],
    "primitiveValue": "labore id qui irure"
   }
  ]
 ],
 "sampleSize": "ad",
 "sampleSpace": "voluptate Ut amet",
 "selfLink": "adipisicing Ut f",
 "totalResults": 3569524,
 "totalsForAllResults": {}
}
```

<br>

### analytics.data.realtime.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/data/realtime?ids=<string>&metrics=<string>&dimensions=<string>&filters=<string>&max-results=<integer>&sort=<string>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`ids`**

(Required) Unique table ID for retrieving real time data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.

**`metrics`**

(Required) A comma-separated list of real time metrics. E.g., 'rt:activeUsers'. At least one metric must be specified.

**`dimensions`**

A comma-separated list of real time dimensions. E.g., 'rt:medium,rt:city'.

**`filters`**

A comma-separated list of dimension or metric filters to be applied to real time data.

**`max-results`**

The maximum number of entries to include in this feed.

**`sort`**

A comma-separated list of dimensions or metrics that determine the sort order for real time data.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "columnHeaders": [
  {
   "columnType": "dolore Lorem sint ad",
   "dataType": "ea in",
   "name": "do cillum laboris nisi Lorem"
  },
  {
   "columnType": "voluptate nostrud proident",
   "dataType": "veniam Lorem aute",
   "name": "ad reprehenderit Duis aliquip"
  }
 ],
 "id": "id tempor Duis irure",
 "kind": "analytics#realtimeData",
 "profileInfo": {
  "accountId": "tempor irure in ad",
  "internalWebPropertyId": "velit labore",
  "profileId": "fugiat ex dolo",
  "profileName": "dolore ea exercitation Excepteur adipisicin",
  "tableId": "elit voluptate reprehenderit au",
  "webPropertyId": "in magna aliqua"
 },
 "query": {
  "dimensions": "do veniam proident",
  "filters": "sed labore",
  "ids": "cupidatat",
  "max-results": -68455575,
  "metrics": [
   "nulla pariatur voluptate",
   "do ips"
  ],
  "sort": [
   "id ut elit sunt nulla",
   "in magna ipsum consectetur aliqu"
  ]
 },
 "rows": [
  [
   "minim deserun",
   "occaecat sint"
  ],
  [
   "occaecat veniam",
   "cupidatat irure"
  ]
 ],
 "selfLink": "Lorem",
 "totalResults": 69564883,
 "totalsForAllResults": {}
}
```

<br>

### analytics.management.account User Links.delete ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
DELETE {{baseUrl}}/management/accounts/:accountId/entityUserLinks/:linkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*: No response specified

<br>

### analytics.management.account User Links.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/entityUserLinks/:linkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "entity": {
        "accountRef": {
            "href": "sit tempor ut ea",
            "id": "ut ea",
            "kind": "analytics#accountRef",
            "name": "veniam"
        },
        "profileRef": {
            "accountId": "culpa",
            "href": "ipsum nostrud minim occaecat",
            "id": "laboris aute id est",
            "internalWebPropertyId": "enim in non tempor quis",
            "kind": "analytics#profileRef",
            "name": "Duis veniam",
            "webPropertyId": "Lorem in"
        },
        "webPropertyRef": {
            "accountId": "amet",
            "href": "sed proident amet tempor Excepteur",
            "id": "qui irure dolor",
            "internalWebPropertyId": "sunt tempor exercitation elit enim",
            "kind": "analytics#webPropertyRef",
            "name": "esse"
        }
    },
    "id": "<string>",
    "kind": "analytics#entityUserLink",
    "permissions": {
        "local": [
            "<string>",
            "<string>"
        ]
    },
    "selfLink": "<string>",
    "userRef": {
        "email": "dolore",
        "id": "sed ex cillum id quis",
        "kind": "analytics#userRef"
    }
}
```


> Response

*Successful response*
```json
{
 "entity": {
  "accountRef": {
   "href": "culpa enim veniam",
   "id": "Lorem tempor exercitation fugiat",
   "kind": "analytics#accountRef",
   "name": "reprehenderit nulla aute aliq"
  },
  "profileRef": {
   "accountId": "Ut amet",
   "href": "proident voluptate amet",
   "id": "quis et deserunt",
   "internalWebPropertyId": "enim velit eiusmod",
   "kind": "analytics#profileRef",
   "name": "esse in aute ullamco",
   "webPropertyId": "Excepteur"
  },
  "webPropertyRef": {
   "accountId": "voluptate dolore nostrud",
   "href": "cillum ullamco in aliquip",
   "id": "consectetur sunt l",
   "internalWebPropertyId": "pariatur in",
   "kind": "analytics#webPropertyRef",
   "name": "laborum quis nulla"
  }
 },
 "id": "<string>",
 "kind": "analytics#entityUserLink",
 "permissions": {
  "effective": [
   "consectetur magna pariatur incididunt",
   "Lorem reprehenderit"
  ],
  "local": [
   "<string>",
   "<string>"
  ]
 },
 "selfLink": "<string>",
 "userRef": {
  "email": "eu elit reprehenderit Excepteur sed",
  "id": "dolor quis",
  "kind": "analytics#userRef"
 }
}
```

<br>

### analytics.management.account User Links.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/entityUserLinks?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of account-user links to include in this response.

**`start-index`**

An index of the first account-user link to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "entity": {
    "accountRef": {
     "href": "ea dolore cupidatat in",
     "id": "commodo in",
     "kind": "analytics#accountRef",
     "name": "magna"
    },
    "profileRef": {
     "accountId": "ullamco veniam velit consectetur aute",
     "href": "cillum enim",
     "id": "voluptate deserunt nostrud aliquip proident",
     "internalWebPropertyId": "laboris id ip",
     "kind": "analytics#profileRef",
     "name": "sit ut",
     "webPropertyId": "velit"
    },
    "webPropertyRef": {
     "accountId": "consectetur ut",
     "href": "ullamco",
     "id": "et pariatur tempor dolore",
     "internalWebPropertyId": "deserunt laborum amet ad",
     "kind": "analytics#webPropertyRef",
     "name": "adipisicing nulla"
    }
   },
   "id": "aliqua voluptate",
   "kind": "analytics#entityUserLink",
   "permissions": {
    "effective": [
     "sed",
     "ullamco"
    ],
    "local": [
     "officia pariat",
     "dolor in elit"
    ]
   },
   "selfLink": "sint sed qui Lorem proident",
   "userRef": {
    "email": "nulla consectetur",
    "id": "quis ipsum laborum c",
    "kind": "analytics#userRef"
   }
  },
  {
   "entity": {
    "accountRef": {
     "href": "Excepteur est esse ipsum adipisicing",
     "id": "mollit cupidatat consequat dolor ut",
     "kind": "analytics#accountRef",
     "name": "dolor nisi id sed"
    },
    "profileRef": {
     "accountId": "amet Ut in laborum",
     "href": "dolore commodo sint",
     "id": "occaecat irure veniam",
     "internalWebPropertyId": "",
     "kind": "analytics#profileRef",
     "name": "sit pariatur magna fugiat",
     "webPropertyId": "dolore"
    },
    "webPropertyRef": {
     "accountId": "in consectetur sint ",
     "href": "cillum dolore commodo nisi",
     "id": "pariatur",
     "internalWebPropertyId": "est culpa",
     "kind": "analytics#webPropertyRef",
     "name": "est velit nulla"
    }
   },
   "id": "amet",
   "kind": "analytics#entityUserLink",
   "permissions": {
    "effective": [
     "in veniam",
     "ullamco labore reprehender"
    ],
    "local": [
     "consectetur enim laboris voluptate",
     "ut irure"
    ]
   },
   "selfLink": "Ut",
   "userRef": {
    "email": "anim",
    "id": "do",
    "kind": "analytics#userRef"
   }
  }
 ],
 "itemsPerPage": -37808693,
 "kind": "analytics#entityUserLinks",
 "nextLink": "non aliqu",
 "previousLink": "in adipisicing dolor ipsum quis",
 "startIndex": -39956183,
 "totalResults": 42780959
}
```

<br>

### analytics.management.account User Links.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/entityUserLinks?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "entity": {
        "accountRef": {
            "href": "sit tempor ut ea",
            "id": "ut ea",
            "kind": "analytics#accountRef",
            "name": "veniam"
        },
        "profileRef": {
            "accountId": "culpa",
            "href": "ipsum nostrud minim occaecat",
            "id": "laboris aute id est",
            "internalWebPropertyId": "enim in non tempor quis",
            "kind": "analytics#profileRef",
            "name": "Duis veniam",
            "webPropertyId": "Lorem in"
        },
        "webPropertyRef": {
            "accountId": "amet",
            "href": "sed proident amet tempor Excepteur",
            "id": "qui irure dolor",
            "internalWebPropertyId": "sunt tempor exercitation elit enim",
            "kind": "analytics#webPropertyRef",
            "name": "esse"
        }
    },
    "id": "<string>",
    "kind": "analytics#entityUserLink",
    "permissions": {
        "local": [
            "<string>",
            "<string>"
        ]
    },
    "selfLink": "<string>",
    "userRef": {
        "email": "dolore",
        "id": "sed ex cillum id quis",
        "kind": "analytics#userRef"
    }
}
```


> Response

*Successful response*
```json
{
 "entity": {
  "accountRef": {
   "href": "culpa enim veniam",
   "id": "Lorem tempor exercitation fugiat",
   "kind": "analytics#accountRef",
   "name": "reprehenderit nulla aute aliq"
  },
  "profileRef": {
   "accountId": "Ut amet",
   "href": "proident voluptate amet",
   "id": "quis et deserunt",
   "internalWebPropertyId": "enim velit eiusmod",
   "kind": "analytics#profileRef",
   "name": "esse in aute ullamco",
   "webPropertyId": "Excepteur"
  },
  "webPropertyRef": {
   "accountId": "voluptate dolore nostrud",
   "href": "cillum ullamco in aliquip",
   "id": "consectetur sunt l",
   "internalWebPropertyId": "pariatur in",
   "kind": "analytics#webPropertyRef",
   "name": "laborum quis nulla"
  }
 },
 "id": "<string>",
 "kind": "analytics#entityUserLink",
 "permissions": {
  "effective": [
   "consectetur magna pariatur incididunt",
   "Lorem reprehenderit"
  ],
  "local": [
   "<string>",
   "<string>"
  ]
 },
 "selfLink": "<string>",
 "userRef": {
  "email": "eu elit reprehenderit Excepteur sed",
  "id": "dolor quis",
  "kind": "analytics#userRef"
 }
}
```

<br>

### analytics.management.filters.delete ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
DELETE {{baseUrl}}/management/accounts/:accountId/filters/:filterId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "advancedDetails": {
  "caseSensitive": "<boolean>",
  "extractA": "<string>",
  "extractB": "<string>",
  "fieldA": "<string>",
  "fieldAIndex": "<integer>",
  "fieldARequired": "<boolean>",
  "fieldB": "<string>",
  "fieldBIndex": "<integer>",
  "fieldBRequired": "<boolean>",
  "outputConstructor": "<string>",
  "outputToField": "<string>",
  "outputToFieldIndex": "<integer>",
  "overrideOutputField": "<boolean>"
 },
 "created": "2015-01-27T01:38:01.293Z",
 "excludeDetails": {
  "caseSensitive": true,
  "expressionValue": "deserunt",
  "field": "anim ullamco",
  "fieldIndex": 98538224,
  "kind": "analytics#filterExpression",
  "matchType": "Excepteur labore Duis est ex"
 },
 "id": "<string>",
 "includeDetails": {
  "caseSensitive": false,
  "expressionValue": "paria",
  "field": "aute officia",
  "fieldIndex": 66221406,
  "kind": "analytics#filterExpression",
  "matchType": "qui sed "
 },
 "kind": "analytics#filter",
 "lowercaseDetails": {
  "field": "<string>",
  "fieldIndex": "<integer>"
 },
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#account"
 },
 "searchAndReplaceDetails": {
  "caseSensitive": "<boolean>",
  "field": "<string>",
  "fieldIndex": "<integer>",
  "replaceString": "<string>",
  "searchString": "<string>"
 },
 "selfLink": "id eiusmod aute",
 "type": "<string>",
 "updated": "1977-12-07T12:59:31.601Z",
 "uppercaseDetails": {
  "field": "<string>",
  "fieldIndex": "<integer>"
 }
}
```

<br>

### analytics.management.filters.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/filters/:filterId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "advancedDetails": {
  "caseSensitive": "<boolean>",
  "extractA": "<string>",
  "extractB": "<string>",
  "fieldA": "<string>",
  "fieldAIndex": "<integer>",
  "fieldARequired": "<boolean>",
  "fieldB": "<string>",
  "fieldBIndex": "<integer>",
  "fieldBRequired": "<boolean>",
  "outputConstructor": "<string>",
  "outputToField": "<string>",
  "outputToFieldIndex": "<integer>",
  "overrideOutputField": "<boolean>"
 },
 "created": "2015-01-27T01:38:01.293Z",
 "excludeDetails": {
  "caseSensitive": true,
  "expressionValue": "deserunt",
  "field": "anim ullamco",
  "fieldIndex": 98538224,
  "kind": "analytics#filterExpression",
  "matchType": "Excepteur labore Duis est ex"
 },
 "id": "<string>",
 "includeDetails": {
  "caseSensitive": false,
  "expressionValue": "paria",
  "field": "aute officia",
  "fieldIndex": 66221406,
  "kind": "analytics#filterExpression",
  "matchType": "qui sed "
 },
 "kind": "analytics#filter",
 "lowercaseDetails": {
  "field": "<string>",
  "fieldIndex": "<integer>"
 },
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#account"
 },
 "searchAndReplaceDetails": {
  "caseSensitive": "<boolean>",
  "field": "<string>",
  "fieldIndex": "<integer>",
  "replaceString": "<string>",
  "searchString": "<string>"
 },
 "selfLink": "id eiusmod aute",
 "type": "<string>",
 "updated": "1977-12-07T12:59:31.601Z",
 "uppercaseDetails": {
  "field": "<string>",
  "fieldIndex": "<integer>"
 }
}
```

<br>

### analytics.management.filters.patch ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PATCH {{baseUrl}}/management/accounts/:accountId/filters/:filterId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "advancedDetails": {
        "caseSensitive": "<boolean>",
        "extractA": "<string>",
        "extractB": "<string>",
        "fieldA": "<string>",
        "fieldAIndex": "<integer>",
        "fieldARequired": "<boolean>",
        "fieldB": "<string>",
        "fieldBIndex": "<integer>",
        "fieldBRequired": "<boolean>",
        "outputConstructor": "<string>",
        "outputToField": "<string>",
        "outputToFieldIndex": "<integer>",
        "overrideOutputField": "<boolean>"
    },
    "excludeDetails": {
        "caseSensitive": true,
        "expressionValue": "nostrud eu pariatur et sed",
        "field": "aliqua dolore consectetur ullamco",
        "fieldIndex": -99094297,
        "kind": "analytics#filterExpression",
        "matchType": "est occaecat do Excepteur"
    },
    "id": "<string>",
    "includeDetails": {
        "caseSensitive": false,
        "expressionValue": "occaecat reprehenderit cupidatat sunt sint",
        "field": "in dolor Ut",
        "fieldIndex": 28991676,
        "kind": "analytics#filterExpression",
        "matchType": "ullamco"
    },
    "lowercaseDetails": {
        "field": "<string>",
        "fieldIndex": "<integer>"
    },
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#account"
    },
    "searchAndReplaceDetails": {
        "caseSensitive": "<boolean>",
        "field": "<string>",
        "fieldIndex": "<integer>",
        "replaceString": "<string>",
        "searchString": "<string>"
    },
    "type": "<string>",
    "uppercaseDetails": {
        "field": "<string>",
        "fieldIndex": "<integer>"
    }
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "advancedDetails": {
  "caseSensitive": "<boolean>",
  "extractA": "<string>",
  "extractB": "<string>",
  "fieldA": "<string>",
  "fieldAIndex": "<integer>",
  "fieldARequired": "<boolean>",
  "fieldB": "<string>",
  "fieldBIndex": "<integer>",
  "fieldBRequired": "<boolean>",
  "outputConstructor": "<string>",
  "outputToField": "<string>",
  "outputToFieldIndex": "<integer>",
  "overrideOutputField": "<boolean>"
 },
 "created": "2015-01-27T01:38:01.293Z",
 "excludeDetails": {
  "caseSensitive": true,
  "expressionValue": "deserunt",
  "field": "anim ullamco",
  "fieldIndex": 98538224,
  "kind": "analytics#filterExpression",
  "matchType": "Excepteur labore Duis est ex"
 },
 "id": "<string>",
 "includeDetails": {
  "caseSensitive": false,
  "expressionValue": "paria",
  "field": "aute officia",
  "fieldIndex": 66221406,
  "kind": "analytics#filterExpression",
  "matchType": "qui sed "
 },
 "kind": "analytics#filter",
 "lowercaseDetails": {
  "field": "<string>",
  "fieldIndex": "<integer>"
 },
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#account"
 },
 "searchAndReplaceDetails": {
  "caseSensitive": "<boolean>",
  "field": "<string>",
  "fieldIndex": "<integer>",
  "replaceString": "<string>",
  "searchString": "<string>"
 },
 "selfLink": "id eiusmod aute",
 "type": "<string>",
 "updated": "1977-12-07T12:59:31.601Z",
 "uppercaseDetails": {
  "field": "<string>",
  "fieldIndex": "<integer>"
 }
}
```

<br>

### analytics.management.filters.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/filters/:filterId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "advancedDetails": {
        "caseSensitive": "<boolean>",
        "extractA": "<string>",
        "extractB": "<string>",
        "fieldA": "<string>",
        "fieldAIndex": "<integer>",
        "fieldARequired": "<boolean>",
        "fieldB": "<string>",
        "fieldBIndex": "<integer>",
        "fieldBRequired": "<boolean>",
        "outputConstructor": "<string>",
        "outputToField": "<string>",
        "outputToFieldIndex": "<integer>",
        "overrideOutputField": "<boolean>"
    },
    "excludeDetails": {
        "caseSensitive": true,
        "expressionValue": "nostrud eu pariatur et sed",
        "field": "aliqua dolore consectetur ullamco",
        "fieldIndex": -99094297,
        "kind": "analytics#filterExpression",
        "matchType": "est occaecat do Excepteur"
    },
    "id": "<string>",
    "includeDetails": {
        "caseSensitive": false,
        "expressionValue": "occaecat reprehenderit cupidatat sunt sint",
        "field": "in dolor Ut",
        "fieldIndex": 28991676,
        "kind": "analytics#filterExpression",
        "matchType": "ullamco"
    },
    "lowercaseDetails": {
        "field": "<string>",
        "fieldIndex": "<integer>"
    },
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#account"
    },
    "searchAndReplaceDetails": {
        "caseSensitive": "<boolean>",
        "field": "<string>",
        "fieldIndex": "<integer>",
        "replaceString": "<string>",
        "searchString": "<string>"
    },
    "type": "<string>",
    "uppercaseDetails": {
        "field": "<string>",
        "fieldIndex": "<integer>"
    }
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "advancedDetails": {
  "caseSensitive": "<boolean>",
  "extractA": "<string>",
  "extractB": "<string>",
  "fieldA": "<string>",
  "fieldAIndex": "<integer>",
  "fieldARequired": "<boolean>",
  "fieldB": "<string>",
  "fieldBIndex": "<integer>",
  "fieldBRequired": "<boolean>",
  "outputConstructor": "<string>",
  "outputToField": "<string>",
  "outputToFieldIndex": "<integer>",
  "overrideOutputField": "<boolean>"
 },
 "created": "2015-01-27T01:38:01.293Z",
 "excludeDetails": {
  "caseSensitive": true,
  "expressionValue": "deserunt",
  "field": "anim ullamco",
  "fieldIndex": 98538224,
  "kind": "analytics#filterExpression",
  "matchType": "Excepteur labore Duis est ex"
 },
 "id": "<string>",
 "includeDetails": {
  "caseSensitive": false,
  "expressionValue": "paria",
  "field": "aute officia",
  "fieldIndex": 66221406,
  "kind": "analytics#filterExpression",
  "matchType": "qui sed "
 },
 "kind": "analytics#filter",
 "lowercaseDetails": {
  "field": "<string>",
  "fieldIndex": "<integer>"
 },
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#account"
 },
 "searchAndReplaceDetails": {
  "caseSensitive": "<boolean>",
  "field": "<string>",
  "fieldIndex": "<integer>",
  "replaceString": "<string>",
  "searchString": "<string>"
 },
 "selfLink": "id eiusmod aute",
 "type": "<string>",
 "updated": "1977-12-07T12:59:31.601Z",
 "uppercaseDetails": {
  "field": "<string>",
  "fieldIndex": "<integer>"
 }
}
```

<br>

### analytics.management.filters.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/filters?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of filters to include in this response.

**`start-index`**

An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "mollit Lorem deserunt",
   "advancedDetails": {
    "caseSensitive": true,
    "extractA": "Ut est qui ad",
    "extractB": "qui incididunt",
    "fieldA": "aute adipisici",
    "fieldAIndex": -11978549,
    "fieldARequired": true,
    "fieldB": "ipsum adipisicing in",
    "fieldBIndex": -33638555,
    "fieldBRequired": false,
    "outputConstructor": "nulla",
    "outputToField": "dolor nostrud et ut",
    "outputToFieldIndex": 80607666,
    "overrideOutputField": false
   },
   "created": "1964-10-14T22:43:00.278Z",
   "excludeDetails": {
    "caseSensitive": false,
    "expressionValue": "sunt nostrud sit",
    "field": "Duis velit nulla nostrud",
    "fieldIndex": 66794825,
    "kind": "analytics#filterExpression",
    "matchType": "mollit aliquip cillum"
   },
   "id": "elit qui anim magna",
   "includeDetails": {
    "caseSensitive": true,
    "expressionValue": "laboris et",
    "field": "ex esse ea nulla cillum",
    "fieldIndex": -90599547,
    "kind": "analytics#filterExpression",
    "matchType": "dolore ea ex dolo"
   },
   "kind": "analytics#filter",
   "lowercaseDetails": {
    "field": "eu ut exercitation",
    "fieldIndex": -461594
   },
   "name": "proident occaecat Lorem",
   "parentLink": {
    "href": "proident irure culpa ullamco",
    "type": "analytics#account"
   },
   "searchAndReplaceDetails": {
    "caseSensitive": false,
    "field": "sit cupidatat esse",
    "fieldIndex": 55860523,
    "replaceString": "in est laboru",
    "searchString": "Lorem anim nisi eiusmod est"
   },
   "selfLink": "consectetur dolore ",
   "type": "dolore aliqua",
   "updated": "2005-12-28T12:54:17.357Z",
   "uppercaseDetails": {
    "field": "ut",
    "fieldIndex": -32469776
   }
  },
  {
   "accountId": "elit nostrud",
   "advancedDetails": {
    "caseSensitive": false,
    "extractA": "sed ut in",
    "extractB": "cupidatat et sed",
    "fieldA": "",
    "fieldAIndex": -16753451,
    "fieldARequired": true,
    "fieldB": "enim occaecat culpa",
    "fieldBIndex": 87492746,
    "fieldBRequired": false,
    "outputConstructor": "eiusmod Ut aute fugiat",
    "outputToField": "elit qui",
    "outputToFieldIndex": 23362448,
    "overrideOutputField": false
   },
   "created": "1978-04-01T09:34:09.436Z",
   "excludeDetails": {
    "caseSensitive": false,
    "expressionValue": "in aute anim et",
    "field": "pariatur reprehenderit eu",
    "fieldIndex": 31620959,
    "kind": "analytics#filterExpression",
    "matchType": "eiusmod ani"
   },
   "id": "consectetur sunt mo",
   "includeDetails": {
    "caseSensitive": true,
    "expressionValue": "est in ut reprehenderit",
    "field": "labori",
    "fieldIndex": -45848463,
    "kind": "analytics#filterExpression",
    "matchType": "eiusmod exercitation"
   },
   "kind": "analytics#filter",
   "lowercaseDetails": {
    "field": "nostrud",
    "fieldIndex": 18233361
   },
   "name": "amet dolor qui culp",
   "parentLink": {
    "href": "minim ullamco magna commodo",
    "type": "analytics#account"
   },
   "searchAndReplaceDetails": {
    "caseSensitive": true,
    "field": "quis inci",
    "fieldIndex": -47453104,
    "replaceString": "aliquip proident reprehenderit qui eiusmod",
    "searchString": "laborum Duis commodo"
   },
   "selfLink": "occaeca",
   "type": "adipisicing cillum",
   "updated": "2019-03-13T03:52:38.874Z",
   "uppercaseDetails": {
    "field": "dolor",
    "fieldIndex": 69625508
   }
  }
 ],
 "itemsPerPage": 30858091,
 "kind": "analytics#filters",
 "nextLink": "proident rep",
 "previousLink": "ad velit ipsum",
 "startIndex": -12489201,
 "totalResults": -69310077,
 "username": "quis"
}
```

<br>

### analytics.management.filters.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/filters?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "advancedDetails": {
        "caseSensitive": "<boolean>",
        "extractA": "<string>",
        "extractB": "<string>",
        "fieldA": "<string>",
        "fieldAIndex": "<integer>",
        "fieldARequired": "<boolean>",
        "fieldB": "<string>",
        "fieldBIndex": "<integer>",
        "fieldBRequired": "<boolean>",
        "outputConstructor": "<string>",
        "outputToField": "<string>",
        "outputToFieldIndex": "<integer>",
        "overrideOutputField": "<boolean>"
    },
    "excludeDetails": {
        "caseSensitive": true,
        "expressionValue": "nostrud eu pariatur et sed",
        "field": "aliqua dolore consectetur ullamco",
        "fieldIndex": -99094297,
        "kind": "analytics#filterExpression",
        "matchType": "est occaecat do Excepteur"
    },
    "id": "<string>",
    "includeDetails": {
        "caseSensitive": false,
        "expressionValue": "occaecat reprehenderit cupidatat sunt sint",
        "field": "in dolor Ut",
        "fieldIndex": 28991676,
        "kind": "analytics#filterExpression",
        "matchType": "ullamco"
    },
    "lowercaseDetails": {
        "field": "<string>",
        "fieldIndex": "<integer>"
    },
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#account"
    },
    "searchAndReplaceDetails": {
        "caseSensitive": "<boolean>",
        "field": "<string>",
        "fieldIndex": "<integer>",
        "replaceString": "<string>",
        "searchString": "<string>"
    },
    "type": "<string>",
    "uppercaseDetails": {
        "field": "<string>",
        "fieldIndex": "<integer>"
    }
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "advancedDetails": {
  "caseSensitive": "<boolean>",
  "extractA": "<string>",
  "extractB": "<string>",
  "fieldA": "<string>",
  "fieldAIndex": "<integer>",
  "fieldARequired": "<boolean>",
  "fieldB": "<string>",
  "fieldBIndex": "<integer>",
  "fieldBRequired": "<boolean>",
  "outputConstructor": "<string>",
  "outputToField": "<string>",
  "outputToFieldIndex": "<integer>",
  "overrideOutputField": "<boolean>"
 },
 "created": "2015-01-27T01:38:01.293Z",
 "excludeDetails": {
  "caseSensitive": true,
  "expressionValue": "deserunt",
  "field": "anim ullamco",
  "fieldIndex": 98538224,
  "kind": "analytics#filterExpression",
  "matchType": "Excepteur labore Duis est ex"
 },
 "id": "<string>",
 "includeDetails": {
  "caseSensitive": false,
  "expressionValue": "paria",
  "field": "aute officia",
  "fieldIndex": 66221406,
  "kind": "analytics#filterExpression",
  "matchType": "qui sed "
 },
 "kind": "analytics#filter",
 "lowercaseDetails": {
  "field": "<string>",
  "fieldIndex": "<integer>"
 },
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#account"
 },
 "searchAndReplaceDetails": {
  "caseSensitive": "<boolean>",
  "field": "<string>",
  "fieldIndex": "<integer>",
  "replaceString": "<string>",
  "searchString": "<string>"
 },
 "selfLink": "id eiusmod aute",
 "type": "<string>",
 "updated": "1977-12-07T12:59:31.601Z",
 "uppercaseDetails": {
  "field": "<string>",
  "fieldIndex": "<integer>"
 }
}
```

<br>

### analytics.management.uploads.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customDataSources/:customDataSourceId/uploads?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of uploads to include in this response.

**`start-index`**

A 1-based index of the first upload to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "ipsum ea cill",
   "customDataSourceId": "sunt esse ea quis",
   "errors": [
    "o",
    "sed labore"
   ],
   "id": "ut voluptate aliquip tempor est",
   "kind": "analytics#upload",
   "status": "ut",
   "uploadTime": "1990-11-12T01:31:46.585Z"
  },
  {
   "accountId": "consectetur sunt commodo occaecat sed",
   "customDataSourceId": "est nulla",
   "errors": [
    "ex ad Ut Duis",
    "con"
   ],
   "id": "pariatur Duis nulla eu",
   "kind": "analytics#upload",
   "status": "proident dolor",
   "uploadTime": "1964-03-18T02:12:32.351Z"
  }
 ],
 "itemsPerPage": 6054565,
 "kind": "analytics#uploads",
 "nextLink": "deserunt",
 "previousLink": "sed ea non dolore",
 "startIndex": 66469637,
 "totalResults": 24595644
}
```

<br>

### analytics.management.uploads.upload Data ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customDataSources/:customDataSourceId/uploads?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "minim ven",
 "customDataSourceId": "elit aliqua incididunt",
 "errors": [
  "ut",
  "in amet cillum"
 ],
 "id": "anim magna ullamco",
 "kind": "analytics#upload",
 "status": "in fugiat ",
 "uploadTime": "1987-07-31T14:32:15.737Z"
}
```

<br>

### analytics.management.uploads.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customDataSources/:customDataSourceId/uploads/:uploadId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "minim ven",
 "customDataSourceId": "elit aliqua incididunt",
 "errors": [
  "ut",
  "in amet cillum"
 ],
 "id": "anim magna ullamco",
 "kind": "analytics#upload",
 "status": "in fugiat ",
 "uploadTime": "1987-07-31T14:32:15.737Z"
}
```

<br>

### analytics.management.uploads.delete Upload Data ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customDataSources/:customDataSourceId/deleteUploadData?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "customDataImportUids": [
        "<string>",
        "<string>"
    ]
}
```


> Response

*Successful response*: No response specified

<br>

### analytics.management.custom Data Sources.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customDataSources?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of custom data sources to include in this response.

**`start-index`**

A 1-based index of the first custom data source to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "consequat occaecat",
   "childLink": {
    "href": "in",
    "type": "consectetur"
   },
   "created": "2018-05-20T22:51:34.895Z",
   "description": "consectetur incididunt",
   "id": "est magna mollit si",
   "importBehavior": "labore dolor",
   "kind": "analytics#customDataSource",
   "name": "tempor",
   "parentLink": {
    "href": "non consectetur aliqua",
    "type": "analytics#webproperty"
   },
   "profilesLinked": [
    "quis adipisicing aute",
    "dolore minim"
   ],
   "schema": [
    "quis laboris",
    "dolore elit esse"
   ],
   "selfLink": "est id adipisicing laboris",
   "type": "exercitation consectetur ut",
   "updated": "1989-08-07T07:14:45.361Z",
   "uploadType": "cupidatat",
   "webPropertyId": "tempor co"
  },
  {
   "accountId": "nisi",
   "childLink": {
    "href": "Lorem laborum non aute",
    "type": "Duis culpa in"
   },
   "created": "2003-03-30T10:08:35.683Z",
   "description": "eiusmod sit",
   "id": "mol",
   "importBehavior": "culpa Duis tempor fugiat",
   "kind": "analytics#customDataSource",
   "name": "veniam sunt",
   "parentLink": {
    "href": "mollit",
    "type": "analytics#webproperty"
   },
   "profilesLinked": [
    "Lorem officia",
    "Excepteur non sit"
   ],
   "schema": [
    "eu tempor nostrud in",
    "anim mollit"
   ],
   "selfLink": "occaecat quis proident",
   "type": "in ad aliqua adipisicing Lorem",
   "updated": "1980-03-02T17:27:56.032Z",
   "uploadType": "pariatur deserunt",
   "webPropertyId": "nostrud ex mollit ea"
  }
 ],
 "itemsPerPage": -46739517,
 "kind": "analytics#customDataSources",
 "nextLink": "culpa nisi eu",
 "previousLink": "nisi in elit",
 "startIndex": 81067669,
 "totalResults": -30280371,
 "username": "qui elit in"
}
```

<br>

### analytics.management.custom Dimensions.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customDimensions/:customDimensionId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "1945-12-12T05:27:54.027Z",
 "id": "<string>",
 "index": 81606079,
 "kind": "analytics#customDimension",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "scope": "<string>",
 "selfLink": "minim qui ex dolore",
 "updated": "1960-11-10T01:37:51.615Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.custom Dimensions.patch ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PATCH {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customDimensions/:customDimensionId?ignoreCustomDataSourceLinks=<boolean>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`ignoreCustomDataSourceLinks`**

Force the update and ignore any warnings related to the custom dimension being linked to a custom data source / data set.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "active": "<boolean>",
    "id": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#webproperty"
    },
    "scope": "<string>",
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "1945-12-12T05:27:54.027Z",
 "id": "<string>",
 "index": 81606079,
 "kind": "analytics#customDimension",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "scope": "<string>",
 "selfLink": "minim qui ex dolore",
 "updated": "1960-11-10T01:37:51.615Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.custom Dimensions.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customDimensions/:customDimensionId?ignoreCustomDataSourceLinks=<boolean>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`ignoreCustomDataSourceLinks`**

Force the update and ignore any warnings related to the custom dimension being linked to a custom data source / data set.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "active": "<boolean>",
    "id": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#webproperty"
    },
    "scope": "<string>",
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "1945-12-12T05:27:54.027Z",
 "id": "<string>",
 "index": 81606079,
 "kind": "analytics#customDimension",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "scope": "<string>",
 "selfLink": "minim qui ex dolore",
 "updated": "1960-11-10T01:37:51.615Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.custom Dimensions.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customDimensions?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of custom dimensions to include in this response.

**`start-index`**

An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "Duis Ut qui id",
   "active": true,
   "created": "1972-11-14T02:40:28.036Z",
   "id": "Ut eu cupidatat",
   "index": 46981364,
   "kind": "analytics#customDimension",
   "name": "anim exercitation nulla aute",
   "parentLink": {
    "href": "elit sit velit in",
    "type": "analytics#webproperty"
   },
   "scope": "nulla ea voluptate pariatur",
   "selfLink": "occaecat sunt non in velit",
   "updated": "1974-09-02T22:27:57.616Z",
   "webPropertyId": "labori"
  },
  {
   "accountId": "aute veniam commodo",
   "active": true,
   "created": "1991-01-26T01:37:52.831Z",
   "id": "Ut ipsum magna aute aliquip",
   "index": 94476489,
   "kind": "analytics#customDimension",
   "name": "officia dolor pariatur",
   "parentLink": {
    "href": "Excepteur proident ut anim et",
    "type": "analytics#webproperty"
   },
   "scope": "ut qui fugiat oc",
   "selfLink": "ad ea",
   "updated": "1941-04-02T17:18:18.408Z",
   "webPropertyId": "non est et"
  }
 ],
 "itemsPerPage": 20506079,
 "kind": "analytics#customDimensions",
 "nextLink": "in",
 "previousLink": "nostrud",
 "startIndex": 62726140,
 "totalResults": -10505671,
 "username": "proident ad et magna"
}
```

<br>

### analytics.management.custom Dimensions.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customDimensions?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "active": "<boolean>",
    "id": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#webproperty"
    },
    "scope": "<string>",
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "1945-12-12T05:27:54.027Z",
 "id": "<string>",
 "index": 81606079,
 "kind": "analytics#customDimension",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "scope": "<string>",
 "selfLink": "minim qui ex dolore",
 "updated": "1960-11-10T01:37:51.615Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.custom Metrics.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customMetrics/:customMetricId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "1957-12-12T23:34:50.176Z",
 "id": "<string>",
 "index": -27884243,
 "kind": "analytics#customMetric",
 "max_value": "<string>",
 "min_value": "<string>",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "scope": "<string>",
 "selfLink": "laborum labore enim ex amet",
 "type": "<string>",
 "updated": "1975-09-12T02:47:05.399Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.custom Metrics.patch ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PATCH {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customMetrics/:customMetricId?ignoreCustomDataSourceLinks=<boolean>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`ignoreCustomDataSourceLinks`**

Force the update and ignore any warnings related to the custom metric being linked to a custom data source / data set.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "active": "<boolean>",
    "id": "<string>",
    "max_value": "<string>",
    "min_value": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#webproperty"
    },
    "scope": "<string>",
    "type": "<string>",
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "1957-12-12T23:34:50.176Z",
 "id": "<string>",
 "index": -27884243,
 "kind": "analytics#customMetric",
 "max_value": "<string>",
 "min_value": "<string>",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "scope": "<string>",
 "selfLink": "laborum labore enim ex amet",
 "type": "<string>",
 "updated": "1975-09-12T02:47:05.399Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.custom Metrics.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customMetrics/:customMetricId?ignoreCustomDataSourceLinks=<boolean>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`ignoreCustomDataSourceLinks`**

Force the update and ignore any warnings related to the custom metric being linked to a custom data source / data set.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "active": "<boolean>",
    "id": "<string>",
    "max_value": "<string>",
    "min_value": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#webproperty"
    },
    "scope": "<string>",
    "type": "<string>",
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "1957-12-12T23:34:50.176Z",
 "id": "<string>",
 "index": -27884243,
 "kind": "analytics#customMetric",
 "max_value": "<string>",
 "min_value": "<string>",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "scope": "<string>",
 "selfLink": "laborum labore enim ex amet",
 "type": "<string>",
 "updated": "1975-09-12T02:47:05.399Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.custom Metrics.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customMetrics?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of custom metrics to include in this response.

**`start-index`**

An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "incididunt",
   "active": false,
   "created": "1945-11-21T12:03:30.916Z",
   "id": "officia Lorem consequat anim",
   "index": -93202731,
   "kind": "analytics#customMetric",
   "max_value": "aliquip",
   "min_value": "in id Excepteur mollit ut",
   "name": "occaecat labore id",
   "parentLink": {
    "href": "Excepteur ",
    "type": "analytics#webproperty"
   },
   "scope": "consectetur id",
   "selfLink": "anim voluptate ame",
   "type": "do",
   "updated": "1954-09-14T08:40:23.372Z",
   "webPropertyId": "Ut in exercitation"
  },
  {
   "accountId": "minim non ullamco enim deserunt",
   "active": true,
   "created": "1981-10-28T23:52:20.060Z",
   "id": "voluptate",
   "index": 92867764,
   "kind": "analytics#customMetric",
   "max_value": "nulla eu consectetur Ut",
   "min_value": "aute nulla in sit",
   "name": "adipisicing nostrud dolor",
   "parentLink": {
    "href": "officia occaecat aliqua",
    "type": "analytics#webproperty"
   },
   "scope": "in tempor labore eiusmod aliquip",
   "selfLink": "Ut sint",
   "type": "labore sint fugiat",
   "updated": "1987-01-31T06:37:57.064Z",
   "webPropertyId": "sunt culpa"
  }
 ],
 "itemsPerPage": 22740955,
 "kind": "analytics#customMetrics",
 "nextLink": "amet sunt aliquip consectetur id",
 "previousLink": "anim cupi",
 "startIndex": -28429458,
 "totalResults": 9738868,
 "username": "dolore Excepteur velit"
}
```

<br>

### analytics.management.custom Metrics.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/customMetrics?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "active": "<boolean>",
    "id": "<string>",
    "max_value": "<string>",
    "min_value": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#webproperty"
    },
    "scope": "<string>",
    "type": "<string>",
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "1957-12-12T23:34:50.176Z",
 "id": "<string>",
 "index": -27884243,
 "kind": "analytics#customMetric",
 "max_value": "<string>",
 "min_value": "<string>",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "scope": "<string>",
 "selfLink": "laborum labore enim ex amet",
 "type": "<string>",
 "updated": "1975-09-12T02:47:05.399Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.web Property Ad Words Links.delete ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
DELETE {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/entityAdWordsLinks/:webPropertyAdWordsLinkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*: No response specified

<br>

### analytics.management.web Property Ad Words Links.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/entityAdWordsLinks/:webPropertyAdWordsLinkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "adWordsAccounts": [
  {
   "autoTaggingEnabled": true,
   "customerId": "veniam in occaecat laboris",
   "kind": "analytics#adWordsAccount"
  },
  {
   "autoTaggingEnabled": true,
   "customerId": "aute reprehenderit nostrud",
   "kind": "analytics#adWordsAccount"
  }
 ],
 "entity": {
  "webPropertyRef": {
   "accountId": "labore dolor dolore elit",
   "href": "labore veniam",
   "id": "enim cillum ut",
   "internalWebPropertyId": "est Lorem culpa nulla",
   "kind": "analytics#webPropertyRef",
   "name": "incididunt sed "
  }
 },
 "id": "<string>",
 "kind": "analytics#entityAdWordsLink",
 "name": "<string>",
 "profileIds": [
  "<string>",
  "<string>"
 ],
 "selfLink": "<string>"
}
```

<br>

### analytics.management.web Property Ad Words Links.patch ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PATCH {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/entityAdWordsLinks/:webPropertyAdWordsLinkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "adWordsAccounts": [
        {
            "autoTaggingEnabled": true,
            "customerId": "exercitat",
            "kind": "analytics#adWordsAccount"
        },
        {
            "autoTaggingEnabled": true,
            "customerId": "et sit qui voluptate",
            "kind": "analytics#adWordsAccount"
        }
    ],
    "entity": {
        "webPropertyRef": {
            "accountId": "veniam incididunt",
            "href": "nisi quis v",
            "id": "occaecat dolore",
            "internalWebPropertyId": "Duis Ut cupidatat adipisicing qui",
            "kind": "analytics#webPropertyRef",
            "name": "consectetur eiusmod eu"
        }
    },
    "id": "<string>",
    "kind": "analytics#entityAdWordsLink",
    "name": "<string>",
    "profileIds": [
        "<string>",
        "<string>"
    ],
    "selfLink": "<string>"
}
```


> Response

*Successful response*
```json
{
 "adWordsAccounts": [
  {
   "autoTaggingEnabled": true,
   "customerId": "veniam in occaecat laboris",
   "kind": "analytics#adWordsAccount"
  },
  {
   "autoTaggingEnabled": true,
   "customerId": "aute reprehenderit nostrud",
   "kind": "analytics#adWordsAccount"
  }
 ],
 "entity": {
  "webPropertyRef": {
   "accountId": "labore dolor dolore elit",
   "href": "labore veniam",
   "id": "enim cillum ut",
   "internalWebPropertyId": "est Lorem culpa nulla",
   "kind": "analytics#webPropertyRef",
   "name": "incididunt sed "
  }
 },
 "id": "<string>",
 "kind": "analytics#entityAdWordsLink",
 "name": "<string>",
 "profileIds": [
  "<string>",
  "<string>"
 ],
 "selfLink": "<string>"
}
```

<br>

### analytics.management.web Property Ad Words Links.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/entityAdWordsLinks/:webPropertyAdWordsLinkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "adWordsAccounts": [
        {
            "autoTaggingEnabled": true,
            "customerId": "exercitat",
            "kind": "analytics#adWordsAccount"
        },
        {
            "autoTaggingEnabled": true,
            "customerId": "et sit qui voluptate",
            "kind": "analytics#adWordsAccount"
        }
    ],
    "entity": {
        "webPropertyRef": {
            "accountId": "veniam incididunt",
            "href": "nisi quis v",
            "id": "occaecat dolore",
            "internalWebPropertyId": "Duis Ut cupidatat adipisicing qui",
            "kind": "analytics#webPropertyRef",
            "name": "consectetur eiusmod eu"
        }
    },
    "id": "<string>",
    "kind": "analytics#entityAdWordsLink",
    "name": "<string>",
    "profileIds": [
        "<string>",
        "<string>"
    ],
    "selfLink": "<string>"
}
```


> Response

*Successful response*
```json
{
 "adWordsAccounts": [
  {
   "autoTaggingEnabled": true,
   "customerId": "veniam in occaecat laboris",
   "kind": "analytics#adWordsAccount"
  },
  {
   "autoTaggingEnabled": true,
   "customerId": "aute reprehenderit nostrud",
   "kind": "analytics#adWordsAccount"
  }
 ],
 "entity": {
  "webPropertyRef": {
   "accountId": "labore dolor dolore elit",
   "href": "labore veniam",
   "id": "enim cillum ut",
   "internalWebPropertyId": "est Lorem culpa nulla",
   "kind": "analytics#webPropertyRef",
   "name": "incididunt sed "
  }
 },
 "id": "<string>",
 "kind": "analytics#entityAdWordsLink",
 "name": "<string>",
 "profileIds": [
  "<string>",
  "<string>"
 ],
 "selfLink": "<string>"
}
```

<br>

### analytics.management.web Property Ad Words Links.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/entityAdWordsLinks?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of webProperty-Google Ads links to include in this response.

**`start-index`**

An index of the first webProperty-Google Ads link to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "adWordsAccounts": [
    {
     "autoTaggingEnabled": true,
     "customerId": "voluptate laborum e",
     "kind": "analytics#adWordsAccount"
    },
    {
     "autoTaggingEnabled": false,
     "customerId": "est sint",
     "kind": "analytics#adWordsAccount"
    }
   ],
   "entity": {
    "webPropertyRef": {
     "accountId": "voluptate nulla sit",
     "href": "eu",
     "id": "incididunt nulla minim tempor",
     "internalWebPropertyId": "sint eiusmod laboris cillum",
     "kind": "analytics#webPropertyRef",
     "name": "ex sed"
    }
   },
   "id": "proident in",
   "kind": "analytics#entityAdWordsLink",
   "name": "cillum cupidatat dolore in",
   "profileIds": [
    "amet sunt in non",
    "consectetur sed"
   ],
   "selfLink": "ea qui pariatur laborum"
  },
  {
   "adWordsAccounts": [
    {
     "autoTaggingEnabled": false,
     "customerId": "eiusmod mollit sunt",
     "kind": "analytics#adWordsAccount"
    },
    {
     "autoTaggingEnabled": true,
     "customerId": "labo",
     "kind": "analytics#adWordsAccount"
    }
   ],
   "entity": {
    "webPropertyRef": {
     "accountId": "nisi in",
     "href": "irure ea ad",
     "id": "anim",
     "internalWebPropertyId": "cillum elit consectetur",
     "kind": "analytics#webPropertyRef",
     "name": "proident et laborum sed"
    }
   },
   "id": "cillum laborum Lorem in",
   "kind": "analytics#entityAdWordsLink",
   "name": "nulla Excepteur in Lorem",
   "profileIds": [
    "inci",
    "culpa enim Lorem"
   ],
   "selfLink": "et sint"
  }
 ],
 "itemsPerPage": -57101132,
 "kind": "analytics#entityAdWordsLinks",
 "nextLink": "esse adipisici",
 "previousLink": "esse elit",
 "startIndex": 92454366,
 "totalResults": -56649379
}
```

<br>

### analytics.management.web Property Ad Words Links.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/entityAdWordsLinks?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "adWordsAccounts": [
        {
            "autoTaggingEnabled": true,
            "customerId": "exercitat",
            "kind": "analytics#adWordsAccount"
        },
        {
            "autoTaggingEnabled": true,
            "customerId": "et sit qui voluptate",
            "kind": "analytics#adWordsAccount"
        }
    ],
    "entity": {
        "webPropertyRef": {
            "accountId": "veniam incididunt",
            "href": "nisi quis v",
            "id": "occaecat dolore",
            "internalWebPropertyId": "Duis Ut cupidatat adipisicing qui",
            "kind": "analytics#webPropertyRef",
            "name": "consectetur eiusmod eu"
        }
    },
    "id": "<string>",
    "kind": "analytics#entityAdWordsLink",
    "name": "<string>",
    "profileIds": [
        "<string>",
        "<string>"
    ],
    "selfLink": "<string>"
}
```


> Response

*Successful response*
```json
{
 "adWordsAccounts": [
  {
   "autoTaggingEnabled": true,
   "customerId": "veniam in occaecat laboris",
   "kind": "analytics#adWordsAccount"
  },
  {
   "autoTaggingEnabled": true,
   "customerId": "aute reprehenderit nostrud",
   "kind": "analytics#adWordsAccount"
  }
 ],
 "entity": {
  "webPropertyRef": {
   "accountId": "labore dolor dolore elit",
   "href": "labore veniam",
   "id": "enim cillum ut",
   "internalWebPropertyId": "est Lorem culpa nulla",
   "kind": "analytics#webPropertyRef",
   "name": "incididunt sed "
  }
 },
 "id": "<string>",
 "kind": "analytics#entityAdWordsLink",
 "name": "<string>",
 "profileIds": [
  "<string>",
  "<string>"
 ],
 "selfLink": "<string>"
}
```

<br>

### analytics.management.webproperty User Links.delete ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
DELETE {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/entityUserLinks/:linkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*: No response specified

<br>

### analytics.management.webproperty User Links.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/entityUserLinks/:linkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "entity": {
        "accountRef": {
            "href": "sit tempor ut ea",
            "id": "ut ea",
            "kind": "analytics#accountRef",
            "name": "veniam"
        },
        "profileRef": {
            "accountId": "culpa",
            "href": "ipsum nostrud minim occaecat",
            "id": "laboris aute id est",
            "internalWebPropertyId": "enim in non tempor quis",
            "kind": "analytics#profileRef",
            "name": "Duis veniam",
            "webPropertyId": "Lorem in"
        },
        "webPropertyRef": {
            "accountId": "amet",
            "href": "sed proident amet tempor Excepteur",
            "id": "qui irure dolor",
            "internalWebPropertyId": "sunt tempor exercitation elit enim",
            "kind": "analytics#webPropertyRef",
            "name": "esse"
        }
    },
    "id": "<string>",
    "kind": "analytics#entityUserLink",
    "permissions": {
        "local": [
            "<string>",
            "<string>"
        ]
    },
    "selfLink": "<string>",
    "userRef": {
        "email": "dolore",
        "id": "sed ex cillum id quis",
        "kind": "analytics#userRef"
    }
}
```


> Response

*Successful response*
```json
{
 "entity": {
  "accountRef": {
   "href": "culpa enim veniam",
   "id": "Lorem tempor exercitation fugiat",
   "kind": "analytics#accountRef",
   "name": "reprehenderit nulla aute aliq"
  },
  "profileRef": {
   "accountId": "Ut amet",
   "href": "proident voluptate amet",
   "id": "quis et deserunt",
   "internalWebPropertyId": "enim velit eiusmod",
   "kind": "analytics#profileRef",
   "name": "esse in aute ullamco",
   "webPropertyId": "Excepteur"
  },
  "webPropertyRef": {
   "accountId": "voluptate dolore nostrud",
   "href": "cillum ullamco in aliquip",
   "id": "consectetur sunt l",
   "internalWebPropertyId": "pariatur in",
   "kind": "analytics#webPropertyRef",
   "name": "laborum quis nulla"
  }
 },
 "id": "<string>",
 "kind": "analytics#entityUserLink",
 "permissions": {
  "effective": [
   "consectetur magna pariatur incididunt",
   "Lorem reprehenderit"
  ],
  "local": [
   "<string>",
   "<string>"
  ]
 },
 "selfLink": "<string>",
 "userRef": {
  "email": "eu elit reprehenderit Excepteur sed",
  "id": "dolor quis",
  "kind": "analytics#userRef"
 }
}
```

<br>

### analytics.management.webproperty User Links.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/entityUserLinks?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of webProperty-user Links to include in this response.

**`start-index`**

An index of the first webProperty-user link to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "entity": {
    "accountRef": {
     "href": "Duis a",
     "id": "sint",
     "kind": "analytics#accountRef",
     "name": "commodo cupidatat elit"
    },
    "profileRef": {
     "accountId": "consequat eu aliqua sint",
     "href": "enim nisi nulla pa",
     "id": "irure ut dolor Excepteur",
     "internalWebPropertyId": "nisi",
     "kind": "analytics#profileRef",
     "name": "fugiat enim occaecat eu amet",
     "webPropertyId": "enim tempor"
    },
    "webPropertyRef": {
     "accountId": "in nulla",
     "href": "anim sint adipisicing dolore",
     "id": "dolore occaecat",
     "internalWebPropertyId": "eiusmo",
     "kind": "analytics#webPropertyRef",
     "name": "eni"
    }
   },
   "id": "<string>",
   "kind": "analytics#entityUserLink",
   "permissions": {
    "effective": [
     "voluptate eiusmod irure anim",
     "qui"
    ],
    "local": [
     "<string>",
     "<string>"
    ]
   },
   "selfLink": "<string>",
   "userRef": {
    "email": "eu labore",
    "id": "velit labore in veniam magna",
    "kind": "analytics#userRef"
   }
  },
  {
   "entity": {
    "accountRef": {
     "href": "esse",
     "id": "aliqua ea anim non",
     "kind": "analytics#accountRef",
     "name": "Lorem cillum non"
    },
    "profileRef": {
     "accountId": "voluptate officia",
     "href": "quis anim deserunt",
     "id": "ipsum id",
     "internalWebPropertyId": "consequat cillum",
     "kind": "analytics#profileRef",
     "name": "pariatur Excepteur ut et",
     "webPropertyId": "Lorem mollit nisi aliq"
    },
    "webPropertyRef": {
     "accountId": "aute ea",
     "href": "eiusmod",
     "id": "est dolor commodo ad",
     "internalWebPropertyId": "dolore laborum in ut esse",
     "kind": "analytics#webPropertyRef",
     "name": "ut tempor laboris enim"
    }
   },
   "id": "<string>",
   "kind": "analytics#entityUserLink",
   "permissions": {
    "effective": [
     "non in ipsum",
     "ipsum ut cillum aute"
    ],
    "local": [
     "<string>",
     "<string>"
    ]
   },
   "selfLink": "<string>",
   "userRef": {
    "email": "anim ut veniam",
    "id": "proident dolore",
    "kind": "analytics#userRef"
   }
  }
 ],
 "itemsPerPage": -68569132,
 "kind": "analytics#entityUserLinks",
 "nextLink": "tempor amet",
 "previousLink": "elit sint non",
 "startIndex": -52723348,
 "totalResults": 9642425
}
```

<br>

### analytics.management.webproperty User Links.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/entityUserLinks?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "entity": {
        "accountRef": {
            "href": "sit tempor ut ea",
            "id": "ut ea",
            "kind": "analytics#accountRef",
            "name": "veniam"
        },
        "profileRef": {
            "accountId": "culpa",
            "href": "ipsum nostrud minim occaecat",
            "id": "laboris aute id est",
            "internalWebPropertyId": "enim in non tempor quis",
            "kind": "analytics#profileRef",
            "name": "Duis veniam",
            "webPropertyId": "Lorem in"
        },
        "webPropertyRef": {
            "accountId": "amet",
            "href": "sed proident amet tempor Excepteur",
            "id": "qui irure dolor",
            "internalWebPropertyId": "sunt tempor exercitation elit enim",
            "kind": "analytics#webPropertyRef",
            "name": "esse"
        }
    },
    "id": "<string>",
    "kind": "analytics#entityUserLink",
    "permissions": {
        "local": [
            "<string>",
            "<string>"
        ]
    },
    "selfLink": "<string>",
    "userRef": {
        "email": "dolore",
        "id": "sed ex cillum id quis",
        "kind": "analytics#userRef"
    }
}
```


> Response

*Successful response*
```json
{
 "entity": {
  "accountRef": {
   "href": "culpa enim veniam",
   "id": "Lorem tempor exercitation fugiat",
   "kind": "analytics#accountRef",
   "name": "reprehenderit nulla aute aliq"
  },
  "profileRef": {
   "accountId": "Ut amet",
   "href": "proident voluptate amet",
   "id": "quis et deserunt",
   "internalWebPropertyId": "enim velit eiusmod",
   "kind": "analytics#profileRef",
   "name": "esse in aute ullamco",
   "webPropertyId": "Excepteur"
  },
  "webPropertyRef": {
   "accountId": "voluptate dolore nostrud",
   "href": "cillum ullamco in aliquip",
   "id": "consectetur sunt l",
   "internalWebPropertyId": "pariatur in",
   "kind": "analytics#webPropertyRef",
   "name": "laborum quis nulla"
  }
 },
 "id": "<string>",
 "kind": "analytics#entityUserLink",
 "permissions": {
  "effective": [
   "consectetur magna pariatur incididunt",
   "Lorem reprehenderit"
  ],
  "local": [
   "<string>",
   "<string>"
  ]
 },
 "selfLink": "<string>",
 "userRef": {
  "email": "eu elit reprehenderit Excepteur sed",
  "id": "dolor quis",
  "kind": "analytics#userRef"
 }
}
```

<br>

### analytics.management.profile User Links.delete ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
DELETE {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/entityUserLinks/:linkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*: No response specified

<br>

### analytics.management.profile User Links.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/entityUserLinks/:linkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "entity": {
        "accountRef": {
            "href": "sit tempor ut ea",
            "id": "ut ea",
            "kind": "analytics#accountRef",
            "name": "veniam"
        },
        "profileRef": {
            "accountId": "culpa",
            "href": "ipsum nostrud minim occaecat",
            "id": "laboris aute id est",
            "internalWebPropertyId": "enim in non tempor quis",
            "kind": "analytics#profileRef",
            "name": "Duis veniam",
            "webPropertyId": "Lorem in"
        },
        "webPropertyRef": {
            "accountId": "amet",
            "href": "sed proident amet tempor Excepteur",
            "id": "qui irure dolor",
            "internalWebPropertyId": "sunt tempor exercitation elit enim",
            "kind": "analytics#webPropertyRef",
            "name": "esse"
        }
    },
    "id": "<string>",
    "kind": "analytics#entityUserLink",
    "permissions": {
        "local": [
            "<string>",
            "<string>"
        ]
    },
    "selfLink": "<string>",
    "userRef": {
        "email": "dolore",
        "id": "sed ex cillum id quis",
        "kind": "analytics#userRef"
    }
}
```


> Response

*Successful response*
```json
{
 "entity": {
  "accountRef": {
   "href": "culpa enim veniam",
   "id": "Lorem tempor exercitation fugiat",
   "kind": "analytics#accountRef",
   "name": "reprehenderit nulla aute aliq"
  },
  "profileRef": {
   "accountId": "Ut amet",
   "href": "proident voluptate amet",
   "id": "quis et deserunt",
   "internalWebPropertyId": "enim velit eiusmod",
   "kind": "analytics#profileRef",
   "name": "esse in aute ullamco",
   "webPropertyId": "Excepteur"
  },
  "webPropertyRef": {
   "accountId": "voluptate dolore nostrud",
   "href": "cillum ullamco in aliquip",
   "id": "consectetur sunt l",
   "internalWebPropertyId": "pariatur in",
   "kind": "analytics#webPropertyRef",
   "name": "laborum quis nulla"
  }
 },
 "id": "<string>",
 "kind": "analytics#entityUserLink",
 "permissions": {
  "effective": [
   "consectetur magna pariatur incididunt",
   "Lorem reprehenderit"
  ],
  "local": [
   "<string>",
   "<string>"
  ]
 },
 "selfLink": "<string>",
 "userRef": {
  "email": "eu elit reprehenderit Excepteur sed",
  "id": "dolor quis",
  "kind": "analytics#userRef"
 }
}
```

<br>

### analytics.management.profile User Links.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/entityUserLinks?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of profile-user links to include in this response.

**`start-index`**

An index of the first profile-user link to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "entity": {
    "accountRef": {
     "href": "Duis a",
     "id": "sint",
     "kind": "analytics#accountRef",
     "name": "commodo cupidatat elit"
    },
    "profileRef": {
     "accountId": "consequat eu aliqua sint",
     "href": "enim nisi nulla pa",
     "id": "irure ut dolor Excepteur",
     "internalWebPropertyId": "nisi",
     "kind": "analytics#profileRef",
     "name": "fugiat enim occaecat eu amet",
     "webPropertyId": "enim tempor"
    },
    "webPropertyRef": {
     "accountId": "in nulla",
     "href": "anim sint adipisicing dolore",
     "id": "dolore occaecat",
     "internalWebPropertyId": "eiusmo",
     "kind": "analytics#webPropertyRef",
     "name": "eni"
    }
   },
   "id": "<string>",
   "kind": "analytics#entityUserLink",
   "permissions": {
    "effective": [
     "voluptate eiusmod irure anim",
     "qui"
    ],
    "local": [
     "<string>",
     "<string>"
    ]
   },
   "selfLink": "<string>",
   "userRef": {
    "email": "eu labore",
    "id": "velit labore in veniam magna",
    "kind": "analytics#userRef"
   }
  },
  {
   "entity": {
    "accountRef": {
     "href": "esse",
     "id": "aliqua ea anim non",
     "kind": "analytics#accountRef",
     "name": "Lorem cillum non"
    },
    "profileRef": {
     "accountId": "voluptate officia",
     "href": "quis anim deserunt",
     "id": "ipsum id",
     "internalWebPropertyId": "consequat cillum",
     "kind": "analytics#profileRef",
     "name": "pariatur Excepteur ut et",
     "webPropertyId": "Lorem mollit nisi aliq"
    },
    "webPropertyRef": {
     "accountId": "aute ea",
     "href": "eiusmod",
     "id": "est dolor commodo ad",
     "internalWebPropertyId": "dolore laborum in ut esse",
     "kind": "analytics#webPropertyRef",
     "name": "ut tempor laboris enim"
    }
   },
   "id": "<string>",
   "kind": "analytics#entityUserLink",
   "permissions": {
    "effective": [
     "non in ipsum",
     "ipsum ut cillum aute"
    ],
    "local": [
     "<string>",
     "<string>"
    ]
   },
   "selfLink": "<string>",
   "userRef": {
    "email": "anim ut veniam",
    "id": "proident dolore",
    "kind": "analytics#userRef"
   }
  }
 ],
 "itemsPerPage": -68569132,
 "kind": "analytics#entityUserLinks",
 "nextLink": "tempor amet",
 "previousLink": "elit sint non",
 "startIndex": -52723348,
 "totalResults": 9642425
}
```

<br>

### analytics.management.profile User Links.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/entityUserLinks?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "entity": {
        "accountRef": {
            "href": "sit tempor ut ea",
            "id": "ut ea",
            "kind": "analytics#accountRef",
            "name": "veniam"
        },
        "profileRef": {
            "accountId": "culpa",
            "href": "ipsum nostrud minim occaecat",
            "id": "laboris aute id est",
            "internalWebPropertyId": "enim in non tempor quis",
            "kind": "analytics#profileRef",
            "name": "Duis veniam",
            "webPropertyId": "Lorem in"
        },
        "webPropertyRef": {
            "accountId": "amet",
            "href": "sed proident amet tempor Excepteur",
            "id": "qui irure dolor",
            "internalWebPropertyId": "sunt tempor exercitation elit enim",
            "kind": "analytics#webPropertyRef",
            "name": "esse"
        }
    },
    "id": "<string>",
    "kind": "analytics#entityUserLink",
    "permissions": {
        "local": [
            "<string>",
            "<string>"
        ]
    },
    "selfLink": "<string>",
    "userRef": {
        "email": "dolore",
        "id": "sed ex cillum id quis",
        "kind": "analytics#userRef"
    }
}
```


> Response

*Successful response*
```json
{
 "entity": {
  "accountRef": {
   "href": "culpa enim veniam",
   "id": "Lorem tempor exercitation fugiat",
   "kind": "analytics#accountRef",
   "name": "reprehenderit nulla aute aliq"
  },
  "profileRef": {
   "accountId": "Ut amet",
   "href": "proident voluptate amet",
   "id": "quis et deserunt",
   "internalWebPropertyId": "enim velit eiusmod",
   "kind": "analytics#profileRef",
   "name": "esse in aute ullamco",
   "webPropertyId": "Excepteur"
  },
  "webPropertyRef": {
   "accountId": "voluptate dolore nostrud",
   "href": "cillum ullamco in aliquip",
   "id": "consectetur sunt l",
   "internalWebPropertyId": "pariatur in",
   "kind": "analytics#webPropertyRef",
   "name": "laborum quis nulla"
  }
 },
 "id": "<string>",
 "kind": "analytics#entityUserLink",
 "permissions": {
  "effective": [
   "consectetur magna pariatur incididunt",
   "Lorem reprehenderit"
  ],
  "local": [
   "<string>",
   "<string>"
  ]
 },
 "selfLink": "<string>",
 "userRef": {
  "email": "eu elit reprehenderit Excepteur sed",
  "id": "dolor quis",
  "kind": "analytics#userRef"
 }
}
```

<br>

### analytics.management.experiments.delete ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
DELETE {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/experiments/:experimentId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*: No response specified

<br>

### analytics.management.experiments.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/experiments/:experimentId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "created": "<dateTime>",
 "description": "<string>",
 "editableInGaUi": "<boolean>",
 "endTime": "<dateTime>",
 "equalWeighting": "<boolean>",
 "id": "<string>",
 "internalWebPropertyId": "<string>",
 "kind": "analytics#experiment",
 "minimumExperimentLengthInDays": "<integer>",
 "name": "<string>",
 "objectiveMetric": "<string>",
 "optimizationType": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#profile"
 },
 "profileId": "<string>",
 "reasonExperimentEnded": "<string>",
 "rewriteVariationUrlsAsOriginal": "<boolean>",
 "selfLink": "<string>",
 "servingFramework": "<string>",
 "snippet": "<string>",
 "startTime": "<dateTime>",
 "status": "<string>",
 "trafficCoverage": "<number>",
 "updated": "<dateTime>",
 "variations": [
  {
   "name": "<string>",
   "status": "<string>",
   "url": "<string>",
   "weight": "<number>",
   "won": "<boolean>"
  },
  {
   "name": "<string>",
   "status": "<string>",
   "url": "<string>",
   "weight": "<number>",
   "won": "<boolean>"
  }
 ],
 "webPropertyId": "<string>",
 "winnerConfidenceLevel": "<number>",
 "winnerFound": "<boolean>"
}
```

<br>

### analytics.management.experiments.patch ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PATCH {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/experiments/:experimentId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "created": "<dateTime>",
    "description": "<string>",
    "editableInGaUi": "<boolean>",
    "endTime": "<dateTime>",
    "equalWeighting": "<boolean>",
    "id": "<string>",
    "internalWebPropertyId": "<string>",
    "kind": "analytics#experiment",
    "minimumExperimentLengthInDays": "<integer>",
    "name": "<string>",
    "objectiveMetric": "<string>",
    "optimizationType": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#profile"
    },
    "profileId": "<string>",
    "reasonExperimentEnded": "<string>",
    "rewriteVariationUrlsAsOriginal": "<boolean>",
    "selfLink": "<string>",
    "servingFramework": "<string>",
    "snippet": "<string>",
    "startTime": "<dateTime>",
    "status": "<string>",
    "trafficCoverage": "<number>",
    "updated": "<dateTime>",
    "variations": [
        {
            "name": "<string>",
            "status": "<string>",
            "url": "<string>",
            "weight": "<number>",
            "won": "<boolean>"
        },
        {
            "name": "<string>",
            "status": "<string>",
            "url": "<string>",
            "weight": "<number>",
            "won": "<boolean>"
        }
    ],
    "webPropertyId": "<string>",
    "winnerConfidenceLevel": "<number>",
    "winnerFound": "<boolean>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "created": "<dateTime>",
 "description": "<string>",
 "editableInGaUi": "<boolean>",
 "endTime": "<dateTime>",
 "equalWeighting": "<boolean>",
 "id": "<string>",
 "internalWebPropertyId": "<string>",
 "kind": "analytics#experiment",
 "minimumExperimentLengthInDays": "<integer>",
 "name": "<string>",
 "objectiveMetric": "<string>",
 "optimizationType": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#profile"
 },
 "profileId": "<string>",
 "reasonExperimentEnded": "<string>",
 "rewriteVariationUrlsAsOriginal": "<boolean>",
 "selfLink": "<string>",
 "servingFramework": "<string>",
 "snippet": "<string>",
 "startTime": "<dateTime>",
 "status": "<string>",
 "trafficCoverage": "<number>",
 "updated": "<dateTime>",
 "variations": [
  {
   "name": "<string>",
   "status": "<string>",
   "url": "<string>",
   "weight": "<number>",
   "won": "<boolean>"
  },
  {
   "name": "<string>",
   "status": "<string>",
   "url": "<string>",
   "weight": "<number>",
   "won": "<boolean>"
  }
 ],
 "webPropertyId": "<string>",
 "winnerConfidenceLevel": "<number>",
 "winnerFound": "<boolean>"
}
```

<br>

### analytics.management.experiments.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/experiments/:experimentId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "created": "<dateTime>",
    "description": "<string>",
    "editableInGaUi": "<boolean>",
    "endTime": "<dateTime>",
    "equalWeighting": "<boolean>",
    "id": "<string>",
    "internalWebPropertyId": "<string>",
    "kind": "analytics#experiment",
    "minimumExperimentLengthInDays": "<integer>",
    "name": "<string>",
    "objectiveMetric": "<string>",
    "optimizationType": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#profile"
    },
    "profileId": "<string>",
    "reasonExperimentEnded": "<string>",
    "rewriteVariationUrlsAsOriginal": "<boolean>",
    "selfLink": "<string>",
    "servingFramework": "<string>",
    "snippet": "<string>",
    "startTime": "<dateTime>",
    "status": "<string>",
    "trafficCoverage": "<number>",
    "updated": "<dateTime>",
    "variations": [
        {
            "name": "<string>",
            "status": "<string>",
            "url": "<string>",
            "weight": "<number>",
            "won": "<boolean>"
        },
        {
            "name": "<string>",
            "status": "<string>",
            "url": "<string>",
            "weight": "<number>",
            "won": "<boolean>"
        }
    ],
    "webPropertyId": "<string>",
    "winnerConfidenceLevel": "<number>",
    "winnerFound": "<boolean>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "created": "<dateTime>",
 "description": "<string>",
 "editableInGaUi": "<boolean>",
 "endTime": "<dateTime>",
 "equalWeighting": "<boolean>",
 "id": "<string>",
 "internalWebPropertyId": "<string>",
 "kind": "analytics#experiment",
 "minimumExperimentLengthInDays": "<integer>",
 "name": "<string>",
 "objectiveMetric": "<string>",
 "optimizationType": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#profile"
 },
 "profileId": "<string>",
 "reasonExperimentEnded": "<string>",
 "rewriteVariationUrlsAsOriginal": "<boolean>",
 "selfLink": "<string>",
 "servingFramework": "<string>",
 "snippet": "<string>",
 "startTime": "<dateTime>",
 "status": "<string>",
 "trafficCoverage": "<number>",
 "updated": "<dateTime>",
 "variations": [
  {
   "name": "<string>",
   "status": "<string>",
   "url": "<string>",
   "weight": "<number>",
   "won": "<boolean>"
  },
  {
   "name": "<string>",
   "status": "<string>",
   "url": "<string>",
   "weight": "<number>",
   "won": "<boolean>"
  }
 ],
 "webPropertyId": "<string>",
 "winnerConfidenceLevel": "<number>",
 "winnerFound": "<boolean>"
}
```

<br>

### analytics.management.experiments.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/experiments?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of experiments to include in this response.

**`start-index`**

An index of the first experiment to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "culpa nisi commodo Excepteur ea",
   "created": "2007-03-12T17:21:30.333Z",
   "description": "Ut laborum",
   "editableInGaUi": false,
   "endTime": "2019-03-21T15:12:16.173Z",
   "equalWeighting": false,
   "id": "sit in",
   "internalWebPropertyId": "ut amet aute ulla",
   "kind": "analytics#experiment",
   "minimumExperimentLengthInDays": -27512308,
   "name": "dolor dolore",
   "objectiveMetric": "esse consectetur Lorem minim",
   "optimizationType": "nulla consequat",
   "parentLink": {
    "href": "esse velit in",
    "type": "analytics#profile"
   },
   "profileId": "Duis",
   "reasonExperimentEnded": "aute Ut irure",
   "rewriteVariationUrlsAsOriginal": true,
   "selfLink": "cillum",
   "servingFramework": "nisi reprehenderit anim amet",
   "snippet": "Excepteur nulla cupidatat",
   "startTime": "1941-06-15T04:43:06.571Z",
   "status": "consectetur com",
   "trafficCoverage": -2169815.4452963024,
   "updated": "1941-06-29T23:15:16.441Z",
   "variations": [
    {
     "name": "ad consectetur anim",
     "status": "irure non",
     "url": "et ea nisi",
     "weight": -71034640.69566843,
     "won": true
    },
    {
     "name": "incididunt fugiat cillum labore id",
     "status": "enim sunt",
     "url": "Duis Lorem",
     "weight": -85732420.99877532,
     "won": true
    }
   ],
   "webPropertyId": "ullamco reprehe",
   "winnerConfidenceLevel": -98416344.5185223,
   "winnerFound": false
  },
  {
   "accountId": "occaecat do aliqua",
   "created": "1959-07-31T07:22:27.082Z",
   "description": "commodo sit nulla aliqua",
   "editableInGaUi": true,
   "endTime": "1995-10-30T19:17:34.587Z",
   "equalWeighting": true,
   "id": "velit et dolore",
   "internalWebPropertyId": "laborum ut",
   "kind": "analytics#experiment",
   "minimumExperimentLengthInDays": -82147581,
   "name": "dolor incididunt",
   "objectiveMetric": "id dolor ut ut",
   "optimizationType": "commodo nostrud eu ut",
   "parentLink": {
    "href": "dolor quis aliqua voluptate",
    "type": "analytics#profile"
   },
   "profileId": "aute exercitation",
   "reasonExperimentEnded": "ut dolor voluptate sunt commodo",
   "rewriteVariationUrlsAsOriginal": true,
   "selfLink": "ut voluptate sed laborum",
   "servingFramework": "magna laborum",
   "snippet": "deserunt",
   "startTime": "1980-03-03T13:04:28.716Z",
   "status": "dolore cillum",
   "trafficCoverage": -8522464.13441731,
   "updated": "1944-05-31T20:28:20.844Z",
   "variations": [
    {
     "name": "ullamco Duis occaecat",
     "status": "pariatur nisi",
     "url": "nisi",
     "weight": 84954887.95994136,
     "won": true
    },
    {
     "name": "dolor est officia mollit",
     "status": "cillum",
     "url": "laboris ut qui laborum",
     "weight": -44651039.74729523,
     "won": true
    }
   ],
   "webPropertyId": "aliquip qui",
   "winnerConfidenceLevel": -83934058.86880356,
   "winnerFound": false
  }
 ],
 "itemsPerPage": 47652099,
 "kind": "analytics#experiments",
 "nextLink": "anim aliqua Excepteur",
 "previousLink": "consectetur mollit enim",
 "startIndex": -31543664,
 "totalResults": 61174629,
 "username": "sed U"
}
```

<br>

### analytics.management.experiments.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/experiments?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "created": "<dateTime>",
    "description": "<string>",
    "editableInGaUi": "<boolean>",
    "endTime": "<dateTime>",
    "equalWeighting": "<boolean>",
    "id": "<string>",
    "internalWebPropertyId": "<string>",
    "kind": "analytics#experiment",
    "minimumExperimentLengthInDays": "<integer>",
    "name": "<string>",
    "objectiveMetric": "<string>",
    "optimizationType": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#profile"
    },
    "profileId": "<string>",
    "reasonExperimentEnded": "<string>",
    "rewriteVariationUrlsAsOriginal": "<boolean>",
    "selfLink": "<string>",
    "servingFramework": "<string>",
    "snippet": "<string>",
    "startTime": "<dateTime>",
    "status": "<string>",
    "trafficCoverage": "<number>",
    "updated": "<dateTime>",
    "variations": [
        {
            "name": "<string>",
            "status": "<string>",
            "url": "<string>",
            "weight": "<number>",
            "won": "<boolean>"
        },
        {
            "name": "<string>",
            "status": "<string>",
            "url": "<string>",
            "weight": "<number>",
            "won": "<boolean>"
        }
    ],
    "webPropertyId": "<string>",
    "winnerConfidenceLevel": "<number>",
    "winnerFound": "<boolean>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "created": "<dateTime>",
 "description": "<string>",
 "editableInGaUi": "<boolean>",
 "endTime": "<dateTime>",
 "equalWeighting": "<boolean>",
 "id": "<string>",
 "internalWebPropertyId": "<string>",
 "kind": "analytics#experiment",
 "minimumExperimentLengthInDays": "<integer>",
 "name": "<string>",
 "objectiveMetric": "<string>",
 "optimizationType": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#profile"
 },
 "profileId": "<string>",
 "reasonExperimentEnded": "<string>",
 "rewriteVariationUrlsAsOriginal": "<boolean>",
 "selfLink": "<string>",
 "servingFramework": "<string>",
 "snippet": "<string>",
 "startTime": "<dateTime>",
 "status": "<string>",
 "trafficCoverage": "<number>",
 "updated": "<dateTime>",
 "variations": [
  {
   "name": "<string>",
   "status": "<string>",
   "url": "<string>",
   "weight": "<number>",
   "won": "<boolean>"
  },
  {
   "name": "<string>",
   "status": "<string>",
   "url": "<string>",
   "weight": "<number>",
   "won": "<boolean>"
  }
 ],
 "webPropertyId": "<string>",
 "winnerConfidenceLevel": "<number>",
 "winnerFound": "<boolean>"
}
```

<br>

### analytics.management.goals.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/goals/:goalId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "<dateTime>",
 "eventDetails": {
  "eventConditions": [
   {
    "comparisonType": "<string>",
    "comparisonValue": "<string>",
    "expression": "<string>",
    "matchType": "<string>",
    "type": "<string>"
   },
   {
    "comparisonType": "<string>",
    "comparisonValue": "<string>",
    "expression": "<string>",
    "matchType": "<string>",
    "type": "<string>"
   }
  ],
  "useEventValue": "<boolean>"
 },
 "id": "<string>",
 "internalWebPropertyId": "<string>",
 "kind": "analytics#goal",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#profile"
 },
 "profileId": "<string>",
 "selfLink": "<string>",
 "type": "<string>",
 "updated": "<dateTime>",
 "urlDestinationDetails": {
  "caseSensitive": "<boolean>",
  "firstStepRequired": "<boolean>",
  "matchType": "<string>",
  "steps": [
   {
    "name": "<string>",
    "number": "<integer>",
    "url": "<string>"
   },
   {
    "name": "<string>",
    "number": "<integer>",
    "url": "<string>"
   }
  ],
  "url": "<string>"
 },
 "value": "<number>",
 "visitNumPagesDetails": {
  "comparisonType": "<string>",
  "comparisonValue": "<string>"
 },
 "visitTimeOnSiteDetails": {
  "comparisonType": "<string>",
  "comparisonValue": "<string>"
 },
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.goals.patch ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PATCH {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/goals/:goalId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "active": "<boolean>",
    "created": "<dateTime>",
    "eventDetails": {
        "eventConditions": [
            {
                "comparisonType": "<string>",
                "comparisonValue": "<string>",
                "expression": "<string>",
                "matchType": "<string>",
                "type": "<string>"
            },
            {
                "comparisonType": "<string>",
                "comparisonValue": "<string>",
                "expression": "<string>",
                "matchType": "<string>",
                "type": "<string>"
            }
        ],
        "useEventValue": "<boolean>"
    },
    "id": "<string>",
    "internalWebPropertyId": "<string>",
    "kind": "analytics#goal",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#profile"
    },
    "profileId": "<string>",
    "selfLink": "<string>",
    "type": "<string>",
    "updated": "<dateTime>",
    "urlDestinationDetails": {
        "caseSensitive": "<boolean>",
        "firstStepRequired": "<boolean>",
        "matchType": "<string>",
        "steps": [
            {
                "name": "<string>",
                "number": "<integer>",
                "url": "<string>"
            },
            {
                "name": "<string>",
                "number": "<integer>",
                "url": "<string>"
            }
        ],
        "url": "<string>"
    },
    "value": "<number>",
    "visitNumPagesDetails": {
        "comparisonType": "<string>",
        "comparisonValue": "<string>"
    },
    "visitTimeOnSiteDetails": {
        "comparisonType": "<string>",
        "comparisonValue": "<string>"
    },
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "<dateTime>",
 "eventDetails": {
  "eventConditions": [
   {
    "comparisonType": "<string>",
    "comparisonValue": "<string>",
    "expression": "<string>",
    "matchType": "<string>",
    "type": "<string>"
   },
   {
    "comparisonType": "<string>",
    "comparisonValue": "<string>",
    "expression": "<string>",
    "matchType": "<string>",
    "type": "<string>"
   }
  ],
  "useEventValue": "<boolean>"
 },
 "id": "<string>",
 "internalWebPropertyId": "<string>",
 "kind": "analytics#goal",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#profile"
 },
 "profileId": "<string>",
 "selfLink": "<string>",
 "type": "<string>",
 "updated": "<dateTime>",
 "urlDestinationDetails": {
  "caseSensitive": "<boolean>",
  "firstStepRequired": "<boolean>",
  "matchType": "<string>",
  "steps": [
   {
    "name": "<string>",
    "number": "<integer>",
    "url": "<string>"
   },
   {
    "name": "<string>",
    "number": "<integer>",
    "url": "<string>"
   }
  ],
  "url": "<string>"
 },
 "value": "<number>",
 "visitNumPagesDetails": {
  "comparisonType": "<string>",
  "comparisonValue": "<string>"
 },
 "visitTimeOnSiteDetails": {
  "comparisonType": "<string>",
  "comparisonValue": "<string>"
 },
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.goals.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/goals/:goalId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "active": "<boolean>",
    "created": "<dateTime>",
    "eventDetails": {
        "eventConditions": [
            {
                "comparisonType": "<string>",
                "comparisonValue": "<string>",
                "expression": "<string>",
                "matchType": "<string>",
                "type": "<string>"
            },
            {
                "comparisonType": "<string>",
                "comparisonValue": "<string>",
                "expression": "<string>",
                "matchType": "<string>",
                "type": "<string>"
            }
        ],
        "useEventValue": "<boolean>"
    },
    "id": "<string>",
    "internalWebPropertyId": "<string>",
    "kind": "analytics#goal",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#profile"
    },
    "profileId": "<string>",
    "selfLink": "<string>",
    "type": "<string>",
    "updated": "<dateTime>",
    "urlDestinationDetails": {
        "caseSensitive": "<boolean>",
        "firstStepRequired": "<boolean>",
        "matchType": "<string>",
        "steps": [
            {
                "name": "<string>",
                "number": "<integer>",
                "url": "<string>"
            },
            {
                "name": "<string>",
                "number": "<integer>",
                "url": "<string>"
            }
        ],
        "url": "<string>"
    },
    "value": "<number>",
    "visitNumPagesDetails": {
        "comparisonType": "<string>",
        "comparisonValue": "<string>"
    },
    "visitTimeOnSiteDetails": {
        "comparisonType": "<string>",
        "comparisonValue": "<string>"
    },
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "<dateTime>",
 "eventDetails": {
  "eventConditions": [
   {
    "comparisonType": "<string>",
    "comparisonValue": "<string>",
    "expression": "<string>",
    "matchType": "<string>",
    "type": "<string>"
   },
   {
    "comparisonType": "<string>",
    "comparisonValue": "<string>",
    "expression": "<string>",
    "matchType": "<string>",
    "type": "<string>"
   }
  ],
  "useEventValue": "<boolean>"
 },
 "id": "<string>",
 "internalWebPropertyId": "<string>",
 "kind": "analytics#goal",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#profile"
 },
 "profileId": "<string>",
 "selfLink": "<string>",
 "type": "<string>",
 "updated": "<dateTime>",
 "urlDestinationDetails": {
  "caseSensitive": "<boolean>",
  "firstStepRequired": "<boolean>",
  "matchType": "<string>",
  "steps": [
   {
    "name": "<string>",
    "number": "<integer>",
    "url": "<string>"
   },
   {
    "name": "<string>",
    "number": "<integer>",
    "url": "<string>"
   }
  ],
  "url": "<string>"
 },
 "value": "<number>",
 "visitNumPagesDetails": {
  "comparisonType": "<string>",
  "comparisonValue": "<string>"
 },
 "visitTimeOnSiteDetails": {
  "comparisonType": "<string>",
  "comparisonValue": "<string>"
 },
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.goals.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/goals?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of goals to include in this response.

**`start-index`**

An index of the first goal to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "nostrud dolore",
   "active": true,
   "created": "2017-06-03T17:02:23.975Z",
   "eventDetails": {
    "eventConditions": [
     {
      "comparisonType": "esse aliqua",
      "comparisonValue": "sint Lorem ea",
      "expression": "laborum incididunt",
      "matchType": "in et ipsum",
      "type": "fugiat E"
     },
     {
      "comparisonType": "proident elit",
      "comparisonValue": "velit id et",
      "expression": "fug",
      "matchType": "voluptate deserunt",
      "type": "culpa Ut enim veniam anim"
     }
    ],
    "useEventValue": true
   },
   "id": "anim irure aliqua sed",
   "internalWebPropertyId": "Excepteur nulla",
   "kind": "analytics#goal",
   "name": "exercitation",
   "parentLink": {
    "href": "Lorem",
    "type": "analytics#profile"
   },
   "profileId": "non sit voluptate",
   "selfLink": "et enim mollit quis",
   "type": "ut proident ut est",
   "updated": "2010-03-11T03:31:08.253Z",
   "urlDestinationDetails": {
    "caseSensitive": false,
    "firstStepRequired": false,
    "matchType": "officia minim exercitation",
    "steps": [
     {
      "name": "Duis nostrud Ut Lorem",
      "number": 17419537,
      "url": "cill"
     },
     {
      "name": "a",
      "number": -89375531,
      "url": "nisi"
     }
    ],
    "url": "ea voluptate"
   },
   "value": 28186092.5502083,
   "visitNumPagesDetails": {
    "comparisonType": "adipisicing",
    "comparisonValue": "occaecat minim"
   },
   "visitTimeOnSiteDetails": {
    "comparisonType": "sint cupidatat",
    "comparisonValue": "do cupidatat ad amet esse"
   },
   "webPropertyId": "amet"
  },
  {
   "accountId": "enim nostrud fugiat",
   "active": true,
   "created": "1960-09-12T17:01:01.054Z",
   "eventDetails": {
    "eventConditions": [
     {
      "comparisonType": "ipsu",
      "comparisonValue": "incididunt adipisicing",
      "expression": "tempor Lorem nisi cupidatat",
      "matchType": "mollit dolor laboris cillum in",
      "type": "ut officia commodo do"
     },
     {
      "comparisonType": "sint aliqua",
      "comparisonValue": "est id sed",
      "expression": "deserunt aliquip",
      "matchType": "ad irure",
      "type": "reprehenderit"
     }
    ],
    "useEventValue": false
   },
   "id": "deserunt sit",
   "internalWebPropertyId": "commodo ea",
   "kind": "analytics#goal",
   "name": "dolor voluptate",
   "parentLink": {
    "href": "tempor ipsum proident",
    "type": "analytics#profile"
   },
   "profileId": "nulla non fugiat",
   "selfLink": "nisi",
   "type": "culpa dolor",
   "updated": "1995-09-27T16:58:52.233Z",
   "urlDestinationDetails": {
    "caseSensitive": false,
    "firstStepRequired": true,
    "matchType": "ea nulla Lorem dolore",
    "steps": [
     {
      "name": "velit labore cillum ipsum",
      "number": 58032760,
      "url": "ea pariatur"
     },
     {
      "name": "dolore",
      "number": -47861284,
      "url": "occaecat"
     }
    ],
    "url": "sint ipsum est quis"
   },
   "value": 9983549.732959718,
   "visitNumPagesDetails": {
    "comparisonType": "ad cillum",
    "comparisonValue": "sunt"
   },
   "visitTimeOnSiteDetails": {
    "comparisonType": "est qui",
    "comparisonValue": "aliqua reprehenderit"
   },
   "webPropertyId": "enim non quis"
  }
 ],
 "itemsPerPage": 47192781,
 "kind": "analytics#goals",
 "nextLink": "dolor id",
 "previousLink": "sed nostrud et aute ",
 "startIndex": -1155695,
 "totalResults": -34200603,
 "username": "sed exercitation ut"
}
```

<br>

### analytics.management.goals.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/goals?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "active": "<boolean>",
    "created": "<dateTime>",
    "eventDetails": {
        "eventConditions": [
            {
                "comparisonType": "<string>",
                "comparisonValue": "<string>",
                "expression": "<string>",
                "matchType": "<string>",
                "type": "<string>"
            },
            {
                "comparisonType": "<string>",
                "comparisonValue": "<string>",
                "expression": "<string>",
                "matchType": "<string>",
                "type": "<string>"
            }
        ],
        "useEventValue": "<boolean>"
    },
    "id": "<string>",
    "internalWebPropertyId": "<string>",
    "kind": "analytics#goal",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#profile"
    },
    "profileId": "<string>",
    "selfLink": "<string>",
    "type": "<string>",
    "updated": "<dateTime>",
    "urlDestinationDetails": {
        "caseSensitive": "<boolean>",
        "firstStepRequired": "<boolean>",
        "matchType": "<string>",
        "steps": [
            {
                "name": "<string>",
                "number": "<integer>",
                "url": "<string>"
            },
            {
                "name": "<string>",
                "number": "<integer>",
                "url": "<string>"
            }
        ],
        "url": "<string>"
    },
    "value": "<number>",
    "visitNumPagesDetails": {
        "comparisonType": "<string>",
        "comparisonValue": "<string>"
    },
    "visitTimeOnSiteDetails": {
        "comparisonType": "<string>",
        "comparisonValue": "<string>"
    },
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "active": "<boolean>",
 "created": "<dateTime>",
 "eventDetails": {
  "eventConditions": [
   {
    "comparisonType": "<string>",
    "comparisonValue": "<string>",
    "expression": "<string>",
    "matchType": "<string>",
    "type": "<string>"
   },
   {
    "comparisonType": "<string>",
    "comparisonValue": "<string>",
    "expression": "<string>",
    "matchType": "<string>",
    "type": "<string>"
   }
  ],
  "useEventValue": "<boolean>"
 },
 "id": "<string>",
 "internalWebPropertyId": "<string>",
 "kind": "analytics#goal",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#profile"
 },
 "profileId": "<string>",
 "selfLink": "<string>",
 "type": "<string>",
 "updated": "<dateTime>",
 "urlDestinationDetails": {
  "caseSensitive": "<boolean>",
  "firstStepRequired": "<boolean>",
  "matchType": "<string>",
  "steps": [
   {
    "name": "<string>",
    "number": "<integer>",
    "url": "<string>"
   },
   {
    "name": "<string>",
    "number": "<integer>",
    "url": "<string>"
   }
  ],
  "url": "<string>"
 },
 "value": "<number>",
 "visitNumPagesDetails": {
  "comparisonType": "<string>",
  "comparisonValue": "<string>"
 },
 "visitTimeOnSiteDetails": {
  "comparisonType": "<string>",
  "comparisonValue": "<string>"
 },
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.profile Filter Links.delete ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
DELETE {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/profileFilterLinks/:linkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*: No response specified

<br>

### analytics.management.profile Filter Links.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/profileFilterLinks/:linkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "filterRef": {
  "accountId": "occaecat Lorem",
  "href": "pariatur Lorem nisi laborum",
  "id": "ipsum Duis do",
  "kind": "analytics#filterRef",
  "name": "adipisicing amet"
 },
 "id": "<string>",
 "kind": "analytics#profileFilterLink",
 "profileRef": {
  "accountId": "pariatur sit cillum",
  "href": "aute ullamco veniam irure",
  "id": "nisi Lorem sint est proident",
  "internalWebPropertyId": "occaecat elit non Lorem",
  "kind": "analytics#profileRef",
  "name": "voluptate oc",
  "webPropertyId": "nulla mollit"
 },
 "rank": "<integer>",
 "selfLink": "et est ad"
}
```

<br>

### analytics.management.profile Filter Links.patch ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PATCH {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/profileFilterLinks/:linkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "filterRef": {
        "accountId": "dolore exercitation Excepteur",
        "href": "laboris eu in labore",
        "id": "mollit",
        "kind": "analytics#filterRef",
        "name": "anim do"
    },
    "id": "<string>",
    "profileRef": {
        "accountId": "in nulla Excepteur esse",
        "href": "id amet qui aliqua consequat",
        "id": "laboris qui",
        "internalWebPropertyId": "ut tempor",
        "kind": "analytics#profileRef",
        "name": "dolor occaecat exercitation nisi",
        "webPropertyId": "labore sit dolore"
    },
    "rank": "<integer>"
}
```


> Response

*Successful response*
```json
{
 "filterRef": {
  "accountId": "occaecat Lorem",
  "href": "pariatur Lorem nisi laborum",
  "id": "ipsum Duis do",
  "kind": "analytics#filterRef",
  "name": "adipisicing amet"
 },
 "id": "<string>",
 "kind": "analytics#profileFilterLink",
 "profileRef": {
  "accountId": "pariatur sit cillum",
  "href": "aute ullamco veniam irure",
  "id": "nisi Lorem sint est proident",
  "internalWebPropertyId": "occaecat elit non Lorem",
  "kind": "analytics#profileRef",
  "name": "voluptate oc",
  "webPropertyId": "nulla mollit"
 },
 "rank": "<integer>",
 "selfLink": "et est ad"
}
```

<br>

### analytics.management.profile Filter Links.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/profileFilterLinks/:linkId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "filterRef": {
        "accountId": "dolore exercitation Excepteur",
        "href": "laboris eu in labore",
        "id": "mollit",
        "kind": "analytics#filterRef",
        "name": "anim do"
    },
    "id": "<string>",
    "profileRef": {
        "accountId": "in nulla Excepteur esse",
        "href": "id amet qui aliqua consequat",
        "id": "laboris qui",
        "internalWebPropertyId": "ut tempor",
        "kind": "analytics#profileRef",
        "name": "dolor occaecat exercitation nisi",
        "webPropertyId": "labore sit dolore"
    },
    "rank": "<integer>"
}
```


> Response

*Successful response*
```json
{
 "filterRef": {
  "accountId": "occaecat Lorem",
  "href": "pariatur Lorem nisi laborum",
  "id": "ipsum Duis do",
  "kind": "analytics#filterRef",
  "name": "adipisicing amet"
 },
 "id": "<string>",
 "kind": "analytics#profileFilterLink",
 "profileRef": {
  "accountId": "pariatur sit cillum",
  "href": "aute ullamco veniam irure",
  "id": "nisi Lorem sint est proident",
  "internalWebPropertyId": "occaecat elit non Lorem",
  "kind": "analytics#profileRef",
  "name": "voluptate oc",
  "webPropertyId": "nulla mollit"
 },
 "rank": "<integer>",
 "selfLink": "et est ad"
}
```

<br>

### analytics.management.profile Filter Links.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/profileFilterLinks?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of profile filter links to include in this response.

**`start-index`**

An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "filterRef": {
    "accountId": "dolor aliqua cillum aute est",
    "href": "nostrud voluptate nisi ullamco",
    "id": "ut",
    "kind": "analytics#filterRef",
    "name": "dolore ipsum nostrud re"
   },
   "id": "Ut labore ipsum reprehenderit",
   "kind": "analytics#profileFilterLink",
   "profileRef": {
    "accountId": "laborum fugiat ut",
    "href": "in magna",
    "id": "cillum",
    "internalWebPropertyId": "nulla Duis ipsum",
    "kind": "analytics#profileRef",
    "name": "culpa consectetur ea nulla",
    "webPropertyId": "exercitation"
   },
   "rank": 51037643,
   "selfLink": "id elit commodo"
  },
  {
   "filterRef": {
    "accountId": "nostrud irure deserunt",
    "href": "exercitation Lorem minim",
    "id": "dolor nostrud",
    "kind": "analytics#filterRef",
    "name": "veniam aute fugia"
   },
   "id": "laborum",
   "kind": "analytics#profileFilterLink",
   "profileRef": {
    "accountId": "ex aute in pariatur",
    "href": "incididunt eu",
    "id": "dolor id nisi",
    "internalWebPropertyId": "velit Excepteur incididunt",
    "kind": "analytics#profileRef",
    "name": "do mollit elit adipisicing",
    "webPropertyId": "ex est Duis laborum"
   },
   "rank": 92660653,
   "selfLink": "min"
  }
 ],
 "itemsPerPage": -22340129,
 "kind": "analytics#profileFilterLinks",
 "nextLink": "ullamco consequat",
 "previousLink": "ut esse re",
 "startIndex": -11185856,
 "totalResults": -95747537,
 "username": "Duis labore nulla"
}
```

<br>

### analytics.management.profile Filter Links.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/profileFilterLinks?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "filterRef": {
        "accountId": "dolore exercitation Excepteur",
        "href": "laboris eu in labore",
        "id": "mollit",
        "kind": "analytics#filterRef",
        "name": "anim do"
    },
    "id": "<string>",
    "profileRef": {
        "accountId": "in nulla Excepteur esse",
        "href": "id amet qui aliqua consequat",
        "id": "laboris qui",
        "internalWebPropertyId": "ut tempor",
        "kind": "analytics#profileRef",
        "name": "dolor occaecat exercitation nisi",
        "webPropertyId": "labore sit dolore"
    },
    "rank": "<integer>"
}
```


> Response

*Successful response*
```json
{
 "filterRef": {
  "accountId": "occaecat Lorem",
  "href": "pariatur Lorem nisi laborum",
  "id": "ipsum Duis do",
  "kind": "analytics#filterRef",
  "name": "adipisicing amet"
 },
 "id": "<string>",
 "kind": "analytics#profileFilterLink",
 "profileRef": {
  "accountId": "pariatur sit cillum",
  "href": "aute ullamco veniam irure",
  "id": "nisi Lorem sint est proident",
  "internalWebPropertyId": "occaecat elit non Lorem",
  "kind": "analytics#profileRef",
  "name": "voluptate oc",
  "webPropertyId": "nulla mollit"
 },
 "rank": "<integer>",
 "selfLink": "et est ad"
}
```

<br>

### analytics.management.unsampled Reports.delete ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
DELETE {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/unsampledReports/:unsampledReportId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*: No response specified

<br>

### analytics.management.unsampled Reports.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/unsampledReports/:unsampledReportId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "cloudStorageDownloadDetails": {
  "bucketId": "dolor id Lorem",
  "objectId": "incididunt consequat in et"
 },
 "created": "1977-09-13T06:34:49.463Z",
 "dimensions": "<string>",
 "downloadType": "quis sit et anim magna",
 "driveDownloadDetails": {
  "documentId": "Ut"
 },
 "end-date": "<string>",
 "filters": "<string>",
 "id": "<string>",
 "kind": "analytics#unsampledReport",
 "metrics": "<string>",
 "profileId": "<string>",
 "segment": "<string>",
 "selfLink": "ex esse cupidatat",
 "start-date": "<string>",
 "status": "ut aliquip",
 "title": "<string>",
 "updated": "1976-12-25T03:24:26.985Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.unsampled Reports.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/unsampledReports?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of unsampled reports to include in this response.

**`start-index`**

An index of the first unsampled report to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "dolore",
   "cloudStorageDownloadDetails": {
    "bucketId": "amet minim qui sunt",
    "objectId": "incididunt aute aliqua"
   },
   "created": "2017-12-09T11:53:45.240Z",
   "dimensions": "ex",
   "downloadType": "laborum eu nisi",
   "driveDownloadDetails": {
    "documentId": "sit non incid"
   },
   "end-date": "quis non irure ",
   "filters": "qui incididunt sint",
   "id": "occaecat",
   "kind": "analytics#unsampledReport",
   "metrics": "nulla in in",
   "profileId": "in aliquip eu id",
   "segment": "dolore est nostrud elit veniam",
   "selfLink": "in occaecat id sunt",
   "start-date": "occaecat eiusmod sint aliquip",
   "status": "cillum esse anim",
   "title": "fugiat Duis sint",
   "updated": "1998-02-21T11:14:38.670Z",
   "webPropertyId": "qui anim occaecat"
  },
  {
   "accountId": "eu qui",
   "cloudStorageDownloadDetails": {
    "bucketId": "esse magna officia est",
    "objectId": "ex aliquip aute"
   },
   "created": "1983-11-28T03:39:15.524Z",
   "dimensions": "proident est",
   "downloadType": "Excepteur consequat",
   "driveDownloadDetails": {
    "documentId": "eiusmod laborum ut ullamco cillum"
   },
   "end-date": "ipsum qui et exercitation ut",
   "filters": "enim proident labore sed",
   "id": "magna dolore velit incididunt",
   "kind": "analytics#unsampledReport",
   "metrics": "deserunt minim",
   "profileId": "in",
   "segment": "aliqua nisi officia",
   "selfLink": "veniam in ea",
   "start-date": "commodo Lorem do",
   "status": "in ut non",
   "title": "cillum veniam laboris ad",
   "updated": "1980-02-12T19:02:12.426Z",
   "webPropertyId": "dolore non qui sint"
  }
 ],
 "itemsPerPage": 52188230,
 "kind": "analytics#unsampledReports",
 "nextLink": "Ut sit irure",
 "previousLink": "sed cupidatat nulla",
 "startIndex": 75920547,
 "totalResults": -92147202,
 "username": "dolore officia"
}
```

<br>

### analytics.management.unsampled Reports.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId/unsampledReports?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "dimensions": "<string>",
    "end-date": "<string>",
    "filters": "<string>",
    "id": "<string>",
    "metrics": "<string>",
    "profileId": "<string>",
    "segment": "<string>",
    "start-date": "<string>",
    "title": "<string>",
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "cloudStorageDownloadDetails": {
  "bucketId": "dolor id Lorem",
  "objectId": "incididunt consequat in et"
 },
 "created": "1977-09-13T06:34:49.463Z",
 "dimensions": "<string>",
 "downloadType": "quis sit et anim magna",
 "driveDownloadDetails": {
  "documentId": "Ut"
 },
 "end-date": "<string>",
 "filters": "<string>",
 "id": "<string>",
 "kind": "analytics#unsampledReport",
 "metrics": "<string>",
 "profileId": "<string>",
 "segment": "<string>",
 "selfLink": "ex esse cupidatat",
 "start-date": "<string>",
 "status": "ut aliquip",
 "title": "<string>",
 "updated": "1976-12-25T03:24:26.985Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.profiles.delete ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
DELETE {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*: No response specified

<br>

### analytics.management.profiles.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "botFilteringEnabled": "<boolean>",
 "childLink": {
  "href": "<string>",
  "type": "analytics#goals"
 },
 "created": "2010-02-28T08:19:52.327Z",
 "currency": "<string>",
 "defaultPage": "<string>",
 "eCommerceTracking": "<boolean>",
 "enhancedECommerceTracking": "<boolean>",
 "excludeQueryParameters": "<string>",
 "id": "<string>",
 "internalWebPropertyId": "pariatur consequat aliqua fugiat qui",
 "kind": "analytics#profile",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "permissions": {
  "effective": [
   "elit eu nisi labore",
   "aliqua consectetur tempor elit ex"
  ]
 },
 "selfLink": "eiusmod deserunt labore consectetur culpa",
 "siteSearchCategoryParameters": "<string>",
 "siteSearchQueryParameters": "<string>",
 "starred": "<boolean>",
 "stripSiteSearchCategoryParameters": "<boolean>",
 "stripSiteSearchQueryParameters": "<boolean>",
 "timezone": "<string>",
 "type": "<string>",
 "updated": "1949-05-27T01:17:53.166Z",
 "webPropertyId": "irure minim",
 "websiteUrl": "<string>"
}
```

<br>

### analytics.management.profiles.patch ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PATCH {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "botFilteringEnabled": "<boolean>",
    "childLink": {
        "href": "<string>",
        "type": "analytics#goals"
    },
    "currency": "<string>",
    "defaultPage": "<string>",
    "eCommerceTracking": "<boolean>",
    "enhancedECommerceTracking": "<boolean>",
    "excludeQueryParameters": "<string>",
    "id": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#webproperty"
    },
    "permissions": {},
    "siteSearchCategoryParameters": "<string>",
    "siteSearchQueryParameters": "<string>",
    "starred": "<boolean>",
    "stripSiteSearchCategoryParameters": "<boolean>",
    "stripSiteSearchQueryParameters": "<boolean>",
    "timezone": "<string>",
    "type": "<string>",
    "websiteUrl": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "botFilteringEnabled": "<boolean>",
 "childLink": {
  "href": "<string>",
  "type": "analytics#goals"
 },
 "created": "2010-02-28T08:19:52.327Z",
 "currency": "<string>",
 "defaultPage": "<string>",
 "eCommerceTracking": "<boolean>",
 "enhancedECommerceTracking": "<boolean>",
 "excludeQueryParameters": "<string>",
 "id": "<string>",
 "internalWebPropertyId": "pariatur consequat aliqua fugiat qui",
 "kind": "analytics#profile",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "permissions": {
  "effective": [
   "elit eu nisi labore",
   "aliqua consectetur tempor elit ex"
  ]
 },
 "selfLink": "eiusmod deserunt labore consectetur culpa",
 "siteSearchCategoryParameters": "<string>",
 "siteSearchQueryParameters": "<string>",
 "starred": "<boolean>",
 "stripSiteSearchCategoryParameters": "<boolean>",
 "stripSiteSearchQueryParameters": "<boolean>",
 "timezone": "<string>",
 "type": "<string>",
 "updated": "1949-05-27T01:17:53.166Z",
 "webPropertyId": "irure minim",
 "websiteUrl": "<string>"
}
```

<br>

### analytics.management.profiles.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles/:profileId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "botFilteringEnabled": "<boolean>",
    "childLink": {
        "href": "<string>",
        "type": "analytics#goals"
    },
    "currency": "<string>",
    "defaultPage": "<string>",
    "eCommerceTracking": "<boolean>",
    "enhancedECommerceTracking": "<boolean>",
    "excludeQueryParameters": "<string>",
    "id": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#webproperty"
    },
    "permissions": {},
    "siteSearchCategoryParameters": "<string>",
    "siteSearchQueryParameters": "<string>",
    "starred": "<boolean>",
    "stripSiteSearchCategoryParameters": "<boolean>",
    "stripSiteSearchQueryParameters": "<boolean>",
    "timezone": "<string>",
    "type": "<string>",
    "websiteUrl": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "botFilteringEnabled": "<boolean>",
 "childLink": {
  "href": "<string>",
  "type": "analytics#goals"
 },
 "created": "2010-02-28T08:19:52.327Z",
 "currency": "<string>",
 "defaultPage": "<string>",
 "eCommerceTracking": "<boolean>",
 "enhancedECommerceTracking": "<boolean>",
 "excludeQueryParameters": "<string>",
 "id": "<string>",
 "internalWebPropertyId": "pariatur consequat aliqua fugiat qui",
 "kind": "analytics#profile",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "permissions": {
  "effective": [
   "elit eu nisi labore",
   "aliqua consectetur tempor elit ex"
  ]
 },
 "selfLink": "eiusmod deserunt labore consectetur culpa",
 "siteSearchCategoryParameters": "<string>",
 "siteSearchQueryParameters": "<string>",
 "starred": "<boolean>",
 "stripSiteSearchCategoryParameters": "<boolean>",
 "stripSiteSearchQueryParameters": "<boolean>",
 "timezone": "<string>",
 "type": "<string>",
 "updated": "1949-05-27T01:17:53.166Z",
 "webPropertyId": "irure minim",
 "websiteUrl": "<string>"
}
```

<br>

### analytics.management.profiles.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of views (profiles) to include in this response.

**`start-index`**

An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "officia ",
   "botFilteringEnabled": true,
   "childLink": {
    "href": "aliqua",
    "type": "analytics#goals"
   },
   "created": "2020-08-10T03:07:26.251Z",
   "currency": "nostrud proident",
   "defaultPage": "aliquip ipsum",
   "eCommerceTracking": false,
   "enhancedECommerceTracking": false,
   "excludeQueryParameters": "sed ullamco ut dolore in",
   "id": "labore in",
   "internalWebPropertyId": "aliqua enim in",
   "kind": "analytics#profile",
   "name": "adipisicing Excepteur tempor commodo",
   "parentLink": {
    "href": "fugiat ex dolore nostrud",
    "type": "analytics#webproperty"
   },
   "permissions": {
    "effective": [
     "Duis velit u",
     "amet dolor i"
    ]
   },
   "selfLink": "nisi irure Duis",
   "siteSearchCategoryParameters": "reprehenderit nisi officia",
   "siteSearchQueryParameters": "qui do",
   "starred": true,
   "stripSiteSearchCategoryParameters": false,
   "stripSiteSearchQueryParameters": false,
   "timezone": "elit irure",
   "type": "in laboris",
   "updated": "1943-05-23T13:37:24.821Z",
   "webPropertyId": "voluptate incididunt cillum est",
   "websiteUrl": "et cillum"
  },
  {
   "accountId": "laborum fugiat eu ipsum",
   "botFilteringEnabled": true,
   "childLink": {
    "href": "adipisicing aliquip minim non nostrud",
    "type": "analytics#goals"
   },
   "created": "1982-03-09T10:26:13.985Z",
   "currency": "in consectetur eu sed",
   "defaultPage": "occaecat",
   "eCommerceTracking": false,
   "enhancedECommerceTracking": true,
   "excludeQueryParameters": "Lorem ipsum irure labore dolor",
   "id": "nostrud cil",
   "internalWebPropertyId": "ipsum eiusmod",
   "kind": "analytics#profile",
   "name": "dolore Lorem",
   "parentLink": {
    "href": "voluptate nulla proident",
    "type": "analytics#webproperty"
   },
   "permissions": {
    "effective": [
     "Duis nisi",
     "consectetur quis"
    ]
   },
   "selfLink": "dolore in culpa nisi do",
   "siteSearchCategoryParameters": "ipsum dolore enim consectetur",
   "siteSearchQueryParameters": "dolore minim proident eiusmod anim",
   "starred": true,
   "stripSiteSearchCategoryParameters": false,
   "stripSiteSearchQueryParameters": true,
   "timezone": "adipisicing",
   "type": "pariatur minim Lorem",
   "updated": "1942-01-27T06:37:35.465Z",
   "webPropertyId": "ipsum sint ut Duis",
   "websiteUrl": "ipsum non ullamco nostrud laboris"
  }
 ],
 "itemsPerPage": -38593699,
 "kind": "analytics#profiles",
 "nextLink": "nulla elit q",
 "previousLink": "id ea Ut",
 "startIndex": 79663562,
 "totalResults": 20281102,
 "username": "mollit"
}
```

<br>

### analytics.management.profiles.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/profiles?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "botFilteringEnabled": "<boolean>",
    "childLink": {
        "href": "<string>",
        "type": "analytics#goals"
    },
    "currency": "<string>",
    "defaultPage": "<string>",
    "eCommerceTracking": "<boolean>",
    "enhancedECommerceTracking": "<boolean>",
    "excludeQueryParameters": "<string>",
    "id": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#webproperty"
    },
    "permissions": {},
    "siteSearchCategoryParameters": "<string>",
    "siteSearchQueryParameters": "<string>",
    "starred": "<boolean>",
    "stripSiteSearchCategoryParameters": "<boolean>",
    "stripSiteSearchQueryParameters": "<boolean>",
    "timezone": "<string>",
    "type": "<string>",
    "websiteUrl": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "botFilteringEnabled": "<boolean>",
 "childLink": {
  "href": "<string>",
  "type": "analytics#goals"
 },
 "created": "2010-02-28T08:19:52.327Z",
 "currency": "<string>",
 "defaultPage": "<string>",
 "eCommerceTracking": "<boolean>",
 "enhancedECommerceTracking": "<boolean>",
 "excludeQueryParameters": "<string>",
 "id": "<string>",
 "internalWebPropertyId": "pariatur consequat aliqua fugiat qui",
 "kind": "analytics#profile",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#webproperty"
 },
 "permissions": {
  "effective": [
   "elit eu nisi labore",
   "aliqua consectetur tempor elit ex"
  ]
 },
 "selfLink": "eiusmod deserunt labore consectetur culpa",
 "siteSearchCategoryParameters": "<string>",
 "siteSearchQueryParameters": "<string>",
 "starred": "<boolean>",
 "stripSiteSearchCategoryParameters": "<boolean>",
 "stripSiteSearchQueryParameters": "<boolean>",
 "timezone": "<string>",
 "type": "<string>",
 "updated": "1949-05-27T01:17:53.166Z",
 "webPropertyId": "irure minim",
 "websiteUrl": "<string>"
}
```

<br>

### analytics.management.remarketing Audience.delete ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
DELETE {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/remarketingAudiences/:remarketingAudienceId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*: No response specified

<br>

### analytics.management.remarketing Audience.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/remarketingAudiences/:remarketingAudienceId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "audienceDefinition": {
  "includeConditions": {
   "daysToLookBack": -43162443,
   "isSmartList": true,
   "kind": "analytics#includeConditions",
   "membershipDurationDays": 3013145,
   "segment": "Excepteur"
  }
 },
 "audienceType": "<string>",
 "created": "1979-12-09T18:13:25.816Z",
 "description": "laborum reprehenderit",
 "id": "<string>",
 "internalWebPropertyId": "veniam elit ut incididunt",
 "kind": "analytics#remarketingAudience",
 "linkedAdAccounts": [
  {
   "accountId": "proident in et",
   "eligibleForSearch": false,
   "id": "proident ullamco quis",
   "internalWebPropertyId": "dolore cillum consectetur ut ut",
   "kind": "analytics#linkedForeignAccount",
   "linkedAccountId": "culpa ipsum do est",
   "remarketingAudienceId": "cupidatat ea",
   "status": "sed pariatur anim",
   "type": "commodo dolore Lorem",
   "webPropertyId": "non Excepteur elit dolore"
  },
  {
   "accountId": "fugiat ullamco labore",
   "eligibleForSearch": true,
   "id": "in amet et",
   "internalWebPropertyId": "sunt culpa Lorem",
   "kind": "analytics#linkedForeignAccount",
   "linkedAccountId": "sint l",
   "remarketingAudienceId": "et deserunt veniam eu",
   "status": "occaecat Excepteur",
   "type": "in aliquip",
   "webPropertyId": "veniam nisi"
  }
 ],
 "linkedViews": [
  "<string>",
  "<string>"
 ],
 "name": "<string>",
 "stateBasedAudienceDefinition": {
  "excludeConditions": {
   "exclusionDuration": "<string>",
   "segment": "<string>"
  },
  "includeConditions": {
   "daysToLookBack": 68159292,
   "isSmartList": false,
   "kind": "analytics#includeConditions",
   "membershipDurationDays": -11726770,
   "segment": "pariatur sint ad"
  }
 },
 "updated": "1957-09-30T04:05:04.199Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.remarketing Audience.patch ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PATCH {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/remarketingAudiences/:remarketingAudienceId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "audienceDefinition": {
        "includeConditions": {
            "daysToLookBack": 23059655,
            "isSmartList": true,
            "kind": "analytics#includeConditions",
            "membershipDurationDays": -71076223,
            "segment": "consectetur Duis"
        }
    },
    "audienceType": "<string>",
    "id": "<string>",
    "kind": "analytics#remarketingAudience",
    "linkedAdAccounts": [
        {
            "accountId": "et nisi ea Duis",
            "eligibleForSearch": true,
            "id": "cupidatat",
            "internalWebPropertyId": "laboris ",
            "kind": "analytics#linkedForeignAccount",
            "linkedAccountId": "magna in",
            "remarketingAudienceId": "in sit do",
            "status": "ut non sunt",
            "type": "sit qui",
            "webPropertyId": "tempor consectetur aute do laboris"
        },
        {
            "accountId": "enim adipisicing in laboris",
            "eligibleForSearch": false,
            "id": "enim cillum et",
            "internalWebPropertyId": "ull",
            "kind": "analytics#linkedForeignAccount",
            "linkedAccountId": "dolor",
            "remarketingAudienceId": "ut dolore nisi minim et",
            "status": "sed esse Duis qui ipsum",
            "type": "sit velit in in",
            "webPropertyId": "id laboris esse dolore"
        }
    ],
    "linkedViews": [
        "<string>",
        "<string>"
    ],
    "name": "<string>",
    "stateBasedAudienceDefinition": {
        "excludeConditions": {
            "exclusionDuration": "<string>",
            "segment": "<string>"
        },
        "includeConditions": {
            "daysToLookBack": -44729455,
            "isSmartList": false,
            "kind": "analytics#includeConditions",
            "membershipDurationDays": 88356564,
            "segment": "ullamco"
        }
    },
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "audienceDefinition": {
  "includeConditions": {
   "daysToLookBack": -43162443,
   "isSmartList": true,
   "kind": "analytics#includeConditions",
   "membershipDurationDays": 3013145,
   "segment": "Excepteur"
  }
 },
 "audienceType": "<string>",
 "created": "1979-12-09T18:13:25.816Z",
 "description": "laborum reprehenderit",
 "id": "<string>",
 "internalWebPropertyId": "veniam elit ut incididunt",
 "kind": "analytics#remarketingAudience",
 "linkedAdAccounts": [
  {
   "accountId": "proident in et",
   "eligibleForSearch": false,
   "id": "proident ullamco quis",
   "internalWebPropertyId": "dolore cillum consectetur ut ut",
   "kind": "analytics#linkedForeignAccount",
   "linkedAccountId": "culpa ipsum do est",
   "remarketingAudienceId": "cupidatat ea",
   "status": "sed pariatur anim",
   "type": "commodo dolore Lorem",
   "webPropertyId": "non Excepteur elit dolore"
  },
  {
   "accountId": "fugiat ullamco labore",
   "eligibleForSearch": true,
   "id": "in amet et",
   "internalWebPropertyId": "sunt culpa Lorem",
   "kind": "analytics#linkedForeignAccount",
   "linkedAccountId": "sint l",
   "remarketingAudienceId": "et deserunt veniam eu",
   "status": "occaecat Excepteur",
   "type": "in aliquip",
   "webPropertyId": "veniam nisi"
  }
 ],
 "linkedViews": [
  "<string>",
  "<string>"
 ],
 "name": "<string>",
 "stateBasedAudienceDefinition": {
  "excludeConditions": {
   "exclusionDuration": "<string>",
   "segment": "<string>"
  },
  "includeConditions": {
   "daysToLookBack": 68159292,
   "isSmartList": false,
   "kind": "analytics#includeConditions",
   "membershipDurationDays": -11726770,
   "segment": "pariatur sint ad"
  }
 },
 "updated": "1957-09-30T04:05:04.199Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.remarketing Audience.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/remarketingAudiences/:remarketingAudienceId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "audienceDefinition": {
        "includeConditions": {
            "daysToLookBack": 23059655,
            "isSmartList": true,
            "kind": "analytics#includeConditions",
            "membershipDurationDays": -71076223,
            "segment": "consectetur Duis"
        }
    },
    "audienceType": "<string>",
    "id": "<string>",
    "kind": "analytics#remarketingAudience",
    "linkedAdAccounts": [
        {
            "accountId": "et nisi ea Duis",
            "eligibleForSearch": true,
            "id": "cupidatat",
            "internalWebPropertyId": "laboris ",
            "kind": "analytics#linkedForeignAccount",
            "linkedAccountId": "magna in",
            "remarketingAudienceId": "in sit do",
            "status": "ut non sunt",
            "type": "sit qui",
            "webPropertyId": "tempor consectetur aute do laboris"
        },
        {
            "accountId": "enim adipisicing in laboris",
            "eligibleForSearch": false,
            "id": "enim cillum et",
            "internalWebPropertyId": "ull",
            "kind": "analytics#linkedForeignAccount",
            "linkedAccountId": "dolor",
            "remarketingAudienceId": "ut dolore nisi minim et",
            "status": "sed esse Duis qui ipsum",
            "type": "sit velit in in",
            "webPropertyId": "id laboris esse dolore"
        }
    ],
    "linkedViews": [
        "<string>",
        "<string>"
    ],
    "name": "<string>",
    "stateBasedAudienceDefinition": {
        "excludeConditions": {
            "exclusionDuration": "<string>",
            "segment": "<string>"
        },
        "includeConditions": {
            "daysToLookBack": -44729455,
            "isSmartList": false,
            "kind": "analytics#includeConditions",
            "membershipDurationDays": 88356564,
            "segment": "ullamco"
        }
    },
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "audienceDefinition": {
  "includeConditions": {
   "daysToLookBack": -43162443,
   "isSmartList": true,
   "kind": "analytics#includeConditions",
   "membershipDurationDays": 3013145,
   "segment": "Excepteur"
  }
 },
 "audienceType": "<string>",
 "created": "1979-12-09T18:13:25.816Z",
 "description": "laborum reprehenderit",
 "id": "<string>",
 "internalWebPropertyId": "veniam elit ut incididunt",
 "kind": "analytics#remarketingAudience",
 "linkedAdAccounts": [
  {
   "accountId": "proident in et",
   "eligibleForSearch": false,
   "id": "proident ullamco quis",
   "internalWebPropertyId": "dolore cillum consectetur ut ut",
   "kind": "analytics#linkedForeignAccount",
   "linkedAccountId": "culpa ipsum do est",
   "remarketingAudienceId": "cupidatat ea",
   "status": "sed pariatur anim",
   "type": "commodo dolore Lorem",
   "webPropertyId": "non Excepteur elit dolore"
  },
  {
   "accountId": "fugiat ullamco labore",
   "eligibleForSearch": true,
   "id": "in amet et",
   "internalWebPropertyId": "sunt culpa Lorem",
   "kind": "analytics#linkedForeignAccount",
   "linkedAccountId": "sint l",
   "remarketingAudienceId": "et deserunt veniam eu",
   "status": "occaecat Excepteur",
   "type": "in aliquip",
   "webPropertyId": "veniam nisi"
  }
 ],
 "linkedViews": [
  "<string>",
  "<string>"
 ],
 "name": "<string>",
 "stateBasedAudienceDefinition": {
  "excludeConditions": {
   "exclusionDuration": "<string>",
   "segment": "<string>"
  },
  "includeConditions": {
   "daysToLookBack": 68159292,
   "isSmartList": false,
   "kind": "analytics#includeConditions",
   "membershipDurationDays": -11726770,
   "segment": "pariatur sint ad"
  }
 },
 "updated": "1957-09-30T04:05:04.199Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.remarketing Audience.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/remarketingAudiences?max-results=<integer>&start-index=<integer>&type=<string>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of remarketing audiences to include in this response.

**`start-index`**

An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`type`**

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "exercitation consequat",
   "audienceDefinition": {
    "includeConditions": {
     "daysToLookBack": 55023057,
     "isSmartList": true,
     "kind": "analytics#includeConditions",
     "membershipDurationDays": 38261225,
     "segment": "nisi aliqu"
    }
   },
   "audienceType": "ut aliqua Excepteur Lorem do",
   "created": "2015-02-05T09:37:12.021Z",
   "description": "enim occaecat",
   "id": "dolor Ut esse ullamco",
   "internalWebPropertyId": "consectetur reprehenderit mollit aute",
   "kind": "analytics#remarketingAudience",
   "linkedAdAccounts": [
    {
     "accountId": "sint in",
     "eligibleForSearch": false,
     "id": "ullamco nostrud est enim",
     "internalWebPropertyId": "qui ullamco ex anim",
     "kind": "analytics#linkedForeignAccount",
     "linkedAccountId": "in ullamco sunt ipsum",
     "remarketingAudienceId": "mollit dolor irure id amet",
     "status": "consectetur nostrud quis deserunt",
     "type": "consectetur culpa magna in ex",
     "webPropertyId": "ex nostrud eu Ut ut"
    },
    {
     "accountId": "elit",
     "eligibleForSearch": true,
     "id": "ea sunt pariatur ipsum ut",
     "internalWebPropertyId": "ea commodo voluptate in",
     "kind": "analytics#linkedForeignAccount",
     "linkedAccountId": "nostrud labore",
     "remarketingAudienceId": "laborum ad esse",
     "status": "ut qui",
     "type": "consectetur in aliquip quis",
     "webPropertyId": "amet cillum"
    }
   ],
   "linkedViews": [
    "occaecat Ut qui in",
    "proident laborum"
   ],
   "name": "ipsum dolore non",
   "stateBasedAudienceDefinition": {
    "excludeConditions": {
     "exclusionDuration": "eu commodo",
     "segment": "s"
    },
    "includeConditions": {
     "daysToLookBack": -72953709,
     "isSmartList": true,
     "kind": "analytics#includeConditions",
     "membershipDurationDays": 23413135,
     "segment": "enim ullamco ad cupidatat et"
    }
   },
   "updated": "2019-05-20T10:03:03.058Z",
   "webPropertyId": "minim ullamco"
  },
  {
   "accountId": "sint dolore laborum",
   "audienceDefinition": {
    "includeConditions": {
     "daysToLookBack": 43037280,
     "isSmartList": true,
     "kind": "analytics#includeConditions",
     "membershipDurationDays": -51666222,
     "segment": "enim esse"
    }
   },
   "audienceType": "cupidatat ullamco in ut",
   "created": "1943-01-06T10:37:08.961Z",
   "description": "aliqua incididunt mollit",
   "id": "qui fugiat Lorem ad",
   "internalWebPropertyId": "et officia",
   "kind": "analytics#remarketingAudience",
   "linkedAdAccounts": [
    {
     "accountId": "incididunt qui tempor minim",
     "eligibleForSearch": true,
     "id": "occaecat Excepteur cillum ad",
     "internalWebPropertyId": "in sunt",
     "kind": "analytics#linkedForeignAccount",
     "linkedAccountId": "ut elit",
     "remarketingAudienceId": "consect",
     "status": "ea et cons",
     "type": "anim laborum ",
     "webPropertyId": "Excepteur sed commodo"
    },
    {
     "accountId": "cillum dolore aliqua",
     "eligibleForSearch": false,
     "id": "incididunt veniam ullamco",
     "internalWebPropertyId": "Duis quis ex",
     "kind": "analytics#linkedForeignAccount",
     "linkedAccountId": "eiusmod reprehenderit",
     "remarketingAudienceId": "fugiat",
     "status": "minim cup",
     "type": "Lorem commodo",
     "webPropertyId": "fugiat magna dolore"
    }
   ],
   "linkedViews": [
    "ad",
    "fugiat"
   ],
   "name": "irure commodo ipsum nostrud consequat",
   "stateBasedAudienceDefinition": {
    "excludeConditions": {
     "exclusionDuration": "sit et adipisicing tempor voluptate",
     "segment": "occaecat velit"
    },
    "includeConditions": {
     "daysToLookBack": 17357712,
     "isSmartList": false,
     "kind": "analytics#includeConditions",
     "membershipDurationDays": -4702951,
     "segment": "Duis minim culpa dolor veniam"
    }
   },
   "updated": "2011-04-27T00:37:02.107Z",
   "webPropertyId": "voluptate incididunt"
  }
 ],
 "itemsPerPage": -1622245,
 "kind": "analytics#remarketingAudiences",
 "nextLink": "non nostrud",
 "previousLink": "laborum Lorem occaecat",
 "startIndex": 36943074,
 "totalResults": -71856566,
 "username": "id nisi occaecat"
}
```

<br>

### analytics.management.remarketing Audience.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId/remarketingAudiences?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "audienceDefinition": {
        "includeConditions": {
            "daysToLookBack": 23059655,
            "isSmartList": true,
            "kind": "analytics#includeConditions",
            "membershipDurationDays": -71076223,
            "segment": "consectetur Duis"
        }
    },
    "audienceType": "<string>",
    "id": "<string>",
    "kind": "analytics#remarketingAudience",
    "linkedAdAccounts": [
        {
            "accountId": "et nisi ea Duis",
            "eligibleForSearch": true,
            "id": "cupidatat",
            "internalWebPropertyId": "laboris ",
            "kind": "analytics#linkedForeignAccount",
            "linkedAccountId": "magna in",
            "remarketingAudienceId": "in sit do",
            "status": "ut non sunt",
            "type": "sit qui",
            "webPropertyId": "tempor consectetur aute do laboris"
        },
        {
            "accountId": "enim adipisicing in laboris",
            "eligibleForSearch": false,
            "id": "enim cillum et",
            "internalWebPropertyId": "ull",
            "kind": "analytics#linkedForeignAccount",
            "linkedAccountId": "dolor",
            "remarketingAudienceId": "ut dolore nisi minim et",
            "status": "sed esse Duis qui ipsum",
            "type": "sit velit in in",
            "webPropertyId": "id laboris esse dolore"
        }
    ],
    "linkedViews": [
        "<string>",
        "<string>"
    ],
    "name": "<string>",
    "stateBasedAudienceDefinition": {
        "excludeConditions": {
            "exclusionDuration": "<string>",
            "segment": "<string>"
        },
        "includeConditions": {
            "daysToLookBack": -44729455,
            "isSmartList": false,
            "kind": "analytics#includeConditions",
            "membershipDurationDays": 88356564,
            "segment": "ullamco"
        }
    },
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "audienceDefinition": {
  "includeConditions": {
   "daysToLookBack": -43162443,
   "isSmartList": true,
   "kind": "analytics#includeConditions",
   "membershipDurationDays": 3013145,
   "segment": "Excepteur"
  }
 },
 "audienceType": "<string>",
 "created": "1979-12-09T18:13:25.816Z",
 "description": "laborum reprehenderit",
 "id": "<string>",
 "internalWebPropertyId": "veniam elit ut incididunt",
 "kind": "analytics#remarketingAudience",
 "linkedAdAccounts": [
  {
   "accountId": "proident in et",
   "eligibleForSearch": false,
   "id": "proident ullamco quis",
   "internalWebPropertyId": "dolore cillum consectetur ut ut",
   "kind": "analytics#linkedForeignAccount",
   "linkedAccountId": "culpa ipsum do est",
   "remarketingAudienceId": "cupidatat ea",
   "status": "sed pariatur anim",
   "type": "commodo dolore Lorem",
   "webPropertyId": "non Excepteur elit dolore"
  },
  {
   "accountId": "fugiat ullamco labore",
   "eligibleForSearch": true,
   "id": "in amet et",
   "internalWebPropertyId": "sunt culpa Lorem",
   "kind": "analytics#linkedForeignAccount",
   "linkedAccountId": "sint l",
   "remarketingAudienceId": "et deserunt veniam eu",
   "status": "occaecat Excepteur",
   "type": "in aliquip",
   "webPropertyId": "veniam nisi"
  }
 ],
 "linkedViews": [
  "<string>",
  "<string>"
 ],
 "name": "<string>",
 "stateBasedAudienceDefinition": {
  "excludeConditions": {
   "exclusionDuration": "<string>",
   "segment": "<string>"
  },
  "includeConditions": {
   "daysToLookBack": 68159292,
   "isSmartList": false,
   "kind": "analytics#includeConditions",
   "membershipDurationDays": -11726770,
   "segment": "pariatur sint ad"
  }
 },
 "updated": "1957-09-30T04:05:04.199Z",
 "webPropertyId": "<string>"
}
```

<br>

### analytics.management.webproperties.get ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "childLink": {
  "href": "<string>",
  "type": "analytics#profiles"
 },
 "created": "1989-11-18T07:08:38.601Z",
 "dataRetentionResetOnNewActivity": "<boolean>",
 "dataRetentionTtl": "<string>",
 "defaultProfileId": "<string>",
 "id": "<string>",
 "industryVertical": "<string>",
 "internalWebPropertyId": "l",
 "kind": "analytics#webproperty",
 "level": "ullamco sint laboris anim",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#account"
 },
 "permissions": {
  "effective": [
   "consequat ea",
   "veniam pariatur"
  ]
 },
 "profileCount": 24129104,
 "selfLink": "amet eu",
 "starred": "<boolean>",
 "updated": "1974-07-13T02:27:24.382Z",
 "websiteUrl": "<string>"
}
```

<br>

### analytics.management.webproperties.patch ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PATCH {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "childLink": {
        "href": "<string>",
        "type": "analytics#profiles"
    },
    "dataRetentionResetOnNewActivity": "<boolean>",
    "dataRetentionTtl": "<string>",
    "defaultProfileId": "<string>",
    "id": "<string>",
    "industryVertical": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#account"
    },
    "permissions": {},
    "starred": "<boolean>",
    "websiteUrl": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "childLink": {
  "href": "<string>",
  "type": "analytics#profiles"
 },
 "created": "1989-11-18T07:08:38.601Z",
 "dataRetentionResetOnNewActivity": "<boolean>",
 "dataRetentionTtl": "<string>",
 "defaultProfileId": "<string>",
 "id": "<string>",
 "industryVertical": "<string>",
 "internalWebPropertyId": "l",
 "kind": "analytics#webproperty",
 "level": "ullamco sint laboris anim",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#account"
 },
 "permissions": {
  "effective": [
   "consequat ea",
   "veniam pariatur"
  ]
 },
 "profileCount": 24129104,
 "selfLink": "amet eu",
 "starred": "<boolean>",
 "updated": "1974-07-13T02:27:24.382Z",
 "websiteUrl": "<string>"
}
```

<br>

### analytics.management.webproperties.update ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
PUT {{baseUrl}}/management/accounts/:accountId/webproperties/:webPropertyId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "childLink": {
        "href": "<string>",
        "type": "analytics#profiles"
    },
    "dataRetentionResetOnNewActivity": "<boolean>",
    "dataRetentionTtl": "<string>",
    "defaultProfileId": "<string>",
    "id": "<string>",
    "industryVertical": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#account"
    },
    "permissions": {},
    "starred": "<boolean>",
    "websiteUrl": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "childLink": {
  "href": "<string>",
  "type": "analytics#profiles"
 },
 "created": "1989-11-18T07:08:38.601Z",
 "dataRetentionResetOnNewActivity": "<boolean>",
 "dataRetentionTtl": "<string>",
 "defaultProfileId": "<string>",
 "id": "<string>",
 "industryVertical": "<string>",
 "internalWebPropertyId": "l",
 "kind": "analytics#webproperty",
 "level": "ullamco sint laboris anim",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#account"
 },
 "permissions": {
  "effective": [
   "consequat ea",
   "veniam pariatur"
  ]
 },
 "profileCount": 24129104,
 "selfLink": "amet eu",
 "starred": "<boolean>",
 "updated": "1974-07-13T02:27:24.382Z",
 "websiteUrl": "<string>"
}
```

<br>

### analytics.management.webproperties.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts/:accountId/webproperties?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of web properties to include in this response.

**`start-index`**

An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "accountId": "laboris",
   "childLink": {
    "href": "do Excepteur enim",
    "type": "analytics#profiles"
   },
   "created": "1958-01-26T10:23:57.383Z",
   "dataRetentionResetOnNewActivity": false,
   "dataRetentionTtl": "dolore sint commodo",
   "defaultProfileId": "consectetur do ipsum",
   "id": "fugiat laborum",
   "industryVertical": "nostrud nulla ",
   "internalWebPropertyId": "aute magna",
   "kind": "analytics#webproperty",
   "level": "anim in sit pariatur",
   "name": "nostrud voluptate dolor Duis",
   "parentLink": {
    "href": "nostrud tempor",
    "type": "analytics#account"
   },
   "permissions": {
    "effective": [
     "in",
     "sit eiusmod incididunt"
    ]
   },
   "profileCount": -78749329,
   "selfLink": "laborum in non",
   "starred": true,
   "updated": "1983-04-07T08:03:35.839Z",
   "websiteUrl": "ut magna velit Ut"
  },
  {
   "accountId": "minim irure fugiat",
   "childLink": {
    "href": "dolore fugiat exercitation ullamco",
    "type": "analytics#profiles"
   },
   "created": "2015-12-18T10:56:07.532Z",
   "dataRetentionResetOnNewActivity": true,
   "dataRetentionTtl": "fugiat tempor",
   "defaultProfileId": "consectetur dolore amet consequat",
   "id": "veniam laborum",
   "industryVertical": "consectetur",
   "internalWebPropertyId": "aute veniam ipsum officia",
   "kind": "analytics#webproperty",
   "level": "incididunt sunt",
   "name": "officia",
   "parentLink": {
    "href": "occaecat in incididunt ullamco",
    "type": "analytics#account"
   },
   "permissions": {
    "effective": [
     "laboris ad",
     "consectetur commodo qui"
    ]
   },
   "profileCount": 666473,
   "selfLink": "dolore officia ut fugiat do",
   "starred": false,
   "updated": "1997-11-17T16:24:56.888Z",
   "websiteUrl": "laborum pariatu"
  }
 ],
 "itemsPerPage": 85034293,
 "kind": "analytics#webproperties",
 "nextLink": "reprehenderit",
 "previousLink": "culpa sit ex sint",
 "startIndex": 92375940,
 "totalResults": -94986890,
 "username": "in Lorem ut ipsum"
}
```

<br>

### analytics.management.webproperties.insert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/accounts/:accountId/webproperties?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountId": "<string>",
    "childLink": {
        "href": "<string>",
        "type": "analytics#profiles"
    },
    "dataRetentionResetOnNewActivity": "<boolean>",
    "dataRetentionTtl": "<string>",
    "defaultProfileId": "<string>",
    "id": "<string>",
    "industryVertical": "<string>",
    "name": "<string>",
    "parentLink": {
        "href": "<string>",
        "type": "analytics#account"
    },
    "permissions": {},
    "starred": "<boolean>",
    "websiteUrl": "<string>"
}
```


> Response

*Successful response*
```json
{
 "accountId": "<string>",
 "childLink": {
  "href": "<string>",
  "type": "analytics#profiles"
 },
 "created": "1989-11-18T07:08:38.601Z",
 "dataRetentionResetOnNewActivity": "<boolean>",
 "dataRetentionTtl": "<string>",
 "defaultProfileId": "<string>",
 "id": "<string>",
 "industryVertical": "<string>",
 "internalWebPropertyId": "l",
 "kind": "analytics#webproperty",
 "level": "ullamco sint laboris anim",
 "name": "<string>",
 "parentLink": {
  "href": "<string>",
  "type": "analytics#account"
 },
 "permissions": {
  "effective": [
   "consequat ea",
   "veniam pariatur"
  ]
 },
 "profileCount": 24129104,
 "selfLink": "amet eu",
 "starred": "<boolean>",
 "updated": "1974-07-13T02:27:24.382Z",
 "websiteUrl": "<string>"
}
```

<br>

### analytics.management.accounts.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accounts?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of accounts to include in this response.

**`start-index`**

An index of the first account to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "childLink": {
    "href": "sint dolor",
    "type": "analytics#webproperties"
   },
   "created": "2011-09-30T08:59:45.984Z",
   "id": "mollit fugiat laboris",
   "kind": "analytics#account",
   "name": "dolor commodo laboris fugiat",
   "permissions": {
    "effective": [
     "ut commodo",
     "veniam labore in voluptate"
    ]
   },
   "selfLink": "eu reprehenderit",
   "starred": false,
   "updated": "2006-01-13T18:06:06.517Z"
  },
  {
   "childLink": {
    "href": "aliqua occaecat",
    "type": "analytics#webproperties"
   },
   "created": "1967-11-19T18:51:15.021Z",
   "id": "mollit",
   "kind": "analytics#account",
   "name": "adipisicing in",
   "permissions": {
    "effective": [
     "deserunt eu",
     "proident"
    ]
   },
   "selfLink": "et",
   "starred": false,
   "updated": "1976-05-30T11:27:30.583Z"
  }
 ],
 "itemsPerPage": -79091404,
 "kind": "analytics#accounts",
 "nextLink": "qui ipsum ut elit",
 "previousLink": "elit non dolor",
 "startIndex": -55525845,
 "totalResults": 15985896,
 "username": "Duis"
}
```

<br>

### analytics.management.account Summaries.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/accountSummaries?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of account summaries to include in this response, where the largest acceptable value is 1000.

**`start-index`**

An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "id": "dolore ut enim",
   "kind": "analytics#accountSummary",
   "name": "sed mollit est",
   "starred": false,
   "webProperties": [
    {
     "id": "dolore culpa",
     "internalWebPropertyId": "mollit officia",
     "kind": "analytics#webPropertySummary",
     "level": "in nulla magna irure sint",
     "name": "culpa commodo laborum dolore esse",
     "profiles": [
      {
       "id": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "kind": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "name": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "starred": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "type": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       }
      },
      {
       "id": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "kind": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "name": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "starred": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "type": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       }
      }
     ],
     "starred": false,
     "websiteUrl": "commodo officia in"
    },
    {
     "id": "deserunt",
     "internalWebPropertyId": "ipsum irure",
     "kind": "analytics#webPropertySummary",
     "level": "Duis non quis reprehenderit",
     "name": "non sint in",
     "profiles": [
      {
       "id": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "kind": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "name": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "starred": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "type": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       }
      },
      {
       "id": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "kind": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "name": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "starred": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "type": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       }
      }
     ],
     "starred": false,
     "websiteUrl": "Excepte"
    }
   ]
  },
  {
   "id": "Ut est in",
   "kind": "analytics#accountSummary",
   "name": "sit dolore",
   "starred": true,
   "webProperties": [
    {
     "id": "irure non eiusmod culpa",
     "internalWebPropertyId": "laborum sit Ut reprehenderit",
     "kind": "analytics#webPropertySummary",
     "level": "e",
     "name": "cillum irure deserunt amet commodo",
     "profiles": [
      {
       "id": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "kind": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "name": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "starred": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "type": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       }
      },
      {
       "id": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "kind": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "name": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "starred": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "type": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       }
      }
     ],
     "starred": false,
     "websiteUrl": "voluptate labore ut"
    },
    {
     "id": "dolore in in ex",
     "internalWebPropertyId": "dolor",
     "kind": "analytics#webPropertySummary",
     "level": "consectetur adipisicing pariatur culpa eiusmod",
     "name": "enim do non",
     "profiles": [
      {
       "id": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "kind": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "name": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "starred": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "type": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       }
      },
      {
       "id": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "kind": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "name": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "starred": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       },
       "type": {
        "value": "<Error: Too many levels of nesting to fake this schema>"
       }
      }
     ],
     "starred": false,
     "websiteUrl": "laboris Lorem amet cillum"
    }
   ]
  }
 ],
 "itemsPerPage": 17885038,
 "kind": "analytics#accountSummaries",
 "nextLink": "Excepteur enim magna culpa incididunt",
 "previousLink": "non",
 "startIndex": -6774516,
 "totalResults": -99588311,
 "username": "do"
}
```

<br>

### analytics.management.client Id.hash Client Id ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/management/clientId:hashClientId?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "clientId": "<string>",
    "kind": "analytics#hashClientIdRequest",
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "clientId": "dolore ex laboris",
 "hashedClientId": "proident in in qui",
 "kind": "analytics#hashClientIdResponse",
 "webPropertyId": "sed id sunt tempor"
}
```

<br>

### analytics.management.segments.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/management/segments?max-results=<integer>&start-index=<integer>&alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`max-results`**

The maximum number of segments to include in this response.

**`start-index`**

An index of the first segment to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "items": [
  {
   "created": "1995-01-08T02:36:11.087Z",
   "definition": "id enim reprehenderit Ut",
   "id": "occaecat cillum sunt",
   "kind": "analytics#segment",
   "name": "ulla",
   "segmentId": "in ut ut non",
   "selfLink": "sint incididunt amet aute",
   "type": "ut in incididunt",
   "updated": "1995-05-18T01:34:08.443Z"
  },
  {
   "created": "1981-04-03T04:16:00.150Z",
   "definition": "labore velit occaecat ea",
   "id": "in tempor",
   "kind": "analytics#segment",
   "name": "esse tempor deserunt eiusmod",
   "segmentId": "velit sunt dolor",
   "selfLink": "nostrud minim",
   "type": "pariatur est nisi consequat aliquip",
   "updated": "1953-12-31T07:25:09.843Z"
  }
 ],
 "itemsPerPage": -86165235,
 "kind": "analytics#segments",
 "nextLink": "irure eu quis",
 "previousLink": "Ut occaecat aliquip proident",
 "startIndex": 98846691,
 "totalResults": -10298037,
 "username": "in sed"
}
```

<br>

### analytics.provisioning.create Account Ticket ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/provisioning/createAccountTicket?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "account": {
        "childLink": {
            "href": "magna velit deserunt",
            "type": "analytics#webproperties"
        },
        "created": "2010-09-18T07:19:36.210Z",
        "id": "consequat do nisi elit",
        "kind": "analytics#account",
        "name": "qui Excepteur Ut",
        "permissions": {
            "effective": [
                "dolor ullamco ut",
                "ut Duis aute culpa"
            ]
        },
        "selfLink": "laboris minim",
        "starred": true,
        "updated": "1963-07-02T00:18:55.371Z"
    },
    "id": "<string>",
    "kind": "analytics#accountTicket",
    "profile": {
        "accountId": "<string>",
        "botFilteringEnabled": "<boolean>",
        "childLink": {
            "href": "<string>",
            "type": "analytics#goals"
        },
        "created": "1942-11-11T15:56:18.514Z",
        "currency": "<string>",
        "defaultPage": "<string>",
        "eCommerceTracking": "<boolean>",
        "enhancedECommerceTracking": "<boolean>",
        "excludeQueryParameters": "<string>",
        "id": "<string>",
        "internalWebPropertyId": "in veniam velit",
        "kind": "analytics#profile",
        "name": "<string>",
        "parentLink": {
            "href": "<string>",
            "type": "analytics#webproperty"
        },
        "permissions": {
            "effective": [
                "officia Ut sunt ut incididunt",
                "pariatur exercitation"
            ]
        },
        "selfLink": "nostrud",
        "siteSearchCategoryParameters": "<string>",
        "siteSearchQueryParameters": "<string>",
        "starred": "<boolean>",
        "stripSiteSearchCategoryParameters": "<boolean>",
        "stripSiteSearchQueryParameters": "<boolean>",
        "timezone": "<string>",
        "type": "<string>",
        "updated": "1968-08-08T07:48:25.105Z",
        "webPropertyId": "quis sint enim",
        "websiteUrl": "<string>"
    },
    "redirectUri": "<string>",
    "webproperty": {
        "accountId": "<string>",
        "childLink": {
            "href": "<string>",
            "type": "analytics#profiles"
        },
        "created": "1968-08-21T18:33:52.753Z",
        "dataRetentionResetOnNewActivity": "<boolean>",
        "dataRetentionTtl": "<string>",
        "defaultProfileId": "<string>",
        "id": "<string>",
        "industryVertical": "<string>",
        "internalWebPropertyId": "dolor enim ad",
        "kind": "analytics#webproperty",
        "level": "anim laboris ex id",
        "name": "<string>",
        "parentLink": {
            "href": "<string>",
            "type": "analytics#account"
        },
        "permissions": {
            "effective": [
                "",
                "id incididunt nulla"
            ]
        },
        "profileCount": -96535393,
        "selfLink": "aliquip t",
        "starred": "<boolean>",
        "updated": "1990-05-25T16:35:24.979Z",
        "websiteUrl": "<string>"
    }
}
```


> Response

*Successful response*
```json
{
 "account": {
  "childLink": {
   "href": "laboris cupidatat commodo et",
   "type": "analytics#webproperties"
  },
  "created": "1973-05-10T19:23:56.733Z",
  "id": "aliqua nisi do in ipsum",
  "kind": "analytics#account",
  "name": "ad velit quis sint",
  "permissions": {
   "effective": [
    "in sit co",
    "in quis adipisicing"
   ]
  },
  "selfLink": "veniam irure quis",
  "starred": false,
  "updated": "1972-11-09T20:30:17.892Z"
 },
 "id": "<string>",
 "kind": "analytics#accountTicket",
 "profile": {
  "accountId": "<string>",
  "botFilteringEnabled": "<boolean>",
  "childLink": {
   "href": "<string>",
   "type": "analytics#goals"
  },
  "created": "2000-03-30T16:13:10.350Z",
  "currency": "<string>",
  "defaultPage": "<string>",
  "eCommerceTracking": "<boolean>",
  "enhancedECommerceTracking": "<boolean>",
  "excludeQueryParameters": "<string>",
  "id": "<string>",
  "internalWebPropertyId": "adipisicing do",
  "kind": "analytics#profile",
  "name": "<string>",
  "parentLink": {
   "href": "<string>",
   "type": "analytics#webproperty"
  },
  "permissions": {
   "effective": [
    "in aute irure non",
    "ad sunt quis nisi aliquip"
   ]
  },
  "selfLink": "ea dolore in anim",
  "siteSearchCategoryParameters": "<string>",
  "siteSearchQueryParameters": "<string>",
  "starred": "<boolean>",
  "stripSiteSearchCategoryParameters": "<boolean>",
  "stripSiteSearchQueryParameters": "<boolean>",
  "timezone": "<string>",
  "type": "<string>",
  "updated": "2013-04-01T23:53:12.301Z",
  "webPropertyId": "tempor labore aliqua ut",
  "websiteUrl": "<string>"
 },
 "redirectUri": "<string>",
 "webproperty": {
  "accountId": "<string>",
  "childLink": {
   "href": "<string>",
   "type": "analytics#profiles"
  },
  "created": "1945-04-03T11:50:22.809Z",
  "dataRetentionResetOnNewActivity": "<boolean>",
  "dataRetentionTtl": "<string>",
  "defaultProfileId": "<string>",
  "id": "<string>",
  "industryVertical": "<string>",
  "internalWebPropertyId": "laborum dolore",
  "kind": "analytics#webproperty",
  "level": "Ut nostrud quis",
  "name": "<string>",
  "parentLink": {
   "href": "<string>",
   "type": "analytics#account"
  },
  "permissions": {
   "effective": [
    "reprehenderit minim labore velit",
    "a"
   ]
  },
  "profileCount": 68017244,
  "selfLink": "proident qui dolore",
  "starred": "<boolean>",
  "updated": "1957-10-06T12:31:40.044Z",
  "websiteUrl": "<string>"
 }
}
```

<br>

### analytics.provisioning.create Account Tree ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/provisioning/createAccountTree?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "accountName": "<string>",
    "kind": "analytics#accountTreeRequest",
    "profileName": "<string>",
    "timezone": "<string>",
    "webpropertyName": "<string>",
    "websiteUrl": "<string>"
}
```


> Response

*Successful response*
```json
{
 "account": {
  "childLink": {
   "href": "tempor sed ullamco",
   "type": "analytics#webproperties"
  },
  "created": "2010-08-21T12:27:11.358Z",
  "id": "dolor ex quis reprehenderit",
  "kind": "analytics#account",
  "name": "eu aliqua mi",
  "permissions": {
   "effective": [
    "nisi id veniam enim",
    "ea eu consectetur"
   ]
  },
  "selfLink": "Excepteur laborum in quis",
  "starred": true,
  "updated": "1975-10-08T14:30:49.445Z"
 },
 "kind": "analytics#accountTreeResponse",
 "profile": {
  "accountId": "<string>",
  "botFilteringEnabled": "<boolean>",
  "childLink": {
   "href": "<string>",
   "type": "analytics#goals"
  },
  "created": "1945-12-07T06:37:28.400Z",
  "currency": "<string>",
  "defaultPage": "<string>",
  "eCommerceTracking": "<boolean>",
  "enhancedECommerceTracking": "<boolean>",
  "excludeQueryParameters": "<string>",
  "id": "<string>",
  "internalWebPropertyId": "qui exercitation do tempor",
  "kind": "analytics#profile",
  "name": "<string>",
  "parentLink": {
   "href": "<string>",
   "type": "analytics#webproperty"
  },
  "permissions": {
   "effective": [
    "eiusmod quis et amet",
    "in sunt fugiat"
   ]
  },
  "selfLink": "Ut dolore aliquip",
  "siteSearchCategoryParameters": "<string>",
  "siteSearchQueryParameters": "<string>",
  "starred": "<boolean>",
  "stripSiteSearchCategoryParameters": "<boolean>",
  "stripSiteSearchQueryParameters": "<boolean>",
  "timezone": "<string>",
  "type": "<string>",
  "updated": "1959-05-20T15:12:20.241Z",
  "webPropertyId": "deserunt ea reprehenderit ex",
  "websiteUrl": "<string>"
 },
 "webproperty": {
  "accountId": "<string>",
  "childLink": {
   "href": "<string>",
   "type": "analytics#profiles"
  },
  "created": "1951-01-30T15:46:36.520Z",
  "dataRetentionResetOnNewActivity": "<boolean>",
  "dataRetentionTtl": "<string>",
  "defaultProfileId": "<string>",
  "id": "<string>",
  "industryVertical": "<string>",
  "internalWebPropertyId": "sed ut",
  "kind": "analytics#webproperty",
  "level": "ipsum cupidatat tempor",
  "name": "<string>",
  "parentLink": {
   "href": "<string>",
   "type": "analytics#account"
  },
  "permissions": {
   "effective": [
    "ut dolor",
    "dolore quis qui velit"
   ]
  },
  "profileCount": 55628625,
  "selfLink": "est consectetur ut aute sunt",
  "starred": "<boolean>",
  "updated": "1977-08-21T19:39:41.385Z",
  "websiteUrl": "<string>"
 }
}
```

<br>

### analytics.metadata.columns.list ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
GET {{baseUrl}}/metadata/:reportType/columns?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Response

*Successful response*
```json
{
 "attributeNames": [
  "incididunt nostrud anim",
  "ipsum veniam cillum"
 ],
 "etag": "pariatur tempor Lorem d",
 "items": [
  {
   "attributes": {},
   "id": "adipisicing",
   "kind": "analytics#column"
  },
  {
   "attributes": {},
   "id": "reprehenderit Lorem ut mollit cupidatat",
   "kind": "analytics#column"
  }
 ],
 "kind": "analytics#columns",
 "totalResults": -85376523
}
```

<br>

### analytics.user Deletion.user Deletion Request.upsert ![auth](https://img.shields.io/badge/auth-oauth2-yellow)

---
> Request

```
POST {{baseUrl}}/userDeletion/userDeletionRequests:upsert?alt=<string>&fields=<string>&key=<string>&oauth_token=<string>&prettyPrint=<boolean>&quotaUser=<string>&userIp=<string>
```

> Query parameters

**`alt`**

Data format for the response.

**`fields`**

Selector specifying which fields to include in a partial response.

**`key`**

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**`oauth_token`**

OAuth 2.0 token for the current user.

**`prettyPrint`**

Returns response with indentations and line breaks.

**`quotaUser`**

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**`userIp`**

Deprecated. Please use quotaUser instead.


> Body

```json
{
    "firebaseProjectId": "<string>",
    "id": {
        "type": "<string>",
        "userId": "<string>"
    },
    "kind": "analytics#userDeletionRequest",
    "propertyId": "<string>",
    "webPropertyId": "<string>"
}
```


> Response

*Successful response*
```json
{
 "deletionRequestTime": "1968-06-11T03:31:01.507Z",
 "firebaseProjectId": "<string>",
 "id": {
  "type": "<string>",
  "userId": "<string>"
 },
 "kind": "analytics#userDeletionRequest",
 "propertyId": "<string>",
 "webPropertyId": "<string>"
}
```

<br>

Generated with [Palourde](https://github.com/bagabool/palourde)