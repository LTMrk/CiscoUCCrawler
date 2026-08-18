---
doc_id: webex-admin-post-identity-organizations-orgid-jobs-sendactivationemails
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /identity/organizations/{orgId}/jobs/sendActivationEmails
operation_id: Initiate Bulk Activation Email Resend Job
tags: Send Activation Email
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.588881+00:00
---

# POST /identity/organizations/{orgId}/jobs/sendActivationEmails

**API:** Webex Admin
**Área:** Send Activation Email
**operationId:** `Initiate Bulk Activation Email Resend Job`

## Resumen
Initiate Bulk Activation Email Resend Job

## Descripción
Initiate a bulk activation email resend job that sends an activation email to all eligible users in an organization. Only a single instance of the job can be running for an organization.

Requires a full or user administrator auth token with a scope of `spark-admin:people_write`.

## Parámetros
- `orgId` [path] (string) (**requerido**): Initiate job for this organization.

## Ejemplo de invocación
```bash
curl -X POST '/identity/organizations/<orgId>/jobs/sendActivationEmails' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: Accepted
- `name` (string) (**requerido**): Job name.
- `id` (string) (**requerido**): Unique identifier of the job.
- `trackingId` (string) (**requerido**): Unique identifier to track the flow of HTTP requests.
- `sourceUserId` (string) (**requerido**): Unique identifier to identify which user has run the job.
- `sourceCustomerId` (string) (**requerido**): Unique identifier to identify the customer who has run the job.
- `targetCustomerId` (string) (**requerido**): Unique identifier to identify the customer for which the job was run.
- `instanceId` (number) (**requerido**): Unique identifier to identify the instance of the job.
- `jobExecutionStatus` (array): Contains the execution statuses of all the steps involved in the execution of the job.
  - `id` (number) (**requerido**): Unique identifier of the step
  - `startTime` (string): Step execution start time in UTC format.
  - `endTime` (string): Step execution end time in UTC format.
  - `lastUpdated` (string): Last time the step's execution status was updated in UTC format.
  - `statusMessage` (string): * `COMPLETED` - Step or job has completed.  * `STARTING` - Step or job is starting.  * `STARTED` - Step or job is running.  * `STOPPING` - Step or job is stopping.  * `FAILED` - Step or job has failed with an error.  * `ABANDONED` - Step or job has been abandone (manually stopped).  * `UNKNOWN` - Step or job status is unknown. Valores: COMPLETED, STARTING, STARTED, STOPPING, FAILED, ABANDONED, UNKNOWN.
  - `exitCode` (string): * `COMPLETED` - Step or job has completed.  * `STARTING` - Step or job is starting.  * `STARTED` - Step or job is running.  * `STOPPING` - Step or job is stopping.  * `FAILED` - Step or job has failed with an error.  * `ABANDONED` - Step or job has been abandone (manually stopped).  * `UNKNOWN` - Step or job status is unknown. Valores: COMPLETED, STARTING, STARTED, STOPPING, FAILED, ABANDONED, UNKNOWN.
  - `name` (string): Step name.
  - `timeElapsed` (string): Time elapsed since the step execution started.
- `latestExecutionStatus` (string) (**requerido**): * `COMPLETED` - Step or job has completed.  * `STARTING` - Step or job is starting.  * `STARTED` - Step or job is running.  * `STOPPING` - Step or job is stopping.  * `FAILED` - Step or job has failed with an error.  * `ABANDONED` - Step or job has been abandone (manually stopped).  * `UNKNOWN` - Step or job status is unknown. Valores: COMPLETED, STARTING, STARTED, STOPPING, FAILED, ABANDONED, UNKNOWN.
- `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS.
- `counts` (object) (**requerido**):
  - `userResendInviteSent` (number) (**requerido**): Count of users sent an invitation.
  - `userResendInviteFailed` (number) (**requerido**): Count of users who failed to receive an invitation.
  - `userResendInviteSkipped` (number) (**requerido**): Count of users who were skipped.
  - `totalUsers` (number) (**requerido**): Total count of users processed.
- `allowAdminInviteEmails` (boolean): Indicates if the org allows admin invite emails to be sent.

### Ejemplo — respuesta 202
```json
{
  "name": "resendinviteemail",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC9lNzc4NWU3YS1mNmFiLTRjNTEtYWVjOS00YTg5NWQyOTdjMjc",
  "trackingId": "NA_5c8428d1-dbe9-42c3-bb5d-8f0cd98cea07",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iZmI0YjA5MC1mY2VhLTQ4OGEtOTRmMC0wZWMxODk3ZTIwZGE",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xNjcwNjc3NS00NTQzLTRmZDMtODY3Ny0wYmEwMWYyNTRlZjQ",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8yMDIwYTkyMC0zMTRjLTQ3NmUtYmNiMS1hNDJhNGI2YzM2MDM",
  "instanceId": 3,
  "jobExecutionStatus": [
    {
      "id": 3,
      "startTime": "2024-05-16T20:24:24.924Z",
      "lastUpdated": "2024-05-16T20:24:24.924Z",
      "statusMessage": "STARTED",
      "exitCode": "UNKNOWN",
      "createdTime": "2024-05-16T20:24:24.888Z",
      "timeElapsed": "PT0S"
    }
  ],
  "latestExecutionStatus": "STARTED",
  "latestExecutionExitCode": "UNKNOWN",
  "counts": {
    "userResendInviteSent": 0,
    "userResendInviteFailed": 0,
    "userResendInviteSkipped": 0,
    "totalUsers": 0
  },
  "allowAdminInviteEmails": true
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
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs