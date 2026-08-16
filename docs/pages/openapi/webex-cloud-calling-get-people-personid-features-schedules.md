---
doc_id: webex-cloud-calling-get-people-personid-features-schedules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /people/{personId}/features/schedules
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.641069+00:00
---

# GET /people/{personId}/features/schedules

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `List of Schedules for a Person`

## Resumen
List of Schedules for a Person

## Descripción
List schedules for a person in an organization.

Schedules are used to support calling features and can be defined at the location or person level. `businessHours` schedules allow you to apply specific call settings at different times of the day or week by defining one or more events. `holidays` schedules define exceptions to normal business hours by defining one or more events.

This API requires a full, user, or read-only administrator auth token with a scope of `spark-admin:people_read`.

## Parámetros
- `personId` [path] (string) **(requerido)**: Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
- `start` [query] (number): Specifies the offset from the first result that you want to fetch.
- `max` [query] (number): Specifies the maximum number of records that you want to fetch.
- `name` [query] (string): Specifies the case insensitive substring to be matched against the schedule names. The maximum length is 40.
- `type` [query] (string): Specifies the schedule event type to be matched on the given type.

## Respuestas
- **200**: OK
  - `schedules` (array) **(requerido)**: List of schedules.
    - `id` (string) **(requerido)**: Identifier for a schedule.
    - `name` (string) **(requerido)**: Name for the schedule.
    - `type` (string) **(requerido)**: * `businessHours` - The schedule type that specifies the business or working hours during the day.  * `holidays` - The schedule type that specifies the day when your organization is not open. Valores: businessHours, holidays.
    - `level` (string): * `PEOPLE` - The schedule level that specifies that criteria is of People level.  * `GROUP` - The schedule level that specifies that criteria is of Group level. Valores: PEOPLE, GROUP.
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
