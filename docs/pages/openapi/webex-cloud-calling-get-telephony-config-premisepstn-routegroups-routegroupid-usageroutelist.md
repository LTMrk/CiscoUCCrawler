---
doc_id: webex-cloud-calling-get-telephony-config-premisepstn-routegroups-routegroupid-usageroutelist
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/premisePstn/routeGroups/{routeGroupId}/usageRouteList
operation_id: Read the Route Lists of a Routing Group
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.170676+00:00
---

# GET /telephony/config/premisePstn/routeGroups/{routeGroupId}/usageRouteList

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Read the Route Lists of a Routing Group`

## Resumen
Read the Route Lists of a Routing Group

## Descripción
List Route Lists for a specific route group. Route Lists are a list of numbers that can be reached via a Route Group. It can be used to provide cloud PSTN connectivity to Webex Calling Dedicated Instance.

Retrieving this list of Route Lists requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `routeGroupId` [path] (string) (**requerido**): ID of the requested Route group.
- `orgId` [query] (string): Organization associated with specific route group.
- `name` [query] (string): Return the list of locations matching the location name.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `order` [query] (string): Order the locations according to designated fields.  Available sort orders are `asc`, and `desc`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/premisePstn/routeGroups/<routeGroupId>/usageRouteList' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `routeGroupUsageRouteListGet` (array) (**requerido**): Array of route lists.
  - `routeLists` (array): List of route lists for this route group.
    - `id` (string) (**requerido**): Route list ID.
    - `name` (string) (**requerido**): Route list name.
    - `locationId` (string) (**requerido**): Location ID for route list.
    - `locationName` (string) (**requerido**): Location name for route list.

### Ejemplo — respuesta 200
```json
{
  "routeGroupUsageRouteListGet": [
    {
      "routeLists": [
        {
          "id": "Y2lzY29zcGFyazovL3VzL1JPVVRFX0xJU1QvOTljNjJkMGQtNmFhYi00NGQ0LWE0ZTctZjk0MjQ4OWVhMWJj",
          "name": "routeListName",
          "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2JjNWUwNWFjLTI5ZmEtNGY0NS05MmM1LWUxZTExMDc0OTIwZg",
          "locationName": "locationName"
        }
      ]
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