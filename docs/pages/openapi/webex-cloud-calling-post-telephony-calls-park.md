---
doc_id: webex-cloud-calling-post-telephony-calls-park
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/calls/park
operation_id: park
tags: Call Controls, External Voicemail
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.159497+00:00
---

# POST /telephony/calls/park

**API:** Webex Cloud Calling
**Área:** Call Controls, External Voicemail
**operationId:** `park`

## Resumen
Park

## Descripción
Park a connected call. The number field in the response can be used as the destination for the retrieve command to retrieve the parked call.

## Cuerpo de la petición (application/json)
- `callId` (string) (**requerido**): The call identifier of the call to park.
- `destination` (string): Identifes where the call is to be parked. If not provided, the call is parked against the parking user. The destination can be digits or a URI. Some examples for destination include: `1234`, `2223334444`, `+12223334444`, `*73`, `tel:+12223334444`, `user@company.domain`, `sip:user@company.domain`
- `isGroupPark` (boolean): If set to`true`, the call is parked against an automatically selected member of the user's call park group and the destination parameter is ignored.
- `lineOwnerId` (string): The ID of a user, workspace, or virtual line for which there is a secondary line on a device owned by the user invoking the API.

### Ejemplo — petición
```json
{
  "callId": "Y2lzY29zcGFyazovL3VzL0NBTEwvQkNMRC9jYWxsaGFsZi00ODg6MA",
  "destination": "1000",
  "isGroupPark": false,
  "lineOwnerId": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS8wMDAwODg4OC04ZGU1LTRiMTItOGUyYi0wMDAwMDAxMjM0NTY"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/calls/park' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"callId": "<callId>"}'
```

## Respuestas correctas
**200**: OK
- `parkedAgainst` (object) (**requerido**): The details of where the call has been parked.

### Ejemplo — respuesta 200
```json
{
  "parkedAgainst": {
    "name": "John Smith",
    "number": "+12223334444",
    "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hMTlkODJhMi00ZTY5LTU5YWEtOWYyZi1iY2E2MzEwMTNhNjg=",
    "placeId": "Y2lzY29zcGFyazovL3VzL1BMQUNFL2ExOWQ4MmEyLTRlNjktNTlhYS05ZjJmLWJjYTYzMTAxM2E2OA==",
    "privacyEnabled": false,
    "callType": "location"
  }
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