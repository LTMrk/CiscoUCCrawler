---
doc_id: developer-cisco-com-site-jabber-guestsdk-documents-guest-server-api-v10-0-2-10-6-8-66af407dcd
source_url: https://developer.cisco.com/site/jabber-guestsdk/documents/guest-server-api/v10_0_2-10_6_8/
retrieved_at: 2026-09-01T17:46:22.802489+00:00
---

This site is no longer being maintained. Latest documents are available at Cisco Jabber Guest . Also, we recommend migrating to the Webex App.

# Cisco Jabber Guest API

The Cisco Jabber Guest API provides methods to create, update, and delete links, as well as to retrieve
                information about individual links. The API can return and receive data in either application/json or
                application/xml. Do this by setting the Accepts header.

The Cisco Jabber Guest API supports basic authentication.

View browser requests on the link pages of Cisco Jabber Guest Administration with a tool such as the
                Network tab in the Chrome developer tools for debugging information. You can also use Firebug or the IE
                debugger.

## First Time Access

The first time that you sign in to Cisco Jabber Guest Administration, you must change your password. If
                you have not yet changed your password through Cisco Jabber Guest Administration, you must change your
                password the first time that you access the API.

To change your password, execute the following command:

curl -i -k https://localhost/cjg-api/rest/login/session -X POST -u admin:jabbercserver -H "Content-Type:
                application/json" -d '{"username":"admin" "password":"jabbercserver",
                "newPassword":"<new password>"}'

## Session Time Out

Your session will time out after 30 minutes of inactivity.

## Event Reference

Returns a list of links and the properties for each link.

Parameters:

- limit—The number of items to limit the list to.

- offset—The offset into the full result list to start this list at.

Examples of limit and offset for paging links:

- Gets the first 10 links (page 1): /cjg-api/rest/links?limit=10&offset=0

- Gets the next 10 links (page 2): /cjg-api/rest/links?limit=10&offset=10

Takes a linkObjectID and returns the object properties for the specified link. For example,
                            GET https://someserver/cjg-api/rest/links/5310fa42e4b0e941e6c99f82, where
                            5310fa42e4b0e941e6c99f82 is the linkObjectID.

Create a new link.

Content-Type: application/json Body: { "isEnabled": true, "requestPath": "AnyValueYouWant", "destination": "johndoe@cisco.com" }

The requestPath value must be unique. You also need to pass in the isEnabled flag or the link
                            will be disabled.

Resulting link: https://[Server]/call/AnyValueYouWant

Success is indicated by a 201 code (CREATED).

The URL of the created object is returned in the Location header. This URL can be used to
                            update or delete the link later.

Update a link. For example, PUT
                            https://someserver/cjg-api/rest/links/5310fa42e4b0e941e6c99f82, where
                            5310fa42e4b0e941e6c99f82 is the linkObjectID.

Content-Type: application/json Body: { "isEnabled": true, "requestPath": "AnyValueYouWant", "destination": "johndoe@cisco.com" }

The requestPath value must be specified and must be unique. We recommend using a UUID/GUID if
                            you need a random requestPath. You must pass in theisEnabled flag or the link will be
                            disabled.

Resulting link: https://[Server]/call/AnyValueYouWant

Search for a link.

Parameters:

- q—Search by text query.

- userObjectId—Search by userObjectId.

You must put %20 (escape character for the space) between the name of the
                            parameter and the value.

If you want to include both parameters, you must put a comma between them.

Examples:

Note Text queries return case-insensitive matches that start with
                                    the specified value.

- Search for the userObjectId 5310fa42e4b0e941e6c99f82: /cjg-api/rest/links?search=userObjectId%20 5310fa42e4b0e941e6c99f82

Delete the specified link. For example, DELETE
                            https://someserver/cjg-api/rest/links/5310fa42e4b0e941e6c99f82, where
                            5310fa42e4b0e941e6c99f82 is the linkObjectID.

# Links Object

The following table describes the properties of the links object.

Example links object:

```
{
   "@total":"47",
   "Links":[
      {
         "linkObjectId":"5331d38ce4b0b2e2ef217487",
         "isEnabled":"true",
         "requestPath":"ec774eb8-06b5-4eb9-bea6-ef4a95db158a",
         "destination":"5555",
         "displayName":"(name not available)",
         "callerName":"jsmith",
         "validBefore":"2014-03-25T19:19:17.200Z",
         "linkPrefix":"https://10.93.173.172/call/",
         "userObjectId":"5310fa42e4b0e941e6c99f82",
         "useUniqueSipAlias":"false"
      },
   ],
   "Paging":{
      "next":"/cjg-api/rest/links?limit=10&offset=10"
   }
}
```

