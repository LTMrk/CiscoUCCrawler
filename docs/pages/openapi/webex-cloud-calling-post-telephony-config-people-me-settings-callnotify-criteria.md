---
doc_id: webex-cloud-calling-post-telephony-config-people-me-settings-callnotify-criteria
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/people/me/settings/callNotify/criteria
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.570836+00:00
---

# POST /telephony/config/people/me/settings/callNotify/criteria

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `createMyCallNotifyCriteria`

## Resumen
Add a Call Notify Criteria

## Descripción
Create a Call Notify Criteria for the authenticated user.

Call Notify allows you to set up a unique ringtone based on predefined criteria. This is helpful, when the user wants to be quickly notified that a specific phone number is calling.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Cuerpo de la petición (application/json)
- `scheduleName` (string): Name of the schedule to be associated with the criteria.
- `scheduleType` (string): Type of the schedule.  * `businessHours` - Business hours schedule type.  * `holidays` - Holidays schedule type. Valores: businessHours, holidays.
- `scheduleLevel` (string): * `PEOPLE` - The schedule is at the user level.  * `LOCATION` - The schedule is at the location level. Valores: PEOPLE, LOCATION.
- `callsFrom` (string): Specifies the type of callsFrom, categorizing incoming data based on callsFrom types or numbers that match the current criteria.  * `ANY_PHONE_NUMBER` - The criteria applies to any phone number. * `SELECT_PHONE_NUMBERS` - The criteria applies to selected phone numbers. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS.
- `anonymousCallersEnabled` (boolean): Indicates whether anonymous callers are included in this criteria. Required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `unavailableCallersEnabled` (boolean): Indicates whether unavailable callers are included in this criteria. Required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `phoneNumbers` (array): List of phone numbers to update for this criteria. Required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `notificationEnabled` (boolean): Determines whether call notification is applied for calls matching this criteria. If `true`, call notify is applied. If `false`, this criteria acts as a 'Don't Notify Me' rule, preventing call notification. Criteria with `notificationEnabled` set to `false` (Don't Notify Me) take precedence over criteria with `notificationEnabled` set to `true` (Notify).

### Ejemplo de petición
```json
{
  "scheduleName": "Holiday V2",
  "scheduleType": "businessHours",
  "scheduleLevel": "PEOPLE",
  "callsFrom": "ANY_PHONE_NUMBER",
  "anonymousCallersEnabled": true,
  "unavailableCallersEnabled": false,
  "notificationEnabled": true
}
```

## Respuestas
- **200**: Call Notify Criteria created successfully. Returns the criteria ID.
  - `id` (string): The unique identifier for the criteria.
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
