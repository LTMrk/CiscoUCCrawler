---
doc_id: webex-cloud-calling-get-telephony-config-jobs-devices-dynamicdevicesettings-jobid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/devices/dynamicDeviceSettings/{jobId}
operation_id: getDeviceDynamicSettingsJobStatus
tags: Device Call Settings With Device Dynamic Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.668236+00:00
---

# GET /telephony/config/jobs/devices/dynamicDeviceSettings/{jobId}

**API:** Webex Cloud Calling
**Área:** Device Call Settings With Device Dynamic Settings
**operationId:** `getDeviceDynamicSettingsJobStatus`

## Resumen
Get Device Dynamic Settings Job Status

## Descripción
Get device dynamic settings job status.

Provides details of the job with `jobId` of `jobType` `dynamicdevicesettings`.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `jobId` [path] (string) (**requerido**): Retrieve job details for this `jobId`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/devices/dynamicDeviceSettings/<jobId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `name` (string) (**requerido**): Name of the job which in this case, is `dynamicdevicesettings`.
- `id` (string) (**requerido**): Unique identifier of the job.
- `trackingId` (string) (**requerido**): Unique identifier to track the flow of HTTP requests.
- `sourceUserId` (string) (**requerido**): Unique identifier of the user who has run the job.
- `sourceCustomerId` (string) (**requerido**): Unique identifier of the customer who has run the job.
- `targetCustomerId` (string) (**requerido**): Unique identifier of the customer for which the job was run.
- `instanceId` (number) (**requerido**): Unique identifier to identify the instance of the job.
- `jobExecutionStatus` (array) (**requerido**): Displays the most recent step's execution status. Contains execution statuses of all the steps involved in the execution of the job.
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
- `latestExecutionStatus` (string) (**requerido**): * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has been completed.  * `FAILED` - Job has failed. Valores: STARTING, STARTED, COMPLETED, FAILED.
- `latestExecutionExitCode` (string) (**requerido**): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS.
- `target` (string) (**requerido**): Indicates the target entity. Valores: CUSTOMER, LOCATION.
- `locationId` (string): Unique identifier of a location.
- `locationName` (string): Name of the location. Included only when `target` is `LOCATION`.
- `percentageComplete` (integer) (**requerido**): Indicates the progress of the job.

### Ejemplo — respuesta 200
```json
{
  "name": "dynamicdevicesettings",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC8wMTA4NDJjMy1mNWQ5LTRjOWQtOGZiYi0yYzIxZmU4OWI0YzQ",
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
          "name": "dynamicdevicesettingsUpdate",
          "timeElapsed": "PT11.393S"
        }
      ],
      "timeElapsed": "PT11.393S"
    }
  ],
  "latestExecutionStatus": "COMPLETED",
  "latestExecutionExitCode": "COMPLETED",
  "target": "CUSTOMER",
  "locationId": "",
  "percentageComplete": 100
}
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