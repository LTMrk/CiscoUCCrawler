---
doc_id: webex-cloud-calling-get-telephony-calls-members-memberid-calls-callid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/calls/members/{memberId}/calls/{callId}
operation_id: getCallDetailsByMemberId
tags: Call Controls
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.131343+00:00
---

# GET /telephony/calls/members/{memberId}/calls/{callId}

**API:** Webex Cloud Calling
**Área:** Call Controls
**operationId:** `getCallDetailsByMemberId`

## Resumen
Get Call Details by Member ID

## Descripción
Get the details of the specified active call for the member.

## Parámetros
- `memberId` [path] (string) (**requerido**): Unique identifier for the member. Member ID can be one of the following: person, workspace, or virtual line
- `callId` [path] (string) (**requerido**): The call identifier of the call.
- `orgId` [query] (string): Id of the organization to which the member belongs. If not provided, the orgId of the Service App is used. If provided, the organization must be the same as or managed by the Service App's organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/calls/members/<memberId>/calls/<callId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- (todos de:)
  - `id` (string) (**requerido**): The call identifier of the call.
  - `callSessionId` (string) (**requerido**): The call session identifier of the call session the call belongs to. This can be used to correlate multiple calls that are part of the same call session.
  - `personality` (object) (**requerido**): The personality of the call.
  - `state` (object) (**requerido**): The current state of the call.
  - `remoteParty` (object) (**requerido**): The remote party's details. For example, if user A calls user B then B is the remote party in A's outgoing call details and A is the remote party in B's incoming call details.
  - `appearance` (number): The appearance value for the call. The appearance value can be used to display the user's calls in an order consistent with the user's devices. Only present when the call has an appearance value assigned.
  - `created` (string) (**requerido**): The date and time the call was created.
  - `answered` (string): The date and time the call was answered. Only present when the call has been answered.
  - `redirections` (array): The list of details for previous redirections of the incoming call ordered from most recent to least recent. For example, if user B forwards an incoming call to user C, then a redirection entry is present for B's forwarding in C's incoming call details. Only present when there were previous redirections and the incoming call's state is alerting.
    - `reason` (object) (**requerido**): The reason the incoming call was redirected.
    - `redirectingParty` (object) (**requerido**): The details of a party who redirected the incoming call.
  - `recall` (object): The recall details for the incoming call. Only present when the incoming call is for a recall.
  - `recordingState` (object): The call's current recording state. Only present when the user's call recording has been invoked during the life of the call.
  - `muteCapable` (boolean) (**requerido**): Indicates whether the call is capable of using the [mute](/docs/api/v1/call-controls/mute) and [unmute](/docs/api/v1/call-controls/unmute) APIs.​
  - `muted` (boolean) (**requerido**): Indicates whether the call is currently muted.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0NBTEwvQkNMRC9jYWxsaGFsZi00ODg6MA",
  "callSessionId": "MmFmNThiZjktYWE3Ny00NWE5LThiMDEtYzI4NDMxZWYwNzRm",
  "personality": "originator",
  "state": "connecting",
  "remoteParty": {
    "name": "John Smith",
    "number": "+12223334444",
    "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hMTlkODJhMi00ZTY5LTU5YWEtOWYyZi1iY2E2MzEwMTNhNjg=",
    "placeId": "Y2lzY29zcGFyazovL3VzL1BMQUNFL2ExOWQ4MmEyLTRlNjktNTlhYS05ZjJmLWJjYTYzMTAxM2E2OA==",
    "privacyEnabled": false,
    "callType": "location"
  },
  "appearance": 1,
  "created": "2016-04-21T17:00:00.000Z",
  "answered": "2016-04-21T17:00:00.000Z",
  "redirections": [
    {
      "reason": "busy",
      "redirectingParty": {
        "name": "John Smith",
        "number": "+12223334444",
        "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hMTlkODJhMi00ZTY5LTU5YWEtOWYyZi1iY2E2MzEwMTNhNjg=",
        "placeId": "Y2lzY29zcGFyazovL3VzL1BMQUNFL2ExOWQ4MmEyLTRlNjktNTlhYS05ZjJmLWJjYTYzMTAxM2E2OA==",
        "privacyEnabled": false,
        "callType": "location"
      }
    }
  ],
  "recall": {
    "type": "park",
    "party": {
      "name": "John Smith",
      "number": "+12223334444",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hMTlkODJhMi00ZTY5LTU5YWEtOWYyZi1iY2E2MzEwMTNhNjg=",
      "placeId": "Y2lzY29zcGFyazovL3VzL1BMQUNFL2ExOWQ4MmEyLTRlNjktNTlhYS05ZjJmLWJjYTYzMTAxM2E2OA==",
      "privacyEnabled": false,
      "callType": "location"
    }
  },
  "recordingState": "pending",
  "muteCapable": false
  ... (truncado)
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