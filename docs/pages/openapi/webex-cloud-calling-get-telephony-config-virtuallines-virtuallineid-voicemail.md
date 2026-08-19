---
doc_id: webex-cloud-calling-get-telephony-config-virtuallines-virtuallineid-voicemail
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/virtualLines/{virtualLineId}/voicemail
operation_id: Read Voicemail Settings for a Virtual Line
tags: Virtual Line Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.181546+00:00
---

# GET /telephony/config/virtualLines/{virtualLineId}/voicemail

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Read Voicemail Settings for a Virtual Line`

## Resumen
Read Voicemail Settings for a Virtual Line

## Descripción
Retrieve a virtual line's voicemail settings.

The voicemail feature transfers callers to voicemail based on your settings. You can then retrieve voice messages via voicemail.

Optionally, notifications can be sent to a mobile phone via text or email. These notifications will not include the voicemail files.

Retrieving the voicemail settings for a virtual line requires a full, user, read-only administrator, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `virtualLineId` [path] (string) (**requerido**): Retrieve settings for a virtual line with the matching ID.
- `orgId` [query] (string): ID of the organization in which the virtual line resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/virtualLines/<virtualLineId>/voicemail' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): Voicemail is enabled or disabled.
- `sendAllCalls` (object) (**requerido**): Settings for sending all calls to voicemail.
  - `enabled` (boolean) (**requerido**): All calls will be sent to voicemail.
- `sendBusyCalls` (object) (**requerido**): Settings for sending calls to voicemail when the line is busy.
  - `enabled` (boolean) (**requerido**): Calls will be sent to voicemail when busy.
  - `greeting` (string) (**requerido**): `DEFAULT` indicates the default greeting will be played. `CUSTOM` indicates a custom `.wav` file will be played.  * `DEFAULT` - The default greeting will be played.  * `CUSTOM` - Designates that a custom `.wav` file will be played. Valores: DEFAULT, CUSTOM.
  - `greetingUploaded` (boolean) (**requerido**): A custom greeting has been uploaded.
- `sendUnansweredCalls` (object) (**requerido**):
  - `enabled` (boolean) (**requerido**): Enables and disables sending unanswered calls to voicemail.
  - `greeting` (string) (**requerido**): `DEFAULT` indicates the default greeting will be played. `CUSTOM` indicates a custom `.wav` file will be played.  * `DEFAULT` - The default greeting will be played.  * `CUSTOM` - Designates that a custom `.wav` file will be played. Valores: DEFAULT, CUSTOM.
  - `greetingUploaded` (boolean) (**requerido**): A custom greeting has been uploaded
  - `numberOfRings` (number) (**requerido**): Number of rings before unanswered call will be sent to voicemail.
  - `systemMaxNumberOfRings` (number) (**requerido**): System-wide maximum number of rings allowed for `numberOfRings` setting.
- `notifications` (object) (**requerido**): Settings for notifications when there are any new voicemails.
  - `enabled` (boolean) (**requerido**): Notifications for voicemails will be sent if enabled.
  - `destination` (string): Email address for notification delivery. For US/Canada text messages, use the `smsDestination` field rather than providing a SMS gateway address like `12025551212@txt.example.net` here.
  - `smsDestination` (string): SMS destination for notification delivery. Must be a US or Canada phone number in E.164 format (e.g., +12025551212).
- `transferToNumber` (object) (**requerido**): Settings for voicemail caller to transfer to a different number by pressing zero (0).
  - `enabled` (boolean) (**requerido**): Enabled or disabled state of giving caller option to transfer to destination when pressing zero (0).
  - `destination` (string): Number voicemail caller will be transferred to when they press zero (0).
- `emailCopyOfMessage` (object) (**requerido**): Settings for sending a copy of new voicemail message audio via email.
  - `enabled` (boolean) (**requerido**): When `true` copy of new voicemail message audio will be sent to the designated email.
  - `emailId` (string) (**requerido**): Email address to which the new voicemail audio will be sent.
- `messageStorage` (object) (**requerido**):
  - `mwiEnabled` (boolean) (**requerido**): When `true` desktop phone will indicate there are new voicemails.
  - `storageType` (string) (**requerido**): Designates which type of voicemail message storage is used.  * `INTERNAL` - For message access via phone or the Calling User Portal.  * `EXTERNAL` - For sending all messages to the person's email. Valores: INTERNAL, EXTERNAL.
  - `externalEmail` (string) (**requerido**): External email address to which the new voicemail audio will be sent.  A value for this field must be provided in the request if a `storageType` of `EXTERNAL` is given in the request.
- `faxMessage` (object) (**requerido**):
  - `enabled` (boolean) (**requerido**): When `true` FAX messages for new voicemails will be sent to the designated number.
  - `phoneNumber` (string): Designates phone number for the FAX. A value for this field must be provided in the request if faxMessage `enabled` field is given as `true` in the request.
  - `extension` (string): Designates optional FAX extension.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "sendAllCalls": {
    "enabled": true
  },
  "sendBusyCalls": {
    "enabled": false,
    "greeting": "DEFAULT",
    "greetingUploaded": false
  },
  "sendUnansweredCalls": {
    "enabled": false,
    "greeting": "DEFAULT",
    "greetingUploaded": true,
    "numberOfRings": 3,
    "systemMaxNumberOfRings": 20
  },
  "notifications": {
    "enabled": true,
    "destination": "julie@example.com",
    "smsDestination": "+12025551212"
  },
  "transferToNumber": {
    "enabled": false
  },
  "emailCopyOfMessage": {
    "enabled": false,
    "emailId": "julie@example.com"
  },
  "messageStorage": {
    "mwiEnabled": true,
    "storageType": "INTERNAL",
    "externalEmail": "julia@example.com"
  },
  "faxMessage": {
    "enabled": false
  },
  "voiceMessageForwardingEnabled": false,
  "announcementLanguageCode": "en_us"
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