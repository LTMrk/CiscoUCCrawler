---
doc_id: webex-cloud-calling-get-telephony-config-voicemailgroups
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/voicemailGroups
operation_id: List VoicemailGroup
tags: Location Call Settings:  Voicemail
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.308352+00:00
---

# GET /telephony/config/voicemailGroups

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Voicemail
**operationId:** `List VoicemailGroup`

## Resumen
List VoicemailGroup

## Descripción
List the voicemail group information for the organization.

You can create a shared voicemail box and inbound FAX box to
assign to users or call routing features like an auto attendant, call queue, or hunt group.

Retrieving a voicemail group for the organization requires a full read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Organization to which the voicemail group belongs.
- `locationId` [query] (string): Location to which the voicemail group belongs.
- `name` [query] (string): Search (Contains) based on voicemail group name
- `phoneNumber` [query] (string): Search (Contains) based on number or extension
- `max` [query] (number): Limit the maximum number of events in the response. The maximum value is `200`. Por defecto: 100.
- `start` [query] (number): Offset from the first result that you want to fetch.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/voicemailGroups' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `voicemailGroups` (array) (**requerido**): Array of VoicemailGroups.
  - `id` (string): Voicemail Group ID.
  - `name` (string): Voicemail Group Name.
  - `locationName` (string): Location Name.
  - `locationId` (string): Location ID.
  - `extension` (string): Extension of the voicemail group.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person or workspace.
  - `phoneNumber` (string): Phone number of the voicemail group.
  - `enabled` (boolean): If enabled, incoming calls are sent to voicemail.
  - `tollFreeNumber` (boolean): Flag to indicate if the number is toll free.

### Ejemplo — respuesta 200
```json
{
  "voicemailGroups": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZPSUNFTUFJTF9HUk9VUC9hN2RkNGQzOS00YTc4LTQ1MTYtOTU1Zi03ODEwZGJlMzc5Y2Y",
      "name": "RCDN-VM",
      "locationName": "Dallas",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzljZmRhNzg5LWUwNjItNDU2MC05MzhiLTFmNDYxNmVmNzNmMg",
      "phoneNumber": "+16066412147",
      "extension": "5896",
      "routingPrefix": "123",
      "esn": "1235896",
      "enabled": true,
      "tollFreeNumber": false
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZPSUNFTUFJTF9HUk9VUC8yZmQzZGMwMy0yZWRhLTQ4NmUtODdhYS0xODY1ZDI5YWExZWI",
      "name": "VG1",
      "locationName": "Boston",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2EwYjk2ZWJhLTdiYjAtNDEwNy05NzVmLTBmMzkwZTBlNzc4OA",
      "phoneNumber": null,
      "extension": "1125",
      "routingPrefix": "123",
      "esn": "1235896",
      "enabled": true
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZPSUNFTUFJTF9HUk9VUC8yZTY4ZjJmNC1lYTI2LTQyNjgtOWJmMy03YjNlNmJjMjE5YzE",
      "name": "VG2",
      "locationName": "RCDN",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzZhZjk4ZGViLWVlZGItNGFmYi1hMDAzLTEzNzgyYjdjODAxYw",
      "phoneNumber": null,
      "extension": "4567",
      "routingPrefix": "123",
      "esn": "1235896",
      "enabled": true
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