---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-sequentialring-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/sequentialRing/criteria/{id}
operation_id: getUserSequentialRingCriteria
tags: User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:16.063199+00:00
---

# GET /telephony/config/people/{personId}/sequentialRing/criteria/{id}

**API:** Webex Cloud Calling
**Área:** User Call Settings (3/3)
**operationId:** `getUserSequentialRingCriteria`

## Resumen
Get Sequential Ring Criteria for a Person

## Descripción
Retrieve a criterion from a person’s sequential ring settings.

The Sequential Ring feature lets a person configure a list of up to five phone numbers that ring one after another when the person receives incoming calls. Criteria specify schedules and incoming numbers for which sequential ringing applies or does not apply.

Retrieving a sequential ring criterion requires a full, user, or read-only administrator auth token with the `spark-admin:telephony_config_read` scope. Delegated RBAC2 access is also supported.

## Parámetros
- `personId` [path] (string) (**requerido**): Person ID for the user whose sequential ring criterion is being accessed.
- `id` [path] (string) (**requerido**): Identifier of the sequential ring criterion.
- `orgId` [query] (string): Organization ID. If not specified, uses the organization from the OAuth token.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/sequentialRing/criteria/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for criteria.
- `scheduleName` (string) (**requerido**): Name of the schedule which determines when the sequential ring is in effect.
- `scheduleType` (string) (**requerido**): The type of schedule.  * `holidays` - The Schedule is of type `holidays`.  * `businessHours` - The Schedule is of type `businessHours`. Valores: holidays, businessHours.
- `scheduleLevel` (string) (**requerido**): This indicates the level of the schedule specified by `scheduleName`. * `GROUP` - The schedule is associated with a location. * `ORGANIZATION` - The schedule is associated with an organization. Valores: GROUP, ORGANIZATION.
- `callsFrom` (string) (**requerido**): This indicates if criteria are applicable for calls from any phone number or selected phone numbers.  * `SELECT_PHONE_NUMBERS` - Sequential ring criteria only apply for selected incoming numbers.  * `ANY_PHONE_NUMBER` - Sequential ring criteria apply for any incoming number. Valores: SELECT_PHONE_NUMBERS, ANY_PHONE_NUMBER.
- `anonymousCallersEnabled` (boolean): When `true` incoming calls from private numbers are allowed. This is only applicable when `callsFrom` is set to `SELECT_PHONE_NUMBERS`.
- `unavailableCallersEnabled` (boolean): When `true` incoming calls from unavailable numbers are allowed. This is only applicable when `callsFrom` is set to `SELECT_PHONE_NUMBERS`.
- `phoneNumbers` (array): When callsFrom is set to `SELECT_PHONE_NUMBERS`, indicates a list of incoming phone numbers for which the criteria apply.
- `ringEnabled` (boolean) (**requerido**): When set to `true` sequential ringing is enabled for calls that meet the current criteria. Criteria with `ringEnabled` set to `false` take priority.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1NRLUNyaXRlcmlhLUQtMQ",
  "scheduleName": "BusinessHours_Main",
  "scheduleType": "businessHours",
  "scheduleLevel": "PEOPLE",
  "callsFrom": "SELECT_PHONE_NUMBERS",
  "anonymousCallersEnabled": false,
  "unavailableCallersEnabled": false,
  "phoneNumbers": [
    "+12065550111"
  ],
  "ringEnabled": true
}
```

## Respuestas de error
- **400**: Bad Request: A required field is missing, a field value is invalid, a value is outside its allowed range, or a phone number is not in E.164 format.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The target person or sequential ring criterion does not exist.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The resource is temporarily unavailable. A Retry-After header may specify when to retry.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: The request has been rate limited. A Retry-After header may specify when to retry.
- **500**: Internal Server Error.
- **502**: Bad Gateway: The server received an invalid response from an upstream server. Try again later.
- **503**: Service Unavailable: The server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs