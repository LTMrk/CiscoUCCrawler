---
doc_id: webex-cloud-calling-put-telephony-config-virtuallines-virtuallineid-voicemail
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/virtualLines/{virtualLineId}/voicemail
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.660705+00:00
---

# PUT /telephony/config/virtualLines/{virtualLineId}/voicemail

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Configure Voicemail Settings for a Virtual Line`

## Resumen
Configure Voicemail Settings for a Virtual Line

## Descripción
Configure a virtual line's voicemail settings.

The voicemail feature transfers callers to voicemail based on your settings. You can then retrieve voice messages via voicemail.

Optionally, notifications can be sent to a mobile phone via text or email. These notifications will not include the voicemail files.

Updating the voicemail settings for a virtual line requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `virtualLineId` [path] (string) **(requerido)**: Retrieve settings for a virtual line with the matching ID.
- `orgId` [query] (string): ID of the organization in which the virtual line resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): Voicemail is enabled or disabled.
- `sendAllCalls` (object): Settings for sending all calls to voicemail.
  - `enabled` (boolean): All calls will be sent to voicemail.
- `sendBusyCalls` (object): Settings for sending calls to voicemail when the line is busy.
  - `enabled` (boolean): Calls will be sent to voicemail when busy.
  - `greeting` (string): `DEFAULT` indicates the default greeting will be played. `CUSTOM` indicates a custom `.wav` file will be played.  * `DEFAULT` - The default greeting will be played.  * `CUSTOM` - Designates that a custom `.wav` file will be played. Valores: DEFAULT, CUSTOM.
- `sendUnansweredCalls` (object):
  - `enabled` (boolean): Unanswered call sending to voicemail is enabled or disabled.
  - `greeting` (string): `DEFAULT` indicates the default greeting will be played. `CUSTOM` indicates a custom `.wav` file will be played.  * `DEFAULT` - The default greeting will be played.  * `CUSTOM` - Designates that a custom `.wav` file will be played. Valores: DEFAULT, CUSTOM.
  - `numberOfRings` (number): Number of rings before an unanswered call will be sent to voicemail. `numberOfRings` must be between 2 and 20, inclusive.
- `notifications` (object) **(requerido)**: Settings for notifications when there are any new voicemails.
  - `enabled` (boolean): Notifications for voicemails will be sent if enabled. At least one of the destination or smsDestination fields must be configured when enabled.
  - `destination` (string): Email address for notification delivery. For US/Canada text messages, use the `smsDestination` field rather than providing a SMS gateway address like `12025551212@txt.example.net` here.
  - `smsDestination` (string): SMS destination for notification delivery. Must be a US or Canada phone number in E.164 format (e.g., +12025551212).
- `transferToNumber` (object) **(requerido)**: Settings for voicemail caller to transfer to a different number by pressing zero (0).
  - `enabled` (boolean): Enable or disable  voicemail caller transfer to a destination by pressing zero (0).
  - `destination` (string): Number voicemail caller will be transferred to when they press zero (0).
- `emailCopyOfMessage` (object): Settings for sending a copy of new voicemail message audio via email.
  - `enabled` (boolean): When `true` copy of new voicemail message audio will be sent to the designated email.
  - `emailId` (string): Email address to which the new voicemail audio will be sent.
- `messageStorage` (object):
  - `mwiEnabled` (boolean): When `true` desktop phone will indicate there are new voicemails.
  - `storageType` (string): Designates which type of voicemail message storage is used.  * `INTERNAL` - Internal mailbox storage has the following limitations: Single message limit of 10 minutes and total mailbox limit of 100 minutes.  * `EXTERNAL` - If `EXTERNAL` is selected, all messages will be sent to the email address entered. Messages will not be accessible via phone, clients, or the end user's calling portal. Valores: INTERNAL, EXTERNAL.
  - `externalEmail` (string): External email address to which the new voicemail audio will be sent.
- `faxMessage` (object):
  - `enabled` (boolean): When `true` FAX messages for new voicemails are sent to the designated number.
  - `phoneNumber` (string): Designates FAX number.
  - `extension` (string): Designates Optional FAX extension.

### Ejemplo de petición
```json
{
  "enabled": true,
  "notifications": {
    "enabled": true,
    "destination": "julie@example.com",
    "smsDestination": "+12025551212"
  },
  "sendAllCalls": {
    "enabled": true
  },
  "sendBusyCalls": {
    "enabled": false,
    "greeting": "DEFAULT"
  },
  "sendUnansweredCalls": {
    "enabled": false,
    "greeting": "CUSTOM",
    "numberOfRings": 3
  },
  "transferToNumber": {
    "enabled": false
  },
  "emailCopyOfMessage": {
    "enabled": false,
    "emailId": "julie@example.com"
  },
  "announcementLanguageCode": "en_us"
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
