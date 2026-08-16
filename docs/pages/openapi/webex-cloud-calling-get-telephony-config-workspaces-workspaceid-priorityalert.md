---
doc_id: webex-cloud-calling-get-telephony-config-workspaces-workspaceid-priorityalert
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/workspaces/{workspaceId}/priorityAlert
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.674375+00:00
---

# GET /telephony/config/workspaces/{workspaceId}/priorityAlert

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (2/2)
**operationId:** `Retrieve Priority Alert Settings for a Workspace`

## Resumen
Retrieve Priority Alert Settings for a Workspace

## Descripción
Retrieve Priority Alert Settings for a Workspace.

The priority alert feature enables administrators to configure priority alert settings for a professional workspace.

This API requires a full, user, or location administrator auth token with a scope of `spark-admin:workspaces_read` or a user auth token with a scope of `spark:workspaces_read` to read workspace settings.

**NOTE**: This API is only available for professional licensed workspaces.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Unique identifier for the workspace.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Respuestas
- **200**: OK
  - `enabled` (boolean) **(requerido)**: `true` if the Priority Alert feature is enabled.
  - `criteria` (array): A list of criteria specifying conditions when priority alert is in effect.
    - `id` (string) **(requerido)**: Unique identifier for criteria.
    - `scheduleName` (string): Name of the location's schedule which determines when the priority alert is in effect.
    - `source` (string) **(requerido)**: If criteria are applicable for calls from any phone number or specific phone number.  * `ALL_NUMBERS` - Indicates that priority alert criteria apply for all incoming numbers.  * `SPECIFIC_NUMBERS` - Indicates priority alert criteria only apply to specific incoming numbers. Valores: ALL_NUMBERS, SPECIFIC_NUMBERS.
    - `notificationEnabled` (boolean) **(requerido)**: When set to `true` notification is enabled for calls that meet the current criteria. Criteria with `notificationEnabled` set to `false` take priority.
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
