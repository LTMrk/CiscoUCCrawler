---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-autoattendants-autoattendantid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}
operation_id: updateAutoAttendant
tags: Features:  Auto Attendant
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.663730+00:00
---

# PUT /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}

**API:** Webex Cloud Calling
**Área:** Features:  Auto Attendant
**operationId:** `updateAutoAttendant`

## Resumen
Update an Auto Attendant

## Descripción
Update the designated Auto Attendant.

Auto attendants play customized prompts and provide callers with menu options for routing their calls through your system.

Updating an auto attendant requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location in which this auto attendant exists.
- `autoAttendantId` [path] (string) (**requerido**): Update an auto attendant with the matching ID.
- `orgId` [query] (string): Update an auto attendant from this organization.

## Cuerpo de la petición (application/json)
- `name` (string): Unique name for the auto attendant.
- `phoneNumber` (string): Auto attendant phone number.  Either `phoneNumber` or `extension` is mandatory.
- `extension` (string): Auto attendant extension.  Either `phoneNumber` or `extension` is mandatory.
- `firstName` (string): First name defined for an auto attendant. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name defined for an auto attendant. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `alternateNumbers` (array): Alternate numbers defined for the auto attendant.
  - `phoneNumber` (string) (**requerido**): Phone number defined as alternate number.
  - `tollFreeNumber` (boolean): Flag to indicate if auto attendant number is toll-free number.
  - `ringPattern` (string) (**requerido**): Ring pattern that will be used for the alternate number.  * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a short ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
- `languageCode` (string): Announcement language code for the auto attendant.
- `businessSchedule` (string): Business hours defined for the auto attendant.
- `holidaySchedule` (string): Holiday defined for the auto attendant.
- `extensionDialing` (string): Extension dialing setting. If the values are not set default will be set as `ENTERPRISE`. Valores: ENTERPRISE, GROUP.
- `nameDialing` (string): Name dialing setting. If the values are not set default will be set as `ENTERPRISE`. Valores: ENTERPRISE, GROUP.
- `timeZone` (string): Time zone defined for the auto attendant.
- `businessHoursMenu` (object): Business hours menu defined for the auto attendant.
- `afterHoursMenu` (object): After hours menu defined for the auto attendant.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this auto attendant.
- `dialByName` (string): Sets or clears the name to be used for dial by name functions. To clear the `dialByName`, the attribute must be set to null or empty string. Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.
- `businessScheduleLevel` (string): Level of the business schedule. A nonblank `businessSchedule` is required when this field is supplied. Defaults to the location level when omitted with a schedule.  * `LOCATION` - The schedule belongs to the location.  * `ORGANIZATION` - The schedule belongs to the organization. Valores: LOCATION, ORGANIZATION.
- `holidayScheduleLevel` (string): Level of the holiday schedule. A nonblank `holidaySchedule` is required when this field is supplied. Defaults to the location level when omitted with a schedule.  * `LOCATION` - The schedule belongs to the location.  * `ORGANIZATION` - The schedule belongs to the organization. Valores: LOCATION, ORGANIZATION.

### Ejemplo — petición
```json
{
  "name": "Main Line AA - Test New Name",
  "phoneNumber": "+19705550026",
  "extension": "200",
  "firstName": "Main Line AA",
  "lastName": "Test",
  "languageCode": "en_us",
  "businessSchedule": "TEST-BUSINESS-HOURS-NEW-NAME",
  "holidaySchedule": "AUTOATTENDANT-HOLIDAY",
  "extensionDialing": "ENTERPRISE",
  "nameDialing": "ENTERPRISE",
  "timeZone": "America/Los_Angeles",
  "businessHoursMenu": {
    "greeting": "DEFAULT",
    "extensionEnabled": true,
    "audioAnnouncementFile": {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9jZWRkODcwYS1lMTkzLTQxNmQtYmM3OS1mNzkyYmUyMzlhOGI",
      "fileName": "AUDIO_FILE.wav",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION"
    },
    "keyConfigurations": [
      {
        "key": "0",
        "action": "EXIT"
      },
      {
        "key": "1",
        "action": "TRANSFER_WITHOUT_PROMPT",
        "value": "+19175551092"
      },
      {
        "key": "2",
        "action": "TRANSFER_WITH_PROMPT",
        "value": "+19073569984"
      },
      {
        "key": "3",
        "action": "EXTENSION_DIALING"
      },
      {
        "key": "4",
        "action": "TRANSFER_TO_MAILBOX",
        "value": "+19705550006"
      },
      {
        "key": "5",
        "action": "PLAY_ANNOUNCEMENT",
        "audioAnnouncementFile": {
          "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5UL2J6QjJlRGd6Ym1GeU5rQm1iR1Y0TWk1amFYTmpieTVqYjIw",
          "fileName": "AUDIO_FILE.wav",
          "mediaFileType": "WAV",
          "leve
  ... (truncado)
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/autoAttendants/<autoAttendantId>' \
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