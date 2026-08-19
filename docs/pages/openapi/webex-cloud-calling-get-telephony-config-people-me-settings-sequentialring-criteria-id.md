---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-sequentialring-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/sequentialRing/criteria/{id}
operation_id: getMySequentialRingCriteriaSettings
tags: Call Settings For Me With UserHub Phase3
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.976309+00:00
---

# GET /telephony/config/people/me/settings/sequentialRing/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase3
**operationId:** `getMySequentialRingCriteriaSettings`

## Resumen
Get Sequential Ring Criteria Settings for User

## Descripción
Get Sequential Ring Criteria Settings for the authenticated user.

Sequential Ring criteria defines rules for when sequential ring should activate based on the caller and schedule.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `id` [path] (string) (**requerido**): The `id` parameter specifies the unique identifier for the sequential ring criteria. Example: `Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1oxNzU0MzgzODQzNTA5NzY`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/sequentialRing/criteria/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Sequential Ring Criteria Settings retrieved for the authenticated user.
- `id` (string) (**requerido**): Unique identifier for criteria.
- `scheduleName` (string) (**requerido**): Name of the location's schedule which determines when the sequential ring is in effect.
- `scheduleType` (string) (**requerido**): The type of schedule.  * `holidays` - The Schedule is of type `holidays`.  * `businessHours` - The Schedule is of type `businessHours`. Valores: holidays, businessHours.
- `scheduleLevel` (string) (**requerido**): This indicates the level of the schedule specified by `scheduleName`.  * `GROUP` - The Schedule specified is of `GROUP` level. Valores: GROUP.
- `callsFrom` (string) (**requerido**): This indicates if criteria are applicable for calls from any phone number or selected phone numbers.  * `SELECT_PHONE_NUMBERS` - Sequential ring criteria only apply for selected incoming numbers.  * `ANY_PHONE_NUMBER` - Sequential ring criteria apply for any incoming number. Valores: SELECT_PHONE_NUMBERS, ANY_PHONE_NUMBER.
- `anonymousCallersEnabled` (boolean): When `true` incoming calls from private numbers are allowed. This is only applicable when `callsFrom` is set to `SELECT_PHONE_NUMBERS`.
- `unavailableCallersEnabled` (boolean): When `true` incoming calls from unavailable numbers are allowed. This is only applicable when `callsFrom` is set to `SELECT_PHONE_NUMBERS`.
- `phoneNumbers` (array): When callsFrom is set to `SELECT_PHONE_NUMBERS`, indicates a list of incoming phone numbers for which the criteria apply.
- `ringEnabled` (boolean) (**requerido**): When set to `true` sequential ringing is enabled for calls that meet the current criteria. Criteria with `ringEnabled` set to `false` take priority.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1oxNzU0MzgzODQzNTA5NzY",
  "scheduleName": "BusinessHours",
  "scheduleType": "businessHours",
  "scheduleLevel": "PEOPLE",
  "callsFrom": "SELECT_PHONE_NUMBERS",
  "anonymousCallersEnabled": false,
  "unavailableCallersEnabled": false,
  "phoneNumbers": [
    "+16177817765"
  ],
  "ringEnabled": true
}
```

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