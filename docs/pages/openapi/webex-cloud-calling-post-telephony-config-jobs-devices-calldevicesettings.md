---
doc_id: webex-cloud-calling-post-telephony-config-jobs-devices-calldevicesettings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/jobs/devices/callDeviceSettings
operation_id: changeDeviceSettingsAcrossOrganizationOrLocationJob
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.999395+00:00
---

# POST /telephony/config/jobs/devices/callDeviceSettings

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `changeDeviceSettingsAcrossOrganizationOrLocationJob`

## Resumen
Change Device Settings Across Organization Or Location Job

## Descripción
Change device settings across organization or locations jobs.

Performs bulk and asynchronous processing for all types of device settings initiated by organization and system admins in a stateful persistent manner. This job will modify the requested device settings across all the devices. Whenever a location ID is specified in the request, it will modify the requested device settings only for the devices that are part of the provided location within an organization.

Returns a unique job ID which can then be utilized further to retrieve status and errors for the same.

Only one job per customer can be running at any given time within the same organization. An attempt to run multiple jobs at the same time will result in a 409 error response.

Running a job requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Apply change device settings for all the devices under this organization.

## Cuerpo de la petición (application/json)
- `locationId` (string): Location within an organization where changes of device setings will be applied to all the devices within it.
- `locationCustomizationsEnabled` (boolean): Indicates if all the devices within this location will be customized with new requested customizations(if set to `true`) or will be overridden with the one at organization level (if set to `false` or any other value). This field has no effect when the job is being triggered at organization level.
- `customizations` (object):
  - `ata` (object):
    - `audioCodecPriority` (object) (**requerido**):
      - `selection` (string) (**requerido**): * `REGIONAL` - Indicates the regional selection type for audio codec priority.  * `CUSTOM` - Indicates the custom selection type for audio codec priority. Valores: REGIONAL, CUSTOM.
      - `primary` (string) (**requerido**): Indicates the primary Audio Codec.
      - `secondary` (string) (**requerido**): Indicates the secondary Audio Codec.
      - `tertiary` (string) (**requerido**): Indicates the tertiary Audio Codec.
    - `ataDtmfMode` (string) (**requerido**): * `STRICT` - A DTMF digit requires an extra hold time after detection and the DTMF level threshold is raised to -20 dBm.  * `NORMAL` - Normal threshold mode. Valores: STRICT, NORMAL.
    - `ataDtmfMethod` (string) (**requerido**): * `INBAND` - Sends DTMF by using the audio path.  * `AVT` - Audio video transport. Sends DTMF as AVT events.  * `AUTO` - Uses InBand or AVT based on the outcome of codec negotiation. Valores: INBAND, AVT, AUTO.
    - `cdpEnabled` (boolean) (**requerido**): Enable/disable Cisco Discovery Protocol for local devices.
    - `lldpEnabled` (boolean) (**requerido**): Enable/disable Link Layer Discovery Protocol for local devices.
    - `qosEnabled` (boolean) (**requerido**): Enable/disable quality of service tagging of packets from the local device to the Webex Calling platform.
    - `vlan` (object) (**requerido**):
      - `enabled` (boolean) (**requerido**): Denotes whether the VLAN object of an ATA is enabled.
      - `value` (number) (**requerido**): The value of the VLAN Object of an ATA object.
    - `webAccessEnabled` (boolean) (**requerido**): Enable/disable user level web access to the local device.
    - `nightlyResyncEnabled` (boolean) (**requerido**): Enable/disable the automatic nightly configuration resync of the MPP device.
    - `snmp` (object) (**requerido**):
      - `enabled` (boolean) (**requerido**): Denotes whether the Simple Network Management Protocol of an ATA is enabled.
      - `trustedIP` (string) (**requerido**): Trusted IPv4 address and subnet mask in this order: 0.0.0.0/0.0.0.0.
      - `getCommunity` (string) (**requerido**): Read-only community string that allows/denies access to other device's statistics. Default value is `public`.
      - `setCommunity` (string) (**requerido**): Read-write community string that protects the device against unauthorized changes. Must never be set to `public`.
      - `snmpV3Enabled` (boolean) (**requerido**): Denotes whether the SNMPv3 security is enabled.
  - `dect` (object):
    - `audioCodecPriority` (object) (**requerido**):
      - `selection` (string) (**requerido**): * `REGIONAL` - Indicates the regional selection type for audio codec priority.  * `CUSTOM` - Indicates the custom selection type for audio codec priority. Valores: REGIONAL, CUSTOM.
      - `primary` (string) (**requerido**): Indicates the primary Audio Codec.
      - `secondary` (string) (**requerido**): Indicates the secondary Audio Codec.
      - `tertiary` (string) (**requerido**): Indicates the tertiary Audio Codec.
    - `cdpEnabled` (boolean) (**requerido**): Enable/disable Cisco Discovery Protocol for local devices.
    - `dect6825HandsetEmergencyNumber` (string) (**requerido**): Specify the destination number to be dialled from the DECT Handset top button when pressed.
    - `lldpEnabled` (boolean) (**requerido**): Enable/disable Link Layer Discovery Protocol for local devices.
    - `multicast` (string) (**requerido**): Specify up to 3 multicast group URLs each with a unique listening port.
    - `qosEnabled` (boolean) (**requerido**): Enable/disable quality of service tagging of packets from the local device to the Webex Calling platform.
    - `vlan` (object) (**requerido**):
      - `enabled` (boolean) (**requerido**): Denotes whether the VLAN object of DECT is enabled.
      - `value` (number) (**requerido**): Value of the VLAN Object of DECT.
    - `webAccessEnabled` (boolean) (**requerido**): Enable/disable user level web access to the local device.
    - `nightlyResyncEnabled` (boolean) (**requerido**): Enable/disable phone's default behavior regarding the nightly maintenance synchronization with the Webex Calling platform.
  - `mpp` (object):
    - `pnacEnabled` (boolean) (**requerido**): Indicates whether the PNAC of MPP object is enabled or not.
    - `audioCodecPriority` (object) (**requerido**):
      - `selection` (string) (**requerido**): Indicates the selection of the Audio Codec Priority Object for an MPP object.
      - `primary` (string) (**requerido**): Indicates the primary Audio Codec for an MPP object.
      - `secondary` (string) (**requerido**): Indicates the secondary Audio Codec for an MPP object.
      - `tertiary` (string) (**requerido**): Indicates the tertiary Audio Codec for an MPP object.
    - `backlightTimer` (string) (**requerido**): * `ONE_MIN` - Set the phone's backlight to be on for one minute.  * `FIVE_MIN` - Set the phone's backlight to be on for five minutes.  * `THIRTY_MIN` - Set the phone's backlight to be on for thirty minutes.  * `ALWAYS_ON` - Keep the phone's backlight always on. Valores: ONE_MIN, FIVE_MIN, THIRTY_MIN, ALWAYS_ON.
    - `background` (object) (**requerido**):
      - `image` (string): * `NONE` - Indicates that there will be no background image set for the devices.  * `DARK_BLUE` - Indicates that dark blue background image will be set for the devices.  * `CISCO_DARK_BLUE` - Indicates that Cisco themed dark blue background image will be set for the devices.  * `WEBEX_DARK_BLUE` - Indicates that Cisco Webex dark blue background image will be set for the devices.  * `CUSTOM_BACKGROUND` - Indicates that a custom background image will be set for the devices.  * `customUrl` - When this option is selected, a field 'Custom Background URL' needs to be added with the image url. URLs provided must link directly to an image file and be in HTTP, HTTPS, or filepath format. Valores: NONE, DARK_BLUE, CISCO_DARK_BLUE, WEBEX_DARK_BLUE, CUSTOM_BACKGROUND.
      - `customUrl` (string):
    - `displayNameFormat` (string): * `PERSON_NUMBER` - Indicates that devices will display the person's phone number, or if a person doesn't have a phone number, the location number will be displayed.  * `PERSON_FIRST_THEN_LAST_NAME` - Indicates that devices will display the name in first name then last name format.  * `PERSON_LAST_THEN_FIRST_NAME` - Indicates that devices will display the name in last name then first name format. Valores: PERSON_NUMBER, PERSON_FIRST_THEN_LAST_NAME, PERSON_LAST_THEN_FIRST_NAME.
    - `cdpEnabled` (boolean) (**requerido**): Allows you to enable/disable CDP for local devices.
    - `defaultLoggingLevel` (string) (**requerido**): * `STANDARD` - Enables standard logging.  * `DEBUGGING` - Enables detailed debugging logging. Valores: STANDARD, DEBUGGING.
    - `dndServicesEnabled` (boolean) (**requerido**): Enable/disable Do-Not-Disturb capabilities for Multi-Platform Phones.
    - `acd` (object) (**requerido**):
      - `enabled` (boolean) (**requerido**): Indicates whether the ACD object is enabled.
      - `displayCallqueueAgentSoftkeys` (string) (**requerido**):  Valores: FRONT_PAGE, LAST_PAGE.
    - `shortInterdigitTimer` (number) (**requerido**): Indicates the short inter digit timer value.

