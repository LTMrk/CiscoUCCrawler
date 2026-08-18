---
doc_id: webex-meeting-post-recordings-restore
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: POST
path: /recordings/restore
operation_id: bulkRestoreRecordings
tags: Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.498108+00:00
---

# POST /recordings/restore

**API:** Webex Meetings
**Área:** Recordings
**operationId:** `bulkRestoreRecordings`

## Resumen
Restore Recordings from Recycle Bin

## Descripción
Restore all or some recordings from the recycle bin. Only recordings of meetings hosted by the authenticated user can be restored from recycle bin.

* If `restoreAll` is `true`, `recordingIds` should be empty.

* If `restoreAll` is `false`, `recordingIds` should not be empty and its maximum size is `100`.

* All the IDs of `recordingIds` should belong to the site of `siteUrl` or the user's preferred site if `siteUrl` is not specified.

## Parámetros
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the required [admin-level meeting scopes](/docs/meetings#adminorganization-level-authentication-and-scopes). If set, the admin may specify the email of a user in a site they manage and the API will restore recordings of that user.

## Cuerpo de la petición (application/json)
- `restoreAll` (boolean): If not specified or `false`, restores the recordings specified by `recordingIds`. If `true`, restores all recordings from the recycle bin.
- `recordingIds` (array): Recording IDs for recovering recordings from the recycle bin in batch. Note that all the recording IDs should belong to the site of `siteUrl` or the user's preferred site if `siteUrl` is not specified.
- `siteUrl` (string): URL of the Webex site from which the API restores recordings. If not specified, the API restores recordings from a user's preferred site. All available Webex sites and preferred sites of a user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

### Ejemplo — petición
```json
{
  "restoreAll": false,
  "recordingIds": [
    "4f914b1dfe3c4d11a61730f18c0f5387"
  ],
  "siteUrl": "example.webex.com"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/recordings/restore' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: No Content

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