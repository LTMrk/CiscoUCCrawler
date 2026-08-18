---
doc_id: webex-meeting-get-meetings-meetingid-invitationsources
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetings/{meetingId}/invitationSources
operation_id: listInvitationSources
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.490483+00:00
---

# GET /meetings/{meetingId}/invitationSources

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `listInvitationSources`

## Resumen
List Invitation Sources

## Descripción
Lists invitation sources for a meeting.

#### Request Header

* `hostEmail`: Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin on-behalf-of scopes. If set, the admin may specify the email of a user in a site they manage and the API will return recording details of that user.

* `personId`:  Unique identifier for the meeting host. This attribute should only be set if the user or application calling the API has the admin-level scopes. When used, the admin may specify the email of a user in a site they manage to be the meeting host.

## Parámetros
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting. Only the meeting ID of a scheduled webinar is supported for this API.
- `hostEmail` [header] (string): e.g. john.andersen@example.com
- `personId` [header] (string): e.g. Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNWJiZjgzMS01YmU5LTRjMjUtYjRiMC05YjU5MmM4YTA4NmI

## Ejemplo de invocación
```bash
curl -X GET '/meetings/<meetingId>/invitationSources' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): Invitation source array.
  - `id` (string) (**requerido**): Unique identifier for invitation source.
  - `sourceId` (string) (**requerido**): Source ID for invitation.
  - `sourceEmail` (string) (**requerido**): Email for invitation source.
  - `joinLink` (string): The link bound to `sourceId` can directly join the meeting. If the meeting requires registration,`joinLink` is not returned.
  - `registerLink` (string): The link bound to `sourceId` can directly register the meeting. If the meeting requires registration, `registerLink` is returned.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "1",
      "sourceId": "cisco",
      "joinLink": "https://example.webex.com/example/j.php?MTID=m6d75f1c875b3e3c5d18c7598036bdd8b",
      "registerLink": "https://example.webex.com/example/j.php?RGID=rb05b31307b5b820e16594da9d1cfc5c7",
      "sourceEmail": "john001@example.com"
    },
    {
      "id": "2",
      "sourceId": "webex",
      "joinLink": "https://example.webex.com/example/j.php?MTID=m6d75f1c875b3e3c5d18c7598036bdd8b",
      "registerLink": "https://example.webex.com/example/j.php?RGID=rb05b31307b5b820e16594da9d1cfc588",
      "sourceEmail": "john002@example.com"
    }
  ]
}
```

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
The Webex Meetings APIs enable developers to schedule, manage, and retrieve information about Webex meetings, webinars, and events. They provide endpoints for meeting creation, participant management, recordings, transcripts, in-meeting features such as chat and closed captions, and post-meeting analytics. Common use cases include integrating meeting scheduling into calendar apps, automating follow-ups with recordings and transcripts, embedding meeting controls in custom portals, and extracting insights for compliance or productivity analysis. The APIs support both real-time and asynchronous w...

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs