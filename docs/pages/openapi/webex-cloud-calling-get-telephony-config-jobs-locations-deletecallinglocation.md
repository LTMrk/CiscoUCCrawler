---
doc_id: webex-cloud-calling-get-telephony-config-jobs-locations-deletecallinglocation
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/jobs/locations/deleteCallingLocation
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.624622+00:00
---

# GET /telephony/config/jobs/locations/deleteCallingLocation

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Get List Of Disable Calling Location Jobs`

## Resumen
Get a List of Disable Calling Location Jobs

## Descripción
Get a List of Disable Calling Location Jobs for the organization.

Retrieving the list of disable calling location jobs requires a full administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List disable calling location jobs for this organization.
- `max` [query] (integer): Maximum number of jobs to return.
- `start` [query] (integer): Offset to start returning records from.

## Respuestas
- **200**: OK
  - `items` (array): List of disable calling location jobs.
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
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: Internal Server Error: Something went wrong on the server.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
