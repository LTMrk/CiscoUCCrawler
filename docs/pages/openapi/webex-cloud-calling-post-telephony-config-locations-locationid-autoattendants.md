---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-autoattendants
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/autoAttendants
operation_id: createAutoAttendant
tags: Features:  Auto Attendant
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.289031+00:00
---

# POST /telephony/config/locations/{locationId}/autoAttendants

**API:** Webex Cloud Calling
**Área:** Features:  Auto Attendant
**operationId:** `createAutoAttendant`

## Resumen
Create an Auto Attendant

## Descripción
Create new Auto Attendant for the given location.

Auto attendants play customized prompts and provide callers with menu options for routing their calls through your system.

Creating an auto attendant requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Create the auto attendant for this location.
- `orgId` [query] (string): Create the auto attendant for this organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Unique name for the auto attendant.
- `phoneNumber` (string): Auto attendant phone number.  Either `phoneNumber` or `extension` is mandatory.
- `extension` (string): Auto attendant extension.  Either `phoneNumber` or `extension` is mandatory.
- `firstName` (string): First name defined for an auto attendant. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name defined for an auto attendant. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `alternateNumbers` (array): Alternate numbers defined for the auto attendant.
  - `phoneNumber` (string) (**requerido**): Phone number defined as alternate number.
  - `tollFreeNumber` (boolean): Flag to indicate if auto attendant number is toll-free number.
  - `ringPattern` (string) (**requerido**): Ring pattern that will be used for the alternate number.  * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a short ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
