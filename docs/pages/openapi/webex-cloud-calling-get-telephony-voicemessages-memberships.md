---
doc_id: webex-cloud-calling-get-telephony-voicemessages-memberships
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/voiceMessages/memberships
operation_id: listVoiceMessageMemberships
tags: User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-27T10:51:19.551543+00:00
---

# GET /telephony/voiceMessages/memberships

**API:** Webex Cloud Calling
**Área:** User Call Settings (3/3)
**operationId:** `listVoiceMessageMemberships`

## Resumen
List Voice Message Memberships

## Descripción
Retrieves the list of shared voicemail memberships for the authenticated user. Each membership represents a group calling feature (Call Queue, Hunt Group, or Auto Attendant) whose shared voicemail box the user has access to.

A service may have a phoneNumber, an extension, both, or neither, so any of these optional fields may be absent from a given entry. These can be used as values for the `lineOwnerId` parameter in other voicemail APIs.

This API requires a full, user, or read-only administrator auth token with a scope of `spark-admin:people_read` or a user auth token with `spark:people_read` scope.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/voiceMessages/memberships' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `memberOf` (array) (**requerido**): Array of shared voicemail membership entries.
  - `id` (string) (**requerido**): Unique identifier for the membership.
  - `type` (string) (**requerido**): Type of the membership. One of CALL_QUEUE, HUNT_GROUP, or AUTO_ATTENDANT. Valores: CALL_QUEUE, HUNT_GROUP, AUTO_ATTENDANT.
  - `name` (string): Display name of the call queue, hunt group, or auto attendant.
  - `phoneNumber` (string): Phone number in E.164 format. Omitted when the service has no phone number.
  - `extension` (string): Extension number. Omitted when the service has no extension.
  - `routingPrefix` (string): Location dialing code (routing prefix). Omitted when not set.
  - `esn` (string): Enterprise Significant Number, the concatenation of routingPrefix and extension. Omitted when not set.

### Ejemplo — respuesta 200
```json
{
  "memberOf": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUVVFVUUvYm1kMmVIcHNabTgwWVVBMk5EazBNVEk1Tnk1cGJuUXhNQzVpWTJ4a0xuZGxZbVY0TG1OdmJRPT0",
      "type": "CALL_QUEUE",
      "name": "Engineering Call Center",
      "phoneNumber": "+14085550101",
      "extension": "1001",
      "routingPrefix": "8888",
      "esn": "88881001"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvNmU1NTVjZDAtNjM0MS00MmI4LWEyMWMtZTc1ZjIxNDQ4Mjc1",
      "type": "HUNT_GROUP",
      "name": "Sales Hunt Group",
      "phoneNumber": "+14085550102"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5ULzA1NTJmNjdiLTU5YTktNDFiYi04NzM2LTFiMDQxZDFkZGQ1ZQ",
      "type": "AUTO_ATTENDANT",
      "name": "Support Auto Attendant",
      "extension": "3003",
      "routingPrefix": "9999",
      "esn": "99993003"
    }
  ]
}
```
**204**: No Content - Returned when there are no memberships.

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