---
doc_id: webex-device-get-telephony-config-jobs-devices-calldevicesettings
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
method: GET
path: /telephony/config/jobs/devices/callDeviceSettings
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.129931+00:00
---

# GET /telephony/config/jobs/devices/callDeviceSettings

**API:** Webex Device
**Área:** Device Call Settings
**operationId:** `listChangeDeviceSettingsJobs`

## Resumen
List Change Device Settings Jobs

## Descripción
List change device settings jobs.

Lists all the jobs for jobType `calldevicesettings` for the given organization in order of most recent one to oldest one irrespective of its status.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Retrieve list of 'calldevicesettings' jobs for this organization.
- `start` [query] (number): Start at the zero-based offset in the list of jobs. Default is 0.
- `max` [query] (number): Limit the number of jobs returned to this maximum count. Default is 2000.

## Respuestas
- **200**: OK
  - `items` (array) **(requerido)**: Lists all jobs for the customer in order of most recent one to oldest one irrespective of its status.
    - `name` (string) **(requerido)**: Job name.
    - `id` (string) **(requerido)**: Unique identifier of the job.
    - `jobType` (string) **(requerido)**: Job type.
    - `trackingId` (string) **(requerido)**: Unique identifier to track the flow of HTTP requests.
    - `sourceUserId` (string) **(requerido)**: Unique identifier to identify which user has run the job.
    - `sourceCustomerId` (string) **(requerido)**: Unique identifier to identify the customer who has run the job.
    - `targetCustomerId` (string) **(requerido)**: Unique identifier to identify the customer for which the job was run.
    - `instanceId` (number) **(requerido)**: Unique identifier to identify the instance of the job.
    - `jobExecutionStatus` (array): Displays the most recent step's execution status. Contains execution statuses of all the steps involved in the execution of the job.
      - `id` (number) **(requerido)**: Unique identifier that identifies each instance of the job.
      - `lastUpdated` (string): Last updated time (in UTC format) post one of the step execution completion.
      - `statusMessage` (string): Displays status for overall steps that are part of the job.
      - `exitCode` (string): Exit Code for a job.
      - `createdTime` (string): Job creation time in UTC format.
      - `timeElapsed` (string): Time lapsed since the job execution started.
    - `latestExecutionStatus` (string) **(requerido)**: Indicates the most recent status (STARTING, STARTED, COMPLETED, FAILED) of the job at the time of invocation.
    - `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS.
    - `operationType` (string) **(requerido)**: Indicates operation type that was carried out.
    - `sourceLocationId` (string) **(requerido)**: Unique location identifier for which the job was run.
    - `targetLocationId` (string) **(requerido)**: Unique location identifier for which the numbers have been moved.
    - `counts` (object) **(requerido)**:
      - `totalNumbers` (number) **(requerido)**: Indicates the total number of phone numbers requested to be moved.
      - `numbersDeleted` (number) **(requerido)**: Indicates the total number of phone numbers successfully deleted.
      - `numbersMoved` (number) **(requerido)**: Indicates the total number of phone numbers successfully moved.
      - `numbersFailed` (number) **(requerido)**: Indicates the total number of phone numbers failed.
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
