---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-secondarylines-lineownerid-callpickupgroup
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/secondaryLines/{lineownerId}/callPickupGroup
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.564489+00:00
---

# GET /telephony/config/people/me/settings/secondaryLines/{lineownerId}/callPickupGroup

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMySecondaryLinesCallPickupGroupSettings`

## Resumen
Get My Secondary Line Owner Call Pickup Group Settings

## Descripción
Get Call Pickup Group Settings for the secondary line owner of the authenticated user.

Note that the secondary line information is only available for the authenticated user.

Call pickup group enables a user to answer any ringing line within their pickup group. A call pickup group is an administrator-defined set of users within a location, to which the call pickup feature applies.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `lineownerId` [path] (string) **(requerido)**: Unique identifier for the secondary line owner (applicable only for Virtual Lines).

## Respuestas
- **200**: OK
  - `groupName` (string) **(requerido)**: Name of the call pickup group.
  - `memberList` (array) **(requerido)**: List of members in the call pickup group.
    - `id` (string) **(requerido)**: Unique identifier for the member.
    - `type` (string) **(requerido)**: * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
    - `firstName` (string) **(requerido)**: First name of the member.
    - `lastName` (string) **(requerido)**: Last name of the member.
    - `departmentName` (string) **(requerido)**: Department name of the member.
    - `directNumber` (string): Direct number of the member.
    - `extension` (string): Extension of the member.
    - `email` (string) **(requerido)**: Email address of the member.
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
