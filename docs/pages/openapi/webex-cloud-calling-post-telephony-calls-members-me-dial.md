---
doc_id: webex-cloud-calling-post-telephony-calls-members-me-dial
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/calls/members/me/dial
operation_id: dial
tags: Call Controls
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.944007+00:00
---

# POST /telephony/calls/members/me/dial

**API:** Webex Cloud Calling
**Área:** Call Controls
**operationId:** `dial`

## Resumen
Dial

## Descripción
Initiate an outbound call to a specified destination. This is also commonly referred to as Click to Call or Click to Dial. Alerts occur on all the devices belonging to a user unless an optional endpointId is specified in which case only the device or application identified by the endpointId is alerted. When a user answers an alerting device, an outbound call is placed from that device to the destination.

## Cuerpo de la petición (application/json)
- `destination` (string) (**requerido**): The destination to be dialed. The destination can be digits or a URI. Some examples for destination include: `1234`, `2223334444`, `+12223334444`, `*73`, `tel:+12223334444`, `user@company.domain`, and `sip:user@company.domain`.
- `endpointId` (string): The ID of the device or application to use for the call. The `endpointId` must be one of the endpointIds returned by the [Get Preferred Answer Endpoint API](/docs/api/v1/user-call-settings-2-2/get-preferred-answer-endpoint). Mutually exclusive with `singleNumberReachPhoneNumber`.
- `singleNumberReachPhoneNumber` (string): The Single Number Reach phone number to use for the call. Mutually exclusive with `endpointId`.
- `lineOwnerId` (string): The ID of a user, workspace, or virtual line for which there is a secondary line on a device owned by the user invoking the API.

### Ejemplo — petición
```json
{
  "destination": "+12223334444",
  "endpointId": "Y2lzY29z...",
  "singleNumberReachPhoneNumber": "+12223334444",
  "lineOwnerId": "Y2lzY29z..."
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/calls/members/me/dial' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"destination": "<destination>"}'
```

## Respuestas correctas
**201**: Created
- `callId` (string) (**requerido**): A unique identifier for the call which is used in all subsequent commands for the same call.
- `callSessionId` (string) (**requerido**): A unique identifier for the call session the call belongs to. This can be used to correlate multiple calls that are part of the same call session.

### Ejemplo — respuesta 201
```json
{
  "callId": "Y2lzY29zcGFyazovL3VzL0NBTEwvQkNMRC9jYWxsaGFsZi00ODg6MA",
  "callSessionId": "MmFmNThiZjktYWE3Ny00NWE5LThiMDEtYzI4NDMxZWYwNzRm"
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