### Ejemplo — petición
```json
{
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTA5OA",
  "locationCustomizationsEnabled": true,
  "customizations": {
    "ata": {
      "audioCodecPriority": {
        "primary": "G711a",
        "secondary": "G711u",
        "tertiary": "G729a",
        "selection": "REGIONAL"
      },
      "ataDtmfMode": "NORMAL",
      "ataDtmfMethod": "AVT",
      "cdpEnabled": true,
      "lldpEnabled": true,
      "qosEnabled": true,
      "vlan": {
        "enabled": true,
        "value": 1
      }
    },
    "dect": {
      "audioCodecPriority": {
        "primary": "G729",
        "secondary": "G711u",
        "tertiary": "G711a",
        "selection": "REGIONAL"
      },
      "cdpEnabled": true,
      "lldpEnabled": false,
      "multicast": [],
      "qosEnabled": true,
      "vlan": {
        "enabled": false,
        "value": null
      }
    },
    "mpp": {
      "pnacEnabled": true,
      "audioCodecPriority": {
        "primary": "OPUS",
        "secondary": "G722",
        "tertiary": "G711u",
        "selection": "CUSTOM"
      },
      "backlightTimer": "FIVE_M",
      "background": {
        "customUrl": "",
        "image": "NONE"
      },
      "displayNameFormat": "PERSON_FIRST_THEN_LAST_NAME",
      "cdpEnabled": false,
      "dndServicesEnabled": true,
      "acd": {
        "enabled": false,
        "displayCallqueueAgentSoftkeys": "LAST_PAGE"
      },
      "shortInterdigitTimer": 14,
      "longInterdigitTimer": 1
  ... (truncado)
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/jobs/devices/callDeviceSettings' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `name` (string) (**requerido**): Job name.
- `id` (string) (**requerido**): Unique identifier of the job.
- `jobType` (string) (**requerido**): Job type.
- `trackingId` (string) (**requerido**): Unique identifier to track the flow of HTTP requests.
- `sourceUserId` (string) (**requerido**): Unique identifier to identify which user has run the job.
- `sourceCustomerId` (string) (**requerido**): Unique identifier of the organization that initiated the job.
- `targetCustomerId` (string) (**requerido**): Unique identifier of the organization for which the job was run.
- `instanceId` (integer) (**requerido**): Unique identifier to identify the instance of the job.
- `jobExecutionStatus` (array): Displays the most recent step's execution status. Contains execution statuses of all the steps involved in the execution of the job.
  - `id` (integer) (**requerido**): Unique identifier that identifies each instance of the job.
  - `lastUpdated` (string) (**requerido**): Last updated time (in UTC format) post one of the step execution completion.
  - `statusMessage` (string) (**requerido**): Displays status for overall steps that are part of the job.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
  - `exitCode` (string): Exit Code for a job.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
  - `createdTime` (string) (**requerido**): Job creation time in UTC format.
  - `timeElapsed` (string) (**requerido**): Time lapsed since the job execution started.
- `latestExecutionStatus` (string) (**requerido**): Most recent status of the job at the time of invocation.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
- `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
- `operationType` (string) (**requerido**): The operation type that was carried out.
- `sourceLocationId` (string) (**requerido**): Unique location identifier for which the job was run.
- `targetLocationId` (string) (**requerido**): Unique location identifier for which the numbers have been moved.
- `counts` (object) (**requerido**):
  - `totalMoves` (number) (**requerido**): Total number of user moves requested.
  - `moved` (number) (**requerido**): Total number of user moves completed successfully.
  - `failed` (number) (**requerido**): Total number of user moves that were completed with failures.
  - `pending` (number) (**requerido**): Total number of user moves that were pending with number orders.
  - `skipped` (number) (**requerido**): Total number of user moves that were skipped.

