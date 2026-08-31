---
doc_id: webex-cloud-calling-get-telephony-config-jobs-person-movelocation-jobid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/person/moveLocation/{jobId}
operation_id: getMoveUsersJobStatus
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.333337+00:00
---

# GET /telephony/config/jobs/person/moveLocation/{jobId}

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getMoveUsersJobStatus`

## Resumen
Get Move Users Job Status

## Descripción
Returns the status and other details of the job.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `jobId` [path] (string) (**requerido**): Retrieve job details for this `jobId`.
- `orgId` [query] (string): Retrieve job details for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/person/moveLocation/<jobId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `name` (string) (**requerido**): Job name.
- `id` (string) (**requerido**): Unique identifier of the job.
- `trackingId` (string): d060-4164-9757-48b383423d73` (string, required) - Unique identifier to track the flow of HTTP requests.
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
- `latestExecutionStatus` (string) (**requerido**): Most recent status of the job at the time of invocation.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
- `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
- `counts` (object) (**requerido**):
  - `totalMoves` (number) (**requerido**): Total number of user moves requested.
  - `moved` (number) (**requerido**): Total number of user moves completed successfully.
  - `failed` (number) (**requerido**): Total number of user moves that were completed with failures.
  - `pending` (number) (**requerido**): Total number of user moves that were pending with number orders.
  - `skipped` (number) (**requerido**): Total number of user moves that were skipped.
- `csvFile` (string): Reference ID for the file that holds the errors and impacts.
- `csvFileExpiryTime` (string): Date and time with seconds, the file expires in UTC format.
- `fileFormat` (string): Format of the file generated.
- `csvFileDownloadUrl` (string): URL to the CSV file containing errors and impacts.

### Ejemplo — respuesta 200
```json
{
  "name": "moveusers",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC8xMzFkOTg1ZC1iZThhLTQ3MjgtYjM2MC02MzBjNTAxNTEyNzE",
  "trackingId": "ROUTER_6475F43E-A25A-01BB-76CC-AC108AF376CC",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85YzJhMDUxMC0wOTUwLTQ1MmYtODFmZi05YTVkMjM2OTJkZTY",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8wMjEyNGVlZi04YWY3LTQ4OWMtODA1Yi0zNjNjYzY0MDE4OTM",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8wMjEyNGVlZi04YWY3LTQ4OWMtODA1Yi0zNjNjYzY0MDE4OTM",
  "instanceId": 328660,
  "jobExecutionStatus": [
    {
      "id": 332387,
      "startTime": "2023-05-30T13:04:00.469Z",
      "endTime": "2023-05-30T13:04:03.252Z",
      "lastUpdated": "2023-05-30T13:04:03.574Z",
      "statusMessage": "COMPLETED",
      "exitCode": "COMPLETED",
      "createdTime": "2023-05-30T13:04:00.457Z",
      "stepExecutionStatuses": [
        {
          "id": 1549115,
          "startTime": "2023-05-30T13:04:00.493Z",
          "endTime": "2023-05-30T13:04:03.245Z",
          "lastUpdated": "2023-05-30T13:04:03.246Z",
          "statusMessage": "COMPLETED",
          "exitCode": "COMPLETED",
          "name": "moveusersvalidateAndMove",
          "timeElapsed": "PT2.752S"
        }
      ],
      "timeElapsed": "PT2.752S"
    }
  ],
  "latestExecutionStatus": "COMPLETED",
  "latestExecutionExitCode": "COMPLETED",
  "counts": {
    "totalMoves": 1,
    "moved": 1,
    "failed": 0,
    "pending": 0,
    "skipped": 0
  },
  "csvFile": "02124eef-7be6-489
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