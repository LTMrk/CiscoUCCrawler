---
doc_id: webex-messaging-post-rooms
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: POST
path: /rooms
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.514940+00:00
---

# POST /rooms

**API:** Webex Messaging
**Área:** Rooms
**operationId:** `Create a Room`

## Resumen
Create a Room

## Descripción
Creates a room. The authenticated user is automatically added as a member of the room. See the [Memberships API](/docs/api/v1/memberships) to learn how to add more people to the room.

To create a 1:1 room, use the [Create Messages](/docs/api/v1/messages/create-a-message) endpoint to send a message directly to another person by using the `toPersonId` or `toPersonEmail` parameters.

Bots are not able to create and simultaneously classify a room. A bot may update a space classification after a person of the same owning organization joined the space as the first human user.
A space can only be put into announcement mode when it is locked.

## Cuerpo de la petición (application/json)
- `title` (string) **(requerido)**: A user-friendly name for the room.
- `teamId` (string): The ID for the team with which this room is associated.
- `classificationId` (string): The `classificationId` for the room.
- `isLocked` (boolean): Set the space as locked/moderated and the creator becomes a moderator
- `isPublic` (boolean): The room is public and therefore discoverable within the org. Anyone can find and join that room. When `true` the `description` must be filled in.
- `description` (string): The description of the space.
- `isAnnouncementOnly` (boolean): Sets the space into announcement Mode.

### Ejemplo de petición
```json
{
  "title": "Project Unicorn - Sprint 0",
  "teamId": "Y2lzY29zcGFyazovL3VzL1JPT00vNjRlNDVhZTAtYzQ2Yi0xMWU1LTlkZjktMGQ0MWUzNDIxOTcz",
  "classificationId": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
  "isLocked": false,
  "isPublic": false,
  "description": "Company Announcements",
  "isAnnouncementOnly": false
}
```

## Respuestas
- **200**: OK
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
