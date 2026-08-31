---
doc_id: webex-cloud-calling-get-telephony-config-jobs-updateroutingprefix-jobid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/updateRoutingPrefix/{jobId}
operation_id: Get the job status of Update Routing Prefix job
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.294327+00:00
---

# GET /telephony/config/jobs/updateRoutingPrefix/{jobId}

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Get the job status of Update Routing Prefix job`

## Resumen
Get the job status of Update Routing Prefix job

## Descripción
Get the status of the update routing prefix job by its job ID.

The routing prefix is associated with a location and is used to route calls belonging to that location.
This API allows users to check the status of update routing prefix job by job ID in an organization.

Checking the status of the update routing prefix job in an organization requires a full, user, or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `jobId` [path] (string) (**requerido**): Retrieve job status for this `jobId`.
- `orgId` [query] (string): Check update routing prefix job status in this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/updateRoutingPrefix/<jobId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `name` (string) (**requerido**): Job name.
- `id` (string) (**requerido**): Unique identifier of the job.
- `trackingId` (string) (**requerido**): Unique identifier to track the flow of HTTP requests.
- `sourceUserId` (string) (**requerido**): Unique identifier to identify which user has run the job.
- `sourceCustomerId` (string) (**requerido**): Unique identifier to identify the customer who has run the job.
- `targetCustomerId` (string) (**requerido**): Unique identifier to identify the customer for which the job was run.
- `instanceId` (number) (**requerido**): Unique identifier to identify the instance of the job.
- `jobExecutionStatus` (array): Displays the most recent step's execution status. Contains execution statuses of all the steps involved in the execution of the job.
  - `id` (number) (**requerido**): Unique identifier that identifies each instance of the job.
  - `startTime` (string): Job execution start time in UTC format.
  - `endTime` (string): Job execution end time in UTC format.
  - `lastUpdated` (string): Last updated time (in UTC format) post one of the step execution completion.
  - `statusMessage` (string): Displays status for overall steps that are part of the job.
  - `exitCode` (string): Exit Code for a job.
  - `createdTime` (string): Job creation time in UTC format.
  - `stepExecutionStatuses` (array): Status of each step within a job.
    - `id` (number) (**requerido**): Unique identifier that identifies each step in a job.
    - `startTime` (string): Step execution start time in UTC format.
    - `endTime` (string): Step execution end time in UTC format.
    - `lastUpdated` (string): Last updated time for a step in UTC format.
    - `statusMessage` (string): Displays status for a step.
    - `exitCode` (string): Exit Code for a step.
    - `name` (string): Step name.
    - `timeElapsed` (string): Time lapsed since the step execution started.
- `latestExecutionStatus` (string) (**requerido**): Indicates the most recent status (`STARTING`, `STARTED`, `COMPLETED`, `FAILED`) of the job at the time of invocation.
- `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS.
- `counts` (object) (**requerido**):
  - `routingPrefixUpdated` (number) (**requerido**): Indicates the total number of records whose routing prefix update is successful.
  - `routingPrefixFailed` (number) (**requerido**): Indicates the total number of records whose routing prefix update failed.

### Ejemplo — respuesta 200
```json
{
  "name": "updateroutingprefix",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC81YWE1NWZjNC1lNTYwLTQ3MWQtOGZhZS0yNDc3NDM3MDNkNmI",
  "trackingId": "NA_e82bec92-7a6c-48e5-9511-bfe4da78396e",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85OThhMThhYi1kZjY5LTQ5MWYtYmViZi03MzUxMGE3ODI5N2I",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "instanceId": 1,
  "jobExecutionStatus": [
    {
      "id": 1,
      "startTime": "2023-08-16T18:30:20.901Z",
      "endTime": "2023-08-16T18:30:34.793Z",
      "lastUpdated": "2023-08-16T18:30:36.631Z",
      "statusMessage": "COMPLETED",
      "exitCode": "COMPLETED",
      "createdTime": "2023-08-16T18:30:20.882Z",
      "stepExecutionStatuses": [
        {
          "id": 2,
          "startTime": "2023-08-16T18:30:20.970Z",
          "endTime": "2023-08-16T18:30:22.801Z",
          "lastUpdated": "2023-08-16T18:30:22.801Z",
          "statusMessage": "COMPLETED",
          "exitCode": "COMPLETED",
          "name": "updateroutingprefixPreProcessMemberData",
          "timeElapsed": "PT1.831S"
        },
        {
          "id": 3,
          "startTime": "2023-08-16T18:30:22.811Z",
          "endTime": "2023-08-16T18:30:26.022Z",
          "lastUpdated": "2023-08-16T18:30:26.022Z",
          "statusMessage": "COMPLETED",
          "exitCode": "COMPLETED",
          
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