---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-queues-queueid-callforwarding
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/queues/{queueId}/callForwarding
operation_id: getCallQueueCallForwardingSettings
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.299052+00:00
---

# GET /telephony/config/locations/{locationId}/queues/{queueId}/callForwarding

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `getCallQueueCallForwardingSettings`

## Resumen
Get Call Forwarding Settings for a Call Queue

## Descripción
Retrieve Call Forwarding settings for the specified Call Queue, including the list of call forwarding rules.

The call forwarding feature allows you to direct all incoming calls based on specific criteria that you define.
Below are the available options for configuring your call forwarding:
1. Always forward calls to a designated number.
2. Forward calls to a designated number based on certain criteria.
3. Forward calls using different modes.

Retrieving call forwarding settings for a call queue requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location in which this call queue exists.
- `queueId` [path] (string) (**requerido**): Retrieve the call forwarding settings for this call queue.
- `orgId` [query] (string): Retrieve call queue forwarding settings from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/queues/<queueId>/callForwarding' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `callForwarding` (object) (**requerido**): Settings related to `Always`, `Busy`, and `No Answer` call forwarding.
  - `always` (object) (**requerido**): Settings for forwarding all incoming calls to the destination you choose.
    - `enabled` (boolean) (**requerido**): `Always` call forwarding is enabled or disabled.
    - `destination` (string): Destination for "Always" call forwarding.
    - `ringReminderEnabled` (boolean) (**requerido**): If `true`, a brief tone will be played on the person's phone when a call has been forwarded.
    - `destinationVoicemailEnabled` (boolean) (**requerido**): Indicates enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
  - `selective` (object) (**requerido**): Selectively forward calls to a designated number, depending on criteria rules. You'll need to have at least one rule for forwarding applied for call forwarding to be active.
    - `enabled` (boolean) (**requerido**): `Busy` call forwarding is enabled or disabled.
    - `destination` (string): Destination for `Busy` call forwarding.
    - `ringReminderEnabled` (boolean) (**requerido**): If `true`, a brief tone will be played on the person's phone when a call has been forwarded.
    - `destinationVoicemailEnabled` (boolean) (**requerido**): Indicates enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
  - `rules` (array): Rules for selectively forwarding calls.
    - `id` (string) (**requerido**): Unique ID for the rule.
    - `name` (string): Unique name of rule.
    - `callFrom` (string): Comma-separated list of incoming call numbers that, when matched, will not be forwarded. A Limit of 12 numbers is allowed. Use `Any private Number` in the comma-separated value to indicate rules that match incoming calls from a private number. Use `Any unavailable number` in the comma-separated value to match incoming calls from an unavailable number.
    - `callsTo` (string): Comma-separated list of the types of numbers being matched for incoming call destination.
    - `forwardTo` (string): Number to which calls will be forwarded if the rule is of type "Forward To" and the incoming call is matched.
    - `enabled` (boolean): Reflects if rule is enabled.
  - `operatingModes` (object): Settings related to operating modes.
    - `enabled` (boolean) (**requerido**): Operating modes are enabled or disabled.
    - `currentOperatingModeId` (string) (**requerido**): The ID of the current operating mode.
    - `exceptionType` (string) (**requerido**): The exception type.  * `MANUAL_SWITCH_BACK` - The mode was switched to or extended by the user for manual switch back and runs as an exception until the user manual switches the feature back to normal operation or a different mode.  * `AUTOMATIC_SWITCH_BACK_EARLY_START` - The mode was switched to by the user before its start time and runs as an exception until its end time is reached at which point it automatically switches the feature back to normal operation.  * `AUTOMATIC_SWITCH_BACK_EXTENSION` - The current mode was extended by the user before its end time and runs as an exception until the extension end time (mode's end time + extension of up to 12 hours) is reached at which point it automatically switches the feature back to normal operation.  * `AUTOMATIC_SWITCH_BACK_STANDARD` - The mode will remain the current operating mode for the feature until its normal end time is reached. Valores: MANUAL_SWITCH_BACK, AUTOMATIC_SWITCH_BACK_EARLY_START, AUTOMATIC_SWITCH_BACK_EXTENSION, AUTOMATIC_SWITCH_BACK_STANDARD.
    - `modes` (array): Operating modes.
      - `normalOperationEnabled` (boolean) (**requerido**): Normal operation is enabled or disabled.
      - `id` (string) (**requerido**): The ID of the operating mode.
      - `name` (string) (**requerido**): The name of the operating mode.
      - `type` (string) (**requerido**): The type of the operating mode.  * `NONE` - The operating mode is not scheduled.  * `SAME_HOURS_DAILY` - Single time duration for Monday-Friday and single time duration for Saturday-Sunday.  * `DIFFERENT_HOURS_DAILY` - Individual time durations for every day of the week.  * `HOLIDAY` - Holidays which have date durations spanning multiple days, as well as an optional yearly recurrence by day or date. Valores: NONE, SAME_HOURS_DAILY, DIFFERENT_HOURS_DAILY, HOLIDAY.
      - `level` (string) (**requerido**): The level of the operating mode.  * `LOCATION` - The operating mode is at the location level.  * `ORGANIZATION` - The operating mode is at the organization level. Valores: LOCATION, ORGANIZATION.
      - `forwardTo` (object) (**requerido**): Forward to settings.
        - `selection` (string) (**requerido**): The selection for forwarding.  * `FORWARD_TO_DEFAULT_NUMBER` - When the rule matches, the mode's own default forwarding selection is to be applied.  * `FORWARD_TO_SPECIFIED_NUMBER` - When the rule matches, forward to the destination.  * `DO_NOT_FORWARD` - When the rule matches, do not forward to another number. Valores: FORWARD_TO_DEFAULT_NUMBER, FORWARD_TO_SPECIFIED_NUMBER, DO_NOT_FORWARD.
        - `destination` (string) (**requerido**): The destination for forwarding. Required when the selection is set to `FORWARD_TO_SPECIFIED_NUMBER`.
        - `destinationVoicemailEnabled` (boolean) (**requerido**): Sending incoming calls to voicemail is enabled/disabled when the destination is an internal phone number and that number has the voicemail service enabled.
        - `defaultDestination` (string) (**requerido**): The operating mode's destination.
        - `defaultDestinationVoicemailEnabled` (boolean) (**requerido**): The operating mode's destination voicemail enabled.
        - `defaultForwardToSelection` (string) (**requerido**): The operating mode's forward to selection.  * `FORWARD_TO_SPECIFIED_NUMBER` - When the rule matches, forward to the destination.  * `DO_NOT_FORWARD` - When the rule matches, do not forward to another number. Valores: FORWARD_TO_SPECIFIED_NUMBER, DO_NOT_FORWARD.

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