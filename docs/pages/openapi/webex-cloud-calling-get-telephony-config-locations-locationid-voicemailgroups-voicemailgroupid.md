---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-voicemailgroups-voicemailgroupid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/voicemailGroups/{voicemailGroupId}
operation_id: Get Location Voicemail Group
tags: Location Call Settings:  Voicemail
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.127068+00:00
---

# GET /telephony/config/locations/{locationId}/voicemailGroups/{voicemailGroupId}

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Voicemail
**operationId:** `Get Location Voicemail Group`

## Resumen
Get Location Voicemail Group

## Descripción
Retrieve voicemail group details for a location.

Manage your voicemail group settings for a specific location, like when you want your voicemail to be active, message storage settings, and how you would like to be notified of new voicemail messages.

Retrieving voicemail group details requires a full, user or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve voicemail group details for this location.
- `voicemailGroupId` [path] (string) (**requerido**): Retrieve voicemail group details for this voicemail group ID.
- `orgId` [query] (string): Retrieve voicemail group details for a customer location.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/voicemailGroups/<voicemailGroupId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): UUID of voicemail group of a particular location.
- `name` (string) (**requerido**): Name of the voicemail group.
- `phoneNumber` (string): Voicemail group phone number.
- `extension` (number): Voicemail group extension number.
- `routingPrefix` (string): Routing prefix of location.
- `esn` (string): Routing prefix + extension of a person or workspace.
- `tollFreeNumber` (boolean): Voicemail group toll free number.
- `firstName` (string): Voicemail group caller ID first name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Voicemail group called ID last name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `enabled` (boolean) (**requerido**): Enable/disable voicemail group.
- `languageCode` (string) (**requerido**): Language for voicemail group audio announcement.
- `greeting` (string) (**requerido**): Set voicemail group greeting type.  * `DEFAULT` - Default voicemail group greeting.  * `CUSTOM` - Custom voicemail group greeting. Valores: DEFAULT, CUSTOM.
- `greetingUploaded` (boolean) (**requerido**): Enabled if CUSTOM greeting is previously uploaded.
- `greetingDescription` (string): CUSTOM greeting for previously uploaded.
- `messageStorage` (object): Message storage information
  - `storageType` (string) (**requerido**): Message storage type  * `INTERNAL` - Store messages in internal mailbox.  * `EXTERNAL` - Send messages to the email address provided. Valores: INTERNAL, EXTERNAL.
  - `externalEmail` (string): External email to forward the message.
- `notifications` (object): Message notifications
  - `enabled` (boolean) (**requerido**): Enable/disable messages notification
  - `destination` (string): Notifications to be sent to the provided email to SMS gateway.
- `faxMessage` (object): Fax message receive settings
  - `enabled` (boolean) (**requerido**): Enable/disable fax messaging.
  - `phoneNumber` (string): Phone number to receive fax messages.
  - `extension` (number): Extension to receive fax messages.
- `transferToNumber` (object): Transfer message information
  - `enabled` (boolean) (**requerido**): Enable/disable to transfer message.
  - `destination` (string): Transfer phone number to be called when '0' is dialed.
- `emailCopyOfMessage` (object): Message copy information
  - `enabled` (boolean) (**requerido**): Enable/disable to email message copy.
  - `emailId` (string): Email message copy to email address provided.
- `voiceMessageForwardingEnabled` (boolean) (**requerido**): Enable/disable to forward voice message.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this workspace.
  - `selection` (string): * `DISPLAY_NAME` - When this option is selected, `displayName` is to be shown for this workspace.  * `CUSTOM_NAME` - When this option is selected, `customName` is to be shown for this workspace. Valores: CUSTOM_NAME, DISPLAY_NAME.
  - `customName` (string): The custom direct line caller ID name. Required if `selection` is set to `CUSTOM_NAME`.
- `dialByName` (string): The name to be used for dial by name functions.

### Ejemplo — respuesta 200
```json
{
  "id": "a7dd4d39-4a78-4516-955f-7810dbe379cf",
  "name": "Voicemail Group Name",
  "phoneNumber": "+16066412147",
  "extension": "1273",
  "routingPrefix": "123",
  "esn": "1231273",
  "tollFreeNumber": "false",
  "firstName": "rcdnfTest",
  "lastName": "rcdnlTest",
  "enabled": true,
  "languageCode": "en_us",
  "greeting": "DEFAULT",
  "greetingUploaded": true,
  "greetingDescription": "greetings.wav",
  "messageStorage": {
    "storageType": "EXTERNAL",
    "externalEmail": "user@flex2.cisco.com"
  },
  "notifications": {
    "enabled": true,
    "destination": "user@flex2.cisco.com"
  },
  "faxMessage": {
    "enabled": true,
    "phoneNumber": "+1234234324",
    "extension": "23455"
  },
  "transferToNumber": {
    "enabled": true,
    "destination": "+12147691003"
  },
  "emailCopyOfMessage": {
    "enabled": true,
    "emailId": "<user@flex2.cisco.com"
  },
  "voiceMessageForwardingEnabled": true,
  "directLineCallerIdName": {
    "selection": "CUSTOM_NAME",
    "customName": "Hakim Smith"
  },
  "dialByName": "Hakim Smith"
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