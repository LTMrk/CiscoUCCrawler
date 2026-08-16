---
doc_id: webex-cloud-calling-get-people-personid-features-monitoring
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /people/{personId}/features/monitoring
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.639216+00:00
---

# GET /people/{personId}/features/monitoring

**API:** Webex Cloud Calling
**Área:** Person Call Settings
**operationId:** `getMonitoringSettingsPerson`

## Resumen
Retrieve a Person's Monitoring Settings

## Descripción
Retrieve the monitoring settings for a person, which show specified people, places, virtual lines, or call park extensions that are being monitored.
Monitors the line status, indicating if a person, place, or virtual line is on a call and if a call has been parked on that extension.

This API requires a full, user, or read-only administrator or location administrator auth token with a scope of `spark-admin:people_read`.

## Parámetros
- `personId` [path] (string) **(requerido)**: Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter, as the default is the same organization as the token used to access the API.

## Respuestas
- **200**: OK
  - `callParkNotificationEnabled` (boolean) **(requerido)**: Indicates whether call park notification is enabled.
  - `availableEntriesCount` (integer) **(requerido)**: Indicates additional number of entries that can be stored (more than the number of entries listed).
  - `monitoredElements` (array) **(requerido)**: Settings of monitored elements, which can be a person, place, virtual line, or call park extension.
    - `member` (object): Monitored person, workspace, or virtual line.
      - `id` (string) **(requerido)**: The identifier of the monitored person, workspace, or virtual line.
      - `lastName` (string): Last name of the monitored member (Virtual Line or User). For Workspace, this field is not applicable.
      - `firstName` (string): First name of the monitored member (Virtual Line or User). For Workspace, this field is not applicable.
      - `displayName` (string): The display name of the monitored person, workspace, or virtual line.
      - `lineKeyLabel` (string): This is a custom line key label configured for the Member.
      - `type` (string): * `PEOPLE` - Person or list of people.  * `PLACE` - Workspace that is not assigned to a specific person such as for a shared device in a common area.  * `VIRTUAL_LINE` - Virtual line or list of virtual lines. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
      - `email` (string): The email address of the monitored person.
      - `numbers` (array) **(requerido)**: The list of phone numbers containing only the primary number for the monitored person, workspace or virtual line.
        - `external` (string): External phone number of the monitored person, workspace or virtual line.
        - `extension` (string): Extension number of the monitored person, workspace or virtual line.
        - `routingPrefix` (string): Routing prefix of location.
        - `esn` (string): Routing prefix + extension of a person or workspace.
        - `primary` (boolean): Indicates whether phone number is a primary number.
      - `location` (string) **(requerido)**: The name of the location where the monitored person, workspace, or virtual line is situated.
      - `locationId` (string) **(requerido)**: The ID of the location.
    - `callparkextension` (object): Monitored call park extension.
      - `id` (string) **(requerido)**: The identifier of the call park extension.
      - `name` (string): The name used to describe the call park extension.
      - `lineKeyLabel` (string): This is a custom line key label configured for the Call Park Extension.
      - `extension` (string): The extension number for the call park extension.
      - `routingPrefix` (string): Routing prefix of the location.
      - `esn` (string): Routing prefix plus extension of the Call Park Extension. If routing prefix is not configured for the location, esn will be same as extension.
      - `location` (string) **(requerido)**: The location name where the call park extension is.
      - `locationId` (string) **(requerido)**: The ID of the location.
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
