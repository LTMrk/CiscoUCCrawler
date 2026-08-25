---
doc_id: webex-cloud-calling-get-telephony-config-huntgroups
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/huntGroups
operation_id: listHuntGroups
tags: Features:  Hunt Group
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.492421+00:00
---

# GET /telephony/config/huntGroups

**API:** Webex Cloud Calling
**Área:** Features:  Hunt Group
**operationId:** `listHuntGroups`

## Resumen
Read the List of Hunt Groups

## Descripción
List all calling Hunt Groups for the organization.

Hunt groups can route incoming calls to a group of people or workspaces. You can even configure a pattern to route to a whole group.

Retrieving this list requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List hunt groups for this organization.
- `locationId` [query] (string): Only return hunt groups with matching location ID.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `name` [query] (string): Only return hunt groups with the matching name.
- `phoneNumber` [query] (string): Only return hunt groups with the matching primary phone number or extension.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/huntGroups' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `huntGroups` (array) (**requerido**): Array of hunt groups.
  - `id` (string) (**requerido**): A unique identifier for the hunt group.
  - `name` (string) (**requerido**): Unique name for the hunt group.
  - `locationName` (string) (**requerido**): Name of the location for the hunt group.
  - `locationId` (string) (**requerido**): ID of location for hunt group.
  - `phoneNumber` (string): Primary phone number of the hunt group.
  - `extension` (string): Primary phone extension of the hunt group.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person or workspace.
  - `enabled` (boolean) (**requerido**): Whether or not the hunt group is enabled.

### Ejemplo — respuesta 200
```json
{
  "huntGroups": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvYUhaaFpUTjJNRzh5YjBBMk5EazBNVEk1Tnk1cGJuUXhNQzVpWTJ4a0xuZGxZbVY0TG1OdmJRPT0",
      "name": "5714328359",
      "locationName": "WXCSIVDKCPAPIC4S1",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzMxMTYx",
      "routingPrefix": "123",
      "esn": "1239097",
      "enabled": true
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvYVhZd2QySTJNbmM1YWtBMk5EazBNVEk1Tnk1cGJuUXhNQzVpWTJ4a0xuZGxZbVY0TG1OdmJRPT0",
      "name": "bram",
      "locationName": "Brampton",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzQwMjgw",
      "phoneNumber": "+15558675309",
      "routingPrefix": "123",
      "esn": "1239097",
      "enabled": true
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