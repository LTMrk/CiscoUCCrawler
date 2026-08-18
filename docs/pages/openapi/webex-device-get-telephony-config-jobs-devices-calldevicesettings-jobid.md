---
doc_id: webex-device-get-telephony-config-jobs-devices-calldevicesettings-jobid
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/devices/callDeviceSettings/{jobId}
operation_id: getChangeDeviceSettingsJobStatus
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.199542+00:00
---

# GET /telephony/config/jobs/devices/callDeviceSettings/{jobId}

**API:** Webex Device
**Área:** Device Call Settings
**operationId:** `getChangeDeviceSettingsJobStatus`

## Resumen
Get Change Device Settings Job Status

## Descripción
Get change device settings job status.

Provides details of the job with `jobId` of `jobType` `calldevicesettings`.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `jobId` [path] (string) (**requerido**): Retrieve job details for this `jobId`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/devices/callDeviceSettings/<jobId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `name` (string) (**requerido**): Job name.
- `id` (string) (**requerido**): Unique identifier of the job.
- `jobType` (string) (**requerido**): Job type.
- `trackingId` (string) (**requerido**): Unique identifier to track the flow of HTTP requests.
- `sourceUserId` (string) (**requerido**): Unique identifier to identify which user has run the job.
- `sourceCustomerId` (string) (**requerido**): Unique identifier to identify the customer who has run the job.
- `targetCustomerId` (string) (**requerido**): Unique identifier to identify the customer for which the job was run.
- `instanceId` (number) (**requerido**): Unique identifier to identify the instance of the job.
- `jobExecutionStatus` (array): Displays the most recent step's execution status. Contains execution statuses of all the steps involved in the execution of the job.
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
- `latestExecutionStatus` (string) (**requerido**): Indicates the most recent status (STARTING, STARTED, COMPLETED, FAILED) of the job at the time of invocation.
- `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS.
- `operationType` (string) (**requerido**): Indicates the operation type that was carried out.
- `sourceLocationId` (string) (**requerido**): Unique location identifier for which the job was run.
- `targetLocationId` (string) (**requerido**): Unique location identifier for which the numbers have been moved.
- `sourceLocationName` (string) (**requerido**): The location name for which the job was run.
- `targetLocationName` (string) (**requerido**): The location name for which the numbers have been moved.
- `counts` (object) (**requerido**):
  - `totalNumbers` (number) (**requerido**): Indicates the total number of phone numbers requested to be moved.
  - `numbersDeleted` (number) (**requerido**): Indicates the total number of phone numbers successfully deleted.
  - `numbersMoved` (number) (**requerido**): Indicates the total number of phone numbers successfully moved.
  - `numbersFailed` (number) (**requerido**): Indicates the total number of phone numbers failed.

### Ejemplo — respuesta 200
```json
{
  "name": "calldevicesettings",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC8wMTA4NDJjMy1mNWQ5LTRjOWQtOGZiYi0yYzIxZmU4OWI0YzQ",
  "jobType": "calldevicesettings",
  "trackingId": "ATLAS_89144033-afb5-44e8-bae8-946e84c71fa3_0",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85OThhMThhYi1kZjY5LTQ5MWYtYmViZi03MzUxMGE3ODI5N2I",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9hNDVkNmNkYS1hZTVhLTQwYzMtYTdhZC01NjUwZmRkZGQ1M2M",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9hNDVkNmNkYS1hZTVhLTQwYzMtYTdhZC01NjUwZmRkZGQ1M2M",
  "instanceId": 235690,
  "jobExecutionStatus": [
    {
      "id": 236410,
      "startTime": "2022-08-15T12:54:50.380Z",
      "endTime": "2022-08-15T12:55:01.833Z",
      "lastUpdated": "2022-08-15T12:55:02.160Z",
      "statusMessage": "COMPLETED",
      "exitCode": "COMPLETED",
      "createdTime": "2022-08-15T12:54:50.350Z",
      "stepExecutionStatuses": [
        {
          "id": 1159389,
          "startTime": "2022-08-15T12:54:50.433Z",
          "endTime": "2022-08-15T12:55:01.826Z",
          "lastUpdated": "2022-08-15T12:55:01.826Z",
          "statusMessage": "COMPLETED",
          "exitCode": "COMPLETED",
          "name": "calldevicesettingsOverrideProcess",
          "timeElapsed": "PT11.393S"
        }
      ],
      "timeElapsed": "PT11.393S"
    }
  ],
  "latestExecutionStatus": "COMPLETED",
  "latestExecutionExitCode": "COMPLETED",
  "locationCustomizationsEnabled": false,
  "target": "CUSTOMER",
  "locationId": "
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
The Webex Device APIs provide endpoints for managing and monitoring Webex devices, including registration, configuration, status retrieval, workspace assignment, and firmware management. These APIs support automation of device onboarding, health monitoring, remote troubleshooting, and bulk configuration updates. Integration scenarios include custom device dashboards, proactive alerting, and seamless workspace management for meeting rooms and shared spaces. The APIs are essential for IT teams managing large fleets of Webex devices across distributed environments.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs