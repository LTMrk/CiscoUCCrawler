---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-simultaneousring
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/simultaneousRing
operation_id: getPersonSimultaneousRingSettings
tags: User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.386801+00:00
---

# GET /telephony/config/people/{personId}/simultaneousRing

**API:** Webex Cloud Calling
**Área:** User Call Settings (3/3)
**operationId:** `getPersonSimultaneousRingSettings`

## Resumen
Retrieve Simultaneous Ring Settings for a Person

## Descripción
Retrieve simultaneous ring settings for a person.

The Simultaneous Ring feature allows you to configure your office phone and other phones of your choice to ring simultaneously. Schedules can also be set up to ring these phones during certain times of the day or days of the week.

Viewing requires a full, read-only, user, or location administrator auth token with a scope of `spark-admin:people_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): Organization ID. If not specified, uses the organization from the OAuth token.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/simultaneousRing' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): When set to `true`, simultaneous ring is enabled for this person.
- `doNotRingIfOnCallEnabled` (boolean) (**requerido**): When set to `true`, the configured phone numbers won't ring when you are on a call.
- `criteriasEnabled` (boolean) (**requerido**): When `true`, enables the selected schedule for simultaneous ring.
- `phoneNumbers` (array): Enter up to 10 phone numbers to ring simultaneously when you receive an incoming call.
  - `phoneNumber` (string) (**requerido**): Phone number set for simultaneous ring.
  - `answerConfirmationEnabled` (boolean) (**requerido**): When set to `true`, the called party is required to press 1 on the keypad to confirm answer for the call.
- `criteria` (array): A list of criteria specifying conditions when simultaneous ring is in effect.
  - `id` (string) (**requerido**): Unique identifier for criteria.
  - `scheduleName` (string) (**requerido**): Name of the schedule which determines when the simultaneous ring is in effect.
  - `source` (string) (**requerido**): * `ALL_NUMBERS` - Criteria applies to all incoming numbers.  * `SPECIFIC_NUMBERS` - Criteria applies only for specific incoming numbers. Valores: ALL_NUMBERS, SPECIFIC_NUMBERS.
  - `ringEnabled` (boolean) (**requerido**): When set to `true` simultaneous ringing is enabled for calls that meet this criteria. Criteria with `ringEnabled` set to `false` take priority.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "doNotRingIfOnCallEnabled": true,
  "criteriasEnabled": true,
  "phoneNumbers": [
    {
      "phoneNumber": "+19075552859",
      "answerConfirmationEnabled": true
    },
    {
      "phoneNumber": "+19186663950",
      "answerConfirmationEnabled": false
    }
  ],
  "criteria": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBLzg2NTAxZDFlLTg1MWMtNDgwYi1hZmE2LTA5MTU4NzQ3NzdmZQ",
      "scheduleName": "Business Vacation",
      "source": "ALL_NUMBERS",
      "ringEnabled": true
    }
  ]
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