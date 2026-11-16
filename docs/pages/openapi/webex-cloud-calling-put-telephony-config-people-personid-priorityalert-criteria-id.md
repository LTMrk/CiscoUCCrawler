---
doc_id: webex-cloud-calling-put-telephony-config-people-personid-priorityalert-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/{personId}/priorityAlert/criteria/{id}
operation_id: updatePersonPriorityAlertCriteriaSettings
tags: User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.818761+00:00
---

# PUT /telephony/config/people/{personId}/priorityAlert/criteria/{id}

**API:** Webex Cloud Calling
**Área:** User Call Settings (3/3)
**operationId:** `updatePersonPriorityAlertCriteriaSettings`

## Resumen
Modify Priority Alert Criterion for a Person

## Descripción
Modify Priority Alert criterion settings for a person.

Priority alert allows setting up a distinctive ringtone based on predefined criteria. This API allows modifying attributes such as name, phoneNumbers etc. for a particular criterion.

This API requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `personId` [path] (string) (**requerido**): A unique identifier for the person.
- `id` [path] (string) (**requerido**): Unique identifier for the priority alert criterion.
- `orgId` [query] (string): Optional target organization identifier. Defaults to the token's organization if not provided. A partner administrator must provide this value to specify the target organization.

## Cuerpo de la petición (application/json)
- `scheduleName` (string): Name of the schedule to be associated with the criterion. When provided with a non-empty value, `scheduleType` and `scheduleLevel` must also be provided. Set `scheduleName` to `null` or an empty string to remove the current schedule association. When no schedule is associated, the criterion is active every day, all day. Omit it to preserve the existing schedule. Valid schedule names are 1 to 40 characters. An empty string is allowed in PUT requests only to remove the schedule association. Long. max: 40.
- `scheduleType` (string): Type of the schedule. Provide this with a non-empty `scheduleName` and matching `scheduleLevel`. Omit it when `scheduleName` is omitted or used to clear the schedule. This field is not independently clearable.  * `businessHours` - The Schedule type that specifies the business or working hours during the day.  * `holidays` - The Schedule type that specifies the days when your organization is not open. Valores: businessHours, holidays.
- `scheduleLevel` (string): This indicates the level of the schedule specified by `scheduleName`. Provide this with a non-empty `scheduleName` and matching `scheduleType`. Omit it when `scheduleName` is omitted or used to clear the schedule. This field is not independently clearable.  * `PEOPLE` - The schedule is at the person level.  * `LOCATION` - The schedule is at the location level.  * `ORGANIZATION` - The schedule is at the organization level. Valores: PEOPLE, LOCATION, ORGANIZATION.
- `callsFrom` (string): Identifies which incoming calls this criterion applies to. Omit it to preserve the existing call source selection. When set to `SELECT_PHONE_NUMBERS`, `anonymousCallersEnabled`, `unavailableCallersEnabled`, and `phoneNumbers` are required, and at least one phone number or caller flag must be provided. `ANY_PHONE_NUMBER` is equivalent to `ALL_NUMBERS` and `SELECT_PHONE_NUMBERS` is equivalent to `SPECIFIC_NUMBERS` in the priority alert settings API.  * `ANY_PHONE_NUMBER` - Criterion applies to any external phone number.  * `SELECT_PHONE_NUMBERS` - Criterion applies to selected phone numbers.  * `ANY_INTERNAL` - Criterion applies to any internal source. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS, ANY_INTERNAL.
- `anonymousCallersEnabled` (boolean): Indicates whether anonymous callers are included in this criterion. Required when `callsFrom` is `SELECT_PHONE_NUMBERS`; omit otherwise.
- `unavailableCallersEnabled` (boolean): Indicates whether unavailable callers are included in this criterion. Required when `callsFrom` is `SELECT_PHONE_NUMBERS`; omit otherwise.
- `phoneNumbers` (array): List of phone numbers to update for this criterion. Required when `callsFrom` is `SELECT_PHONE_NUMBERS`; omit otherwise. An empty array is allowed only when `anonymousCallersEnabled` or `unavailableCallersEnabled` is `true`.
- `notificationEnabled` (boolean): Determines whether priority alerting is applied for calls matching this criterion. Omit it to preserve the current value. This field cannot be cleared with `null`. If `true`, priority alerting is applied. If `false`, this criterion acts as a 'Don't Alert' rule, preventing priority alerting. Criteria with `notificationEnabled` set to `false` (Don't Alert) take precedence over criteria with `notificationEnabled` set to `true` (Alert).
- `ringPattern` (string): The distinctive ringtone pattern applied to incoming calls that match the priority alert criterion, allowing the person to distinguish priority calls from regular calls by their ringtone pattern. Omit it to preserve the current value. This field cannot be cleared with `null`.  * `NORMAL` - Standard ring pattern.  * `LONG_LONG` - Two long rings.  * `SHORT_LONG_SHORT` - Short ring, long ring, short ring.  * `SHORT_SHORT_LONG` - Two short rings followed by a long ring. Valores: NORMAL, LONG_LONG, SHORT_LONG_SHORT, SHORT_SHORT_LONG.

### Ejemplo — petición
```json
{
  "scheduleName": "Holiday V2",
  "scheduleType": "holidays",
  "scheduleLevel": "LOCATION",
  "callsFrom": "SELECT_PHONE_NUMBERS",
  "anonymousCallersEnabled": true,
  "unavailableCallersEnabled": true,
  "notificationEnabled": true,
  "phoneNumbers": [
    "+16177817766"
  ],
  "ringPattern": "LONG_LONG"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/<personId>/priorityAlert/criteria/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: Priority Alert criterion settings updated successfully for the person.

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a person, does not exist. Also returned when the requested format is not supported by the requested method.
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs