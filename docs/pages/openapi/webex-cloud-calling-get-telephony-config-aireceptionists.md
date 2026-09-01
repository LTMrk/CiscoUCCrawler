---
doc_id: webex-cloud-calling-get-telephony-config-aireceptionists
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/aiReceptionists
operation_id: listAiReceptionists
tags: AI Receptionist for Webex Calling, AI Receptionist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.551551+00:00
---

# GET /telephony/config/aiReceptionists

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `listAiReceptionists`

## Resumen
List AI Receptionists

## Descripción
Get list of AI Receptionists.

AI Receptionist is a Webex Calling feature that uses AI to greet callers and intelligently route calls to people or services. These APIs let administrators manage AI receptionist resources across organizations and locations.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.
- `max` [query] (integer): Maximum number of items returned in the response. Default: 2000.
- `start` [query] (integer): Zero-based offset for pagination.
- `locationId` [query] (string): Location identifier. If not specified, returns AI receptionists from all locations.
- `name` [query] (string): Search AI receptionists by name (contains match).
- `phoneNumber` [query] (string): Search (Contains) based on number or extension. Search cannot be performed based on esn.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/aiReceptionists' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `aiReceptionists` (array): List of AI Receptionists.
  - `id` (string) (**requerido**): Unique identifier for the AI receptionist.
  - `name` (string) (**requerido**): Name of the AI receptionist. Must be unique within a location.
  - `phoneNumber` (string): Phone number of the AI receptionist in E.164 format.
  - `extension` (string): Extension of the AI Receptionist.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of the AI Receptionist. If the location has no routing prefix, this will only be the extension. If the AI Receptionist has no extension, this field will not be present.
  - `location` (object) (**requerido**): Location of the AI Receptionist.

### Ejemplo — respuesta 200
```json
{
  "aiReceptionists": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FJX1JFQ0VQVElPTklTVC82MDEyNGU1MC03MWNkLTQ2N2QtODkzZS1mMGY5MDc0YWYyYjc",
      "name": "Shine Healthcare Clinic",
      "phoneNumber": "+13504342182",
      "extension": "42182",
      "routingPrefix": "1234",
      "esn": "123442182",
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzgyMjI4MWVkLWUyMmItMTYxNi1hOTYyLTExYTY2OTExYTY2OQ",
        "name": "San Jose"
      }
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