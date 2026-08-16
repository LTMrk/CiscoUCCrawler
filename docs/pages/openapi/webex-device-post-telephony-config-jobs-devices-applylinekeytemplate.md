---
doc_id: webex-device-post-telephony-config-jobs-devices-applylinekeytemplate
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
method: POST
path: /telephony/config/jobs/devices/applyLineKeyTemplate
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.128617+00:00
---

# POST /telephony/config/jobs/devices/applyLineKeyTemplate

**API:** Webex Device
**Área:** Device Call Settings
**operationId:** `applyLineKeyTemplate`

## Resumen
Apply a Line Key Template

## Descripción
Apply a Line Key Template or reset devices to their factory Line Key settings.

Line Keys, also known as Programmable Line Keys (PLK), are the keys found on either side of a typical desk phone display.
A Line Key Template is a definition of actions that will be performed by each of the Line Keys for a particular device model.
This API allows users to apply a line key template or apply factory default Line Key settings to devices in a set of locations or across all locations in the organization.

Applying a Line Key Template or resetting devices to their default Line Key configuration requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Apply Line Key Template for this organization.

## Cuerpo de la petición (application/json)
- `action` (string) **(requerido)**: Line key Template action to perform.  * `APPLY_TEMPLATE` - Used to apply LinekeyTemplate to devices.  * `APPLY_DEFAULT_TEMPLATES` - Used to reset devices to its default Linekey Template configurations. Valores: APPLY_TEMPLATE, APPLY_DEFAULT_TEMPLATES.
- `templateId` (string) **(requerido)**: `templateId` is required for `APPLY_TEMPLATE` action.
- `locationIds` (array): Used to search for devices only in the given locations.
- `excludeDevicesWithCustomLayout` (boolean): Indicates whether to exclude devices with custom layout.
- `includeDeviceTags` (array): Include devices only with these tags.
- `excludeDeviceTags` (array): Exclude devices with these tags.
- `advisoryTypes` (object):
  - `moreSharedAppearancesEnabled` (boolean): Refine search to apply changes to devices that contain the warning "More shared/virtual line appearances than shared/virtual lines requested".
  - `fewSharedAppearancesEnabled` (boolean): Refine search to apply changes to devices that contain the warning "More shared/virtual lines requested than shared/virtual line appearances".
  - `moreMonitorAppearancesEnabled` (boolean): Refine search to apply changes to devices that contain the warning "More monitored line appearances than monitored lines in the user's monitoring list".
  - `moreCPEAppearancesEnabled` (boolean): Refine search to apply changes to devices that contain the warning "More call park extension line appearances than call park extensions in user's monitoring list".
  - `moreModeManagementAppearancesEnabled` (boolean): Refine search to apply changes to devices that contain the warning "More mode management lines configured for the device". The default value is false.

### Ejemplo de petición
```json
{
  "action": "APPLY_TEMPLATE",
  "templateId": "Y2lzY29zcGFyazovL3VzL0RFVklDRV9MSU5FX0tFWV9URU1QTEFURS81NzVhMWY3Zi03MjRkLTRmZGUtODk4NC1mNjNhNDljMzYxZmQ",
  "locationIds": [
    "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTA5OA"
  ],
  "excludeDevicesWithCustomLayout": true,
  "includeDeviceTags": [
    "accounting",
    "sales"
  ],
  "excludeDeviceTags": [
    "admin"
  ],
  "advisoryTypes": {
    "moreSharedAppearancesEnabled": true,
    "fewSharedAppearancesEnabled": true,
    "moreMonitorAppearancesEnabled": "true",
    "moreCPEAppearancesEnabled": "true",
    "moreModeManagementAppearancesEnabled": true
  }
}
```

## Respuestas
- **202**: Accepted
  - `name` (string) **(requerido)**: Job name.
  - `id` (string) **(requerido)**: Unique identifier of the job.
  - `trackingId` (string) **(requerido)**: Unique identifier to track the flow of HTTP requests.
  - `sourceUserId` (string) **(requerido)**: Unique identifier to identify which user has run the job.
  - `sourceCustomerId` (string) **(requerido)**: Unique identifier to identify the customer who has run the job.
  - `targetCustomerId` (string) **(requerido)**: Unique identifier to identify the customer for which the job was run.
  - `instanceId` (number) **(requerido)**: Unique identifier to identify the instance of the job.
  - `jobExecutionStatus` (array): Displays the most recent step's execution status. Contains execution statuses of all the steps involved in the execution of the job.
    - `id` (number) **(requerido)**: Unique identifier that identifies each instance of the job.
    - `startTime` (string): Step execution start time in UTC format.
    - `endTime` (string): Step execution end time in UTC format.
    - `lastUpdated` (string): Last updated time (in UTC format) post one of the step execution completion.
    - `statusMessage` (string): Displays status for overall steps that are part of the job.
    - `exitCode` (string): Exit Code for a job.
    - `createdTime` (string): Job creation time in UTC format.
    - `timeElapsed` (string): Time lapsed since the job execution started.
    - `stepExecutionStatuses` (array): Status of each step within a job.
      - `id` (number) **(requerido)**: Unique identifier that identifies each step in a job.
      - `startTime` (string): Step execution start time in UTC format.
      - `endTime` (string): Step execution end time in UTC format.
      - `lastUpdated` (string): Last updated time for a step in UTC format.
      - `statusMessage` (string): Displays the status of a step.
      - `exitCode` (string): Exit Code for a step.
      - `name` (string): Name of different steps the job goes through.
      - `timeElapsed` (string): Time lapsed since the step execution started.
  - `latestExecutionStatus` (string) **(requerido)**: Indicates the most recent status (`STARTING`, `STARTED`, `COMPLETED`, `FAILED`) of the job at the time of invocation.
  - `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS.
  - `percentageComplete` (integer) **(requerido)**: Indicates the progress of the job.
  - `updatedCount` (integer) **(requerido)**: Number of job steps completed.
  - `advisoryCount` (integer) **(requerido)**: Number of job steps completed with advisories.
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
