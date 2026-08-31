---
doc_id: webex-cloud-calling-get-telephony-config-jobs-devices-applylinekeytemplate
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/devices/applyLineKeyTemplate
operation_id: getListOfApplyLineKeyTemplatesJobs
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.188032+00:00
---

# GET /telephony/config/jobs/devices/applyLineKeyTemplate

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `getListOfApplyLineKeyTemplatesJobs`

## Resumen
Get List of Apply Line Key Template jobs

## Descripción
Get the list of all apply line key templates jobs in an organization.

Line Keys also known as Programmable Line Keys (PLK) are the keys found on either sides of a typical desk phone display.
A Line Key Template is a definition of actions that will be performed by each of the Line Keys for a particular device model.
This API allows users to retrieve all the apply line key templates jobs in an organization.

Retrieving the list of apply line key templates jobs in an organization requires a full, user or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Retrieve list of line key templates jobs in this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/devices/applyLineKeyTemplate' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array) (**requerido**): List of Apply Line Key Template jobs.
  - `name` (string) (**requerido**): Job name.
  - `id` (string) (**requerido**): Unique identifier of the job.
  - `trackingId` (string) (**requerido**): Unique identifier to track the flow of HTTP requests.
  - `sourceUserId` (string) (**requerido**): Unique identifier to identify which user has run the job.
  - `sourceCustomerId` (string) (**requerido**): Unique identifier to identify the customer who has run the job.
  - `targetCustomerId` (string) (**requerido**): Unique identifier to identify the customer for which the job was run.
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
  - `latestExecutionStatus` (string) (**requerido**): Indicates the most recent status (`STARTING`, `STARTED`, `COMPLETED`, `FAILED`) of the job at the time of invocation.
  - `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS.
  - `percentageComplete` (integer) (**requerido**): Indicates the progress of the job.
  - `updatedCount` (integer) (**requerido**): Number of job steps completed.
  - `advisoryCount` (integer) (**requerido**): Number of job steps completed with advisories.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
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
              "name": "applyphonelinekeytemplatesProcess",
              "timeElapsed": "PT11.476S"
            }
          ],
          "timeElapsed": "PT11.476S"
        }
      ],
      "latestExecutionStatus": "COMPLETED",
      "latestExecutionExitCode": "COMPLETED",
      "percentageComplet
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