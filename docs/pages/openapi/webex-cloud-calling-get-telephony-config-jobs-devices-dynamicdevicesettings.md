---
doc_id: webex-cloud-calling-get-telephony-config-jobs-devices-dynamicdevicesettings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/jobs/devices/dynamicDeviceSettings
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.589464+00:00
---

# GET /telephony/config/jobs/devices/dynamicDeviceSettings

**API:** Webex Cloud Calling
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

## Respuestas
- **200**: OK
  - `items` (array) **(requerido)**: Lists all jobs for the customer of type `dynamicdevicesettings` in order of most recent one to oldest one irrespective of its status.
    - `name` (string) **(requerido)**: Name of the job which in this case, is `dynamicdevicesettings`.
    - `id` (string) **(requerido)**: Unique identifier of the job.
    - `trackingId` (string) **(requerido)**: Unique identifier to track the flow of HTTP requests.
    - `sourceUserId` (string) **(requerido)**: Unique identifier of the user who has run the job.
    - `sourceCustomerId` (string) **(requerido)**: Unique identifier of the customer who has run the job.
    - `targetCustomerId` (string) **(requerido)**: Unique identifier of the customer for which the job was run.
    - `instanceId` (number) **(requerido)**: Unique identifier to identify the instance of the job.
    - `jobExecutionStatus` (array) **(requerido)**: Displays the most recent step's execution status. Contains execution statuses of all the steps involved in the execution of the job.
      - `id` (number) **(requerido)**: Unique identifier that identifies each instance of the job.
      - `startTime` (string): The date and time with seconds, the job has started in UTC format.
      - `endTime` (string): The date and time with seconds, the job has ended in UTC format.
      - `lastUpdated` (string) **(requerido)**: The date and time with seconds, the job has last updated in UTC format post one of the step execution completion.
      - `statusMessage` (string) **(requerido)**: Displays status for overall steps that are part of the job.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
      - `exitCode` (string): Exit Code for a job.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
      - `createdTime` (string) **(requerido)**: The date and time with seconds, the job has created in UTC format.
      - `timeElapsed` (string) **(requerido)**: Time lapsed in seconds since the job execution started.
      - `stepExecutionStatuses` (array): Status of each step within a job.
        - `id` (number) **(requerido)**: Unique identifier that identifies each step in a job.
        - `startTime` (string): The date and time with seconds, the step execution has started in UTC format.
        - `endTime` (string): The date and time with seconds, the step execution has ended in UTC format.
        - `lastUpdated` (string) **(requerido)**: The date and time with seconds, the step has last updated in UTC format.
        - `statusMessage` (string) **(requerido)**: Displays status for a step.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
        - `exitCode` (string): Exit Code for a step.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
        - `name` (string) **(requerido)**: Step name.
        - `timeElapsed` (string) **(requerido)**: Time lapsed in seconds since the job execution started.
    - `latestExecutionStatus` (string) **(requerido)**: * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has been completed.  * `FAILED` - Job has failed. Valores: STARTING, STARTED, COMPLETED, FAILED.
    - `latestExecutionExitCode` (string) **(requerido)**: Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS.
    - `target` (string) **(requerido)**: Indicates the target entity. Valores: CUSTOMER, LOCATION.
    - `locationId` (string): Unique identifier of a location.
    - `locationName` (string): Name of the location. Included only when `target` is `LOCATION`.
    - `percentageComplete` (integer) **(requerido)**: Indicates the progress of the job.
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
