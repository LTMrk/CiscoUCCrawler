---
doc_id: webex-cloud-calling-put-telephony-config-people-personid-executive-alert
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/{personId}/executive/alert
operation_id: updatePersonExecutiveAlertSettings
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.384473+00:00
---

# PUT /telephony/config/people/{personId}/executive/alert

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `updatePersonExecutiveAlertSettings`

## Resumen
Modify Person Executive Alert Settings

## Descripción
Update executive alert settings for the specified person.

Executive Alert settings in Webex allow you to control how calls are routed to executive assistants, including alerting mode, rollover options, and caller ID presentation. You can configure settings such as sequential or simultaneous alerting, and specify what happens when calls aren't answered.

This API requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `personId` [path] (string) (**requerido**): A unique identifier for the person.
- `orgId` [query] (string): Organization ID for the person.

## Cuerpo de la petición (application/json)
- `alertingMode` (string): * `SEQUENTIAL` - Alerts assistants one at a time in the defined order.  * `SIMULTANEOUS` - Alerts all assistants at the same time. Valores: SEQUENTIAL, SIMULTANEOUS.
- `nextAssistantNumberOfRings` (integer): Number of rings before alerting the next assistant when `alertingMode` is `SEQUENTIAL`.
- `rolloverEnabled` (boolean): Controls whether the rollover timer (`rolloverWaitTimeInSecs`) is enabled. When set to `true`, rollover will trigger after the timer expires, even if assistants are still available. When `false`, rollover only occurs when no assistants remain.
- `rolloverAction` (string): Specifies what happens when rollover is triggered.  * `VOICE_MESSAGING` - The call is sent to the executive's voicemail.  * `FORWARD` - The call is forwarded to the specified destination (`rolloverForwardToPhoneNumber`).  * `NO_ANSWER_PROCESSING` - The call is sent to no answer processing which may trigger executive services such as call forwarding or voicemail. Rollover is always triggered when no assistants remain for a filtered call. If the rollover timer is enabled, rollover can also be triggered when the timer expires, even if assistants are still available. Valores: VOICE_MESSAGING, NO_ANSWER_PROCESSING, FORWARD.
- `rolloverForwardToPhoneNumber` (string): Phone number to forward calls to when rollover action is set to `FORWARD`.
- `rolloverWaitTimeInSecs` (integer): Time in seconds to wait before applying the rollover action when `rolloverEnabled` is `true`.
- `clidNameMode` (string): Controls how Caller ID name is displayed on assistant's phone.  * `EXECUTIVE_ORIGINATOR` - Display executive name followed by caller name.  * `ORIGINATOR_EXECUTIVE` - Display caller name followed by executive name.  * `EXECUTIVE` - Display only executive name.  * `ORIGINATOR` - Display only caller name.  * `CUSTOM` - Display a custom name. Valores: EXECUTIVE_ORIGINATOR, ORIGINATOR_EXECUTIVE, EXECUTIVE, ORIGINATOR, CUSTOM.
- `customCLIDName` (string): Custom caller ID name to display when `clidNameMode` is set to `CUSTOM` (deprecated).
- `customCLIDNameInUnicode` (string): Unicode Custom caller ID name to display when `clidNameMode` is set to `CUSTOM`.
- `clidPhoneNumberMode` (string): Controls which Caller ID phone number is displayed on assistant's phone.  * `EXECUTIVE` - Display executive's phone number.  * `ORIGINATOR` - Display caller's phone number.  * `CUSTOM` - Display a custom phone number. Valores: EXECUTIVE, ORIGINATOR, CUSTOM.
- `customCLIDPhoneNumber` (string): Custom caller ID phone number to display on assistant's phone when `clidPhoneNumberMode` is set to `CUSTOM`.

### Ejemplo — petición
```json
{
  "alertingMode": "SEQUENTIAL",
  "nextAssistantNumberOfRings": 3,
  "rolloverEnabled": true,
  "rolloverAction": "VOICE_MESSAGING",
  "rolloverForwardToPhoneNumber": "",
  "rolloverWaitTimeInSecs": 60,
  "clidNameMode": "EXECUTIVE_ORIGINATOR",
  "customCLIDName": "John Anderson",
  "customCLIDNameInUnicode": "John Anderson",
  "clidPhoneNumberMode": "EXECUTIVE",
  "customCLIDPhoneNumber": ""
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/<personId>/executive/alert' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: Person executive alert settings modified successfully.

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs