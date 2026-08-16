---
doc_id: webex-cloud-calling-get-telephony-config-virtuallines-virtuallineid-incomingpermission
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/virtualLines/{virtualLineId}/incomingPermission
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.657795+00:00
---

# GET /telephony/config/virtualLines/{virtualLineId}/incomingPermission

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Read Incoming Permission Settings for a Virtual Line`

## Resumen
Read Incoming Permission Settings for a Virtual Line

## Descripción
Retrieve a virtual line's Incoming Permission settings.

You can change the incoming calling permissions for a virtual line if you want them to be different from your organization's default.

Retrieving the incoming permission settings for a virtual line requires a full, user, read-only administrator, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `virtualLineId` [path] (string) **(requerido)**: Retrieve settings for a virtual line with the matching ID.
- `orgId` [query] (string): ID of the organization in which the virtual line resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Respuestas
- **200**: OK
  - `useCustomEnabled` (boolean) **(requerido)**: When true, indicates that this virtual line uses the specified calling permissions for receiving inbound calls rather than the organizational defaults.
  - `externalTransfer` (string) **(requerido)**: Specifies the transfer behavior for incoming, external calls.  * `ALLOW_ALL_EXTERNAL` - Allow transfer and forward for all external calls including those which were transferred.  * `ALLOW_ONLY_TRANSFERRED_EXTERNAL` - Only allow transferred calls to be transferred or forwarded and disallow transfer of other external calls.  * `BLOCK_ALL_EXTERNAL` - Block all external calls from being transferred or forwarded. Valores: ALLOW_ALL_EXTERNAL, ALLOW_ONLY_TRANSFERRED_EXTERNAL, BLOCK_ALL_EXTERNAL.
  - `internalCallsEnabled` (boolean) **(requerido)**: Internal calls are allowed to be received.
  - `collectCallsEnabled` (boolean) **(requerido)**: Collect calls are allowed to be received.
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
