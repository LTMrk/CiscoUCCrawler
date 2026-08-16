---
doc_id: webex-cloud-calling-post-telephony-config-people-me-settings-selectiveforward-criteria
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/people/me/settings/selectiveForward/criteria
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.572088+00:00
---

# POST /telephony/config/people/me/settings/selectiveForward/criteria

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `createMySelectiveCallForwardCriteria`

## Resumen
Add a Selective Call Forwarding Criteria

## Descripción
Create a Selective Call Forwarding Criteria for the authenticated user.

Selective Call Forward allows you to define rules that automatically forward incoming calls based on specific criteria, such as the caller’s phone number, caller identity, and the time and day the call is received.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Cuerpo de la petición (application/json)
- `forwardToPhoneNumber` (string): The phone number to which calls are forwarded when the criteria conditions are met.
- `destinationVoicemailEnabled` (boolean): Indicates whether calls that meet the criteria are forwarded to the destination phone number's voicemail.
- `scheduleName` (string): Name of the schedule to be associated with the criteria.
- `scheduleType` (string): Type of the schedule.  * `businessHours` - Business hours schedule type.  * `holidays` - Holidays schedule type. Valores: businessHours, holidays.
- `scheduleLevel` (string): * `PEOPLE` - The schedule is at the user level.  * `LOCATION` - The schedule is at the location level. Valores: PEOPLE, LOCATION.
- `callsFrom` (string): Specifies the type of callsFrom, categorizing incoming data based on callsFrom types or numbers that match the current criteria.  * `ANY_PHONE_NUMBER` - The criteria applies to any phone number. * `SELECT_PHONE_NUMBERS` - The criteria applies to selected phone numbers. * `ANY_INTERNAL` - The criteria applies to any internal number. * `ANY_EXTERNAL` - The criteria applies to any external number. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS, ANY_INTERNAL, ANY_EXTERNAL.
- `anonymousCallersEnabled` (boolean): Indicates whether anonymous callers are included in this criteria. Required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `unavailableCallersEnabled` (boolean): Indicates whether unavailable callers are included in this criteria. Required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `phoneNumbers` (array): List of phone numbers to update for this criteria. Required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `forwardEnabled` (boolean): Determines whether selective call forwarding is applied for calls matching this criteria. If `true`, the selective forwarding is applied. If `false`, this criteria acts as a 'Don't Forward' rule, preventing selectively forwarding of the calls. Criteria with `forwardEnabled` set to `false` (Don't Forward) take precedence over criteria with `forwardEnabled` set to `true` (Forward).

### Ejemplo de petición
```json
{
  "forwardToPhoneNumber": "+16175550100",
  "destinationVoicemailEnabled": false,
  "scheduleName": "Holiday V2",
  "scheduleType": "businessHours",
  "scheduleLevel": "PEOPLE",
  "callsFrom": "SELECT_PHONE_NUMBERS",
  "phoneNumbers": [
    "+16177817766"
  ],
  "anonymousCallersEnabled": true,
  "unavailableCallersEnabled": false,
  "forwardEnabled": true
}
```

## Respuestas
- **200**: Selective Call Forwarding Criteria created successfully. Returns the criteria ID.
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
