---
doc_id: webex-cloud-calling-post-telephony-config-jobs-locations-deletecallinglocation
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/jobs/locations/deleteCallingLocation
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.624503+00:00
---

# POST /telephony/config/jobs/locations/deleteCallingLocation

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Disable Location For Webex Calling`

## Resumen
Disable a Location for Webex Calling

## Descripción
Disable a Location for Webex Calling.

Initiating a disable calling location job requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

The API returns a jobId that can be used with other job-related APIs to track the status and progress of the disable operation.

## Parámetros
- `orgId` [query] (string): Organization ID for disabling the location for Webex Calling.

## Cuerpo de la petición (application/json)
- `locationId` (string) **(requerido)**: Unique identifier for the calling location to disable.
- `locationName` (string): Name of the calling location to disable.
- `forceDelete` (boolean): Force delete is only applicable when calling features like call queues, hunt groups, virtual lines, etc  or a trunk that is not in use exists in the calling location and customer still wants to disable the calling location.

### Ejemplo de petición
```json
{
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2Y1YjFlMWE3LTQ2MWQtNGUwZC1hYmNiLTQwM2IyMzViNDMzMQ",
  "locationName": "San Jose HQ",
  "forceDelete": true
}
```

## Respuestas
- **202**: Accepted
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
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: Internal Server Error: Something went wrong on the server.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
