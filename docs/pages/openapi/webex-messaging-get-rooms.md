---
doc_id: webex-messaging-get-rooms
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: GET
path: /rooms
operation_id: List Rooms
tags: Rooms
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.812163+00:00
---

# GET /rooms

**API:** Webex Messaging
**Área:** Rooms
**operationId:** `List Rooms`

## Resumen
List Rooms

## Descripción
List rooms to which the authenticated user belongs to.

The `title` of the room for 1:1 rooms will be the display name of the other person. Please use the [memberships API](https://developer.webex.com/docs/api/v1/memberships) to list the people in the space.

Long result sets will be split into [pages](/docs/basics#pagination).

Known Limitations:
The underlying database does not support natural sorting by `lastactivity` and will only sort on limited set of results, which are pulled from the database in order of `roomId`. For users or bots in more than 3000 spaces this can result in anomalies such as spaces that have had recent activity not being returned in the results when sorting by `lastacivity`.

## Parámetros
- `teamId` [query] (string): List rooms associated with a team, by ID. Cannot be set in combination with `orgPublicSpaces`.
- `type` [query] (string): List rooms by type. Cannot be set in combination with `orgPublicSpaces`. Valores: direct, group.
- `orgPublicSpaces` [query] (boolean): Shows the org's public spaces joined and unjoined. When set the result list is sorted by the `madePublic` timestamp.
- `from` [query] (string): Filters rooms, that were made public after this time. See `madePublic` timestamp
- `to` [query] (string): Filters rooms, that were made public before this time. See `maePublic` timestamp
- `sortBy` [query] (string): Sort results. Cannot be set in combination with `orgPublicSpaces`. Valores: id, lastactivity, created.
- `max` [query] (number): Limit the maximum number of rooms in the response. Value must be between 1 and 1000, inclusive. Por defecto: 100.

## Ejemplo de invocación
```bash
curl -X GET '/rooms' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):
  - `id` (string): A unique identifier for the room.
  - `title` (string): A user-friendly name for the room.
  - `type` (string): The room type.  * `direct` - 1:1 room.  * `group` - Group room. Valores: direct, group.
  - `isLocked` (boolean): Whether the room is moderated (locked) or not.
  - `teamId` (string): The ID for the team with which this room is associated.
  - `lastActivity` (string): The date and time of the room's last activity.
  - `creatorId` (string): The ID of the person who created this room.
  - `created` (string): The date and time the room was created.
  - `ownerId` (string): The ID of the organization which owns this room. See [Webex Data](/docs/api/guides/compliance#webex-teams-data) in the [Compliance Guide](/docs/api/guides/compliance) for more information.
  - `classificationId` (string): Space classification ID represents the space's current classification.  It can be attached during space creation time, and can be modified at the request of an authorized user.
  - `isAnnouncementOnly` (boolean): Indicates when a space is in Announcement Mode where only moderators can post messages
  - `isReadOnly` (boolean): A compliance officer can set a direct room as read-only, which will disallow any new information exchanges in this space, while maintaing historical data.
  - `isPublic` (boolean): The room is public and therefore discoverable within the org. Anyone can find and join that room.
  - `madePublic` (string): Date and time when the room was made public.
  - `description` (string): The description of the space.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "title": "Project Unicorn - Sprint 0",
      "type": "group",
      "isLocked": true,
      "teamId": "Y2lzY29zcGFyazovL3VzL1JPT00vNjRlNDVhZTAtYzQ2Yi0xMWU1LTlkZjktMGQ0MWUzNDIxOTcz",
      "lastActivity": "2016-04-21T19:12:48.920Z",
      "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
      "created": "2016-04-21T19:01:55.966Z",
      "ownerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
      "classificationId": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
      "isAnnouncementOnly": false,
      "isReadOnly": false,
      "isPublic": true,
      "madePublic": "2022-10-10T17:24:19.388Z",
      "description": "Company Announcements"
    }
  ]
}
```
- Cabecera `Link`: 

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Messaging APIs offer robust programmatic access to messaging features within Webex, including sending and receiving messages, managing spaces, memberships, attachments, and moderating content. These APIs enable integration with bots, workflow automation, notification systems, and custom messaging solutions to enhance team collaboration and productivity. Use cases include building chatbots, integrating with ticketing or alerting platforms, automating onboarding flows, and creating custom collaboration experiences tailored to business needs.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs