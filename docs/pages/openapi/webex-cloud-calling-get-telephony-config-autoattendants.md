---
doc_id: webex-cloud-calling-get-telephony-config-autoattendants
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/autoAttendants
operation_id: listAutoAttendants
tags: Features:  Auto Attendant
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.251118+00:00
---

# GET /telephony/config/autoAttendants

**API:** Webex Cloud Calling
**Área:** Features:  Auto Attendant
**operationId:** `listAutoAttendants`

## Resumen
Read the List of Auto Attendants

## Descripción
List all Auto Attendants for the organization.

Auto attendants play customized prompts and provide callers with menu options for routing their calls through your system.

Retrieving this list requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List auto attendants for this organization.
- `locationId` [query] (string): Return the list of auto attendants for this location.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `name` [query] (string): Only return auto attendants with the matching name.
- `phoneNumber` [query] (string): Only return auto attendants with the matching phone number.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/autoAttendants' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `autoAttendants` (array) (**requerido**): Array of auto attendants.
  - `id` (string) (**requerido**): A unique identifier for the auto attendant.
  - `name` (string) (**requerido**): Unique name for the auto attendant.
  - `locationName` (string) (**requerido**): Name of location for auto attendant.
  - `locationId` (string) (**requerido**): ID of location for auto attendant.
  - `phoneNumber` (string): Auto attendant phone number.  Either `phoneNumber` or `extension` is mandatory.
  - `extension` (string): Auto attendant extension.  Either `phoneNumber` or `extension` is mandatory.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person or workspace.
  - `tollFreeNumber` (boolean) (**requerido**): Flag to indicate if auto attendant number is toll-free number.

### Ejemplo — respuesta 200
```json
{
  "autoAttendants": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5UL2J6QjJlRGd6Ym1GeU5rQm1iR1Y0TWk1amFYTmpieTVqYjIw",
      "name": "Main Line AA - Test",
      "locationName": "Alaska",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzI0NDY5OA",
      "phoneNumber": "+19705550028",
      "extension": "0028",
      "routingPrefix": "1234",
      "esn": "12340028",
      "tollFreeNumber": false
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5UL2NXZHVjWGg1WkhCbmFVQm1iR1Y0TWk1amFYTmpieTVqYjIw",
      "name": "AUTOATTENDANT-TEST 1",
      "locationName": "Alaska",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzI0NDY5OA",
      "phoneNumber": "+19705550030",
      "extension": "1234",
      "routingPrefix": "1234",
      "esn": "12340028",
      "tollFreeNumber": false
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5UL2QzVjBPWFIxWjJkM2FFQm1iR1Y0TWk1amFYTmpieTVqYjIw",
      "name": "AUTOATTENDANT-TEST 2",
      "locationName": "Houston",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzI2NDE1MA",
      "phoneNumber": "+17135551001",
      "extension": "1001",
      "routingPrefix": "1234",
      "esn": "12340028",
      "tollFreeNumber": false
    }
  ]
}
```
- Cabecera `Link`: 

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