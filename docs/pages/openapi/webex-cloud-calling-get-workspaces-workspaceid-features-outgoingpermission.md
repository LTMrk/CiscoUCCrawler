---
doc_id: webex-cloud-calling-get-workspaces-workspaceid-features-outgoingpermission
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /workspaces/{workspaceId}/features/outgoingPermission
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.665888+00:00
---

# GET /workspaces/{workspaceId}/features/outgoingPermission

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (1/2)
**operationId:** `Retrieve Outgoing Permission Settings for a Workspace`

## Resumen
Retrieve Outgoing Permission Settings for a Workspace

## Descripción
Retrieve Outgoing Permission settings for a Workspace.

Turn on outgoing call settings for this workspace to override the calling settings from the location that are used by default.

This API requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:workspaces_read` or a user auth token with `spark:workspaces_read` scope can be used to read workspace settings.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Respuestas
- **200**: OK
  - `useCustomEnabled` (boolean): When `true`, indicates that this workspace uses the shared control that applies to all outgoing call settings categories when placing outbound calls.
  - `useCustomPermissions` (boolean) **(requerido)**: When `true`, indicates that this workspace uses the specified outgoing calling permissions when placing outbound calls.
  - `callingPermissions` (array) **(requerido)**: Workspace's list of outgoing permissions.
    - `callType` (string) **(requerido)**: Type of the outgoing call.  * `INTERNAL_CALL` - Internal call type.  * `TOLL_FREE` - Toll free call type.  * `INTERNATIONAL` - International call type.  * `OPERATOR_ASSISTED` - Operator Assisted call type.  * `CHARGEABLE_DIRECTORY_ASSISTED` - Chargeable Directory Assisted call type.  * `SPECIAL_SERVICES_I` - Special Services I call type.  * `SPECIAL_SERVICES_II` - Special Services II call type.  * `PREMIUM_SERVICES_I` - Premium Services I call type.  * `PREMIUM_SERVICES_II` - Premium Services II call type.  * `NATIONAL` - National call type. Valores: INTERNAL_CALL, TOLL_FREE, INTERNATIONAL, OPERATOR_ASSISTED, CHARGEABLE_DIRECTORY_ASSISTED, SPECIAL_SERVICES_I, SPECIAL_SERVICES_II, PREMIUM_SERVICES_I, PREMIUM_SERVICES_II, NATIONAL.
    - `action` (string) **(requerido)**: Permission for call types.  * `ALLOW` - The call type is allowed.  * `BLOCK` - The call type is blocked.  * `AUTH_CODE` - Access Code action for the specified call type.  * `TRANSFER_NUMBER_1` - Transfer to Auto Transfer Number 1. The answering person can then approve the call and send it through or reject the call.  * `TRANSFER_NUMBER_2` - Transfer to Auto Transfer Number 2. The answering person can then approve the call and send it through or reject the call.  * `TRANSFER_NUMBER_3` - Transfer to Auto Transfer Number 3. The answering person can then approve the call and send it through or reject the call. Valores: ALLOW, BLOCK, AUTH_CODE, TRANSFER_NUMBER_1, TRANSFER_NUMBER_2, TRANSFER_NUMBER_3.
    - `transferEnabled` (boolean) **(requerido)**: If `true`, allows transfer and forwarding for the call type.
    - `isCallTypeRestrictionEnabled` (boolean) **(requerido)**: Indicates if the restriction is enforced by the system for the corresponding call type and cannot be changed. For example, certain call types (such as `INTERNATIONAL`) may be permanently blocked and this field will be `true` to reflect that the restriction is system-controlled and not editable.
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
