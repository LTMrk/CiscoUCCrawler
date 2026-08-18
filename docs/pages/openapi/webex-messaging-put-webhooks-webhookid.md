---
doc_id: webex-messaging-put-webhooks-webhookid
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: PUT
path: /webhooks/{webhookId}
operation_id: Update a Webhook
tags: Webhooks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.815844+00:00
---

# PUT /webhooks/{webhookId}

**API:** Webex Messaging
**Área:** Webhooks
**operationId:** `Update a Webhook`

## Resumen
Update a Webhook

## Descripción
Updates a webhook, by ID. You cannot use this call to deactivate a webhook, only to activate a webhook that was auto deactivated.
The fields that can be updated are `name`, `targetURL`, `secret` and `status`. All other fields, if supplied, are ignored.

Specify the webhook ID in the `webhookId` parameter in the URI.

## Parámetros
- `webhookId` [path] (string) (**requerido**): The unique identifier for the webhook.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): A user-friendly name for the webhook.
- `targetUrl` (string) (**requerido**): URL that receives POST requests for each event.
- `secret` (string): Secret used to generate payload signature.
- `ownedBy` (string): Specify `org` when creating an org/admin level webhook. Supported for `meetings`, `recordings`, `convergedRecordings`, `meetingParticipants`, `meetingTranscripts`, `videoMeshAlerts`, `controlHubAlerts`, `rooms`, `messaging` and `adminBatchJobs`  (for Compliance Officers and messages with file attachments only - see [inline file DLP](/docs/api/guides/webex-real-time-file-dlp-basics)) resources.
- `status` (string): Status of the webhook. Use "active" to reactivate a disabled webhook. Valores: active.

### Ejemplo — petición
```json
{
  "name": "My Awesome Webhook",
  "targetUrl": "https://example.com/mywebhook",
  "secret": "86dacc007724d8ea666f88fc77d918dad9537a15",
  "ownedBy": "org",
  "status": "active"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/webhooks/<webhookId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "targetUrl": "<targetUrl>"}'
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
The Webex Messaging APIs offer robust programmatic access to messaging features within Webex, including sending and receiving messages, managing spaces, memberships, attachments, and moderating content. These APIs enable integration with bots, workflow automation, notification systems, and custom messaging solutions to enhance team collaboration and productivity. Use cases include building chatbots, integrating with ticketing or alerting platforms, automating onboarding flows, and creating custom collaboration experiences tailored to business needs.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs