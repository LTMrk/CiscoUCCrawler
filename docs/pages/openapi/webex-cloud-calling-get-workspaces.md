---
doc_id: webex-cloud-calling-get-workspaces
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /workspaces
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.676654+00:00
---

# GET /workspaces

**API:** Webex Cloud Calling
**Área:** Workspaces
**operationId:** `listWorkspaces`

## Resumen
List Workspaces

## Descripción
List workspaces.

Use query parameters to filter the response. The `orgId` parameter can only be used by admin users of another organization (such as partners). The `locationId`, `workspaceLocationId`, `indoorNavigation`, `floorId`, `capacity` and `type` fields will only be present for workspaces that have a value set for them. The special values `notSet` (for filtering on category) and `-1` (for filtering on capacity) can be used to filter for workspaces without a type and/or capacity.

## Parámetros
- `orgId` [query] (string): List workspaces in this organization. Only admin users of another organization (such as partners) may use this parameter.
- `locationId` [query] (string): Location associated with the workspace. Values must originate from the /locations API and not the legacy /workspaceLocations API.
- `workspaceLocationId` [query] (string): Location associated with the workspace. Both values from the /locations API and the legacy /workspaceLocations API are supported. This field is deprecated and integrations should prefer `locationId` going forward.
- `floorId` [query] (string): Floor associated with the workspace.
- `displayName` [query] (string): List workspaces by display name.
- `capacity` [query] (number): List workspaces with the given capacity. Must be -1 or higher. A value of -1 lists workspaces with no capacity set.
- `type` [query] (string): List workspaces by type.
- `start` [query] (number): Offset. Default is 0.
- `max` [query] (number): Limit the maximum number of workspaces in the response.
- `calling` [query] (string): List workspaces by calling type.
- `supportedDevices` [query] (string): List workspaces by supported devices.
- `calendar` [query] (string): List workspaces by calendar type.
- `deviceHostedMeetingsEnabled` [query] (boolean): List workspaces enabled for device hosted meetings.
- `devicePlatform` [query] (string): List workspaces by device platform.
- `healthLevel` [query] (string): List workspaces by health level.
- `includeDevices` [query] (boolean): Flag identifying whether to include the devices associated with the workspace in the response.
- `includeCapabilities` [query] (boolean): Flag identifying whether to include the workspace capabilities in the response.
- `plannedMaintenance` [query] (string): List workspaces with given maintenance mode.
- `customAttribute` [query] (string): List workspaces with given custom attribute key.

## Respuestas
- **200**: OK
  - `items` (array): An array of workspace objects.
    - `id` (string): Unique identifier for the Workspace.
    - `orgId` (string): `OrgId` associated with the workspace.
    - `locationId` (string): Location associated with the workspace (ID to use for the [/locations API](/docs/api/v1/locations)).
    - `workspaceLocationId` (string): Legacy workspace location ID associated with the workspace. Prefer `locationId`.
    - `floorId` (string): Floor associated with the workspace.
    - `displayName` (string): A friendly name for the workspace.
    - `capacity` (number): How many people the workspace is suitable for.
    - `type` (string): The workspace type.  * `notSet` - No workspace type set.  * `focus` - High concentration.  * `huddle` - Brainstorm/collaboration.  * `meetingRoom` - Dedicated meeting space.  * `open` - Unstructured agile.  * `desk` - Individual.  * `other` - Unspecified. Valores: notSet, focus, huddle, meetingRoom, open, desk, other.
    - `sipAddress` (string): `SipUrl` to call all the devices associated with the workspace.
    - `created` (string): The date and time that the workspace was registered, in ISO8601 format.
    - `calling` (object): Calling type.
      - `type` (string): Calling.  * `freeCalling` - Free Calling.  * `hybridCalling` - Hybrid Calling.  * `webexCalling` - Webex Calling.  * `webexEdgeForDevices` - Webex Edge For Devices.  * `thirdPartySipCalling` - Third-party SIP URI.  * `none` - No Calling. Valores: freeCalling, hybridCalling, webexCalling, webexEdgeForDevices, thirdPartySipCalling, none.
      - `hybridCalling` (object): The `hybridCalling` object only applies when calling type is `hybridCalling`.
        - `emailAddress` (string): End user email address in Cisco Unified CM.
      - `webexCalling` (object): The `webexCalling` object only applies when calling type is `webexCalling`.
        - `licenses` (array): The Webex Calling license associated with this workspace.
    - `calendar` (object): Calendar type. Calendar of type `none` does not include an `emailAddress` field.
      - `type` (string): * `none` - No calendar.  * `google` - Google Calendar.  * `microsoft` - Microsoft Exchange or Office 365. Valores: none, google, microsoft.
      - `emailAddress` (string): Workspace email address. Will not be set when the calendar type is `none`.
    - `notes` (string): Notes associated to the workspace.
    - `hotdeskingStatus` (string): Hot desking status of the workspace.  * `on` - Workspace supports hotdesking.  * `off` - Workspace does not support hotdesking. Valores: on, off.
    - `supportedDevices` (string): The supported devices for the workspace. Default is `collaborationDevices`.  * `collaborationDevices` - Workspace supports collaboration devices.  * `phones` - Workspace supports MPP phones. Valores: collaborationDevices, phones.
    - `deviceHostedMeetings` (object): Device hosted meetings configuration.
      - `enabled` (boolean): `true` if enabled or `false` otherwise.
      - `siteUrl` (string): The Webex site for the device hosting meetings.
    - `devicePlatform` (string): The device platform.  * `cisco` - Cisco.  * `microsoftTeamsRoom` - Microsoft Teams Room. Valores: cisco, microsoftTeamsRoom.
    - `indoorNavigation` (object): Indoor navigation configuration.
      - `url` (string): URL of a map locating the workspace.
    - `health` (object): The health of the workspace.
      - `level` (string): Health level. The level is based on the list of issues associated with the workspace. Valores: error, warning, info, ok.
      - `issues` (array): A list of workspace issues.
        - `id` (string): Issue id.
        - `createdAt` (string): Issue created timestamp.
        - `title` (string): Issue title.
        - `description` (string): Issue description.
        - `recommendedAction` (string): Recommended action to mitigate issue.
        - `level` (object): Issue level.
          - `Members` (string):  Valores: error, warning, info.
    - `devices` (array): A list of devices associated with the workspace.
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
