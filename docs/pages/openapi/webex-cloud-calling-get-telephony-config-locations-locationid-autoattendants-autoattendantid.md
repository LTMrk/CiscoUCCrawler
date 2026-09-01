---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-autoattendants-autoattendantid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}
operation_id: getAutoAttendant
tags: Features:  Auto Attendant
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.680972+00:00
---

# GET /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}

**API:** Webex Cloud Calling
**Área:** Features:  Auto Attendant
**operationId:** `getAutoAttendant`

## Resumen
Get Details for an Auto Attendant

## Descripción
Retrieve an Auto Attendant details.

Auto attendants play customized prompts and provide callers with menu options for routing their calls through your system.

Retrieving an auto attendant details requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve an auto attendant details in this location.
- `autoAttendantId` [path] (string) (**requerido**): Retrieve the auto attendant with the matching ID.
- `orgId` [query] (string): Retrieve the auto attendant details from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/autoAttendants/<autoAttendantId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for the auto attendant.
- `name` (string) (**requerido**): Unique name for the auto attendant.
- `enabled` (boolean) (**requerido**): If `true` auto attendant is enabled.
- `phoneNumber` (string): Auto attendant phone number.  Either `phoneNumber` or `extension` is mandatory.
- `extension` (string): Auto attendant extension.  Either `phoneNumber` or `extension` is mandatory.
- `routingPrefix` (string): Routing prefix of location.
- `esn` (string): Routing prefix + extension of a person or workspace.
- `tollFreeNumber` (boolean) (**requerido**): Flag to indicate if auto attendant number is toll-free number.
- `firstName` (string): First name defined for an auto attendant. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name defined for an auto attendant. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `alternateNumbers` (array): Alternate numbers defined for the auto attendant.
  - `phoneNumber` (string) (**requerido**): Phone number defined as alternate number.
  - `tollFreeNumber` (boolean): Flag to indicate if auto attendant number is toll-free number.
  - `ringPattern` (string) (**requerido**): Ring pattern that will be used for the alternate number.  * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a short ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
