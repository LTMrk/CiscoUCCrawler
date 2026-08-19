---
doc_id: webex-cloud-calling-get-telephony-config-people-me-organization-locations
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/organization/locations
operation_id: getMyOrganizationLocations
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.983169+00:00
---

# GET /telephony/config/people/me/organization/locations

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyOrganizationLocations`

## Resumen
Get Location List for My Organization

## Descripción
Get the list of locations for the authenticated person's organization.

Locations are used to organize Webex Calling resources such as people, workspaces, and features within an organization. Each location can have its own settings and configurations for calling services.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `max` [query] (integer): Number of records per page. Por defecto: 2000.
- `start` [query] (integer): Start at the zero-based offset in the list of matching objects.
- `name` [query] (array): Search (Contains) based on location name. Multiple values are logically OR-ed.
- `order` [query] (string): Sort by location name (`name`). Sort directions asc or desc.  * `asc` - Sort in ascending order.  * `desc` - Sort in descending order.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/organization/locations' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `locations` (array) (**requerido**): Array of locations. Results are paginated; use max and start query parameters.
  - `id` (string) (**requerido**): Unique identifier for the location.
  - `name` (string) (**requerido**): Name of the location.
  - `routingPrefix` (string): Location's routing prefix.

### Ejemplo — respuesta 200
```json
{
  "locations": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzgzMTA2ZDE0LTRjNzQtNGQ1Zi04YTllLTk3ZTIxNGVmNGE1Yg",
      "name": "Bangalore",
      "routingPrefix": "2345"
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