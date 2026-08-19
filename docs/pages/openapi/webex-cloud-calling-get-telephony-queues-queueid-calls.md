---
doc_id: webex-cloud-calling-get-telephony-queues-queueid-calls
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/queues/{queueId}/calls
operation_id: listcallqueuecalls
tags: Call Controls, External Voicemail
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.942744+00:00
---

# GET /telephony/queues/{queueId}/calls

**API:** Webex Cloud Calling
**Área:** Call Controls, External Voicemail
**operationId:** `listcallqueuecalls`

## Resumen
List Call Queue Calls

## Descripción
List the calls currently in the specified Call Queue. The returned calls follow the same format as the Call Queue events emitted by Webex Calling and include the caller details, position information (priority), and queue timing for each call currently waiting in the queue.

## Parámetros
- `queueId` [path] (string) (**requerido**): The unique identifier of the Call Queue whose calls are to be listed.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/queues/<queueId>/calls' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array) (**requerido**):
  - `callId` (string) (**requerido**): The call identifier of the call currently in the queue.
  - `origCallId` (string): The call identifier of the original call that entered the queue. This differs from `callId` when the call currently in the queue is a new call leg derived from the original call - for example, a Call Queue callback, where `callId` is the new callback call and `origCallId` is the original call that entered the queue. Only present when it differs from the call's `callId`.
  - `callSessionId` (string) (**requerido**): A unique identifier for the call session the call belongs to. This can be used to correlate multiple calls that are part of the same call session.
  - `remoteParty` (object) (**requerido**): The remote party's details for the call waiting in the queue.
  - `addTime` (string): The date and time the call was added to the queue.
  - `removeTime` (string): The date and time the call was removed from the queue. Only present when the call has been removed from the queue.
  - `mandatoryEntrance` (boolean): Indicates whether the call entered the queue as a mandatory entrance.
  - `bounced` (boolean): Indicates whether the call has been bounced from an agent back to the queue.
  - `reordered` (boolean): Indicates whether the call has been reordered within the queue.
  - `preservedWaitTime` (integer): The wait time, in milliseconds, preserved for the call when it was moved between queues.
  - `queueNumber` (string): The phone number of the Call Queue the call is waiting in.
  - `queueName` (string): The name of the Call Queue the call is waiting in.
  - `priority` (string): The priority of the call within the queue. Only present for premium Call Queues that assign a priority. Valores: highest, high, medium, low.
  - `answeringAgentId` (string): The identifier of the agent (person, workspace, or virtual line) who is answering, or has answered, the call. The resource type of this identifier is indicated by `answeringAgentType`. Only present when the call is being answered.
  - `answeringAgentType` (string): The type of agent identified by `answeringAgentId`: `PEOPLE` for a user, `PLACE` for a workspace, and `VIRTUAL_LINE` for a virtual line. Only present when the call is being answered. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `answeringCallId` (string): The call identifier of the answering agent's terminating call. Use this value to correlate the queue call with other call events associated with the agent. Only present when the call is being answered.
  - `answeringNetworkCallId` (string): The SIP Call-ID of the answering call. Only present when the call is being answered.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "callId": "Y2lzY29zcGFyazovL3VzL0NBTEwvQkNMRC9jYWxsaGFsZi00ODg6MA",
      "origCallId": "Y2lzY29zcGFyazovL3VzL0NBTEwvQkNMRC9jYWxsaGFsZi00ODg6MQ",
      "callSessionId": "MmFmNThiZjktYWE3Ny00NWE5LThiMDEtYzI4NDMxZWYwNzRm",
      "remoteParty": {
        "name": "John Smith",
        "number": "+12223334444",
        "privacyEnabled": false,
        "callType": "organization"
      },
      "addTime": "2016-04-21T17:00:00.000Z",
      "queueNumber": "+15559998888",
      "queueName": "Support Queue",
      "priority": "medium",
      "bounced": true
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs