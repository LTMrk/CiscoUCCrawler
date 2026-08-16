---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-selectivereject-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/{personId}/selectiveReject/criteria/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.650018+00:00
---

# GET /telephony/config/people/{personId}/selectiveReject/criteria/{id}

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getCriteriaForUserSelectiveCallRejectionService`

## Resumen
Get a Criteria for the User’s Selective Call Rejection Service

## Descripción
Get a criteria for the user's selective call rejection service.

With the Selective Call Rejection feature, you can create different rules to reject specific calls based on the phone number, who's calling, and/or the time and day of the call.

Requires a full, user, read-only, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) **(requerido)**: A unique identifier for the person.
- `id` [path] (string) **(requerido)**: Criteria ID.
- `orgId` [query] (string): Organization in which the user resides.

## Respuestas
- **200**: OK
  - `id` (string): Criteria ID.
  - `scheduleName` (string): Name of the schedule to which the criteria is created.
  - `scheduleType` (string): * `businessHours` - The schedule type that specifies the business or working hours during the day.  * `holidays` - The schedule type that specifies the day when your organization is not open. Valores: businessHours, holidays.
  - `scheduleLevel` (string): * `PEOPLE` - The schedule level that specifies that criteria is of People level.  * `GROUP` - The schedule level that specifies that criteria is of Group level. Valores: PEOPLE, GROUP.
  - `callsFrom` (string) **(requerido)**: * `ANY_PHONE_NUMBER` - Criteria apply for any incoming number.  * `SELECT_PHONE_NUMBERS` - Criteria only apply for selected incoming numbers.  * `FORWARDED` - Criteria only apply for forwarded incoming numbers. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS, FORWARDED.
  - `anonymousCallersEnabled` (boolean): Boolean flag indicating if calls from custom numbers, private numbers are enabled.
  - `unavailableCallersEnabled` (boolean): Boolean flag indicating if calls from custom numbers, unavailable numbers are enabled.
  - `phoneNumbers` (array): List of phone numbers. It does not include extensions. In some regions phone numbers are not returned in E.164 format. This will be supported in a future update.
  - `rejectEnabled` (boolean) **(requerido)**: Boolean flag to enable/disable rejection.
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
