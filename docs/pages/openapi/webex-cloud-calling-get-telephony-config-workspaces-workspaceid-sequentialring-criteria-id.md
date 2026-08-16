---
doc_id: webex-cloud-calling-get-telephony-config-workspaces-workspaceid-sequentialring-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/workspaces/{workspaceId}/sequentialRing/criteria/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.670978+00:00
---

# GET /telephony/config/workspaces/{workspaceId}/sequentialRing/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Workspace Call Settings (2/2)
**operationId:** `Retrieve Sequential Ring Criteria for a Workspace`

## Resumen
Retrieve Sequential Ring Criteria for a Workspace

## Descripción
Retrieve sequential ring criteria for a workspace.

The sequential ring feature enables you to create a list of up to five phone numbers. When the workspace receives incoming calls, these numbers will ring one after another.
The sequential ring criteria specify settings such as schedule and incoming numbers for which to sequentially ring or not.

This API requires a full, read-only or location administrator auth token with a scope of `spark-admin:workspaces_read` to read workspace settings.

**NOTE**: This API is only available for professional licensed workspaces.

## Parámetros
- `workspaceId` [path] (string) **(requerido)**: Unique identifier for the workspace.
- `id` [path] (string) **(requerido)**: Unique identifier for the criteria.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Unique identifier for criteria.
  - `scheduleName` (string) **(requerido)**: Name of the location's schedule which determines when the sequential ring is in effect.
  - `scheduleType` (string) **(requerido)**: The type of schedule.  * `holidays` - The Schedule is of type `holidays`.  * `businessHours` - The Schedule is of type `businessHours`. Valores: holidays, businessHours.
  - `scheduleLevel` (string) **(requerido)**: This indicates the level of the schedule specified by `scheduleName`.  * `GROUP` - The Schedule specified is of `GROUP` level. Valores: GROUP.
  - `callsFrom` (string) **(requerido)**: This indicates if criteria are applicable for calls from any phone number or selected phone numbers.  * `SELECT_PHONE_NUMBERS` - Sequential ring criteria only apply for selected incoming numbers.  * `ANY_PHONE_NUMBER` - Sequential ring criteria apply for any incoming number. Valores: SELECT_PHONE_NUMBERS, ANY_PHONE_NUMBER.
  - `anonymousCallersEnabled` (boolean): When `true` incoming calls from private numbers are allowed. This is only applicable when `callsFrom` is set to `SELECT_PHONE_NUMBERS`.
  - `unavailableCallersEnabled` (boolean): When `true` incoming calls from unavailable numbers are allowed. This is only applicable when `callsFrom` is set to `SELECT_PHONE_NUMBERS`.
  - `phoneNumbers` (array): When callsFrom is set to `SELECT_PHONE_NUMBERS`, indicates a list of incoming phone numbers for which the criteria apply.
  - `ringEnabled` (boolean) **(requerido)**: When set to `true` sequential ringing is enabled for calls that meet the current criteria. Criteria with `ringEnabled` set to `false` take priority.
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
