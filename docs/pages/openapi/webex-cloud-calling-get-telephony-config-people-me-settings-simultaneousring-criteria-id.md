---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-simultaneousring-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/simultaneousRing/criteria/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.576059+00:00
---

# GET /telephony/config/people/me/settings/simultaneousRing/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Call Settings For Me Phase 4
**operationId:** `getMySimultaneousRingCriteria`

## Resumen
Retrieve My Simultaneous Ring Criteria

## Descripción
Retrieve simultaneous ring criteria settings for the authenticated user.

The Simultaneous Ring feature allows you to configure your office phone and other phones of your choice to ring simultaneously. Simultaneous Ring Criteria (Schedules) can also be set up to ring these phones during certain times of the day or days of the week.

Retrieving criteria requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `id` [path] (string) **(requerido)**: Unique identifier for the criteria.

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Unique identifier for criteria.
  - `scheduleName` (string): Name of the schedule which determines when the simultaneous ring is in effect.
  - `scheduleType` (string): * `businessHours` - The schedule type that specifies the business or working hours during the day.  * `holidays` - The schedule type that specifies the day when your organization is not open. Valores: businessHours, holidays.
  - `scheduleLevel` (string): * `PEOPLE` - The schedule level that specifies that criteria is of People level.  * `GROUP` - The schedule level that specifies that criteria is of Group level. Valores: PEOPLE, GROUP.
  - `callsFrom` (string) **(requerido)**: * `ANY_PHONE_NUMBER` - The Schedule applies to any phone number.  * `SELECT_PHONE_NUMBERS` - Indicates the schedule applies to select phone number defined in the `phoneNumbers` property. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS.
  - `anonymousCallersEnabled` (boolean) **(requerido)**: When `true`, the criteria applies to calls from anonymous callers.
  - `unavailableCallersEnabled` (boolean) **(requerido)**: When `true`, the criteria applies to calls from unavailable callers.
  - `phoneNumbers` (array): The list of phone numbers that will checked against incoming calls for a match.
  - `ringEnabled` (boolean) **(requerido)**: When set to `true` simultaneous ringing is enabled for calls that meet this criteria. Criteria with `ringEnabled` set to `false` take priority.
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
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
