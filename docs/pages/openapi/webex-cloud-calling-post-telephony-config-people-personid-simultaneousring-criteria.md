---
doc_id: webex-cloud-calling-post-telephony-config-people-personid-simultaneousring-criteria
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/people/{personId}/simultaneousRing/criteria
operation_id: createPersonSimultaneousRingCriteria
tags: User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.352431+00:00
---

# POST /telephony/config/people/{personId}/simultaneousRing/criteria

**API:** Webex Cloud Calling
**Área:** User Call Settings (3/3)
**operationId:** `createPersonSimultaneousRingCriteria`

## Resumen
Create Simultaneous Ring Criteria for a Person

## Descripción
Create simultaneous ring criteria settings for a person.

The Simultaneous Ring feature allows you to configure your office phone and other phones of your choice to ring simultaneously. Simultaneous Ring Criteria (Schedules) can also be set up to ring these phones during certain times of the day or days of the week.

Modifying requires a full, user, or location administrator auth token with a scope of `spark-admin:people_write`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): Organization ID. If not specified, uses the organization from the OAuth token.

## Cuerpo de la petición (application/json)
- `scheduleName` (string): Name of the schedule which determines when the simultaneous ring is in effect.
- `scheduleType` (string): * `businessHours` - The Schedule type that specifies the business or working hours during the day.  * `holidays` - The Schedule type that specifies the day when your organization is not open. Valores: businessHours, holidays.
- `scheduleLevel` (string): * `LOCATION` - Indicates the schedule is configured at the location level.  * `PEOPLE` - Indicates the schedule is configured at the person level. Valores: LOCATION, PEOPLE.
- `callsFrom` (string) (**requerido**): * `ANY_PHONE_NUMBER` - The Schedule applies to any phone number.  * `SELECT_PHONE_NUMBERS` - Indicates the schedule applies to select phone number defined in the `phoneNumbers` property. Valores: ANY_PHONE_NUMBER, SELECT_PHONE_NUMBERS.
- `anonymousCallersEnabled` (boolean): When `true`, the criteria applies to calls from anonymous callers. Value for this attribute is required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `unavailableCallersEnabled` (boolean): When `true`, the criteria applies to calls from unavailable callers. Value for this attribute is required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `phoneNumbers` (array): The list of phone numbers that will be checked against incoming calls for a match. Value for this attribute is required if `callsFrom` is `SELECT_PHONE_NUMBERS`.
- `ringEnabled` (boolean) (**requerido**): When set to `true` simultaneous ringing is enabled for calls that meet this criteria. Criteria with `ringEnabled` set to `false` take priority.

### Ejemplo — petición
```json
{
  "scheduleName": "Business Vacation",
  "scheduleType": "businessHours",
  "scheduleLevel": "LOCATION",
  "callsFrom": "SELECT_PHONE_NUMBERS",
  "anonymousCallersEnabled": true,
  "unavailableCallersEnabled": true,
  "phoneNumbers": [
    "+19064441748",
    "+19186663950"
  ],
  "ringEnabled": true
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/people/<personId>/simultaneousRing/criteria' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"callsFrom": "<callsFrom>", "ringEnabled": true}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): Unique identifier for the newly created criteria.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBLzg2NTAxZDFlLTg1MWMtNDgwYi1hZmE2LTA5MTU4NzQ3NzdmZQ"
}
```

## Respuestas de error
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs