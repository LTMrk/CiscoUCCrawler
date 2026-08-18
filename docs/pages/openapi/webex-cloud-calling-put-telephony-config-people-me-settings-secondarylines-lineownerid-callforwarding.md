---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-secondarylines-lineownerid-callforwarding
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/me/settings/secondaryLines/{lineownerId}/callForwarding
operation_id: modifyMySecondaryLinesCallForwardingSettings
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.182732+00:00
---

# PUT /telephony/config/people/me/settings/secondaryLines/{lineownerId}/callForwarding

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `modifyMySecondaryLinesCallForwardingSettings`

## Resumen
Modify My Secondary Line Owner's Call Forwarding Settings

## Descripción
Update call forwarding settings associated with a secondary line owner of the authenticated user.

Note that an authenticated user can only modify information for their configured secondary lines.

Three types of call forwarding are supported:

+ Always - forwards all incoming calls to the destination you choose.

+ When busy - forwards all incoming calls to the destination you chose while the phone is in use or the person is busy.

+ When no answer - forwarding only occurs when you are away or not answering your phone.

In addition, the Business Continuity feature will send calls to a destination of your choice if your phone is not connected to the network for any reason, such as a power outage, failed Internet connection, or wiring problem.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Parámetros
- `lineownerId` [path] (string) (**requerido**): Unique identifier for the secondary line owner (applicable only for Virtual Lines).

## Cuerpo de la petición (application/json)
- `callForwarding` (object): Settings related to "Always", "Busy", and "No Answer" call forwarding.
  - `always` (object): Settings for forwarding all incoming calls to the destination you choose.
    - `enabled` (boolean) (**requerido**): "Always" call forwarding is enabled or disabled.
    - `destination` (string): Destination for "Always" call forwarding.
    - `ringReminderEnabled` (boolean): If `true`, a brief tone will be played on the virtual line's phone when a call has been forwarded.
    - `destinationVoicemailEnabled` (boolean): Enables and disables sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
  - `busy` (object): Settings for forwarding all incoming calls to the destination you chose while the phone is in use or the virtual line is busy.
    - `enabled` (boolean): "Busy" call forwarding is enabled or disabled.
    - `destination` (string): Destination for "Busy" call forwarding.
    - `destinationVoicemailEnabled` (boolean): Enables and disables sending incoming to the destination number's voicemail if the destination is an internal phone number and that number has the voicemail service enabled.
  - `noAnswer` (object): Settings for forwarding which only occurs when you are away or not answering your phone.
    - `enabled` (boolean): "No Answer" call forwarding is enabled or disabled.
    - `destination` (string): Destination for "No Answer" call forwarding.
    - `numberOfRings` (number): Number of rings before the call will be forwarded if unanswered. `numberOfRings` must be between 2 and 20, inclusive.
    - `destinationVoicemailEnabled` (boolean): Enables and disables sending incoming to destination number's voicemail if the destination is an internal phone number and that number has the voicemail service enabled.
- `businessContinuity` (object): Settings for sending calls to a destination of your choice if your phone is not connected to the network for any reason, such as a power outage, failed Internet connection, or wiring problem.
  - `enabled` (boolean): Business Continuity is enabled or disabled.
  - `destination` (string): Destination for Business Continuity.
  - `destinationVoicemailEnabled` (boolean): Enables and disables sending incoming to destination number's voicemail if the destination is an internal phone number and that number has the voicemail service enabled.

### Ejemplo — petición
```json
{
  "callForwarding": {
    "always": {
      "enabled": false,
      "ringReminderEnabled": false,
      "destinationVoicemailEnabled": false
    },
    "busy": {
      "enabled": false,
      "destinationVoicemailEnabled": false
    },
    "noAnswer": {
      "enabled": false,
      "numberOfRings": 2,
      "destinationVoicemailEnabled": false
    }
  },
  "businessContinuity": {
    "enabled": false,
    "destinationVoicemailEnabled": false
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/me/settings/secondaryLines/<lineownerId>/callForwarding' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: No Content

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