---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-sequentialring-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/people/me/settings/sequentialRing/criteria/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.574382+00:00
---

# PUT /telephony/config/people/me/settings/sequentialRing/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase3
**operationId:** `updateMySequentialRingCriteriaSettings`

## Resumen
Modify Sequential Ring Criteria Settings for User

## Descripción
Update Sequential Ring Criteria Settings for the authenticated user.

Sequential Ring criteria defines rules for when sequential ring should activate based on the caller and schedule.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Parámetros
- `id` [path] (string) **(requerido)**: The `id` parameter specifies the unique identifier for the sequential ring criteria. Example: `Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1oxNzU0MzgzODQzNTA5NzY`.

## Cuerpo de la petición (application/json)
- `scheduleName` (string): Name of the schedule to be associated with the criteria.
- `scheduleType` (string): Type of the schedule.  * `businessHours` - Business hours schedule type.  * `holidays` - Holidays schedule type. Valores: businessHours, holidays.
- `scheduleLevel` (string): * `PEOPLE` - The schedule is at the user level.  * `LOCATION` - The schedule is at the location level. Valores: PEOPLE, LOCATION.
- `callsFrom` (string): Specifies the type of calling numbers the criteria applies to.  * `ANY_PHONE_NUMBER` - The criteria applies to any phone number.  * `SELECT_PHONE_NUMBERS` - The criteria applies to selected phone numbers. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS.
- `anonymousCallersEnabled` (boolean): When `true`, means this criteria applies for anonymous callers. Required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `unavailableCallersEnabled` (boolean): When `true`, means this criteria applies for unavailable callers. Required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `phoneNumbers` (array): List of phone numbers to update for this criteria. Required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `ringEnabled` (boolean): Determines whether sequential ring is applied for calls matching this criteria. If `true`, sequential ring is applied. Criteria with ringEnabled set to false have precedence over criteria with ringEnabled set to true.

### Ejemplo de petición
```json
{
  "scheduleName": "Holidays",
  "scheduleType": "holidays",
  "scheduleLevel": "LOCATION",
  "callsFrom": "ANY_PHONE_NUMBER",
  "ringEnabled": false
}
```

## Respuestas
- **204**: Sequential Ring Criteria Settings updated successfully for the authenticated user.
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
