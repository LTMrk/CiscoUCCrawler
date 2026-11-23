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
retrieved_at: 2026-11-23T14:21:15.818087+00:00
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
- `businessHoursMenu` (object) (**requerido**): Business hours menu defined for the auto attendant.
- `afterHoursMenu` (object) (**requerido**): After hours menu defined for the auto attendant.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this auto attendant.
- `dialByName` (string): The name to be used for dial by name functions.
- `businessScheduleLevel` (string): Level of the business schedule.  * `LOCATION` - The schedule belongs to the location.  * `ORGANIZATION` - The schedule belongs to the organization. Valores: LOCATION, ORGANIZATION.
- `holidayScheduleLevel` (string): Level of the holiday schedule.  * `LOCATION` - The schedule belongs to the location.  * `ORGANIZATION` - The schedule belongs to the organization. Valores: LOCATION, ORGANIZATION.

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