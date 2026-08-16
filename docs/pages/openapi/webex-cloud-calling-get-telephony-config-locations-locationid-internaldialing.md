---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-internaldialing
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/locations/{locationId}/internalDialing
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.625512+00:00
---

# GET /telephony/config/locations/{locationId}/internalDialing

**API:** Webex Cloud Calling
**Área:** Location Call Settings: Call Handling
**operationId:** `Read the Internal Dialing configuration for a location`

## Resumen
Read the Internal Dialing configuration for a location

## Descripción
Get current configuration for routing unknown extensions to the Premises as internal calls

If some users in a location are registered to a PBX, retrieve the setting to route unknown extensions (digits that match the extension length) to the PBX.

Retrieving the internal dialing configuration requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: location for which internal calling configuration is being requested
- `orgId` [query] (string): List route identities for this organization.

## Respuestas
- **200**: OK
  - `enableUnknownExtensionRoutePolicy` (boolean): When enabled, calls made by users at the location to an unknown extension (between 2-6 digits) are routed to the selected route group/trunk as premises calls.
  - `unknownExtensionRouteIdentity` (object):
    - `id` (string) **(requerido)**: ID of the route type.
    - `name` (string) **(requerido)**: A unique name for the route identity.
    - `type` (string) **(requerido)**: * `ROUTE_GROUP` - Route group must include at least one trunk with a maximum of 10 trunks per route group.  * `TRUNK` - Connection between Webex Calling and the premises. Valores: ROUTE_GROUP, TRUNK.
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
