---
doc_id: webex-cloud-calling-get-telephony-config-jobs-numbers-managenumbers-jobid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/numbers/manageNumbers/{jobId}
operation_id: Get Manage Numbers Job Status
tags: Numbers
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.741657+00:00
---

# GET /telephony/config/jobs/numbers/manageNumbers/{jobId}

**API:** Webex Cloud Calling
**Área:** Numbers
**operationId:** `Get Manage Numbers Job Status`

## Resumen
Get Manage Numbers Job Status

## Descripción
Returns the status and other details of the job.

Use this API to monitor a Manage Numbers job after it has been initiated.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `jobId` [path] (string) (**requerido**): Retrieve job details for this `jobId`.
- `orgId` [query] (string): Retrieve job details for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/numbers/manageNumbers/<jobId>' \
  -H 'Authorization: Bearer <TOKEN>'
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
  - `id` (number) (**requerido**): Unique identifier that identifies each instance of the job.
  - `startTime` (string): The date and time with seconds, the job has started in UTC format.
  - `endTime` (string): The date and time with seconds, the job has ended in UTC format.
  - `lastUpdated` (string) (**requerido**): The date and time with seconds, the job has last updated in UTC format post one of the step execution completion.
  - `statusMessage` (string) (**requerido**): Displays status for overall steps that are part of the job.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
  - `exitCode` (string): Exit Code for a job.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
  - `createdTime` (string) (**requerido**): The date and time with seconds, the job has created in UTC format.
  - `timeElapsed` (string) (**requerido**): Time lapsed in seconds since the job execution started.
  - `stepExecutionStatuses` (array): Status of each step within a job.
    - `id` (number) (**requerido**): Unique identifier that identifies each step in a job.
    - `startTime` (string): The date and time with seconds, the step execution has started in UTC format.
    - `endTime` (string): The date and time with seconds, the step execution has ended in UTC format.
    - `lastUpdated` (string) (**requerido**): The date and time with seconds, the step has last updated in UTC format.
    - `statusMessage` (string) (**requerido**): Displays status for a step.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
    - `exitCode` (string): Exit Code for a step.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
    - `name` (string) (**requerido**): Step name.
    - `timeElapsed` (string) (**requerido**): Time lapsed in seconds since the job execution started.
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
  "name": "managenumbers",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC83ZWUyMjAzMS0xM2Q5LTRmYTctODQ0NS1lNDMzNjE3MmVjYmU",
  "jobType": "managenumbers",
  "trackingId": "ATLAS_06a92f81-244d-4fd2-b8db-121bc1eeb6c8_11",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wNTUyZjY3Yi01OWE5LTQxYmItODczNi0xYjA0MWQxZGRkNWU",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85MTE1NDM1Ny1iZWQxLTQ1ZDUtYWE4Zi00ZTUwYzBkZWNmMzM",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85MTE1NDM1Ny1iZWQxLTQ1ZDUtYWE4Zi00ZTUwYzBkZWNmMzM",
  "instanceId": 238972,
  "jobExecutionStatus": [
    {
      "id": 239746,
      "startTime": "2022-08-24T06:18:31.092Z",
      "endTime": "2022-08-24T06:18:38.448Z",
      "lastUpdated": "2022-08-24T06:18:38.825Z",
      "statusMessage": "COMPLETED",
      "exitCode": "COMPLETED",
      "createdTime": "2022-08-24T06:18:31.070Z",
      "stepExecutionStatuses": [
        {
          "id": 1172935,
          "startTime": "2022-08-24T06:18:31.203Z",
          "endTime": "2022-08-24T06:18:32.823Z",
          "lastUpdated": "2022-08-24T06:18:32.823Z",
          "statusMessage": "COMPLETED",
          "exitCode": "COMPLETED",
          "name": "manageNumbersDeciderStep",
          "timeElapsed": "PT1.62S"
        },
        {
          "id": 1172936,
          "startTime": "2022-08-24T06:18:32.839Z",
          "endTime": "2022-08-24T06:18:38.439Z",
          "lastUpdated": "2022-08-24T06:18:38.439Z",
          "statusMessage": "COMPLETED",
         
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