---
doc_id: webex-admin-get-identity-organizations-orgid-jobs-sendactivationemails-jobid-status
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: GET
path: /identity/organizations/{orgId}/jobs/sendActivationEmails/{jobId}/status
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.163015+00:00
---

# GET /identity/organizations/{orgId}/jobs/sendActivationEmails/{jobId}/status

**API:** Webex Admin
**Área:** Send Activation Email
**operationId:** `Get Bulk Activation Email Resend Job Status`

## Resumen
Get Bulk Activation Email Resend Job Status

## Descripción
Get the details of an activation email resend job by its job ID.

Requires a full or user administrator auth token with a scope of `spark-admin:people_write` or read-only administrator auth token with a scope of `spark-admin:people_read`.

## Parámetros
- `orgId` [path] (string) **(requerido)**: Check job status for this organization.
- `jobId` [path] (string) **(requerido)**: Retrieve job status for this `jobId`.

## Respuestas
- **200**: OK
  - `name` (string) **(requerido)**: Job name.
  - `id` (string) **(requerido)**: Unique identifier of the job.
  - `trackingId` (string) **(requerido)**: Unique identifier to track the flow of HTTP requests.
  - `sourceUserId` (string) **(requerido)**: Unique identifier to identify which user has run the job.
  - `sourceCustomerId` (string) **(requerido)**: Unique identifier to identify the customer who has run the job.
  - `targetCustomerId` (string) **(requerido)**: Unique identifier to identify the customer for which the job was run.
  - `instanceId` (number) **(requerido)**: Unique identifier to identify the instance of the job.
  - `jobExecutionStatus` (array): Contains the execution statuses of all the steps involved in the execution of the job.
    - `id` (number) **(requerido)**: Unique identifier of the step
    - `startTime` (string): Step execution start time in UTC format.
    - `endTime` (string): Step execution end time in UTC format.
    - `lastUpdated` (string): Last time the step's execution status was updated in UTC format.
    - `statusMessage` (string): * `COMPLETED` - Step or job has completed.  * `STARTING` - Step or job is starting.  * `STARTED` - Step or job is running.  * `STOPPING` - Step or job is stopping.  * `FAILED` - Step or job has failed with an error.  * `ABANDONED` - Step or job has been abandone (manually stopped).  * `UNKNOWN` - Step or job status is unknown. Valores: COMPLETED, STARTING, STARTED, STOPPING, FAILED, ABANDONED, UNKNOWN.
    - `exitCode` (string): * `COMPLETED` - Step or job has completed.  * `STARTING` - Step or job is starting.  * `STARTED` - Step or job is running.  * `STOPPING` - Step or job is stopping.  * `FAILED` - Step or job has failed with an error.  * `ABANDONED` - Step or job has been abandone (manually stopped).  * `UNKNOWN` - Step or job status is unknown. Valores: COMPLETED, STARTING, STARTED, STOPPING, FAILED, ABANDONED, UNKNOWN.
    - `name` (string): Step name.
    - `timeElapsed` (string): Time elapsed since the step execution started.
  - `latestExecutionStatus` (string) **(requerido)**: * `COMPLETED` - Step or job has completed.  * `STARTING` - Step or job is starting.  * `STARTED` - Step or job is running.  * `STOPPING` - Step or job is stopping.  * `FAILED` - Step or job has failed with an error.  * `ABANDONED` - Step or job has been abandone (manually stopped).  * `UNKNOWN` - Step or job status is unknown. Valores: COMPLETED, STARTING, STARTED, STOPPING, FAILED, ABANDONED, UNKNOWN.
  - `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS.
  - `counts` (object) **(requerido)**:
    - `userResendInviteSent` (number) **(requerido)**: Count of users sent an invitation.
    - `userResendInviteFailed` (number) **(requerido)**: Count of users who failed to receive an invitation.
    - `userResendInviteSkipped` (number) **(requerido)**: Count of users who were skipped.
    - `totalUsers` (number) **(requerido)**: Total count of users processed.
  - `allowAdminInviteEmails` (boolean): Indicates if the org allows admin invite emails to be sent.
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
