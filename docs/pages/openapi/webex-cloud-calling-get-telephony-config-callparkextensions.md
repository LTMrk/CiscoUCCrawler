---
doc_id: webex-cloud-calling-get-telephony-config-callparkextensions
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/callParkExtensions
operation_id: Read the List of Call Park Extensions
tags: Features:  Call Park
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.257705+00:00
---

# GET /telephony/config/callParkExtensions

**API:** Webex Cloud Calling
**Área:** Features:  Call Park
**operationId:** `Read the List of Call Park Extensions`

## Resumen
Read the List of Call Park Extensions

## Descripción
List all Call Park Extensions for the organization.

The Call Park service, enabled for all users by default, allows a user to park a call against an available user's extension or to a Call Park Extension. Call Park Extensions are extensions defined within the Call Park service for holding parked calls.

Retrieving this list requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List call park extensions for this organization.
- `locationId` [query] (string): Only return call park extensions with matching location ID.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `extension` [query] (string): Only return call park extensions with the matching extension.
- `locationName` [query] (string): Only return call park extensions with the matching extension.
- `name` [query] (string): Only return call park extensions with the matching name.
- `order` [query] (string): Order the available agents according to the designated fields.  Available sort fields: `groupName`, `callParkExtension`, `callParkExtensionName`, `callParkExtensionExternalId`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/callParkExtensions' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `callParkExtensions` (array) (**requerido**): Array of call park extensions.
  - `id` (string) (**requerido**): Unique identifier for the call park extension.
  - `extension` (string) (**requerido**): The extension for the call park extension.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person or workspace.
  - `name` (string) (**requerido**): A unique name for the call park extension.
  - `locationId` (string) (**requerido**): ID of location for call park extension.
  - `locationName` (string) (**requerido**): Name of location for call park extension.

### Ejemplo — respuesta 200
```json
{
  "callParkExtensions": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUEFSS19FWFRFTlNJT04vMGYzZTkwNGItYzliNC00ODNmLWI4MWItZmI0ZjkyMWcxNDUzCg",
      "extension": "1415",
      "routingPrefix": "1234",
      "esn": "12341415",
      "name": "14159265",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzMxMTYx",
      "locationName": "WXCSIVDKCPAPIC4S1"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUEFSS19FWFRFTlNJT04vMGYzZTkwNGItYzliNC00ODNmLWI4MWItZmI0ZjkyMWcxNDUyCg",
      "extension": "7182",
      "routingPrefix": "1234",
      "esn": "12347182",
      "name": "71828182",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzMxMTYx",
      "locationName": "WXCSIVDKCPAPIC4S1"
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