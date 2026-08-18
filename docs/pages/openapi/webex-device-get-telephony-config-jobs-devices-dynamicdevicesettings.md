---
doc_id: webex-device-get-telephony-config-jobs-devices-dynamicdevicesettings
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/devices/dynamicDeviceSettings
operation_id: listDynamicDeviceSettingsJobs
tags: Device Call Settings With Device Dynamic Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.204751+00:00
---

# GET /telephony/config/jobs/devices/dynamicDeviceSettings

**API:** Webex Device
**Área:** Device Call Settings With Device Dynamic Settings
**operationId:** `listDynamicDeviceSettingsJobs`

## Resumen
List Device Dynamic Settings Jobs

## Descripción
List device dynamic settings jobs.

Lists all the jobs for job type `dynamicdevicesettings` for the given organization in order of most recent one to oldest one irrespective of its status.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Retrieve list of device dynamic settings jobs for this organization.
- `start` [query] (number): Start at the zero-based offset in the list of jobs. Default is 0.
- `max` [query] (number): Limit the number of jobs returned to this maximum count. Default is 2000.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/devices/dynamicDeviceSettings' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array) (**requerido**): Lists all jobs for the customer of type `dynamicdevicesettings` in order of most recent one to oldest one irrespective of its status.
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

### Ejemplo — respuesta 200
```json
{
  "items": [
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
          "startTime": "2023-07-05T21:36:53.749Z",
          "endTime": "2023-07-05T21:37:06.105Z",
          "lastUpdated": "2023-07-05T21:37:06.714Z",
          "statusMessage": "COMPLETED",
          "exitCode": "COMPLETED",
          "createdTime": "2023-07-05T21:36:53.551Z",
          "stepExecutionStatuses": [
            {
              "id": 0,
              "startTime": "2023-07-05T21:36:54.601Z",
              "endTime": "2023-07-05T21:37:06.077Z",
              "lastUpdated": "2023-07-05T21:37:06.078Z",
              "statusMessage": "COMPLETED",
              "exitCode": "COMPLETED",
              "name": "dynamicdevicesettingsUpdate",
              "timeElapsed": "PT11.476S"
            }
          ],
          "timeElapsed": "PT11.476S"
        }
      ],
      "latestExecutionStatus": "COMPLETED",
      "latestExecutionExitCode": "COM
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