---
doc_id: webex-cloud-calling-get-telephony-config-jobs-locations-deletecallinglocation
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/locations/deleteCallingLocation
operation_id: Get List Of Disable Calling Location Jobs
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.337099+00:00
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
- `max` [query] (integer): Maximum number of jobs to return. Por defecto: 20.
- `start` [query] (integer): Offset to start returning records from. Por defecto: 0.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/locations/deleteCallingLocation' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): List of disable calling location jobs.
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
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC80NGNjYzRjMi00YmUxLTRhNjEtOGM5ZC03OTc3YjU4NTM0MWQ",
      "trackingId": "ROUTERGW_c4fc3b45-793e-4744-bb08-ee13032112c7",
      "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kMzg2MjhiYy0zYjk4LTRjMjMtODEwMy0wMzRhMjI0ZmRiNjE",
      "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi84NzU2ZjkwZS1iZDg4LTRhOTQtOGZiZC0wMzM2NzhmMDU5ZjM",
      "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi84NzU2ZjkwZS1iZDg4LTRhOTQtOGZiZC0wMzM2NzhmMDU5ZjM",
      "instanceId": 1488100,
      "jobExecutionStatus": [
        {
          "id": 1512544,
          "startTime": "2025-07-29T13:37:20.098Z",
          "endTime": "2025-07-29T13:37:27.805Z",
          "lastUpdated": "2025-07-29T13:37:33.441Z",
          "statusMessage": "FAILED",
          "exitCode": "FAILED",
          "createdTime": "2025-07-29T13:37:19.995Z",
          "stepExecutionStatuses": [
            {
              "id": 5572963,
              "startTime": "2025-07-29T13:37:25.555Z",
              "endTime": "2025-07-29T13:37:26.283Z",
              "lastUpdated": "2025-07-29T13:37:26.424Z",
              "statusMessage": "COMPLETED",
              "exitCode": "COMPLETED",
              "name": "deletecallinglocationInitializer",
              "timeElapsed": "PT0.727654S"
            },
            {
              "id": 5572964,
              "startTime": "2025-07-29T13:37:26.445Z",
              "endTime": "2025-07-29T13:37:27.603Z",
            
  ... (truncado)
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: Internal Server Error: Something went wrong on the server.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs