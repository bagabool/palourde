# Docker HUB API 

<br>

Docker Hub is a service provided by Docker for finding and sharing container images with your team.
It is the world's largest library and community for container images.
In addition to the [Docker Hub UI](https://docs.docker.com/docker-hub/) and [Docker Hub CLI tool](https://github.com/docker/hub-tool#readme) (currently experimental),
Docker provides an API that allows you to interact with Docker Hub.
Browse through the Docker Hub API documentation to explore the supported endpoints.


<br>

## Requests

<br>

### Update a personal access token 

---
> Request

```
PATCH {{baseUrl}}/v2/access-tokens/:uuid
```


> Body

```json
{
    "token_label": "My read only token",
    "is_active": false
}
```


> Responses

*OK*
```json
{
 "uuid": "b30bbf97-506c-4ecd-aabc-842f3cb484fb",
 "client_id": "HUB",
 "creator_ip": "127.0.0.1",
 "creator_ua": "some user agent",
 "created_at": "laboris quis",
 "last_used": null,
 "generated_by": "manual",
 "is_active": true,
 "token": "a7a5ef25-8889-43a0-8cc7-f2a94268e861",
 "token_label": "My read only token",
 "scopes": [
  "repo:read"
 ]
}
```

*Bad Request*
```json
{
 "fields": {},
 "text": "deserunt ipsum"
}
```

*Unauthorized*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

<br>

### Get a personal access token 

---
> Request

```
GET {{baseUrl}}/v2/access-tokens/:uuid
```


> Responses

*OK*
```json
{
 "uuid": "b30bbf97-506c-4ecd-aabc-842f3cb484fb",
 "client_id": "HUB",
 "creator_ip": "127.0.0.1",
 "creator_ua": "some user agent",
 "created_at": "laboris quis",
 "last_used": null,
 "generated_by": "manual",
 "is_active": true,
 "token": "a7a5ef25-8889-43a0-8cc7-f2a94268e861",
 "token_label": "My read only token",
 "scopes": [
  "repo:read"
 ]
}
```

*Unauthorized*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

*Not Found*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

<br>

### Delete a personal access token 

---
> Request

```
DELETE {{baseUrl}}/v2/access-tokens/:uuid
```


> Responses

*A successful response.*: No response specified

*Unauthorized*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

*Not Found*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

<br>

### Create a personal access token 

---
> Request

```
POST {{baseUrl}}/v2/access-tokens
```


> Body

```json
{
    "token_label": "My read only token",
    "scopes": [
        "repo:read"
    ]
}
```


> Responses

*Created*
```json
{
 "uuid": "b30bbf97-506c-4ecd-aabc-842f3cb484fb",
 "client_id": "HUB",
 "creator_ip": "127.0.0.1",
 "creator_ua": "some user agent",
 "created_at": "aliqua ullamco id",
 "last_used": null,
 "generated_by": "manual",
 "is_active": true,
 "token": "a7a5ef25-8889-43a0-8cc7-f2a94268e861",
 "token_label": "My read only token",
 "scopes": [
  "repo:read"
 ]
}
```

*Bad Request*
```json
{
 "fields": {},
 "text": "deserunt ipsum"
}
```

*Unauthorized*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

<br>

### Get a list of personal access tokens 

---
> Request

```
GET {{baseUrl}}/v2/access-tokens?page=1&page_size=10
```

> Query parameters

**`page`**

**`page_size`**


> Responses

*OK*
```json
{
 "count": 1,
 "next": "laborum nisi laboris aute",
 "previous": "dolor culpa id ipsum",
 "active_count": 1,
 "results": [
  {
   "uuid": "b30bbf97-506c-4ecd-aabc-842f3cb484fb",
   "client_id": "HUB",
   "creator_ip": "127.0.0.1",
   "creator_ua": "some user agent",
   "created_at": "Duis minim",
   "last_used": null,
   "generated_by": "manual",
   "is_active": true,
   "token": "a7a5ef25-8889-43a0-8cc7-f2a94268e861",
   "token_label": "My read only token",
   "scopes": [
    "repo:read"
   ]
  },
  {
   "uuid": "b30bbf97-506c-4ecd-aabc-842f3cb484fb",
   "client_id": "HUB",
   "creator_ip": "127.0.0.1",
   "creator_ua": "some user agent",
   "created_at": "aute cupidatat sed non consectetur",
   "last_used": null,
   "generated_by": "manual",
   "is_active": true,
   "token": "a7a5ef25-8889-43a0-8cc7-f2a94268e861",
   "token_label": "My read only token",
   "scopes": [
    "repo:read"
   ]
  }
 ]
}
```

*Bad Request*
```json
{
 "fields": {},
 "text": "deserunt ipsum"
}
```

*Unauthorized*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

<br>

### Get details of repository's images 

---
> Request

```
GET {{baseUrl}}/v2/namespaces/:namespace/repositories/:repository/images?status=active&currently_tagged=false&ordering=-digest&active_from=tempor in sit in&page=97793012&page_size=97793012
```

> Query parameters

**`status`**

Filters to only show images of this status.

**`currently_tagged`**

Filters to only show images with:
* `true`: at least 1 current tag.
* `false`: no current tags.


**`ordering`**

Orders the results by this property.

Prefixing with `-` sorts by descending order.


**`active_from`**

Sets the time from which an image must have been pushed or pulled to be counted as active.

Defaults to 1 month before the current time.


**`page`**

Page number to get. Defaults to 1.

**`page_size`**

Number of images to get per page. Defaults to 10. Max of 100.


> Responses

*Success*
```json
{
 "count": 100,
 "next": "https://hub.docker.com/v2/namespaces/mynamespace/repositories/myrepo/images?&page=4&page_size=20",
 "previous": "https://hub.docker.com/v2/namespaces/mynamespace/repositories/myrepo/images?&page=2&page_size=20",
 "results": [
  {
   "namespace": "mynamespace",
   "repository": "myrepo",
   "digest": "sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr",
   "tags": [
    {
     "tag": "latest",
     "is_current": true
    },
    {
     "tag": "latest",
     "is_current": true
    }
   ],
   "last_pushed": "2021-02-24T22:05:27.526308Z",
   "last_pulled": "2021-02-24T23:16:10.200008Z",
   "status": "active"
  },
  {
   "namespace": "mynamespace",
   "repository": "myrepo",
   "digest": "sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr",
   "tags": [
    {
     "tag": "latest",
     "is_current": true
    },
    {
     "tag": "latest",
     "is_current": true
    }
   ],
   "last_pushed": "2021-02-24T22:05:27.526308Z",
   "last_pulled": "2021-02-24T23:16:10.200008Z",
   "status": "active"
  }
 ]
}
```

*Unauthorized - user does not have read access to the namespace.*
```json
{
 "txnid": "pariatur aliquip",
 "message": "mollit aliquip",
 "errinfo": {
  "api_call_docker_id": "Excepteur aliqua ut ea Ut",
  "api_call_name": "dolore mollit Duis consequat laborum",
  "api_call_start": "labore Excepteur adipisicing commodo",
  "api_call_txnid": "sit in cillum"
 }
}
```

*Forbidden - this API is only available to users on Pro or Team plans.*
```json
{
 "txnid": "pariatur aliquip",
 "message": "mollit aliquip",
 "errinfo": {
  "api_call_docker_id": "Excepteur aliqua ut ea Ut",
  "api_call_name": "dolore mollit Duis consequat laborum",
  "api_call_start": "labore Excepteur adipisicing commodo",
  "api_call_txnid": "sit in cillum"
 }
}
```

<br>

### Get image's tags 

---
> Request

```
GET {{baseUrl}}/v2/namespaces/:namespace/repositories/:repository/images/:digest/tags?page=97793012&page_size=97793012
```

> Query parameters

**`page`**

Page number to get. Defaults to 1.

**`page_size`**

Number of images to get per page. Defaults to 10. Max of 100.


> Responses

*Success*
```json
{
 "count": 100,
 "next": "https://hub.docker.com/v2/namespaces/mynamespace/repositories/myrepo/images/sha256:mydigest/tags?&page=4&page_size=20",
 "previous": "https://hub.docker.com/v2/namespaces/mynamespace/repositories/myrepo/images/sha256:mydigest/tags?&page=2&page_size=20",
 "results": [
  {
   "tag": "latest",
   "is_current": true
  },
  {
   "tag": "latest",
   "is_current": true
  }
 ]
}
```

*Unauthorized - user does not have read access to the namespace*
```json
{
 "txnid": "pariatur aliquip",
 "message": "mollit aliquip",
 "errinfo": {
  "api_call_docker_id": "Excepteur aliqua ut ea Ut",
  "api_call_name": "dolore mollit Duis consequat laborum",
  "api_call_start": "labore Excepteur adipisicing commodo",
  "api_call_txnid": "sit in cillum"
 }
}
```

*Forbidden - this API is only available to users on Pro or Team plans*
```json
{
 "txnid": "pariatur aliquip",
 "message": "mollit aliquip",
 "errinfo": {
  "api_call_docker_id": "Excepteur aliqua ut ea Ut",
  "api_call_name": "dolore mollit Duis consequat laborum",
  "api_call_start": "labore Excepteur adipisicing commodo",
  "api_call_txnid": "sit in cillum"
 }
}
```

<br>

### Get summary of repository's images 

---
> Request

```
GET {{baseUrl}}/v2/namespaces/:namespace/repositories/:repository/images-summary?active_from=tempor in sit in
```

> Query parameters

**`active_from`**

Sets the time from which an image must have been pushed or pulled to be counted as active.

Defaults to 1 month before the current time.



> Responses

*Success*
```json
{
 "active_from": "2021-01-25T14:25:37.076343059Z",
 "statistics": {
  "total": 3,
  "active": 2,
  "inactive": 1
 }
}
```

*Unauthorized - user does not have read access to the namespace*
```json
{
 "txnid": "pariatur aliquip",
 "message": "mollit aliquip",
 "errinfo": {
  "api_call_docker_id": "Excepteur aliqua ut ea Ut",
  "api_call_name": "dolore mollit Duis consequat laborum",
  "api_call_start": "labore Excepteur adipisicing commodo",
  "api_call_txnid": "sit in cillum"
 }
}
```

<br>

### Delete images 

---
> Request

```
POST {{baseUrl}}/v2/namespaces/:namespace/delete-images
```


> Body

```json
{
    "dry_run": false,
    "active_from": "2020-12-01T12:00:00Z",
    "manifests": [
        {
            "repository": "myrepo",
            "digest": "sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr"
        },
        {
            "repository": "myrepo",
            "digest": "sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr"
        }
    ],
    "ignore_warnings": [
        {
            "repository": "myrepo",
            "digest": "sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr",
            "warning": "current_tag",
            "tags": [
                "latest",
                "latest"
            ]
        },
        {
            "repository": "myrepo",
            "digest": "sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr",
            "warning": "current_tag",
            "tags": [
                "latest",
                "latest"
            ]
        }
    ]
}
```


> Responses

*Deletion completed*
```json
{
 "dry_run": false,
 "metrics": {
  "manifest_deletes": 3,
  "manifest_errors": 0,
  "tag_deletes": 1,
  "tag_errors": 0
 }
}
```

*Deletion not possible*
```json
{
 "txnid": "proident cupidatat",
 "message": "pariatur Lorem cupidatat laborum",
 "errinfo": {
  "api_call_docker_id": "aute aliquip incididunt",
  "api_call_name": "magna irure quis id cillum",
  "api_call_start": "fugiat est aute deserunt dolore",
  "api_call_txnid": "non fugiat in anim",
  "type": "validation",
  "details": {
   "errors": [
    {
     "repository": "myrepo",
     "digest": "sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr",
     "error": "not_found"
    },
    {
     "repository": "myrepo",
     "digest": "sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr",
     "error": "not_found"
    }
   ],
   "warnings": [
    {
     "repository": "myrepo",
     "digest": "sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr",
     "warning": "current_tag",
     "tags": [
      "latest",
      "latest"
     ]
    },
    {
     "repository": "myrepo",
     "digest": "sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr",
     "warning": "current_tag",
     "tags": [
      "latest",
      "latest"
     ]
    }
   ]
  }
 }
}
```

*Forbidden - this API is only available to users on Pro or Team plans*
```json
{
 "txnid": "pariatur aliquip",
 "message": "mollit aliquip",
 "errinfo": {
  "api_call_docker_id": "Excepteur aliqua ut ea Ut",
  "api_call_name": "dolore mollit Duis consequat laborum",
  "api_call_start": "labore Excepteur adipisicing commodo",
  "api_call_txnid": "sit in cillum"
 }
}
```

<br>

### Returns list of audit log  events. 

---
> Request

```
GET {{baseUrl}}/v2/auditlogs/:account?action=tempor in sit in&name=tempor in sit in&actor=tempor in sit in&from=1965-07-27T06:51:19.907Z&to=1965-07-27T06:51:19.907Z&page=1&page_size=25
```

> Query parameters

**`action`**

action name one of ["repo.tag.push", ...]. Optional parameter to filter specific audit log actions.

**`name`**

name. Optional parameter to filter audit log events to a specific name. For repository events, this is the name of the repository. For organization events, this is the name of the organization. For team member events, this is the username of the team member.

**`actor`**

actor name. Optional parameter to filter audit log events to the specific user who triggered the event.

**`from`**

Start of the time window you wish to query audit events for.

**`to`**

End of the time window you wish to query audit events for.

**`page`**

page - specify page number. Page number to get.

**`page_size`**

page_size - specify page size. Number of events to return per page.


> Responses

*A successful response.*
```json
{
 "logs": [
  {
   "account": "docker",
   "action": "repo.tag.push",
   "name": "docker/example",
   "actor": "docker",
   "data": {
    "digest": "sha256:c1ae9c435032a276f80220c7d9b40f76266bbe79243d34f9cda30b76fe114dfa",
    "tag": "latest"
   },
   "timestamp": "2021-02-19T01:34:35Z",
   "action_description": "pushed the tag latest with the digest sha256:c1ae9c435032a to the repository docker/example"
  }
 ]
}
```

*Untitled Example*
```json
{
 "detail": "Rate limit exceeded",
 "error": false
}
```

*Untitled Example*
```json
{}
```

*An unexpected error response.*
```json
{
 "code": -37352657,
 "message": "enim aliqua",
 "details": [
  {
   "type_url": "aliqua quis sunt nostrud",
   "value": "ad magna ut Duis"
  },
  {
   "type_url": "in magna ea tempor cillum",
   "value": "Lorem"
  }
 ]
}
```

<br>

### Returns list of audit log actions. 

---
> Request

```
GET {{baseUrl}}/v2/auditlogs/:account/actions
```


> Responses

*A successful response.*
```json
{
 "actions": {
  "org": {
   "actions": [
    {
     "name": "team.create",
     "description": "contains team create events",
     "label": "Team Created"
    },
    {
     "name": "team.delete",
     "description": "contains team delete events",
     "label": "Team Deleted"
    },
    {
     "name": "team.member.add",
     "description": "contains team member add events",
     "label": "Team Member Added"
    },
    {
     "name": "team.member.remove",
     "description": "contains team member remove events",
     "label": "Team Member Removed"
    },
    {
     "name": "team.member.invite",
     "description": "contains team member invite events",
     "label": "Team Member Invited"
    },
    {
     "name": "member.removed",
     "description": "contains org member remove events",
     "label": "Organization Member Removed"
    },
    {
     "name": "create",
     "description": "contains organization create events",
     "label": "Organization Created"
    }
   ],
   "label": "Organization"
  },
  "repo": {
   "actions": [
    {
     "name": "create",
     "description": "contains repository create events",
     "label": "Repository Created"
    },
    {
     "name": "delete",
     "description": "contains repository delete events",
     "label": "Repository Deleted"
    },
    {
     "name": "change_privacy",
     "description": "contains repository privacy change events",
     "label": "Privacy Changed"
    },
    {
     "name": "tag.push",
     "description": "contains image tag push events",
     "label": "Tag Pushed"
    },
    {
     "name": "tag.delete",
     "description": "contains image tag delete events",
     "label": "Tag Deleted"
    }
   ],
   "label": "Repository"
  }
 }
}
```

*Untitled Example*
```json
{
 "detail": "Rate limit exceeded",
 "error": false
}
```

*Untitled Example*
```json
{}
```

*An unexpected error response.*
```json
{
 "code": 43996722,
 "message": "magna exercitation",
 "details": [
  {
   "type_url": "enim Duis voluptate quis dolor",
   "value": "cillum laborum quis id"
  },
  {
   "type_url": "ea Duis cillum mollit",
   "value": "eiusmod do esse nisi"
  }
 ]
}
```

<br>

### Get organization settings 

---
> Request

```
GET {{baseUrl}}/v2/orgs/:name/settings
```


> Responses

*OK*
```json
{
 "restricted_images": {
  "enabled": true,
  "allow_official_images": true,
  "allow_verified_publishers": true
 }
}
```

*Unauthorized*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

*Forbidden*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

*Not Found*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

<br>

### Update organization settings 

---
> Request

```
PUT {{baseUrl}}/v2/orgs/:name/settings
```


> Body

```json
{
    "restricted_images": {
        "enabled": true,
        "allow_official_images": true,
        "allow_verified_publishers": true
    }
}
```


> Responses

*OK*
```json
{
 "restricted_images": {
  "enabled": true,
  "allow_official_images": true,
  "allow_verified_publishers": true
 }
}
```

*Unauthorized*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

*Forbidden*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

*Not Found*
```json
{
 "detail": "quis ipsum",
 "message": "ex culpa aliquip enim"
}
```

<br>

### Create an authentication token 

---
> Request

```
POST {{baseUrl}}/v2/users/login
```


> Body

```json
{
    "username": "myusername",
    "password": "hunter2"
}
```


> Responses

*Authentication successful*
```json
{
 "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

*Authentication failed*
```json
{
 "details": "Incorrect authentication credentials"
}
```

<br>

Generated with [Palourde](https://github.com/bagabool/palourde)