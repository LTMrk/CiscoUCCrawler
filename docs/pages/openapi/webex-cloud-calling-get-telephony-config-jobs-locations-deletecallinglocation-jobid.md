---
doc_id: webex-cloud-calling-get-telephony-config-jobs-locations-deletecallinglocation-jobid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/jobs/locations/deleteCallingLocation/{jobId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.625095+00:00
---

# GET /telephony/config/jobs/locations/deleteCallingLocation/{jobId}

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Get Disable Calling Location Job Status`

## Resumen
Get Disable Calling Location Job Status

## Descripción
Get the status and details of a specific disable calling location job.

Retrieving job status requires a full administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `jobId` [path] (string) **(requerido)**: Unique identifier for the job.
- `orgId` [query] (string): Organization ID for which to retrieve the job status.

## Respuestas
- **200**: OK
  - `name` (string): Name of the job
  - `id` (string): Unique identifier for the job.
  - `locationName` (string): Name of the calling location being disabled.
  - `trackingId` (string): Tracking identifier for the job.
  - `sourceUserId` (string): ID of the user who initiated the job.
  - `sourceCustomerId` (string): Organization ID of the source customer.
  - `targetCustomerId` (string): Organization ID of the target customer.
  - `instanceId` (integer): Instance identifier for the job.
  - `latestExecutionStatus` (string): Latest execution status of the job.
  - `latestExecutionExitCode` (string): Latest execution exit code.
  - `counts` (object): Counts of processed accounts during disable calling location operation.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: Internal Server Error: Something went wrong on the server.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
