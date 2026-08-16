---
doc_id: webex-messaging-put-rooms-roomid
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: PUT
path: /rooms/{roomId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.515161+00:00
---

# PUT /rooms/{roomId}

**API:** Webex Messaging
**Área:** Rooms
**operationId:** `Update a Room`

## Resumen
Update a Room

## Descripción
Updates details for a room, by ID.

Specify the room ID in the `roomId` parameter in the URI.
A space can only be put into announcement mode when it is locked.
Any space participant or compliance officer can convert a space from public to private. Only a compliance officer can convert a space from private to public and only if the space is classified with the lowest category (usually `public`), and the space has a description.
To remove a `description` please use a space character ` ` by itself.

<div><Callout type="info">When using this method for moving a space under a team, ensure that all moderators in the space are also team members. If a moderator is not part of the team, demote or remove them as a moderator. Alternatively, add the non-team moderators to the team. This ensures compliance with the requirement that all space moderators must be team members for successful operation execution.
</Callout></div>

<div><Callout type="info">A Compliance Officer who is not a member of a space can only update the `classificationId`, `isAnnouncementOnly`, `description`, and `isPublic` fields.
</Callout></div>

## Parámetros
- `roomId` [path] (string) **(requerido)**: The unique identifier for the room.

## Cuerpo de la petición (application/json)
- `title` (string) **(requerido)**: A user-friendly name for the room.
- `classificationId` (string): The classificationId for the room.
- `teamId` (string): The teamId to which this space should be assigned. Only unowned spaces can be assigned to a team. Assignment between teams is unsupported.
- `isLocked` (boolean): Set the space as locked/moderated and the creator becomes a moderator
- `isPublic` (boolean): The room is public and therefore discoverable within the org. Anyone can find and join that room. When `true` the `description` must be filled in.
- `description` (string): The description of the space.
- `isAnnouncementOnly` (boolean): Sets the space into Announcement Mode or clears the Anouncement Mode (`false`)
- `isReadOnly` (boolean): A compliance officer can set a direct room as read-only, which will disallow any new information exchanges in this space, while maintaing historical data.

### Ejemplo de petición
```json
{
  "title": "Project Unicorn - Sprint 0",
  "classificationId": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
  "teamId": "Y2lzY29zcGFyazovL3VzL1RFQU0vZWUwMWIxMzAtMjJlYi0xMWVjLTg5MTktMGY0NjdjMGNlZmFk",
  "isLocked": false,
  "isPublic": false,
  "description": "Company Announcements",
  "isAnnouncementOnly": false,
  "isReadOnly": false
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
