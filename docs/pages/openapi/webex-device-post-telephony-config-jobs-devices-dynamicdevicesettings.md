---
doc_id: webex-device-post-telephony-config-jobs-devices-dynamicdevicesettings
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: POST
path: /telephony/config/jobs/devices/dynamicDeviceSettings
operation_id: updatesDynamicDeviceSettingsAcrossOrganizationOrLocation
tags: Device Call Settings With Device Dynamic Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.204502+00:00
---

# POST /telephony/config/jobs/devices/dynamicDeviceSettings

**API:** Webex Device
**Área:** Device Call Settings With Device Dynamic Settings
**operationId:** `updatesDynamicDeviceSettingsAcrossOrganizationOrLocation`

## Resumen
Update Device Dynamic Settings Across Organization or Location

## Descripción
Creates a job to update device settings at location or organization level.

The job runs asynchronously and persistently, applying the requested settings in bulk to all relevant devices, which may belong to multiple families as specified in the request. If a `locationId` is provided, only devices in that location are affected.

A unique job ID is returned to track status and errors.

Only one job can run per customer per organization at a time. Additionally, this job cannot run in parallel with other device jobs such as [Call device settings](/docs/api/v1/device-call-settings/change-device-settings-across-organization-or-location-job) and [Rebuild Phones](/docs/api/v1/device-call-settings/rebuild-phones-configuration).

Running a job requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Apply update device dynamic settings for all the devices under this organization.

## Cuerpo de la petición (application/json)
- `locationId` (string): If present, the requested settings will be updated to devices under this location.
- `tags` (array) (**requerido**): Array of tag identifiers for settings to be updated. Each setting is identified by a `familyOrModelDisplayName` and `tag`. Supports updating multiple settings across different device families in a single request.
  - `familyOrModelDisplayName` (string) (**requerido**): The `familyOrModelDisplayName` of the device to which the tag applies. This value must exist in the validation schema. Long. max: 40.
  - `tag` (string) (**requerido**): The unique identifier for the setting to be updated. Long. max: 64.
  - `action` (string) (**requerido**): The action to perform on the setting. When action is `SET`, `tag` is updated to specified value. When action is `CLEAR`, the `tag` value at device level is removed, and the device will inherit the value from the parent level, if it exists. Valores: SET, CLEAR.
  - `value` (string): The new value to set for the setting. This field is required when `action` is `SET` and ignored otherwise. Long. max: 256.

### Ejemplo — petición
```json
{
  "locationId": "",
  "tags": [
    {
      "familyOrModelDisplayName": "Poly",
      "tag": "%DO_MENU_TITLE_BACKGROUND%",
      "action": "CLEAR"
    },
    {
      "familyOrModelDisplayName": "Poly",
      "tag": "%ENABLE_BLUETOOTH%",
      "action": "SET",
      "value": "1"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/jobs/devices/dynamicDeviceSettings' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"tags": []}'
```

## Respuestas correctas
**202**: Accepted
- `name` (string) (**requerido**): Name of the job which in this case, is `dynamicdevicesettings`.
- `id` (string) (**requerido**): Unique identifier of the job.
- `trackingId` (string) (**requerido**): Unique identifier to track the flow of HTTP requests.
- `sourceUserId` (string) (**requerido**): Unique identifier of the user who has run the job.
- `sourceCustomerId` (string) (**requerido**): Unique identifier of the customer who has run the job.
- `targetCustomerId` (string) (**requerido**): Unique identifier of the customer for which the job was run.
- `instanceId` (number) (**requerido**): Unique identifier to identify the instance of the job.
- `jobExecutionStatus` (array) (**requerido**): Displays the most recent step's execution status. Contains execution statuses of all the steps involved in the execution of the job.
  - `id` (number) (**requerido**): Unique identifier that identifies each instance of the job.
  - `startTime` (string): Step execution start time in UTC format.
  - `endTime` (string): Step execution end time in UTC format.
  - `lastUpdated` (string): Last updated time (in UTC format) post one of the step execution completion.
  - `statusMessage` (string): Displays status for overall steps that are part of the job.
  - `exitCode` (string): Exit Code for a job.
  - `createdTime` (string): Job creation time in UTC format.
  - `timeElapsed` (string): Time lapsed since the job execution started.
  - `stepExecutionStatuses` (array): Status of each step within a job.
    - `id` (number) (**requerido**): Unique identifier that identifies each step in a job.
    - `startTime` (string): Step execution start time in UTC format.
    - `endTime` (string): Step execution end time in UTC format.
    - `lastUpdated` (string): Last updated time for a step in UTC format.
    - `statusMessage` (string): Displays the status of a step.
    - `exitCode` (string): Exit Code for a step.
    - `name` (string): Name of different steps the job goes through.
    - `timeElapsed` (string): Time lapsed since the step execution started.
- `latestExecutionStatus` (string) (**requerido**): * `STARTING` - Indicates the job has started.  * `STARTED` - Indicates the job is in progress.  * `COMPLETED` - Indicates the job has completed.  * `FAILED` - Indicates the job has failed. Valores: STARTING, STARTED, COMPLETED, FAILED.
- `latestExecutionExitCode` (string) (**requerido**): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS.
- `target` (string) (**requerido**): Indicates the target entity. Valores: CUSTOMER, LOCATION.
- `locationId` (string): Unique identifier of a location.
- `locationName` (string): Name of the location. Included only when `target` is `LOCATION`.
- `percentageComplete` (integer) (**requerido**): Indicates the progress of the job.

### Ejemplo — respuesta 202
```json
{
  "name": "dynamicdevicesettings",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC8wZTJjNmI5NC1hNDdlLTQxZGUtODE5ZS04YTcwNTZjMTc5MDk",
  "trackingId": "NA_a9ef6908-60cf-40e6-b56f-461abffd6fa3",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85OThhMThhYi1kZjY5LTQ5MWYtYmViZi03MzUxMGE3ODI5N2I",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9hNDVkNmNkYS1hZTVhLTQwYzMtYTdhZC01NjUwZmRkZGQ1M2M",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9hNDVkNmNkYS1hZTVhLTQwYzMtYTdhZC01NjUwZmRkZGQ1M2M",
  "instanceId": 0,
  "jobExecutionStatus": [
    {
      "id": 0,
      "startTime": "2025-05-13T10:59:44.106Z",
      "lastUpdated": "2025-05-13T10:59:44.106Z",
      "statusMessage": "STARTED",
      "exitCode": "UNKNOWN",
      "createdTime": "2025-05-13T10:50:01.352Z",
      "timeElapsed": "PT11.476S"
    }
  ],
  "latestExecutionStatus": "STARTED",
  "latestExecutionExitCode": "UNKNOWN",
  "target": "CUSTOMER",
  "locationId": "",
  "percentageComplete": 0
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
The Webex Device APIs provide endpoints for managing and monitoring Webex devices, including registration, configuration, status retrieval, workspace assignment, and firmware management. These APIs support automation of device onboarding, health monitoring, remote troubleshooting, and bulk configuration updates. Integration scenarios include custom device dashboards, proactive alerting, and seamless workspace management for meeting rooms and shared spaces. The APIs are essential for IT teams managing large fleets of Webex devices across distributed environments.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs