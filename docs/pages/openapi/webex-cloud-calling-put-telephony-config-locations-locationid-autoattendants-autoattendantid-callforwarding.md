---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-autoattendants-autoattendantid-callforwarding
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}/callForwarding
operation_id: updateAutoAttendantCallForwardingSettings
tags: Features:  Auto Attendant
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.682584+00:00
---

# PUT /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}/callForwarding

**API:** Webex Cloud Calling
**Área:** Features:  Auto Attendant
**operationId:** `updateAutoAttendantCallForwardingSettings`

## Resumen
Update Call Forwarding Settings for an Auto Attendant

## Descripción
Update Call Forwarding settings for the designated Auto Attendant.

The call forwarding feature allows you to direct all incoming calls based on specific criteria that you define.
Below are the available options for configuring your call forwarding:
1. Always forward calls to a designated number.
2. Forward calls to a designated number based on certain criteria.
3. Forward calls using different modes.

Updating call forwarding settings for an auto attendant requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location in which this auto attendant exists.
- `autoAttendantId` [path] (string) (**requerido**): Update call forwarding settings for this auto attendant.
- `orgId` [query] (string): Update auto attendant forwarding settings from this organization.

## Cuerpo de la petición (application/json)
- `callForwarding` (object) (**requerido**):
  - `always` (object):
    - `enabled` (boolean): `Always` call forwarding is enabled or disabled.
    - `destination` (string): Destination for `Always` call forwarding. Required if field `enabled` is set tu true.
    - `ringReminderEnabled` (boolean): If `true`, a brief tone will be played on the person's phone when a call has been forwarded.
    - `sendToVoicemailEnabled` (boolean): Indicates enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
  - `selective` (object):
    - `enabled` (boolean): `Busy` call forwarding is enable or disabled.
    - `destination` (string): Destination for `Busy` call forwarding.
    - `ringReminderEnabled` (boolean): If `true`, a brief tone will be played on the person's phone when a call has been forwarded.
    - `sendToVoicemailEnabled` (boolean): Indicates enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
  - `rules` (array): Rules for selectively forwarding calls. (Rules which are omitted in the list will not be deleted.)
    - `id` (string) (**requerido**): A unique identifier for the auto attendant call forward selective rule.
    - `enabled` (boolean): Flag to indicate if always call forwarding selective rule criteria is active. If not set, flag will be set to false.
  - `operatingModes` (object): Configuration for forwarding via Operating modes (Schedule Based Routing).
    - `enabled` (boolean) (**requerido**): Indicates whether operating modes forwarding is enabled.
    - `modes` (array) (**requerido**): List of operating mode configurations.
      - `normalOperationEnabled` (boolean) (**requerido**): Normal operation is enabled or disabled.
      - `id` (string) (**requerido**): The ID of the operating mode.
      - `forwardTo` (object) (**requerido**): Forward to settings.
        - `selection` (string) (**requerido**): The selection for forwarding.  * `FORWARD_TO_DEFAULT_NUMBER` - When the rule matches, forward to the destination for the hunt group.  * `FORWARD_TO_SPECIFIED_NUMBER` - When the rule matches, forward to the destination for this rule.  * `DO_NOT_FORWARD` - When the rule matches, do not forward to another number. Valores: FORWARD_TO_DEFAULT_NUMBER, FORWARD_TO_SPECIFIED_NUMBER, DO_NOT_FORWARD.
        - `destination` (string): The destination for forwarding. Required when the selection is set to `FORWARD_TO_SPECIFIED_NUMBER`.
        - `destinationVoicemailEnabled` (boolean): Sending incoming calls to voicemail is enabled/disabled when the destination is an internal phone number and that number has the voicemail service enabled.

### Ejemplo — petición
```json
{
  "callForwarding": {
    "always": {
      "enabled": false,
      "destination": "+19705550006",
      "ringReminderEnabled": false,
      "sendToVoicemailEnabled": false
    },
    "selective": {
      "enabled": true,
      "destination": "+19705550006",
      "ringReminderEnabled": false,
      "sendToVoicemailEnabled": false
    },
    "rules": [
      {
        "id": "Y2lzY29zcGFyazovL3VzL0NBTExfRk9SV0FSRElOR19TRUxFQ1RJVkVfUlVMRS9WR1Z6ZENCU2RXeGw",
        "enabled": false
      }
    ],
    "operatingModes": {
      "enabled": true,
      "modes": [
        {
          "normalOperationEnabled": true,
          "id": "Y2lzY29zcGFyazovL3VzL09QRVJBVElOR19NT0RFL2JiOTc1OTcxLTBjZWYtNDdhNi05Yzc5LTliZWFjY2IwYjg4Mg",
          "forwardTo": {
            "selection": "FORWARD_TO_SPECIFIED_NUMBER",
            "destination": "00000",
            "destinationVoicemailEnabled": false
          }
        }
      ]
    }
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/autoAttendants/<autoAttendantId>/callForwarding' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"callForwarding": {}}'
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