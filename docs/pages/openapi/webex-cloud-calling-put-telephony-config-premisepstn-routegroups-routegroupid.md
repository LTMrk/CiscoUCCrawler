---
doc_id: webex-cloud-calling-put-telephony-config-premisepstn-routegroups-routegroupid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/premisePstn/routeGroups/{routeGroupId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.556888+00:00
---

# PUT /telephony/config/premisePstn/routeGroups/{routeGroupId}

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Modify a Route Group for a Organization`

## Resumen
Modify a Route Group for a Organization

## Descripción
Modifies an existing Route Group for an organization based on id.

A Route Group is a collection of trunks that allows further scale and redundancy with the connection to the premises. Route groups can include up to 10 trunks from different locations.

Modifying a Route Group requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `routeGroupId` [path] (string) **(requerido)**: Route Group for which details are being requested.
- `orgId` [query] (string): Organization of the Route Group.

## Cuerpo de la petición (application/json)
- `name` (string) **(requerido)**: A unique name for the Route Group.
- `localGateways` (array) **(requerido)**: Local Gateways that are part of this Route Group.
  - `id` (string) **(requerido)**: ID of type local gateway.
  - `name` (string): Name of the local gateway.
  - `locationId` (string): Location ID to which local gateway belongs.
  - `priority` (number) **(requerido)**: Prioritizes local gateways based on these numbers; the lowest number gets the highest priority.

### Ejemplo de petición
```json
{
  "name": "hydra4",
  "localGateways": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1RSVU5LLzY1Zjc4YzgxLTcwMTYtNDc0Ny05M2EyLWIxMGVlZjBhMWI1Ng",
      "name": "Route List Trunk",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL1dTV1laMjEyODA2TDIxMjg0MQ",
      "priority": 2
    }
  ]
}
```

## Respuestas
- **204**: No Content
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
