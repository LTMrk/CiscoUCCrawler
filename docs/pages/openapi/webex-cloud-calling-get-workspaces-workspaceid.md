---
doc_id: webex-cloud-calling-get-workspaces-workspaceid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /workspaces/{workspaceId}
operation_id: getWorkspaceDetails
tags: Workspaces
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.816813+00:00
---

# GET /workspaces/{workspaceId}

**API:** Webex Cloud Calling
**Área:** Workspaces
**operationId:** `getWorkspaceDetails`

## Resumen
Get Workspace Details

## Descripción
Shows details for a workspace, by ID.

The `locationId`, `workspaceLocationId`, `floorId`, `indoorNavigation`, `capacity`, `type` and `notes` fields will only be present if they have been set for the workspace. Specify the workspace ID in the `workspaceId` parameter in the URI.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): A unique identifier for the workspace.
- `includeDevices` [query] (boolean): Flag identifying whether to include the devices associated with the workspace in the response.
- `includeCapabilities` [query] (boolean): Flag identifying whether to include the workspace capabilities in the response.

## Ejemplo de invocación
```bash
curl -X GET '/workspaces/<workspaceId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
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
  - `id` (string): A unique identifier for the device.
  - `displayName` (string): A friendly name for the device.
  - `placeId` (string): The `placeId` field has been deprecated. Please use `workspaceId` instead.
  - `workspaceId` (string): The workspace associated with the device.
  - `personId` (string): The person associated with the device.
  - `orgId` (string): The organization associated with the device.
  - `capabilities` (array): The capabilities of the device.
  - `permissions` (array): The permissions the user has for this device. For example, `xapi` means this user is entitled to using the `xapi` against this device.
  - `connectionStatus` (string): The connection status of the device. Valores: connected, disconnected, connected_with_issues, offline_expired, activating, pending, unknown, offline_deep_sleep.
  - `product` (string): The product name. A display friendly version of the device's `model`.
  - `type` (string): The product type.
  - `tags` (array): Tags assigned to the device.
  - `ip` (string): The current IP address of the device.
  - `activeInterface` (string): The current network connectivity for the device. Valores: wired.
  - `mac` (string): The unique address for the network adapter.
  - `primarySipUrl` (string): The primary SIP address to dial this device.
  - `sipUrls` (array): All SIP addresses to dial this device.
  - `serial` (string): Serial number for the device.
  - `software` (string): The operating system name data and version tag.
  - `upgradeChannel` (string): The upgrade channel the device is assigned to.
  - `created` (string) (**requerido**): The date and time that the device was registered, in ISO8601 format.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1BMQUNFUy81MTAxQjA3Qi00RjhGLTRFRjctQjU2NS1EQjE5QzdCNzIzRjc",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY",
  "locationId": "Y2lzY29...",
  "workspaceLocationId": "YL34GrT...",
  "floorId": "Y2lzY29z...",
  "displayName": "SFO-12 Capanina",
  "capacity": 5,
  "type": "notSet",
  "sipAddress": "test_workspace_1@trialorg.room.ciscospark.com",
  "created": "2016-04-21T17:00:00.000Z",
  "calling": {
    "type": "hybridCalling",
    "hybridCalling": {
      "emailAddress": "workspace@example.com"
    },
    "webexCalling": {
      "licenses": [
        "Y2lzY29g4..."
      ]
    }
  },
  "notes": "this is a note",
  "hotdeskingStatus": "on",
  "supportedDevices": "collaborationDevices",
  "calendar": {
    "type": "microsoft",
    "emailAddress": "workspace@example.com"
  },
  "deviceHostedMeetings": {
    "enabled": true,
    "siteUrl": "'example.webex.com'"
  },
  "devicePlatform": "cisco",
  "indoorNavigation": {},
  "health": {
    "level": "error",
    "issues": [
      {
        "id": "",
        "createdAt": "",
        "title": "",
        "description": "",
        "recommendedAction": "",
        "level": {
          "Members": "error"
        }
      }
    ]
  },
  "devices": [
    {
      "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9ERVZJQ0UvNTEwMUIwN0ItNEY4Ri00RUY3LUI1NjUtREIxOUM3QjcyM0Y3",
      "displayName": "SFO12-3-PanHandle",
      "placeId": "Y2lzY29zcGFyazovL3Vz
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