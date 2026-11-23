---
doc_id: webex-cloud-calling-post-telephony-config-people-personid-priorityalert-criteria
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/people/{personId}/priorityAlert/criteria
operation_id: createPersonPriorityAlertCriteria
tags: User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:16.061239+00:00
---

# POST /telephony/config/people/{personId}/priorityAlert/criteria

**API:** Webex Cloud Calling
**Área:** User Call Settings (3/3)
**operationId:** `createPersonPriorityAlertCriteria`

## Resumen
Add a Priority Alert Criterion for a Person

## Descripción
Create a Priority Alert criterion for a person.

Priority alert allows setting up a distinctive ringtone based on predefined criteria. This is helpful when a person wants to be quickly notified that a specific phone number is calling.

This API requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `personId` [path] (string) (**requerido**): A unique identifier for the person.
- `orgId` [query] (string): Optional target organization identifier. Defaults to the token's organization if not provided. A partner administrator must provide this value to specify the target organization.

## Cuerpo de la petición (application/json)
- `scheduleName` (string): Name of the schedule to be associated with the criterion. When provided with a non-empty value, `scheduleType` and `scheduleLevel` must also be provided. Omit this field or set it to an empty string to create the criterion without a schedule association. When no schedule is associated, the criterion is active every day, all day. Valid schedule names are 1 to 40 characters. An empty string is allowed in POST requests only to create a criterion without a schedule association. Long. max: 40.
- `scheduleType` (string): Type of the schedule. Provide this with a non-empty `scheduleName` and matching `scheduleLevel`. Omit it when `scheduleName` is omitted, `null`, or an empty string.  * `businessHours` - The Schedule type that specifies the business or working hours during the day.  * `holidays` - The Schedule type that specifies the days when your organization is not open. Valores: businessHours, holidays.
- `scheduleLevel` (string): This indicates the level of the schedule specified by `scheduleName`. Provide this with a non-empty `scheduleName` and matching `scheduleType`. Omit it when `scheduleName` is omitted, `null`, or an empty string.  * `PEOPLE` - The schedule is at the person level.  * `LOCATION` - The schedule is at the location level.  * `ORGANIZATION` - The schedule is at the organization level. Valores: PEOPLE, LOCATION, ORGANIZATION.
- `callsFrom` (string) (**requerido**): Identifies which incoming calls this criterion applies to. When set to `SELECT_PHONE_NUMBERS`, `anonymousCallersEnabled`, `unavailableCallersEnabled`, and `phoneNumbers` are required, and at least one phone number or caller flag must be provided. `ANY_PHONE_NUMBER` is equivalent to `ALL_NUMBERS` and `SELECT_PHONE_NUMBERS` is equivalent to `SPECIFIC_NUMBERS` in the priority alert settings API.  * `ANY_PHONE_NUMBER` - Criterion applies to any external phone number.  * `SELECT_PHONE_NUMBERS` - Criterion applies to selected phone numbers.  * `ANY_INTERNAL` - Criterion applies to any internal source. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS, ANY_INTERNAL.
- `anonymousCallersEnabled` (boolean): Indicates whether anonymous callers are included in this criterion. Required when `callsFrom` is `SELECT_PHONE_NUMBERS`; omit otherwise.
- `unavailableCallersEnabled` (boolean): Indicates whether unavailable callers are included in this criterion. Required when `callsFrom` is `SELECT_PHONE_NUMBERS`; omit otherwise.
- `phoneNumbers` (array): List of phone numbers for this criterion. Required when `callsFrom` is `SELECT_PHONE_NUMBERS`; omit otherwise. An empty array is allowed only when `anonymousCallersEnabled` or `unavailableCallersEnabled` is `true`.
- `notificationEnabled` (boolean) (**requerido**): Determines whether priority alerting is applied for calls matching this criterion. This field is required and cannot be `null`. If `true`, priority alerting is applied. If `false`, this criterion acts as a 'Don't Alert' rule, preventing priority alerting. Criteria with `notificationEnabled` set to `false` (Don't Alert) take precedence over criteria with `notificationEnabled` set to `true` (Alert).
- `ringPattern` (string): The distinctive ringtone pattern applied to incoming calls that match the priority alert criterion, allowing the person to distinguish priority calls from regular calls by their ringtone pattern. Defaults to `LONG_LONG` when omitted.  * `NORMAL` - Standard ring pattern.  * `LONG_LONG` - Two long rings.  * `SHORT_LONG_SHORT` - Short ring, long ring, short ring.  * `SHORT_SHORT_LONG` - Two short rings followed by a long ring. Valores: NORMAL, LONG_LONG, SHORT_LONG_SHORT, SHORT_SHORT_LONG.

### Ejemplo — petición
```json
{
  "scheduleName": "Holiday V2",
  "scheduleType": "businessHours",
  "scheduleLevel": "PEOPLE",
  "callsFrom": "ANY_PHONE_NUMBER",
  "anonymousCallersEnabled": true,
  "unavailableCallersEnabled": false,
  "notificationEnabled": true,
  "ringPattern": "LONG_LONG"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/people/<personId>/priorityAlert/criteria' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"callsFrom": "<callsFrom>", "notificationEnabled": true}'
```

## Respuestas correctas
**201**: Priority Alert criterion created successfully. Returns the criterion ID.
- `id` (string) (**requerido**): The unique identifier for the criteria.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1oxNzU0MzgzODQzNTA5NzY"
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a person, does not exist. Also returned when the requested format is not supported by the requested method.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs