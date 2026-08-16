---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-dectnetworks-dectnetworkid-serviceabilitypassword
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/serviceabilityPassword
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.547084+00:00
---

# GET /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/serviceabilityPassword

**API:** Webex Cloud Calling
**Área:** DECT Devices Settings
**operationId:** `Get DECT Serviceability Password Status`

## Resumen
Get DECT Serviceability Password Status

## Descripción
Retrieves the DECT serviceability password status.

<div><Callout type="info">If the serviceability password is enabled but has not been generated, the `enabled` status will be returned as `true` even though there is no active serviceability password.</Callout></div>

The DECT serviceability password, also known as the admin override password, provides read/write access to DECT base stations for performing system serviceability and troubleshooting functions.

This API requires an auth token with either a full, read-only, or location administrator token with the scope of `spark-admin:telephony_config_read`, or a device administrator token with the scope of `spark-admin:devices_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Unique identifier for the location.
- `dectNetworkId` [path] (string) **(requerido)**: Unique identifier for the DECT network.
- `orgId` [query] (string): Unique identifier for the organization.

## Respuestas
- **200**: OK
  - `enabled` (boolean) **(requerido)**: DECT serviceability password status. When `enabled` is set to `true`, the serviceability password can be used to manage DECT. When `enabled` is set to `false`, the serviceability password is disabled and the password owned and known by Cisco is required to perform serviceability and troubleshooting.
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
