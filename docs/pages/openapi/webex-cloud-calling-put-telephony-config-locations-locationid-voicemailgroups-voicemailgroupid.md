---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-voicemailgroups-voicemailgroupid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/voicemailGroups/{voicemailGroupId}
operation_id: Modify Location Voicemail Group
tags: Location Call Settings:  Voicemail
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.127343+00:00
---

# PUT /telephony/config/locations/{locationId}/voicemailGroups/{voicemailGroupId}

**API:** Webex Cloud Calling
**Área:** Location Call Settings:  Voicemail
**operationId:** `Modify Location Voicemail Group`

## Resumen
Modify Location Voicemail Group

## Descripción
Modifies the voicemail group location details for a particular location for a customer.

Manage your voicemail settings, like when you want your voicemail to be active, message storage settings, and how you would like to be notified of new voicemail messages.

Modifying the voicemail group location details requires a full, user administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Modifies the voicemail group details for this location.
- `voicemailGroupId` [path] (string) (**requerido**): Modifies the voicemail group details for this voicemail group ID.
- `orgId` [query] (string): Modifies the voicemail group details for a customer location.

## Cuerpo de la petición (application/json)
- `name` (string): Set the name of the voicemail group.
- `phoneNumber` (string): Set voicemail group phone number.
- `extension` (number): Set unique voicemail group extension number.
- `firstName` (string): Set the voicemail group caller ID first name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Set the voicemail group called ID last name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `enabled` (boolean): Set to `true` to enable the voicemail group.
- `passcode` (number): Set passcode to access voicemail group when calling.
- `languageCode` (string): Language code for the voicemail group audio announcement.
- `greeting` (string): Voicemail group greeting type.  * `DEFAULT` - Set to `DEFAULT` to play default voicemail group greeting.  * `CUSTOM` - Set to `CUSTOM` to play previously uploaded custom voicemail group greeting. Valores: DEFAULT, CUSTOM.
- `greetingDescription` (string): CUSTOM greeting for previously uploaded.
- `messageStorage` (object): Message storage information
  - `storageType` (string): Message storage type.  * `INTERNAL` - Set to `INTERNAL` to store messages in internal mailbox.  * `EXTERNAL` - Set to `EXTERNAL` to send messages to the email address provided. Valores: INTERNAL, EXTERNAL.
  - `externalEmail` (string): Set external email to forward the messages.
- `notifications` (object): Message notifications
  - `enabled` (boolean): Set to `true` to enable message notification.
  - `destination` (string): Set email to SMS gateway to send notifications.
- `faxMessage` (object): Fax message receive settings
  - `enabled` (boolean): Set to `true` to enable FAX messaging.
  - `phoneNumber` (string): Set valid phone number to receive FAX messages.
  - `extension` (number): Set FAX messaging extension number.
- `transferToNumber` (object): Transfer message information
  - `enabled` (boolean): Set to `true` to enable to transfer message.
  - `destination` (string): Set phone number and transfer message to the provided number when '0' is dialed.
- `emailCopyOfMessage` (object): Message copy information
  - `enabled` (boolean): Set to `true` to enable email message copy.
  - `emailId` (string): Set email to receive message copy to the email address provided.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this workspace.
  - `selection` (string): * `DISPLAY_NAME` - When this option is selected, `displayName` is to be shown for this workspace.  * `CUSTOM_NAME` - When this option is selected, `customName` is to be shown for this workspace. Valores: CUSTOM_NAME, DISPLAY_NAME.
  - `customName` (string): Sets or clears the custom direct line caller ID name.  To clear the `customName`, the attribute must be set to null or empty string. Required if `selection` is set to `CUSTOM_NAME`.
- `dialByName` (string): Sets or clears the name to be used for dial by name functions. To clear the `dialByName`, the attribute must be set to null or empty string. Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.

### Ejemplo — petición
```json
{
  "name": "Voicemail Group Name",
  "phoneNumber": "+16066412147",
  "extension": "1273",
  "firstName": "rcdnfTest",
  "lastName": "rcdnlTest",
  "passcode": "1234",
  "enabled": true,
  "languageCode": "en_us",
  "greeting": "DEFAULT",
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
  "directLineCallerIdName": {
    "selection": "CUSTOM_NAME",
    "customName": "Hakim Smith"
  },
  "dialByName": "Hakim Smith"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/voicemailGroups/<voicemailGroupId>' \
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