### Ejemplo — respuesta 200
```json
{
  "name": "calldevicesettings",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC8wMTA4NDJjMy1mNWQ5LTRjOWQtOGZiYi0yYzIxZmU4OWI0YzQ",
  "jobType": "calldevicesettings",
  "trackingId": "ROUTER_62F66055-8D70-01BB-0137-AC10A8310137",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85OThhMThhYi1kZjY5LTQ5MWYtYmViZi03MzUxMGE3ODI5N2I",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9hNDVkNmNkYS1hZTVhLTQwYzMtYTdhZC01NjUwZmRkZGQ1M2M",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9hNDVkNmNkYS1hZTVhLTQwYzMtYTdhZC01NjUwZmRkZGQ1M2M",
  "instanceId": 235142,
  "jobExecutionStatus": [
    {
      "id": 235842,
      "lastUpdated": "2022-08-12T14:15:14.591Z",
      "statusMessage": "STARTING",
      "exitCode": "UNKNOWN",
      "createdTime": "2022-08-12T14:15:14.591Z",
      "timeElapsed": "PT0S"
    }
  ],
  "latestExecutionStatus": "STARTING",
  "latestExecutionExitCode": "UNKNOWN",
  "locationCustomizationsEnabled": false,
  "target": "CUSTOMER",
  "locationId": "",
  "percentageComplete": 0
}
```
- Cabecera `Link`: 

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