---
doc_id: webex-meeting-post-meetings-meetingid-invitationsources
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: POST
path: /meetings/{meetingId}/invitationSources
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.399288+00:00
---

# POST /meetings/{meetingId}/invitationSources

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `createInvitationSources`

## Resumen
Create Invitation Sources

## Descripción
Creates one or more invitation sources for a meeting.

## Parámetros
- `meetingId` [path] (string) **(requerido)**: Unique identifier for the meeting. Only the meeting ID of a scheduled webinar is supported for this API.

## Cuerpo de la petición (application/json)
- `hostEmail` (string): Email address for the meeting host. This parameter is only used if a user or application calling the API has the admin-level scopes. The admin may specify the email of a user on a site they manage and the API will return meeting participants of the meetings that are hosted by that user.
- `personId` (string): Unique identifier for the meeting host. Should only be set if the user or application calling the API has the admin-level scopes. When used, the admin may specify the email of a user in a site they manage to be the meeting host.
- `items` (array):
  - `sourceId` (string) **(requerido)**: Source ID for the invitation.
  - `sourceEmail` (string) **(requerido)**: Email for invitation source.

### Ejemplo de petición
```json
{
  "hostEmail": "john.andersen@example.com",
  "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xYTY5MmE2Mi00MTNmLTRjYWEtYjdkOS0wYzg0ZDZmMDdlNzY",
  "items": [
    {
      "sourceId": "cisco",
      "sourceEmail": "john001@example.com"
    },
    {
      "sourceId": "webex",
      "sourceEmail": "john002@example.com"
    }
  ]
}
```

## Respuestas
- **200**: OK
  - `items` (array): Invitation source array.
    - `id` (string) **(requerido)**: Unique identifier for invitation source.
    - `sourceId` (string) **(requerido)**: Source ID for invitation.
    - `sourceEmail` (string) **(requerido)**: Email for invitation source.
    - `joinLink` (string): The link bound to `sourceId` can directly join the meeting. If the meeting requires registration,`joinLink` is not returned.
    - `registerLink` (string): The link bound to `sourceId` can directly register the meeting. If the meeting requires registration, `registerLink` is returned.
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
