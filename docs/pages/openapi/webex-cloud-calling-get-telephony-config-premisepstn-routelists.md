---
doc_id: webex-cloud-calling-get-telephony-config-premisepstn-routelists
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/premisePstn/routeLists
operation_id: Read the List of Route Lists
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.170868+00:00
---

# GET /telephony/config/premisePstn/routeLists

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Read the List of Route Lists`

## Resumen
Read the List of Route Lists

## Descripción
List all Route Lists for the organization.

A Route List is a list of numbers that can be reached via a Route Group. It can be used to provide cloud PSTN connectivity to Webex Calling Dedicated Instance.

Retrieving the Route List requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List all Route List for this organization.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `order` [query] (string): Order the Route List according to the designated fields. Available sort fields are `name`, and `locationId`. Sort order is ascending by default
- `name` [query] (array): Return the list of Route List matching the route list name.
- `locationId` [query] (array): Return the list of Route Lists matching the location id.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/premisePstn/routeLists' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `routeLists` (array) (**requerido**): Array of route lists.
  - `id` (string) (**requerido**): ID of the Route List.
  - `name` (string) (**requerido**): Name of the Route List.
  - `locationId` (string) (**requerido**): Location associated with the Route List.
  - `locationName` (string) (**requerido**): Location associated with the Route List.
  - `routeGroupId` (string): ID of the route group associated with Route List.
  - `routeGroupName` (string): Name of the Route Group associated with Route List.

### Ejemplo — respuesta 200
```json
{
  "routeLists": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1JPVVRFX0xJU1QvOTljNjJkMGQtNmFhYi00NGQ0LWE0ZTctZjk0MjQ4OWVhMWJj",
      "name": "RouteList Name",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2JjNWUwNWFjLTI5ZmEtNGY0NS05MmM1LWUxZTExMDc0OTIwZg",
      "locationName": "locationName",
      "routeGroupId": "Y2lzY29zcGFyazovL3VzL1JPVVRFX0dST1VQL2ZjN2EzZDU2LTg1OGMtNDVkZC1iZDA1LTE2OWM2NGU1OTRmMQ",
      "routeGroupName": "RouteGroup01"
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