- `languageCode` (string): Announcement language code for the auto attendant.
- `businessSchedule` (string) (**requerido**): Business hours defined for the auto attendant.
- `holidaySchedule` (string): Holiday defined for the auto attendant.
- `extensionDialing` (string): Extension dialing setting. If the values are not set default will be set as `ENTERPRISE`. Valores: ENTERPRISE, GROUP.
- `nameDialing` (string): Name dialing setting. If the values are not set default will be set as `ENTERPRISE`. Valores: ENTERPRISE, GROUP.
- `timeZone` (string): Time zone defined for the auto attendant.
- `businessHoursMenu` (object) (**requerido**):
  - `greeting` (string) (**requerido**): Greeting type defined for the auto attendant. Valores: DEFAULT, CUSTOM.
  - `extensionEnabled` (boolean) (**requerido**): Flag to indicate if auto attendant extension is enabled or not.
  - `audioAnnouncementFile` (object):
    - `id` (string): A unique identifier for the [announcement](/docs/api/v1/features-announcement-repository). `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement. If all four fields are provided, file with given `id` is used and other fields are ignored.
    - `fileName` (string): Audio announcement file name.
    - `mediaFileType` (string): Audio announcement file type.  * `WAV` - WAV File Extension. Valores: WAV.
    - `level` (string): Audio announcement file type location.  * `ORGANIZATION` - Specifies this audio file is configured across the organization.  * `LOCATION` - Specifies this audio file is configured across the location. Valores: ORGANIZATION, LOCATION.
  - `keyConfigurations` (object) (**requerido**):
    - `key` (string) (**requerido**): Key assigned to specific menu configuration. Valores: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, *, #.
    - `action` (string) (**requerido**): Action assigned to specific menu key configuration.  * `PLAY_ANNOUNCEMENT` - Plays a recorded message and then returns to the current Auto Attendant menu.  * `TRANSFER_WITH_PROMPT` - Transfers the call to the specified number, without playing a transfer prompt.  * `TRANSFER_WITHOUT_PROMPT` - Plays the message and then transfers the call to the specified number.  * `TRANSFER_TO_OPERATOR` - Plays the message and then transfers the call to the specified operator number.  * `TRANSFER_TO_MAILBOX` - Prompts the user for an extension, and transfers the user to voice mailbox of the dialed extension.  * `NAME_DIALING` - Brings the user into the automated name directory.  * `EXTENSION_DIALING` - Prompts the user for an extension, and transfers the user.  * `REPEAT_MENU` - Replays the Auto Attendant greeting.  * `EXIT` - Terminates the call. Valores: PLAY_ANNOUNCEMENT, TRANSFER_WITH_PROMPT, TRANSFER_WITHOUT_PROMPT, TRANSFER_TO_OPERATOR, TRANSFER_TO_MAILBOX, NAME_DIALING, EXTENSION_DIALING, REPEAT_MENU, EXIT.
    - `description` (string): The description of each menu key.
    - `value` (string): Value based on actions.
    - `audioAnnouncementFile` (object):
      - `id` (string): A unique identifier for the [announcement](/docs/api/v1/features-announcement-repository). `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement. If all four fields are provided, file with given `id` is used and other fields are ignored.
      - `fileName` (string): Audio announcement file name.
      - `mediaFileType` (string): Audio announcement file type.  * `WAV` - WAV File Extension. Valores: WAV.
      - `level` (string): Audio announcement file type location.  * `ORGANIZATION` - Specifies this audio file is configured across the organization.  * `LOCATION` - Specifies this audio file is configured across the location. Valores: ORGANIZATION, LOCATION.
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
  - `greeting` (string) (**requerido**): Greeting type defined for the auto attendant. Valores: DEFAULT, CUSTOM.
  - `extensionEnabled` (boolean) (**requerido**): Flag to indicate if auto attendant extension is enabled or not.
  - `audioAnnouncementFile` (object):
    - `id` (string): A unique identifier for the [announcement](/docs/api/v1/features-announcement-repository). `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement. If all four fields are provided, file with given `id` is used and other fields are ignored.
    - `fileName` (string): Audio announcement file name.
    - `mediaFileType` (string): Audio announcement file type.  * `WAV` - WAV File Extension. Valores: WAV.
    - `level` (string): Audio announcement file type location.  * `ORGANIZATION` - Specifies this audio file is configured across the organization.  * `LOCATION` - Specifies this audio file is configured across the location. Valores: ORGANIZATION, LOCATION.
  - `keyConfigurations` (object) (**requerido**):
    - `key` (string) (**requerido**): Key assigned to specific menu configuration. Valores: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, *, #.
    - `action` (string) (**requerido**): Action assigned to specific menu key configuration.  * `PLAY_ANNOUNCEMENT` - Plays a recorded message and then returns to the current Auto Attendant menu.  * `TRANSFER_WITH_PROMPT` - Transfers the call to the specified number, without playing a transfer prompt.  * `TRANSFER_WITHOUT_PROMPT` - Plays the message and then transfers the call to the specified number.  * `TRANSFER_TO_OPERATOR` - Plays the message and then transfers the call to the specified operator number.  * `TRANSFER_TO_MAILBOX` - Prompts the user for an extension, and transfers the user to voice mailbox of the dialed extension.  * `NAME_DIALING` - Brings the user into the automated name directory.  * `EXTENSION_DIALING` - Prompts the user for an extension, and transfers the user.  * `REPEAT_MENU` - Replays the Auto Attendant greeting.  * `EXIT` - Terminates the call. Valores: PLAY_ANNOUNCEMENT, TRANSFER_WITH_PROMPT, TRANSFER_WITHOUT_PROMPT, TRANSFER_TO_OPERATOR, TRANSFER_TO_MAILBOX, NAME_DIALING, EXTENSION_DIALING, REPEAT_MENU, EXIT.
    - `description` (string): The description of each menu key.
    - `value` (string): Value based on actions.
    - `audioAnnouncementFile` (object):
      - `id` (string): A unique identifier for the [announcement](/docs/api/v1/features-announcement-repository). `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement. If all four fields are provided, file with given `id` is used and other fields are ignored.

### Ejemplo — petición
```json
{
  "name": "Main Line AA - Test",
  "phoneNumber": "+19705550026",
  "extension": "200",
  "firstName": "Main Line AA",
  "lastName": "Test",
  "languageCode": "en_us",
  "businessSchedule": "AUTOATTENDANT-BUSINESS-HOURS",
  "holidaySchedule": "AUTOATTENDANT-HOLIDAY",
  "extensionDialing": "ENTERPRISE",
  "nameDialing": "ENTERPRISE",
  "timeZone": "America/Los_Angeles",
  "businessHoursMenu": {
    "greeting": "DEFAULT",
    "audioAnnouncementFile": {
      "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5UL2J6QjJlRGd6Ym1GeU5rQm1iR1Y0TWk1amFYTmpieTVqYjIw",
      "fileName": "AUDIO_FILE.wav",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION"
    },
    "extensionEnabled": true,
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
          "level": "ORG
  ... (truncado)
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/autoAttendants' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "businessSchedule": "<businessSchedule>", "businessHoursMenu": {}, "afterHoursMenu": {}}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): ID of the newly created auto attendant.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5UL2J6QjJlRGd6Ym1GeU5rQm1iR1Y0TWk1amFYTmpieTVqYjIw"
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