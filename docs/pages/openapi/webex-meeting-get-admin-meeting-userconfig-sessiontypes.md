---
doc_id: webex-meeting-get-admin-meeting-userconfig-sessiontypes
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /admin/meeting/userconfig/sessionTypes
operation_id: List User Session Type
tags: Session Types
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.473015+00:00
---

# GET /admin/meeting/userconfig/sessionTypes

**API:** Webex Meetings
**Área:** Session Types
**operationId:** `List User Session Type`

## Resumen
List User Session Type

## Descripción
List session types for a specific user.

## Parámetros
- `siteUrl` [query] (string): URL of the Webex site to query.
- `personId` [query] (string): A unique identifier for the user.
- `email` [header] (string): e.g. `john.andersen@example.com` (string, optional) - The email of the user.

## Ejemplo de invocación
```bash
curl -X GET '/admin/meeting/userconfig/sessionTypes' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of the user's session types.
  - `personId` (string): A unique identifier for the user.
  - `email` (string): The email of the user.
  - `siteUrl` (string): Site URL for the user.
  - `sessionTypes` (array): All session types are supported by the user on the site.
    - `id` (string): The ID of the session type.
    - `shortName` (string): The short name of the session type.
    - `name` (string): The name of the session type.
    - `type` (string): The meeting type of meeting that you can create with the session type.  * `meeting` - Meeting Center.  * `webinar` - Webinar meeting.  * `privateMeeting` - Private meeting.  * `EventCenter` - Event Center.  * `SupportCenter` - Support Center.  * `TrainCenter` - Training Center. Valores: meeting, webinar, privateMeeting, EventCenter, SupportCenter, TrainCenter.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNWJiZjgzMS01YmU5LTRjMjUtYjRiMC05YjU5MmM4YTA4NmI",
      "email": "john.andersen@example.com",
      "siteUrl": "example.webex.com",
      "sessionTypes": [
        {
          "id": "3",
          "shortName": "PRO",
          "name": "Pro meeting",
          "type": "meeting"
        },
        {
          "id": "9",
          "shortName": "ONS",
          "name": "Online Event",
          "type": "EventCenter"
        }
      ]
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