- `language` (string): Language for the auto attendant.
- `languageCode` (string): Language code for the auto attendant.
- `businessSchedule` (string) (**requerido**): Business hours defined for the auto attendant.
- `holidaySchedule` (string): Holiday defined for the auto attendant.
- `extensionDialing` (string) (**requerido**): Extension dialing setting. If the values are not set default will be set as `ENTERPRISE`.  * `ENTERPRISE` - Enterprise (organization) level extension dialing.  * `GROUP` - Group (location) level extension dialing. Valores: ENTERPRISE, GROUP.
- `nameDialing` (string) (**requerido**): Name dialing setting. If the values are not set default will be set as `ENTERPRISE`.  * `ENTERPRISE` - Enterprise (organization) level name dialing.  * `GROUP` - Group (location) level name dialing. Valores: ENTERPRISE, GROUP.
- `timeZone` (string): Time zone defined for the auto attendant.
- `businessHoursMenu` (object) (**requerido**):
  - `greeting` (string) (**requerido**): Greeting type defined for the auto attendant.  * `DEFAULT` - Play default greeting.  * `CUSTOM` - Play custom greeting. Valores: DEFAULT, CUSTOM.
  - `extensionEnabled` (boolean) (**requerido**): If `true`, extension dialing without requiring a menu item is enabled.
  - `audioAnnouncementFile` (object):
    - `id` (string) (**requerido**): A unique identifier for the announcement.
    - `fileName` (string) (**requerido**): Audio announcement file name.
    - `mediaFileType` (string) (**requerido**): Audio announcement file type.  * `WAV` - WAV File Extension. Valores: WAV.
    - `level` (string) (**requerido**): Audio announcement file type location.  * `ORGANIZATION` - Specifies this audio file is configured across the organization.  * `LOCATION` - Specifies this audio file is configured across the location. Valores: ORGANIZATION, LOCATION.
  - `keyConfigurations` (object) (**requerido**):
    - `key` (string) (**requerido**): Key assigned to specific menu configuration.  * `0` - When the 0 key is pressed, perform the operation specified by the `action` field.  * `1` - When the 1 key is pressed, perform the operation specified by the `action` field.  * `2` - When the 2 key is pressed, perform the operation specified by the `action` field.  * `3` - When the 3 key is pressed, perform the operation specified by the `action` field.  * `4` - When the 4 key is pressed, perform the operation specified by the `action` field.  * `5` - When the 5 key is pressed, perform the operation specified by the `action` field.  * `6` - When the 6 key is pressed, perform the operation specified by the `action` field.  * `7` - When the 7 key is pressed, perform the operation specified by the `action` field.  * `8` - When the 8 key is pressed, perform the operation specified by the `action` field.  * `9` - When the 9 key is pressed, perform the operation specified by the `action` field.  * `*` - When the * key is pressed, perform the operation specified by the `action` field.  * `#` - When the # key is pressed, perform the operation specified by the `action` field. Valores: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, *, #.
    - `action` (string) (**requerido**): Action assigned to specific menu key configuration.  * `PLAY_ANNOUNCEMENT` - Plays a recorded message and then returns to the current Auto Attendant menu.  * `TRANSFER_WITH_PROMPT` - Plays the message and then transfers the call to the specified number.  * `TRANSFER_WITHOUT_PROMPT` - Transfers the call to the specified number, without playing a transfer prompt.  * `TRANSFER_TO_OPERATOR` - Plays the message and then transfers the call to the specified operator number.  * `TRANSFER_TO_MAILBOX` - Transfers the call to the configured mailbox, without playing a transfer prompt.  * `NAME_DIALING` - Brings the user into the automated name directory.  * `EXTENSION_DIALING` - Prompts the user for an extension, and transfers the user.  * `REPEAT_MENU` - Replays the Auto Attendant greeting.  * `EXIT` - Terminates the call. Valores: PLAY_ANNOUNCEMENT, TRANSFER_WITH_PROMPT, TRANSFER_WITHOUT_PROMPT, TRANSFER_TO_OPERATOR, TRANSFER_TO_MAILBOX, NAME_DIALING, EXTENSION_DIALING, REPEAT_MENU, EXIT.
    - `description` (string): The description of each menu key.
    - `value` (string): Value based on actions.
    - `audioAnnouncementFile` (object):
      - `id` (string) (**requerido**): A unique identifier for the announcement.
      - `fileName` (string) (**requerido**): Audio announcement file name.
      - `mediaFileType` (string) (**requerido**): Audio announcement file type.  * `WAV` - WAV File Extension. Valores: WAV.
      - `level` (string) (**requerido**): Audio announcement file type location.  * `ORGANIZATION` - Specifies this audio file is configured across the organization.  * `LOCATION` - Specifies this audio file is configured across the location. Valores: ORGANIZATION, LOCATION.
  - `callTreatment` (object):
    - `retryAttemptForNoInput` (string): Number of times to repeat the Welcome greeting when the user does not provide an input. By default, NO_REPEAT is set.  * `NO_REPEAT` - Announcement will not be repeated.  * `ONE_TIME` - Repeat the announcement once.  * `TWO_TIMES` - Repeat the announcement twice.  * `THREE_TIMES` - Repeat the announcement thrice. Valores: NO_REPEAT, ONE_TIME, TWO_TIMES, THREE_TIMES.
    - `noInputTimer` (string): Interval the Auto Attendant service waits before timing out. By default, 10 seconds. Min value is 1, and max value is 60.
    - `actionToBePerformed` (object):
      - `action` (string) (**requerido**): Action to perform after the retry attempt is reached.  * `PLAY_MESSAGE_AND_DISCONNECT` - Plays a recorded message and then disconnects the call.  * `TRANSFER_WITHOUT_PROMPT` - Transfers the call to the specified number, without playing a transfer prompt.  * `TRANSFER_WITH_PROMPT` - Plays the message and then transfers the call to the specified number.  * `TRANSFER_TO_OPERATOR` - Plays the message and then transfers the call to the specified operator number.  * `TRANSFER_TO_MAILBOX` - Transfers the call to the configured mailbox, without playing a transfer prompt.  * `DISCONNECT` - Disconnect the call. Valores: PLAY_MESSAGE_AND_DISCONNECT, TRANSFER_WITHOUT_PROMPT, TRANSFER_WITH_PROMPT, TRANSFER_TO_OPERATOR, TRANSFER_TO_MAILBOX, DISCONNECT.
      - `greeting` (string) (**requerido**): Greeting type is defined when `action` is set to `PLAY_MESSAGE_AND_DISCONNECT`.  * `DEFAULT` - Play default greeting.  * `CUSTOM` - Play custom greeting. Valores: DEFAULT, CUSTOM.
      - `audioAnnouncementFile` (object):
        - `id` (string) (**requerido**): A unique identifier for the announcement.
        - `fileName` (string) (**requerido**): Audio announcement file name.
        - `mediaFileType` (string) (**requerido**): Audio announcement file type.  * `WAV` - WAV File Extension. Valores: WAV.
        - `level` (string) (**requerido**): Audio announcement file type location.  * `ORGANIZATION` - Specifies this audio file is configured across the organization.  * `LOCATION` - Specifies this audio file is configured across the location. Valores: ORGANIZATION, LOCATION.
      - `transferCallTo` (string): Transfer call to the specified number when `action` is set to `TRANSFER_WITH_PROMPT`, `TRANSFER_WITHOUT_PROMPT` and `TRANSFER_TO_OPERATOR` and `TRANSFER_TO_MAILBOX`.
