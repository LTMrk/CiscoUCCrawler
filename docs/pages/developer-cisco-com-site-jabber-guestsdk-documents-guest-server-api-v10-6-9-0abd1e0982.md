---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-guest-server-api-v10-6-9-0abd1e0982
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/guest-server-api/v10_6_9/
retrieved_at: 2026-09-01T17:46:18.610004+00:00
---

About this Document

Title: Cisco Jabber Guest API

Version: V10.6.9

Publisher: DevNet, Cisco's Developer Program

Publisher Address: Cisco Systems, Inc., 150 W Tasman Dr, San Jose, CA 95134, USA

Comments: DevNet Slate is based upon the open source project called Slate

Published Date: January 08, 2016

# Introduction

The Cisco Jabber Guest API provides methods to create, read, update, and delete Jabber Guest links.  Links map administrator defined Jabber Guest URLs (for example, https://jabberguest/call/tech_support) to directory number or SIP URI destinations.

API requests and responses can use either application/json or application/xml formatted data. Do this by using the HTTP Content-Type (requests) and Accepts (response) headers.

The Cisco Jabber Guest API supports HTTP Basic authentication , using the username and password of a Jabber Guest application user with API access permissions.

# First Time Access

```
> curl -i -k https:// { jabberguest } /cjg-api/rest/login/session -X POST -H "Content-Type: application/json" -u admin:jabbercserver -d '{"username":"admin", "password":"jabbercserver", "newPassword":"my new password"}'
```

The first time that the administrator signs in to the Cisco Jabber Guest Administration web pages, the default password must be changed. If you have not yet changed the default password through Cisco Jabber Guest Administration, the API can be used to do so.  Execute the command on the right (which uses the cURL web request tool).

# Session Time Out

Applications may use HTTP 1.1 persistent connections for efficient pipe-lining of multiple requests. The Jabber Guest API server will maintain a session for up to 30 minutes of inactivity.

# API Reference

API Base REST URI

All Jabber Guest API requests are based on the REST API design pattern, using URL endpoints based on the URL below:

https://{jabberguest}/cjg-api/rest/

## Managing Links

### List Links

#### Request

Resource

GET /cjg-api/rest/links

Example requesting the first 10 links

```
/cjg-api/rest/links?limit=10&offset=0
```

Example requesting the next 10 links

```
/cjg-api/rest/links?limit=10&offset=10
```

Returns a list of links and the properties for each link.

#### Response

Status-Code: 200 OK

Example list links response (partial)

```
{ "@total" : "47" , "Links" :[ { "linkObjectId" : "5331d38ce4b0b2e2ef217487" , "isEnabled" : "true" , "requestPath" : "ec774eb8-06b5-4eb9-bea6-ef4a95db158a" , "destination" : "5555" , "displayName" : "(name not available)" , "callerName" : "jsmith" , "validBefore" : "2014-03-25T19:19:17.200Z" , "linkPrefix" : "https://10.93.173.172/call/" , "userObjectId" : "5310fa42e4b0e941e6c99f82" , "useUniqueSipAlias" : "false" }, ... ], "Paging" :{ "next" : "/cjg-api/rest/links?limit=10&offset=10" } }
```

Content-Type: application/json response body:

### Search Links

#### Request

Resource

Example link search request by text query

```
GET https://{jabberguest}/cjg-api/rest/links?search=q%20smith
```

Example link search request by objectUserId

```
GET https://{jabberguest}/cjg-api/rest/links?search=objectUserId%205310fa42e4b0e941e6c99f82
```

GET /cjg-api/rest/links?search

Search for a link by text or object user ID.  You must put ‘%20’ (URL escape character for the space) between the search type parameter and the value.  If you want to include both parameters, you must put a comma between them.  Note, limit and offset parameters are also accepted for this request (see List Links ).

#### Response

Status-Code: 200 OK

Example list links response (partial)

```
{ "@total" : "47" , "Links" :[ { "linkObjectId" : "5331d38ce4b0b2e2ef217487" , "isEnabled" : "true" , "requestPath" : "ec774eb8-06b5-4eb9-bea6-ef4a95db158a" , "destination" : "5555" , "displayName" : "(name not available)" , "callerName" : "jsmith" , "validBefore" : "2014-03-25T19:19:17.200Z" , "linkPrefix" : "https://10.93.173.172/call/" , "userObjectId" : "5310fa42e4b0e941e6c99f82" , "useUniqueSipAlias" : "false" }, ... ] }
```

Content-Type: application/json response body:

### Get link

#### Request

Resource

Example link retrieve request

```
GET https://{jabberguest}/cjg-api/rest/links/5310fa42e4b0e941e6c99f82
```

GET /cjg-api/rest/links/{link_object_id}

Takes a link object ID and returns the properties for the specified link.

#### Response

Example link retrieve response body

```
{ "linkObjectId" : "5331d38ce4b0b2e2ef217487" , "isEnabled" : "true" , "requestPath" : "ec774eb8-06b5-4eb9-bea6-ef4a95db158a" , "destination" : "5555" , "displayName" : "(name not available)" , "callerName" : "jsmith" , "validBefore" : "2014-03-25T19:19:17.200Z" , "linkPrefix" : "https://10.93.173.172/call/" , "userObjectId" : "5310fa42e4b0e941e6c99f82" , "useUniqueSipAlias" : "false" }
```

Status-Code: 200 OK

Content-Type: application/json response body is a link object

### Create Link

#### Request

Resource

Example create link request

```
POST https://{jabberguest}/cjg-api/rest/links HTTP / 1.1 {
 "isEnabled":"true",
 "requestPath":"tech_support",
 "destination":"5555",
 "displayName":"(name not available)",
 "callerName":"jsmith",
 "validBefore":"2015-03-25T19:19:17.200Z",
 "linkPrefix":"https://jabberguest/call/",
 "useUniqueSipAlias":"false"
}
```

POST /cjg-api/rest/links

Create a new link, where the request body is a link object .  The link object requestPath value must be unique, for example a random UUID/GUID.  You also need to pass in the isEnabled flag or the link will be disabled when added.

#### Response

Status-Code: 201 created

No response body is returned.  The URL of the created object is returned in the HTTP Location header. This URL can be used to update or delete the link later.

### Update a link

Resource

Example link update request

```
PUT https://{jabberguest}}/cjg-api/rest/links/5310fa42e4b0e941e6c99f82

{
 "isEnabled":"true",
 "requestPath":"tech_support",
 "destination":"5555",
 "displayName":"(name not available)",
 "callerName":"jdoe",
 "validBefore":"2015-03-25T19:19:17.200Z",
 "linkPrefix":"https://jabberguest/call/",
 "useUniqueSipAlias":"false"
}
```

PUT /cjg-api/rest/links/{link_object_id}

Update a link, where the request body is a link object which replaces the specified link.  The link object requestPath value must be unique, for example a random UUID/GUID.  You also need to pass in the isEnabled flag or the link will be disabled when added.

#### Response

Status-Code: 204 No Content

No response body is returned.

### Remove a link

Resource

Example link remove request

```
DELETE https://{jabberguest}/cjg-api/rest/links/5310fa42e4b0e941e6c99f82
```

DELETE /cjg-api/rest/links/{link_object_id}

Delete the specified link.

#### Response

Status-Code: 204 No Content

No response body is returned.

## Links Object

Example link object

```
{ "linkObjectId" : "5331d38ce4b0b2e2ef217487" , "isEnabled" : "true" , "requestPath" : "ec774eb8-06b5-4eb9-bea6-ef4a95db158a" , "destination" : "5555" , "displayName" : "(name not available)" , "callerName" : "jsmith" , "validBefore" : "2014-03-25T19:19:17.200Z" , "linkPrefix" : "https://10.93.173.172/call/" , "userObjectId" : "5310fa42e4b0e941e6c99f82" , "useUniqueSipAlias" : "false" , "autoCallAfterSecs" : "-1" , "videoPolicy" : "sendrecv" }
```

The following table describes the properties of the links object.

- sendrecv: send and receive, can start/stop sending during call (default)

- inactive: can not send or receive throughout call

- recvonly: receive only, cannot start sending during call

- recvonlyinitially: receive only initially, can start/stop sending during call

# Rate Limit for Creating, Updating, or Deleting Links

There is no rate limit for creating, updating, or deleting links; however, one API call per second is recommended. For example, creating no more than 60 links in one minute is recommended.

| Parameter | Description |
|---|---|
| limit | The number of items that is the list limit |
| offset | The offset into the full result list where this list starts |

| Element | Description |
|---|---|
| @total | Total number of links available |
| Links | An array of link objects |
| Paging | A URI representing the next ‘page’ of results, based on the limit and offset parameters of the GET request |

| Parameter | Description |
|---|---|
| q | Search by text query |
| userObjectId | Search by user object ID |

| Element | Description |
|---|---|
| @total | Total number of links available |
| Links | An array of link objects |

| Property | Description | Modifiable |
|---|---|---|
| linkObjectId | Unique identifier for a link. | No |
| isEnabled | The status of the link. This flag must be passed in when creating or updating a link or the link will default to disabled. | Yes |
| requestPath | The part of the link after /call. For example, https://[linkPrefix]/ [requestPath] .  Must be unique. | No |
| destination | DN or SIP URI that is called when a user clicks on the link. Destination is required. | Yes |
| displayName | The name displayed on the client when placing a call using this link. Optional. | Yes |
| callerName | The name displayed on the destination endpoint in the enterprise when a call is placed using this link. Optional. | Yes |
| callerAlias | The Caller ID displayed on the destination endpoint in the enterprise when a call is placed using this link. Optional. | Yes |
| validAfter | The date and time when a link becomes active. Default value: If left blank, the link can be used immediately to route calls. Optional. | Yes |
| validBefore | The date and time when a link expires, and can no longer be used to route calls. If left blank, the link never expires. Optional. | Yes |
| linkPrefix | The part of the link before the request path. linkPrefix is the same for all links in a cluster. | No |
| userObjectId | The user responsible for creating the link. Default: If left blank, defaults to the API authenticated user. | No |
| autoCallAfterSecs | Timer (in seconds) to automatically start a guest call. The value range is [-1,60], as an integer. The default value of -1  means not to start a call automatically. A value of 0 means start an immediate call automatically. | Yes |
| videoPolicy | Guest video policy which can be set as four options: sendrecv: send and receive, can start/stop sending during call (default) inactive: can not send or receive throughout call recvonly: receive only, cannot start sending during call recvonlyinitially: receive only initially, can start/stop sending during call | Yes |