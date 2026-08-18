---
doc_id: webex-meeting-post-meetingparticipants-callout
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: POST
path: /meetingParticipants/callout
operation_id: Call Out a SIP Participant
tags: Participants
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.466879+00:00
---

# POST /meetingParticipants/callout

**API:** Webex Meetings
**Área:** Participants
**operationId:** `Call Out a SIP Participant`

## Resumen
Call Out a SIP Participant

## Descripción
Initiate a call to a SIP participant to join a meeting.

If a user invoking the API is not a [Service App](/docs/service-apps), the user must join the meeting before invoking the API. If a user is a [Service App](/docs/service-apps), the service app can invoke the API without joining the meeting. In both cases, the normal user or the service app that invokes the API must be the meeting host or cohost. If the meeting is created by the service app on behalf of the real host, the service app cannot use the admin on behalf function to invoke this API. Instead the host or cohost must execute the action.

The authenticated user calling this API must have the `meeting:participants_write` scope.

The ringing on the invited SIP device stops in 30 seconds if there is no response.

## Cuerpo de la petición (application/json)
- `meetingId` (string): Unique identifier of the meeting to which the SIP participant is to be called out. Either `meetingId` or `meetingNumber` must be specified.
- `meetingNumber` (string): Number of the meeting to which the SIP participant is to be called out. Either `meetingId` or `meetingNumber` must be specified.
- `address` (string) (**requerido**): SIP address of the invited SIP participant.
- `addressType` (string): Type of the `address`. The default value is `sipAddress`.  * `sipAddress` - SIP address. Valores: sipAddress.
- `invitationCorrelationId` (string): An internal ID that is associated with the call-out invitation. Only UUIDs with hyphens are supported. The letters in the UUID must be in lowercase. A random UUID will be generated automatically if not specified.
- `displayName` (string) (**requerido**): The display name of the invited SIP participant. The maximum length is 32 characters.

### Ejemplo — petición
```json
{
  "meetingId": "d8c3347d7ec04242ba9b856184b334ac",
  "address": "SIP:9053523155@examplezone.cisco.com",
  "addressType": "sipAddress",
  "invitationCorrelationId": "871ab255-64e6-4cd2-a5af-d33953898356",
  "displayName": "Brenda DX80"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/meetingParticipants/callout' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"address": "<address>", "displayName": "<displayName>"}'
```

## Respuestas correctas
**200**: OK
- `participantId` (string): Participant ID. It can be used in the "Cancel Call Out a SIP Participant" API.
- `invitationCorrelationId` (string): An internal ID that is associated with the call-out invitation.
- `meetingNumber` (string): Number of the meeting to which the SIP participant is to be called out.
- `meetingId` (string): Unique identifier of the meeting to which the SIP participant is to be called out.
- `address` (string): SIP address of the invited SIP participant.
- `addressType` (string): Type of the `address`.  * `sipAddress` - SIP address. Valores: sipAddress.
- `displayName` (string): The display name of the invited SIP participant.
- `state` (string): The state of the invited SIP participant.  * `pending` - The invited SIP participant is waiting for approval. Participants in the `pending` state will not be listed by the "List Meeting Participants" API. Valores: pending.

### Ejemplo — respuesta 200
```json
{
  "participantId": "d8c3347d7ec04242ba9b856184b334ac_I_630641605678082408_57514861-50f7-3f5b-864f-ce0e308bf653",
  "invitationCorrelationId": "871ab255-64e6-4cd2-a5af-d33953898356",
  "meetingNumber": "79100342367",
  "meetingId": "d8c3347d7ec04242ba9b856184b334ac",
  "address": "SIP:9053523155@examplezone.cisco.com",
  "addressType": "sipAddress",
  "displayName": "Brenda DX80",
  "state": "pending"
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