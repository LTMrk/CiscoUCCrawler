---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-executive-alert
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/executive/alert
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.568137+00:00
---

# GET /telephony/config/people/me/settings/executive/alert

**API:** Webex Cloud Calling
**Área:** Beta Call Settings For Me With Userhub Phase1
**operationId:** `getMyExecutiveAlertSettings`

## Resumen
Get User Executive Alert Settings

## Descripción
Get executive alert settings for the authenticated user.

Executive Alert settings in Webex allow you to control how calls are routed to executive assistants, including alerting mode, rollover options, and caller ID presentation. You can configure settings such as sequential or simultaneous alerting, and specify what happens when calls aren't answered.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Respuestas
- **200**: User executive alert settings retrieved successfully.
  - `alertingMode` (string) **(requerido)**: * `SEQUENTIAL` - Alerts assistants one at a time in the defined order.  * `SIMULTANEOUS` - Alerts all assistants at the same time. Valores: SEQUENTIAL, SIMULTANEOUS.
  - `nextAssistantNumberOfRings` (integer): Number of rings before alerting the next assistant when `alertingMode` is `SEQUENTIAL`.
  - `rolloverEnabled` (boolean): Controls whether the rollover timer (`rolloverWaitTimeInSecs`) is enabled. When set to `true`, rollover will trigger after the timer expires, even if assistants are still available. When `false`, rollover only occurs when no assistants remain.
  - `rolloverAction` (string): Specifies what happens when rollover is triggered.  * `VOICE_MESSAGING` - The call is sent to the executive's voicemail.  * `FORWARD` - The call is forwarded to the specified destination (`rolloverForwardToPhoneNumber`).  * `NO_ANSWER_PROCESSING` - The call is sent to no answer processing which may trigger executive services such as call forwarding or voicemail. Rollover is always triggered when no assistants remain for a filtered call. If the rollover timer is enabled, rollover can also be triggered when the timer expires, even if assistants are still available. Valores: VOICE_MESSAGING, NO_ANSWER_PROCESSING, FORWARD.
  - `rolloverForwardToPhoneNumber` (string): Phone number to forward calls to when rollover action is set to `FORWARD`.
  - `rolloverWaitTimeInSecs` (integer) **(requerido)**: Time in seconds to wait before applying the rollover action when `rolloverEnabled` is `true`.
  - `clidNameMode` (string) **(requerido)**: Controls how Caller ID name is displayed on assistant's phone.  * `EXECUTIVE_ORIGINATOR` - Display executive name followed by caller name.  * `ORIGINATOR_EXECUTIVE` - Display caller name followed by executive name.  * `EXECUTIVE` - Display only executive name.  * `ORIGINATOR` - Display only caller name.  * `CUSTOM` - Display a custom name. Valores: EXECUTIVE_ORIGINATOR, ORIGINATOR_EXECUTIVE, EXECUTIVE, ORIGINATOR, CUSTOM.
  - `customCLIDName` (string): Custom caller ID name to display when `clidNameMode` is set to `CUSTOM` (deprecated).
  - `customCLIDNameInUnicode` (string): Unicode Custom caller ID name to display when `clidNameMode` is set to `CUSTOM`.
  - `clidPhoneNumberMode` (string) **(requerido)**: Controls which Caller ID phone number is displayed on assistant's phone.  * `EXECUTIVE` - Display executive's phone number.  * `ORIGINATOR` - Display caller's phone number.  * `CUSTOM` - Display a custom phone number. Valores: EXECUTIVE, ORIGINATOR, CUSTOM.
  - `customCLIDPhoneNumber` (string): Custom caller ID phone number to display on assistant's phone when `clidPhoneNumberMode` is set to `CUSTOM`.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
