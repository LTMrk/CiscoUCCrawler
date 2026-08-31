---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-selectiveforward-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/me/settings/selectiveForward/criteria/{id}
operation_id: updateMySelectiveCallForwardingCriteriaSettings
tags: Call Settings For Me With UserHub Phase2
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.163536+00:00
---

# PUT /telephony/config/people/me/settings/selectiveForward/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `updateMySelectiveCallForwardingCriteriaSettings`

## Resumen
Modify Settings for a Selective Call Forwarding Criteria

## Descripción
Modify settings for a Selective Call Forwarding Criteria for the authenticated user.

Selective Call Forward allows you to define rules that automatically forward incoming calls based on specific criteria, such as the caller’s phone number, caller identity, and the time and day the call is received.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Parámetros
- `id` [path] (string) (**requerido**): The `id` parameter specifies the unique identifier for the selective call forwarding criteria. Example: `Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1oxNzU0MzgzODQzNTA5NzY`.

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

### Ejemplo — petición
```json
{
  "forwardToPhoneNumber": "+16175550100",
  "destinationVoicemailEnabled": true,
  "scheduleName": "Holiday ABC",
  "scheduleType": "holidays",
  "scheduleLevel": "LOCATION",
  "callsFrom": "ANY_PHONE_NUMBER",
  "anonymousCallersEnabled": false,
  "unavailableCallersEnabled": true,
  "forwardEnabled": true
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/me/settings/selectiveForward/criteria/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: Selective Call Forward Criteria Settings updated successfully.

## Respuestas de error
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs