---
doc_id: webex-cloud-calling-put-telephony-config-voicemail-rules
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/voicemail/rules
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.578102+00:00
---

# PUT /telephony/config/voicemail/rules

**API:** Webex Cloud Calling
**Área:** Calling Service Settings
**operationId:** `Update Voicemail Rules`

## Resumen
Update Voicemail Rules

## Descripción
Update the organization's default voicemail passcode and/or rules.

Organizational voicemail rules specify the default passcode requirements.

If you choose to set a default passcode for new people added to your organization, communicate to your people what that passcode is, and that it must be reset before they can access their voicemail. If this feature is not turned on, each new person must initially set their own passcode.

Updating an organization's voicemail passcode and/or rules requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Update voicemail rules for this organization.

## Cuerpo de la petición (application/json)
- `defaultVoicemailPinEnabled` (boolean): Set to `true` to enable the default voicemail passcode.
- `defaultVoicemailPin` (string): Default voicemail passcode.
- `expirePasscode` (object): Settings for passcode expiry.
  - `enabled` (boolean): Set to `true` to expire passcode after the number of days specified.
  - `numberOfDays` (number): Number of days for password expiry. The minimum value is 15. The maximum value is 100.
- `changePasscode` (object): Settings for passcode changes.
  - `enabled` (boolean): Set to `true` to change the minimum number of days between passcode changes.
  - `numberOfDays` (number): Number of days between passcode changes. The minimum value is 1. The maximum value is 7.
- `blockPreviousPasscodes` (object): Settings for previous passcode usage.
  - `enabled` (boolean): Set to `true` to specify how many of the previous passcode are not allowed to be re-used.
  - `numberOfPasscodes` (number): Number of previous passcodes. The minimum value is 1. The maximum value is 10.

### Ejemplo de petición
```json
{
  "defaultVoicemailPinEnabled": true,
  "defaultVoicemailPin": "123544",
  "expirePasscode": {
    "enabled": true,
    "numberOfDays": 100
  },
  "changePasscode": {
    "enabled": true,
    "numberOfDays": 1
  },
  "blockPreviousPasscodes": {
    "enabled": false,
    "numberOfPasscodes": 10
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
