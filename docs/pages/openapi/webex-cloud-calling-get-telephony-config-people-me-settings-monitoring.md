---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-monitoring
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/monitoring
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.565816+00:00
---

# GET /telephony/config/people/me/settings/monitoring

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyMonitoringSettings`

## Resumen
Get My Monitoring Settings

## Descripción
Retrieves the monitoring settings for the authenticated person, which shows specified people, places, virtual lines or call park extensions that are being monitored.

Monitors the line status which indicates if a person, place or virtual line is on a call and if a call has been parked on that extension.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Respuestas
- **200**: OK
  - `callParkNotificationEnabled` (boolean) **(requerido)**: Call park notification is enabled or disabled. Only applies to monitored users, workspaces, and virtual lines. Does not apply to call park extensions.
  - `monitoredElements` (array) **(requerido)**: Settings of monitored elements which can be person, place, virtual line or call park extension.
    - `callparkextension` (object):
      - `id` (string) **(requerido)**: ID of call park extension.
      - `name` (string) **(requerido)**: Name of call park extension.
      - `extension` (string) **(requerido)**: Extension of call park extension.
      - `routingPrefix` (string): Routing prefix of location.
      - `esn` (string): Routing prefix + extension of a person or workspace.
      - `location` (string) **(requerido)**: Name of location for call park extension.
      - `locationId` (string) **(requerido)**: ID of location for call park extension.
      - `lineKeyLabel` (string): Customizable line key label for monitored call park extension.
    - `member` (object):
      - `id` (string): The identifier of the monitored person or workspace.
      - `firstName` (string): The first name of the monitored person, place, or virtual line.
      - `lastName` (string): The last name of the monitored person, place, or virtual line.
      - `displayName` (string): The display name of the monitored person, place, or virtual line.
      - `type` (string): The type of the monitored person, place, or virtual line.  * `PEOPLE` - Object is a user.  * `PLACE` - Object is a workspace. Valores: PEOPLE, PLACE.
      - `email` (string): The email address of the monitored person, place, or virtual line.
      - `numbers` (array): The list of phone numbers of the monitored person, place, or virtual line.
        - `external` (string): Phone number of person or workspace. Either `phoneNumber` or `extension` is mandatory.
        - `extension` (string): Extension of person or workspace. Either `phoneNumber` or `extension` is mandatory.
        - `routingPrefix` (string): Routing prefix of location.
        - `esn` (string): Routing prefix + extension of a person or workspace.
        - `primary` (boolean) **(requerido)**: Flag to indicate primary phone.
        - `tollFreeNumber` (boolean): Flag to indicate toll free number.
      - `location` (string): The location name where the line is.
      - `locationId` (string): The ID for the location.
      - `lineKeyLabel` (string): Customizable line key label for monitored member.
    - `speedDial` (object):
      - `id` (string): The identifier of the speed dial.
      - `displayName` (string): The display name of the speed dial.
      - `type` (string): The type of the speed dial.  * `PEOPLE` - Object is a user.  * `PLACE` - Object is a workspace.  * `VIRTUAL_LINE` - Object is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
      - `lineKeyLabel` (string): Customizable line key label for speed dial.
      - `phoneNumber` (string): The phone number of the speed dial.
      - `location` (string): The location name where the speed dial is.
      - `locationId` (string): The ID for the location.
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
