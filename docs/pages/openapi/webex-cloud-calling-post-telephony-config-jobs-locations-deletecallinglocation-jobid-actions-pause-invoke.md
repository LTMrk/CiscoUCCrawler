---
doc_id: webex-cloud-calling-post-telephony-config-jobs-locations-deletecallinglocation-jobid-actions-pause-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/jobs/locations/deleteCallingLocation/{jobId}/actions/pause/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.624821+00:00
---

# POST /telephony/config/jobs/locations/deleteCallingLocation/{jobId}/actions/pause/invoke

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Pause Disable Calling Location Job`

## Resumen
Pause a Disable Calling Location Job

## Descripción
Pause an in-progress disable calling location job. The job must be in the PROCESSING state to be paused.

Pausing a job requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `jobId` [path] (string) **(requerido)**: Unique identifier for the job to pause.
- `orgId` [query] (string): Organization ID for which to pause the job.

## Respuestas
- **202**: Accepted
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: Internal Server Error: Something went wrong on the server.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
