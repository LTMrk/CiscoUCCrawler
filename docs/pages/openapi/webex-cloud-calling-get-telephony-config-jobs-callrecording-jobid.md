---
doc_id: webex-cloud-calling-get-telephony-config-jobs-callrecording-jobid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/callRecording/{jobId}
operation_id: getTheJobStatusOfACallRecordingJob
tags: Features: Call Recording
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.042930+00:00
---

# GET /telephony/config/jobs/callRecording/{jobId}

**API:** Webex Cloud Calling
**Área:** Features: Call Recording
**operationId:** `getTheJobStatusOfACallRecordingJob`

## Resumen
Get the Job Status of a Call Recording Job

## Descripción
Get the details of a call recording job by its job ID.

The Call Recording feature supports multiple third-party call recording providers, or vendors, to capture and manage call recordings. An organization is configured with an overall provider, but locations can be configured to use a different vendor than the overall organization default.

Requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `jobId` [path] (string) (**requerido**): Retrieve job status for this `jobId`.
- `orgId` [query] (string): Retrieve job status in this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/callRecording/<jobId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `name` (string): Name of the job.
- `id` (string) (**requerido**): Unique identifier of the job.
- `trackingId` (string) (**requerido**): Unique identifier to track the flow of HTTP requests.
- `sourceUserId` (string) (**requerido**): Unique identifier of the user who has run the job.
- `sourceCustomerId` (string) (**requerido**): Unique identifier of the customer who has run the job.
- `targetCustomerId` (string) (**requerido**): Unique identifier of the customer for which the job was run.
- `instanceId` (number) (**requerido**): Unique identifier to identify the instance of the job.
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
- `latestExecutionStatus` (object) (**requerido**): Most recent status of the job at the time of invocation.
- `locationId` (string): Unique identifier of a location.
- `vendorId` (string) (**requerido**): Unique identifier of a vendor.
- `counts` (object) (**requerido**): Job statistics.

### Ejemplo — respuesta 200
```json
{
  "name": "managecallrecordingprovider",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC80ZDA4MDZhYy1hN2M3LTRjM2MtYmVlNy01NDM3MDk4MmYzMWI",
  "trackingId": "ADMINBATCHCLIENT_a02c7b0c-4d28-4e98-b47b-0a135a4b287f_0",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODA2NzZhZC0yNjRlLTRmMWMtYmIwYS1jMWZiNmQ0ODlmZTI",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8zNDEyODExZi0xMWI4LTQ2YTAtYWExNS1lZmEwMjRjODI5ODM",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8zNDEyODExZi0xMWI4LTQ2YTAtYWExNS1lZmEwMjRjODI5ODM",
  "instanceId": 637210,
  "jobExecutionStatus": [
    {
      "id": 660884,
      "startTime": "2024-05-08T13:51:47.275Z",
      "endTime": "2024-05-08T13:51:57.873Z",
      "lastUpdated": "2024-05-08T13:51:57.978Z",
      "statusMessage": "COMPLETED",
      "exitCode": "COMPLETED",
      "createdTime": "2024-05-08T13:51:47.018Z",
      "stepExecutionStatuses": [
        {
          "id": 1909908,
          "startTime": "2024-05-08T13:51:47.550Z",
          "endTime": "2024-05-08T13:51:47.978Z",
          "lastUpdated": "2024-05-08T13:51:47.978Z",
          "statusMessage": "COMPLETED",
          "exitCode": "COMPLETED",
          "name": "managecallrecordingproviderGetUserThatNeedCallRecProviderUpdate",
          "timeElapsed": "PT0.428S"
        },
        {
          "id": 1909909,
          "startTime": "2024-05-08T13:51:47.994Z",
          "endTime": "2024-05-08T13:51:57.866Z",
          "lastUpdated": "2024-05-08T13:51:57.866Z",
          "stat
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