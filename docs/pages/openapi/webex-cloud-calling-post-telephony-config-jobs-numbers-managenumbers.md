---
doc_id: webex-cloud-calling-post-telephony-config-jobs-numbers-managenumbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/jobs/numbers/manageNumbers
operation_id: Initiate Number Jobs
tags: Numbers
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.528360+00:00
---

# POST /telephony/config/jobs/numbers/manageNumbers

**API:** Webex Cloud Calling
**Área:** Numbers
**operationId:** `Initiate Number Jobs`

## Resumen
Initiate Number Jobs

## Descripción
Starts the execution of an operation on a set of numbers. Supported operations are: `MOVE`, `NUMBER_USAGE_CHANGE`.

Up to 1000 numbers can be given in `MOVE` operation type and `NUMBER_USAGE_CHANGE` operation type per request.
If another move number job request is initiated while a move job is in progress, the API call will receive a `409` HTTP status code.

In order to move a number the following is required:

* The number must be unassigned.

* Both locations must have the same PSTN Connection Type.

* Both locations must have the same PSTN Provider.

* Both locations have to be in the same country.

For example, you can move from Cisco Calling Plan to Cisco Calling Plan, but you cannot move from Cisco Calling Plan to a location with Cloud Connected PSTN.

In order to change the number usage the following is required:

* The number must be unassigned.

* Number Usage Type can be set to `NONE` if carrier has the PSTN service `GEOGRAPHIC_NUMBERS`.

* Number Usage Type can be set to `SERVICE` if carrier has the PSTN service `SERVICE_NUMBERS`.

For example, you can initiate a `NUMBER_USAGE_CHANGE` job to change the number type from Standard number to Service number, or the other way around.

This API requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Initiate a Manage Numbers job for this organization.

## Cuerpo de la petición (application/json)
- `operation` (string) (**requerido**): The kind of operation to be carried out.
- `targetLocationId` (string): Mandatory for a `MOVE` operation. The target location within organization where the unassigned numbers will be moved from the source location.
- `numberUsageType` (string): The number usage type. Mandatory for `NUMBER_USAGE_CHANGE` operation.
- `numberList` (array) (**requerido**): Numbers on which to execute the operation.
  - `locationId` (string) (**requerido**): The source location of the numbers on which to execute the operation.
  - `numbers` (array) (**requerido**): The numbers on which to execute the operation.

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/jobs/numbers/manageNumbers' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"operation": "<operation>", "numberList": []}'
```

## Respuestas correctas
**201**: Created
- `name` (string) (**requerido**): Job name.
- `id` (string) (**requerido**): Unique identifier of the job.
- `jobType` (string) (**requerido**): Job type.
- `trackingId` (string) (**requerido**): Unique identifier to track the flow of HTTP requests.
- `sourceUserId` (string) (**requerido**): Unique identifier to identify which user has run the job.
- `sourceCustomerId` (string) (**requerido**): Unique identifier of the organization that initiated the job.
- `targetCustomerId` (string) (**requerido**): Unique identifier of the organization for which the job was run.
- `instanceId` (integer) (**requerido**): Unique identifier to identify the instance of the job.
- `jobExecutionStatus` (array): Displays the most recent step's execution status. Contains execution statuses of all the steps involved in the execution of the job.
  - `id` (integer) (**requerido**): Unique identifier that identifies each instance of the job.
  - `lastUpdated` (string) (**requerido**): Last updated time (in UTC format) post one of the step execution completion.
  - `statusMessage` (string) (**requerido**): Displays status for overall steps that are part of the job.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
  - `exitCode` (string): Exit Code for a job.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
  - `createdTime` (string) (**requerido**): Job creation time in UTC format.
  - `timeElapsed` (string) (**requerido**): Time lapsed since the job execution started.
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

### Ejemplo — respuesta 201
```json
{
  "name": "managenumbers",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC84M2U1MjNlYy02NjY2LTRlZjAtODcwYi0xZjViZGI1NDNhZDU",
  "jobType": "managenumbers",
  "trackingId": "NA_c989fd47-391e-47c0-8fe4-b45711871a42",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wNTUyZjY3Yi01OWE5LTQxYmItODczNi0xYjA0MWQxZGRkNWU",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85MTE1NDM1Ny1iZWQxLTQ1ZDUtYWE4Zi00ZTUwYzBkZWNmMzM",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85MTE1NDM1Ny1iZWQxLTQ1ZDUtYWE4Zi00ZTUwYzBkZWNmMzM",
  "instanceId": 0,
  "jobExecutionStatus": [
    {
      "id": 0,
      "startTime": "2022-09-13T10:56:41.241Z",
      "lastUpdated": "2022-09-13T10:56:41.242Z",
      "statusMessage": "STARTED",
      "exitCode": "UNKNOWN",
      "createdTime": "2022-09-13T10:56:41.054Z",
      "timeElapsed": "PT0S"
    }
  ],
  "latestExecutionStatus": "STARTED",
  "latestExecutionExitCode": "UNKNOWN",
  "operationType": "MOVE",
  "sourceLocationId": "5223bbed-42c9-454d-a1f3-7fad5cc7e6e3",
  "targetLocationId": "81b53c97-414d-48cc-ae8b-cafc40784007",
  "counts": {
    "totalNumbers": 0,
    "numbersDeleted": 0,
    "numbersMoved": 0,
    "numbersFailed": 0,
    "numbersUsageChanged": 0
  }
}
```

## Respuestas de error
- **400**: Bad Request
  Ejemplo:
```json
{
  "error": {
    "key": "400",
    "message": [
      {
        "description": "Invalid phone number.",
        "code": "BATCH-1017017",
        "location": null
      }
    ]
  },
  "trackingId": "ROUTER_6364F0A9-D48A-01BB-0128-0AFDEB7B0128"
}
```
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