---
doc_id: webex-cloud-calling-post-telephony-config-jobs-locations-deletecallinglocation
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/jobs/locations/deleteCallingLocation
operation_id: Disable Location For Webex Calling
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.117891+00:00
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
- `locationId` (string) (**requerido**): Unique identifier for the calling location to disable.
- `locationName` (string): Name of the calling location to disable.
- `forceDelete` (boolean): Force delete is only applicable when calling features like call queues, hunt groups, virtual lines, etc  or a trunk that is not in use exists in the calling location and customer still wants to disable the calling location.

### Ejemplo — petición
```json
{
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2Y1YjFlMWE3LTQ2MWQtNGUwZC1hYmNiLTQwM2IyMzViNDMzMQ",
  "locationName": "San Jose HQ",
  "forceDelete": true
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/jobs/locations/deleteCallingLocation' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"locationId": "<locationId>"}'
```

## Respuestas correctas
**202**: Accepted
- `name` (string): Name of the job
- `id` (string): Unique identifier for the job.
- `locationName` (string): Name of the calling location being disabled.
- `trackingId` (string): Tracking identifier for the job.
- `sourceUserId` (string): ID of the user who initiated the job.
- `sourceCustomerId` (string): Organization ID of the source customer.
- `targetCustomerId` (string): Organization ID of the target customer.
- `instanceId` (integer/int64): Instance identifier for the job.
- `latestExecutionStatus` (string): Latest execution status of the job.
- `latestExecutionExitCode` (string): Latest execution exit code.
- `counts` (object): Counts of processed accounts during disable calling location operation.

### Ejemplo — respuesta 202
```json
{
  "name": "deletecallinglocation",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC8zZjczYTAyOS1lYWZkLTQ5NzUtYjcyYi1jNzlkYWE1ZTkyZmE",
  "trackingId": "ROUTERGW_882b1b3b-b247-4d4f-abe9-4ccec7f7e3b0",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kMzg2MjhiYy0zYjk4LTRjMjMtODEwMy0wMzRhMjI0ZmRiNjE",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi84NzU2ZjkwZS1iZDg4LTRhOTQtOGZiZC0wMzM2NzhmMDU5ZjM",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi84NzU2ZjkwZS1iZDg4LTRhOTQtOGZiZC0wMzM2NzhmMDU5ZjM",
  "instanceId": 1472955,
  "jobExecutionStatus": [
    {
      "id": 1497186,
      "lastUpdated": "2025-07-27T13:19:39.702Z",
      "statusMessage": "STARTING",
      "exitCode": "UNKNOWN",
      "createdTime": "2025-07-27T13:19:39.702Z",
      "timeElapsed": "PT0S"
    }
  ],
  "latestExecutionStatus": "STARTING",
  "latestExecutionExitCode": "UNKNOWN",
  "locationName": "San Jose HQ"
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: Internal Server Error: Something went wrong on the server.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs