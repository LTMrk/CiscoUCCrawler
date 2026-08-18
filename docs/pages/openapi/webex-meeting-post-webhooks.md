---
doc_id: webex-meeting-post-webhooks
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: POST
path: /webhooks
operation_id: Create a Webhook
tags: Webhooks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.509732+00:00
---

# POST /webhooks

**API:** Webex Meetings
**Área:** Webhooks
**operationId:** `Create a Webhook`

## Resumen
Create a Webhook

## Descripción
Creates a webhook.

To learn more about how to create and use webhooks, see The [Webhooks Guide](/docs/api/guides/webhooks).

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): A user-friendly name for the webhook.
- `targetUrl` (string) (**requerido**): URL that receives POST requests for each event.
- `resource` (string) (**requerido**): Resource type for the webhook. Creating a webhook requires 'read' scope on the resource the webhook is for.  * `attachmentActions` - [Attachment Actions](/docs/api/v1/attachment-actions) resource.  * `dataSources` - [data sources](/docs/api/v1/data-sources) resource.  * `memberships` - [Memberships](/docs/api/v1/memberships) resource.  * `messages` - [Messages](/docs/api/v1/messages) resource.  * `rooms` - [Rooms](/docs/api/v1/rooms) resource.  * `meetings` - [Meetings](/docs/api/v1/meetings) resource.  * `recordings` - [Recordings](/docs/api/v1/recordings) resource.  * `convergedRecordings` - [CallRecordings](/docs/api/v1/converged-recordings) resource.  * `meetingParticipants` - [Meeting Participants](/docs/api/v1/meeting-participants) resource.  * `meetingTranscripts` - [Meeting Transcripts](/docs/api/v1/meeting-transcripts) resource.  * `telephony_calls` - [Webex Calling](/docs/webex-calling-overview) call resources.  * `telephony_conference` - [Webex Calling](/docs/webex-calling-overview) conference controls resource.  * `telephony_mwi` - [Webex Calling](/docs/webex-calling-overview) voicemail message waiting indicator resource.  * `uc_counters` - Performance counter for a dedicated instance.  * `serviceApp` - Service App authorization notification.  * `adminBatchJobs` - Admin Batch Jobs notification. Valores: attachmentActions, dataSources, memberships, messages, rooms, meetings, recordings, convergedRecordings, meetingParticipants, meetingTranscripts, telephony_calls, telephony_conference, telephony_mwi, uc_counters, serviceApp.
- `event` (string) (**requerido**): Event type for the webhook.  * `created` - An object is created.  * `updated` - An object is updated.  * `deleted` - An object is deleted.  * `started` - A meeting is started.  * `ended` - A meeting is ended.  * `joined` - A participant joined.  * `left` - A participant left.  * `migrated` - A room was migrated to a different geography. The roomId has changed.  * `authorized` - A Service App was authorized.  * `deauthorized` - A Service App was deauthorized.  * `statusChanged` - Status of admin batch job was changed. Valores: created, updated, deleted, started, ended, joined, left, migrated, authorized, deauthorized, statusChanged.
- `filter` (string): Filter that defines the webhook scope. See [Filtering Webhooks](/docs/api/guides/webhooks#filtering-webhooks) for more information. Please note that if a filter of `hostEmail`, `hostUserId`, `ownerEmail` or `ownerId` is specified, `ownedBy` must be set to `org`.
- `secret` (string): Secret used to generate payload signature.
- `ownedBy` (string): Specify `org` when creating an org/admin level webhook. Supported for `meetings`, `recordings`, `convergedRecordings`,`meetingParticipants`, `meetingTranscripts`, `videoMeshAlerts`, `controlHubAlerts`, `rooms`, `messaging` and `adminBatchJobs` (for Compliance Officers and messages with file attachments only - see [inline file DLP](/docs/api/guides/webex-real-time-file-dlp-basics)) resources.

### Ejemplo — petición
```json
{
  "name": "My Awesome Webhook",
  "targetUrl": "https://example.com/mywebhook",
  "resource": "messages",
  "event": "created",
  "filter": "roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
  "secret": "86dacc007724d8ea666f88fc77d918dad9537a15",
  "ownedBy": "org"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/webhooks' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "targetUrl": "<targetUrl>", "resource": "<resource>", "event": "<event>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string): A unique identifier for the webhook.
- `name` (string): A user-friendly name for the webhook.
- `targetUrl` (string): URL that receives POST requests for each event.
- `resource` (string): Resource type for the webhook. Creating a webhook requires 'read' scope on the resource the webhook is for.  * `attachmentActions` - [Attachment Actions](/docs/api/v1/attachment-actions) resource.  * `dataSources` - [data sources](/docs/api/v1/data-sources) resource.  * `memberships` - [Memberships](/docs/api/v1/memberships) resource.  * `messages` - [Messages](/docs/api/v1/messages) resource.  * `rooms` - [Rooms](/docs/api/v1/rooms) resource.  * `meetings` - [Meetings](/docs/api/v1/meetings) resource.  * `recordings` - [Recordings](/docs/api/v1/recordings) resource.  * `convergedRecordings` - [CallRecordings](/docs/api/v1/converged-recordings) resource.  * `meetingParticipants` - [Meeting Participants](/docs/api/v1/meeting-participants) resource.  * `meetingTranscripts` - [Meeting Transcripts](/docs/api/v1/meeting-transcripts) resource.  * `telephony_calls` - [Webex Calling](/docs/webex-calling-overview) call resources.  * `telephony_conference` - [Webex Calling](/docs/webex-calling-overview) conference controls resource.  * `telephony_mwi` - [Webex Calling](/docs/webex-calling-overview) voicemail message waiting indicator resource.  * `uc_counters` - Performance counter for a dedicated instance.  * `serviceApp` - Service App authorization notification.  * `adminBatchJobs` - Admin Batch Jobs notification. Valores: attachmentActions, dataSources, memberships, messages, rooms, meetings, recordings, convergedRecordings, meetingParticipants, meetingTranscripts, telephony_calls, telephony_conference, telephony_mwi, uc_counters, serviceApp.
- `event` (string): Event type for the webhook.  * `created` - An object was created.  * `updated` - An object was updated.  * `deleted` - An object was deleted.  * `started` - A meeting was started.  * `ended` - A meeting was ended.  * `joined` - A participant joined.  * `left` - A participant left.  * `migrated` - A room was migrated to a different geography. The roomId has changed.  * `authorized` - A Service App was authorized.  * `deauthorized` - A Service App was deauthorized.  * `statusChanged` - Status of admin batch job was changed. Valores: created, updated, deleted, started, ended, joined, left, migrated, authorized, deauthorized, statusChanged.
- `filter` (string): Filter that defines the webhook scope.
- `secret` (string): Secret used to generate payload signature.
- `status` (string): Status of the webhook. Use `active` to reactivate a disabled webhook.  * `active` - Webhook is active.  * `inactive` - Webhook is inactive. Valores: active, inactive.
- `created` (string): Date and time the webhook was created.
- `ownedBy` (string): Specify `org` when creating an org/admin level webhook. Supported for `meetings`, `recordings`, `convergedRecordings`, `meetingParticipants`, `meetingTranscripts`, `videoMeshAlerts`, `controlHubAlerts`, `rooms`, `messaging` and `adminBatchJobs`  (for Compliance Officers and messages with file attachments only - see [inline file DLP](/docs/api/guides/webex-real-time-file-dlp-basics)) resources.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1dFQkhPT0svOTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
  "name": "My Awesome Webhook",
  "targetUrl": "https://example.com/mywebhook",
  "resource": "messages",
  "event": "created",
  "filter": "roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
  "secret": "86dacc007724d8ea666f88fc77d918dad9537a15",
  "status": "active",
  "created": "2015-10-18T14:26:16+00:00",
  "ownedBy": "org"
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