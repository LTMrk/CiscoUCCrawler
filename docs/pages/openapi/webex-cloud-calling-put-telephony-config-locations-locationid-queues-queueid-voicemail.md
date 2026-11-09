---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-queues-queueid-voicemail
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/queues/{queueId}/voicemail
operation_id: configureVoicemailSettingsForCallQueue
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-09T12:44:28.064303+00:00
---

# PUT /telephony/config/locations/{locationId}/queues/{queueId}/voicemail

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `configureVoicemailSettingsForCallQueue`

## Resumen
Configure Voicemail Settings for a Call Queue

## Descripción
Configure Voicemail settings for a Call Queue.

The voicemail feature transfers callers to voicemail based on your settings. You can then retrieve voice messages via Voicemail. Voicemail audio is sent in Waveform Audio File Format, `.wav`, format. Optionally, notifications can be sent via email. These notifications will not include the voicemail files.

Configuring a call queue's voicemail settings requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Unique Identifier of the Location.
- `queueId` [path] (string) (**requerido**): Unique Identifier of the Call Queue.
- `orgId` [query] (string): Configure voicemail settings for this organization.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): Voicemail is enabled or disabled.
- `greeting` (object): Greeting settings for calls sent to voicemail.
  - `type` (string): Greeting type.  - `DEFAULT` - The default greeting will be played. - `CUSTOM` - Designates that a custom file will be played. Valores: DEFAULT, CUSTOM.
- `notifications` (object): Settings for notifications when there are any new voicemails.
  - `enabled` (boolean) (**requerido**): When true, Notifications for voicemails will be sent.
  - `destination` (string) (**requerido**): Email address to which the notification will be sent.
- `transferToNumber` (object): Settings for voicemail caller to transfer to a different number by pressing zero (0).
  - `enabled` (boolean) (**requerido**): If true, state of giving caller option to transfer to destination when pressing zero (0) is enabled.
  - `destination` (string) (**requerido**): Number voicemail caller will be transferred to when they press zero (0).
- `emailCopyOfMessage` (object): Settings for sending a copy of new voicemail message audio via email.
  - `enabled` (boolean) (**requerido**): When true copy of new voicemail message audio will be sent to the designated email.
  - `emailId` (string) (**requerido**): Email address to which the new voicemail audio will be sent. This is not a Hydra ID but an email address (e.g., `user@example.com`).
- `messageStorage` (object): Settings for voicemail message storage and message waiting indicator.
  - `mwiEnabled` (boolean) (**requerido**): When true desktop phone will indicate there are new voicemails.
  - `storageType` (string) (**requerido**): Designates which type of voicemail message storage is used.  - `INTERNAL` - For message access via phone or User Hub. - `EXTERNAL` - For sending all messages to the externalEmail. Valores: INTERNAL, EXTERNAL.
  - `externalEmail` (string): External email address to which the new voicemail audio will be sent. A value for this field must be provided in the request if a storageType of EXTERNAL is given in the request.
- `faxMessage` (object): Settings for sending a FAX message for new voicemails.
  - `enabled` (boolean) (**requerido**): When true, FAX messages for new voicemails will be sent to the designated number.
  - `phoneNumber` (string): Designates phone number for the FAX. A value for this field must be provided in the request if faxMessage enabled field is given as true in the request.
  - `extension` (string): Designates optional extension for the FAX.

### Ejemplo — petición
```json
{
  "enabled": true,
  "greeting": {
    "type": "DEFAULT"
  },
  "notifications": {
    "enabled": true,
    "destination": "test@cisco.com"
  },
  "transferToNumber": {
    "enabled": false,
    "destination": ""
  },
  "emailCopyOfMessage": {
    "enabled": true,
    "emailId": "copy@cisco.com"
  },
  "messageStorage": {
    "mwiEnabled": true,
    "storageType": "INTERNAL",
    "externalEmail": ""
  },
  "faxMessage": {
    "enabled": false,
    "phoneNumber": "",
    "extension": ""
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/queues/<queueId>/voicemail' \
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