- `afterHoursMenu` (object) (**requerido**):
  - `greeting` (string) (**requerido**): Greeting type defined for the auto attendant.  * `DEFAULT` - Play default greeting.  * `CUSTOM` - Play custom greeting. Valores: DEFAULT, CUSTOM.
  - `extensionEnabled` (boolean) (**requerido**): If `true`, extension dialing without requiring a menu item is enabled.
  - `audioAnnouncementFile` (object):
    - `id` (string) (**requerido**): A unique identifier for the announcement.
    - `fileName` (string) (**requerido**): Audio announcement file name.
    - `mediaFileType` (string) (**requerido**): Audio announcement file type.  * `WAV` - WAV File Extension. Valores: WAV.
    - `level` (string) (**requerido**): Audio announcement file type location.  * `ORGANIZATION` - Specifies this audio file is configured across the organization.  * `LOCATION` - Specifies this audio file is configured across the location. Valores: ORGANIZATION, LOCATION.
  - `keyConfigurations` (object) (**requerido**):

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5UL2J6QjJlRGd6Ym1GeU5rQm1iR1Y0TWk1amFYTmpieTVqYjIw",
  "name": "Main Line AA - Test",
  "enabled": true,
  "phoneNumber": "+19705550026",
  "extension": "200",
  "routingPrefix": "1234",
  "esn": "1234200",
  "tollFreeNumber": false,
  "firstName": "Main Line AA",
  "lastName": "Test",
  "language": "English",
  "languageCode": "en_us",
  "businessSchedule": "AUTOATTENDANT-BUSINESS-HOURS",
  "holidaySchedule": "AUTOATTENDANT-HOLIDAY",
  "extensionDialing": "ENTERPRISE",
  "nameDialing": "ENTERPRISE",
  "timeZone": "America/Los_Angeles",
  "businessHoursMenu": {
    "greeting": "DEFAULT",
    "extensionEnabled": true,
    "audioAnnouncementFile": {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9jZWRkODcwYS1lMTkzLTQxNmQtYmM3OS1mNzkyYmUyMzlhOGI",
      "fileName": "announcement.wav",
      "mediaFileType": "WAV",
      "level": "LOCATION"
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
        "audioAnnouncemen
  ... (truncado)
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