## Rate Limit for Creating, Updating, or Deleting Links

There is no rate limit for creating, updating, or deleting links; however, we recommend one API call per
                second. For example, we recommend creating no more than 60 links in one minute.

| Resource | Description |
|---|---|
| GET https://[IP address]/cjg-api/rest/links/ | Returns a list of links and the properties for each link. Parameters: limit—The number of items to limit the list to. offset—The offset into the full result list to start this list at. Examples of limit and offset for paging links: Gets the first 10 links (page 1): /cjg-api/rest/links?limit=10&offset=0 Gets the next 10 links (page 2): /cjg-api/rest/links?limit=10&offset=10 |
| GET [link URL] | Takes a linkObjectID and returns the object properties for the specified link. For example,
                            GET https://someserver/cjg-api/rest/links/5310fa42e4b0e941e6c99f82, where
                            5310fa42e4b0e941e6c99f82 is the linkObjectID. |
| POST https://[IPaddress]/cjg-api/rest/links/ | Create a new link. Content-Type: application/json Body: { "isEnabled": true, "requestPath": "AnyValueYouWant", "destination": "johndoe@cisco.com" } The requestPath value must be unique. You also need to pass in the isEnabled flag or the link
                            will be disabled. Resulting link: https://[Server]/call/AnyValueYouWant Success is indicated by a 201 code (CREATED). The URL of the created object is returned in the Location header. This URL can be used to
                            update or delete the link later. |
| PUT [link URL] | Update a link. For example, PUT
                            https://someserver/cjg-api/rest/links/5310fa42e4b0e941e6c99f82, where
                            5310fa42e4b0e941e6c99f82 is the linkObjectID. Content-Type: application/json Body: { "isEnabled": true, "requestPath": "AnyValueYouWant", "destination": "johndoe@cisco.com" } The requestPath value must be specified and must be unique. We recommend using a UUID/GUID if
                            you need a random requestPath. You must pass in theisEnabled flag or the link will be
                            disabled. Resulting link: https://[Server]/call/AnyValueYouWant |
| https://[IPaddress]/cjg-api/rest/links?search | Search for a link. Parameters: q—Search by text query. userObjectId—Search by userObjectId. You must put %20 (escape character for the space) between the name of the
                            parameter and the value. If you want to include both parameters, you must put a comma between them. Examples: Search for the text Smith: /cjg-api/rest/links?search=q%20Smith Note Text queries return case-insensitive matches that start with
                                    the specified value. Search for the userObjectId 5310fa42e4b0e941e6c99f82: /cjg-api/rest/links?search=userObjectId%20 5310fa42e4b0e941e6c99f82 |
| DELETE [link URL] | Delete the specified link. For example, DELETE
                            https://someserver/cjg-api/rest/links/5310fa42e4b0e941e6c99f82, where
                            5310fa42e4b0e941e6c99f82 is the linkObjectID. |

| Property | Description | Modifiable |
|---|---|---|
| linkObjectId | Unique identifier for a link. | No |
| isEnabled | The status of the link. This flag must be passed in when creating or updating a link or the link
                        will be disabled. | Yes |
| requestPath | The part of the link after /call. For example,
                        https://[linkPrefix] [requestPath] .
                        Must be unique. | No |
| destination | DN or URI that is called when a user clicks on the link. Destination is required. | Yes |
| displayName | The name displayed on the client when placing a call using this link. Optional. | Yes |
| callerName | The name displayed on the destination endpoint in the enterprise when a call is placed using
                        this link. Optional. | Yes |
| callerAlias | The Caller ID displayed on the destination endpoint in the enterprise when a call is placed
                        using this link. Optional. | Yes |
| validAfter | The date and time when a link becomes active. Default value: If left blank, the link can be used immediately to route calls. Optional. | Yes |
| validBefore | The date and time when a link expires, and can no longer be used to route calls. If left blank, the link never expires. Optional. | Yes |
| linkPrefix | The part of the link before the request path. linkPrefix is the same for all links in a cluster. | No |
| userObjectId | The user responsible for creating the link. Default: If left blank, defaults to the logged-in user. | No |