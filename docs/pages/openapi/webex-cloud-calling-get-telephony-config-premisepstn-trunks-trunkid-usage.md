---
doc_id: webex-cloud-calling-get-telephony-config-premisepstn-trunks-trunkid-usage
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/premisePstn/trunks/{trunkId}/usage
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.554847+00:00
---

# GET /telephony/config/premisePstn/trunks/{trunkId}/usage

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Get Local Gateway Usage Count`

## Resumen
Get Local Gateway Usage Count

## Descripción
Get Local Gateway Usage Count

A trunk is a connection between Webex Calling and the premises, which terminates on the premises with a local gateway or other supported device.
The trunk can be assigned to a Route Group which is a group of trunks that allow Webex Calling to distribute calls over multiple trunks or to provide redundancy.

Retrieving this information requires a full administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `trunkId` [path] (string) **(requerido)**: ID of the trunk.
- `orgId` [query] (string): Organization to which the trunk belongs.

## Respuestas
- **200**: OK
  - `pstnConnectionCount` (number) **(requerido)**: The count where the local gateway is used as a PSTN Connection setting.
  - `callToExtensionCount` (number) **(requerido)**: The count where the given local gateway is used as call to extension setting.
  - `dialPlanCount` (number) **(requerido)**: The count where the given local gateway is used by the dial plan.
  - `routeGroupCount` (number) **(requerido)**: The count where the given local gateway is used by the route group.
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
