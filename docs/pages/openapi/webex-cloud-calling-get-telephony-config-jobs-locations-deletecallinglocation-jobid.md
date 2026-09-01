---
doc_id: webex-cloud-calling-get-telephony-config-jobs-locations-deletecallinglocation-jobid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/locations/deleteCallingLocation/{jobId}
operation_id: Get Disable Calling Location Job Status
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.728578+00:00
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
- `jobId` [path] (string) (**requerido**): Unique identifier for the job.
- `orgId` [query] (string): Organization ID for which to retrieve the job status.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/locations/deleteCallingLocation/<jobId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
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

### Ejemplo — respuesta 200
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
      "startTime": "2025-07-27T13:19:39.875Z",
      "endTime": "2025-07-27T13:19:51.752Z",
      "lastUpdated": "2025-07-27T13:19:55.413Z",
      "statusMessage": "COMPLETED",
      "exitCode": "COMPLETED",
      "createdTime": "2025-07-27T13:19:39.702Z",
      "stepExecutionStatuses": [
        {
          "id": 5543084,
          "startTime": "2025-07-27T13:19:43.449Z",
          "endTime": "2025-07-27T13:19:44.328Z",
          "lastUpdated": "2025-07-27T13:19:44.523Z",
          "statusMessage": "COMPLETED",
          "exitCode": "COMPLETED",
          "name": "deletecallinglocationInitializer",
          "timeElapsed": "PT0.878554S"
        },
        {
          "id": 5543085,
          "startTime": "2025-07-27T13:19:44.534Z",
          "endTime": "2025-07-27T13:19:46.029Z",
          "lastUpdated": "2025-07-27T13:19:46.212Z",
          "statusMessage": "COMPLETED",
          "exitCo
  ... (truncado)
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: Internal Server Error: Something went wrong on the server.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs