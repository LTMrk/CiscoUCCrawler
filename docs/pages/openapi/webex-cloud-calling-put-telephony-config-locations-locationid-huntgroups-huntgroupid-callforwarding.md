---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-huntgroups-huntgroupid-callforwarding
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/locations/{locationId}/huntGroups/{huntGroupId}/callForwarding
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.615093+00:00
---

# PUT /telephony/config/locations/{locationId}/huntGroups/{huntGroupId}/callForwarding

**API:** Webex Cloud Calling
**Área:** Features:  Hunt Group
**operationId:** `updateHuntGroupCallForwardingSettings`

## Resumen
Update Call Forwarding Settings for a Hunt Group

## Descripción
Update Call Forwarding settings for the specified Hunt Group.

The call forwarding feature allows you to direct all incoming calls based on specific criteria that you define.
Below are the available options for configuring your call forwarding:
1. Always forward calls to a designated number.
2. Forward calls to a designated number based on certain criteria.
3. Forward calls using different modes.

Updating call forwarding settings for a hunt group requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Location from which this hunt group exists.
- `huntGroupId` [path] (string) **(requerido)**: Update call forwarding settings for this hunt group.
- `orgId` [query] (string): Update hunt group forwarding settings from this organization.

## Cuerpo de la petición (application/json)
- `callForwarding` (object): Settings related to `Always`, `Busy`, and `No Answer` call forwarding.
  - `always` (object): Settings for forwarding all incoming calls to the destination you choose.
    - `enabled` (boolean): `Always` call forwarding is enabled or disabled.
    - `destination` (string): Destination for `Always` call forwarding.
    - `ringReminderEnabled` (boolean): If `true`, a brief tone will be played on the person's phone when a call has been forwarded.
    - `destinationVoicemailEnabled` (boolean): Sending incoming calls to voicemail is enabled/disabled when the destination is an internal phone number and that number has the voicemail service enabled.
  - `selective` (object): Selectively forward calls to a designated number, depending on criteria rules. You'll need to have at least one rule for forwarding applied for call forwarding to be active.
    - `enabled` (boolean): `Busy` call forwarding is enabled or disabled.
    - `destination` (string): Destination for `Busy` call forwarding.
    - `ringReminderEnabled` (boolean): If `true`, a brief tone will be played on the person's phone when a call has been forwarded.
    - `destinationVoicemailEnabled` (boolean): Sending incoming calls to voicemail is enabled/disabled when the destination is an internal phone number and that number has the voicemail service enabled.
  - `rules` (array): Rules for selectively forwarding calls.
    - `id` (string) **(requerido)**: Unique ID for the rule.
    - `enabled` (boolean): Reflects if rule is enabled.
  - `operatingModes` (object): Configuration for forwarding via Operating modes (Schedule Based Routing).
    - `enabled` (boolean) **(requerido)**: Indicates whether operating modes forwarding is enabled.
    - `modes` (array) **(requerido)**: List of operating mode configurations.
      - `normalOperationEnabled` (boolean) **(requerido)**: Normal operation is enabled or disabled.
      - `id` (string) **(requerido)**: The ID of the operating mode.
      - `forwardTo` (object) **(requerido)**: Forward to settings.
        - `selection` (string) **(requerido)**: The selection for forwarding.  * `FORWARD_TO_DEFAULT_NUMBER` - When the rule matches, forward to the destination for the hunt group.  * `FORWARD_TO_SPECIFIED_NUMBER` - When the rule matches, forward to the destination for this rule.  * `DO_NOT_FORWARD` - When the rule matches, do not forward to another number. Valores: FORWARD_TO_DEFAULT_NUMBER, FORWARD_TO_SPECIFIED_NUMBER, DO_NOT_FORWARD.
        - `destination` (string): The destination for forwarding. Required when the selection is set to `FORWARD_TO_SPECIFIED_NUMBER`.
        - `destinationVoicemailEnabled` (boolean): Sending incoming calls to voicemail is enabled/disabled when the destination is an internal phone number and that number has the voicemail service enabled.

### Ejemplo de petición
```json
{
  "callForwarding": {
    "always": {
      "enabled": false,
      "destination": ""
    },
    "selective": {
      "enabled": true,
      "destination": "35556",
      "destinationVoicemailEnabled": true
    },
    "rules": [
      {
        "id": "Y2lzY29zcGFyazovL3VzL0NBTExfRk9SV0FSRElOR19TRUxFQ1RJVkVfUlVMRS9RbTlpVW1WdVlXMWw",
        "enabled": true
      },
      {
        "id": "Y2lzY29zcGFyazovL3VzL0NBTExfRk9SV0FSRElOR19TRUxFQ1RJVkVfUlVMRS9WMmhsYmxSdg",
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

## Respuestas
- **204**: No Content
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
