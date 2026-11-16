---
doc_id: webex-cloud-calling-post-telephony-config-jobs-schedules-exportusage
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/jobs/schedules/exportUsage
operation_id: createExportScheduleUsageJob
tags: Export Schedule Usage Jobs
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.654756+00:00
---

# POST /telephony/config/jobs/schedules/exportUsage

**API:** Webex Cloud Calling
**Área:** Export Schedule Usage Jobs
**operationId:** `createExportScheduleUsageJob`

## Resumen
Create Export Schedule Usage Job

## Descripción
Starts an export job for a business hours or holiday schedule and returns the job details. Use the job status API to check its progress and retrieve the CSV download URL when the export is complete.

A schedule can be used by different people and calling services. Schedule usage export creates a CSV report showing which ones use the selected schedule. For an organization-level schedule, the report can include usage across the organization or be limited to one location. For a location-level schedule, it includes usage within that location.

A full administrator token with spark-admin:telephony_config_write is required.

Select exactly one schedule using level, scheduleId and type. For ORGANIZATION, omit locationId or set it to null for no location filter, or supply a nonblank locationId to filter consumers. For LOCATION, a non-null, nonblank locationId is required. Unknown request fields are rejected.

After acceptance, dependency failures are reported through job status and itemized errors; no partial CSV is uploaded. Retrieve a fresh signed download URL through Get Job Status when the file is available.

## Parámetros
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization, such as partners, may use this parameter because the default is the same organization as the token used to access the API.

## Cuerpo de la petición (application/json)
- (uno de:)
  - `level` (string) (**requerido**): Schedule scope.  - `ORGANIZATION`: An organization-level schedule. Usage can include the whole organization or be limited to one location. Valores: ORGANIZATION.
  - `locationId` (string): Encoded LOCATION ID. For ORGANIZATION, omission or null applies no location filter; a supplied non-null value must be nonblank. For LOCATION, this field is required, non-null and nonblank, and identifies the schedule's location.
  - `scheduleId` (string) (**requerido**): Encoded SCHEDULE ID identifying the single schedule whose usage is exported.
  - `type` (string) (**requerido**): Schedule type. Values are case sensitive.  - `businessHours`: A schedule defining normal operating hours. - `holidays`: A schedule defining holiday dates or periods. Valores: businessHours, holidays.
  - `level` (string) (**requerido**): Schedule scope.  - `LOCATION`: A location-level schedule. Usage is limited to the location specified by locationId. Valores: LOCATION.
  - `locationId` (string) (**requerido**): Encoded LOCATION ID. For ORGANIZATION, omission or null applies no location filter; a supplied non-null value must be nonblank. For LOCATION, this field is required, non-null and nonblank, and identifies the schedule's location.
  - `scheduleId` (string) (**requerido**): Encoded SCHEDULE ID identifying the single schedule whose usage is exported.
  - `type` (string) (**requerido**): Schedule type. Values are case sensitive.  - `businessHours`: A schedule defining normal operating hours. - `holidays`: A schedule defining holiday dates or periods. Valores: businessHours, holidays.

### Organization schedule without a location filter — petición
```json
{
  "level": "ORGANIZATION",
  "scheduleId": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFLzMzMzMzMzMzLTMzMzMtNDMzMy04MzMzLTMzMzMzMzMzMzMzMw",
  "type": "businessHours"
}
```

### Organization schedule filtered to one location — petición
```json
{
  "level": "ORGANIZATION",
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzIyMjIyMjIyLTIyMjItNDIyMi04MjIyLTIyMjIyMjIyMjIyMg",
  "scheduleId": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFLzMzMzMzMzMzLTMzMzMtNDMzMy04MzMzLTMzMzMzMzMzMzMzMw",
  "type": "businessHours"
}
```

### Organization schedule with an explicit null location filter — petición
```json
{
  "level": "ORGANIZATION",
  "locationId": null,
  "scheduleId": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFLzMzMzMzMzMzLTMzMzMtNDMzMy04MzMzLTMzMzMzMzMzMzMzMw",
  "type": "holidays"
}
```

### Location-level holiday schedule — petición
```json
{
  "level": "LOCATION",
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzIyMjIyMjIyLTIyMjItNDIyMi04MjIyLTIyMjIyMjIyMjIyMg",
  "scheduleId": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFLzMzMzMzMzMzLTMzMzMtNDMzMy04MzMzLTMzMzMzMzMzMzMzMw",
  "type": "holidays"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/jobs/schedules/exportUsage' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**202**: Accepted. The export job was created. Poll the URL in the Location header.
- (todos de:)
  - `name` (string) (**requerido**): Job type identified by this response.  - `exportscheduleusage`: A job that exports the people and calling services using the selected schedule to a CSV report. Valores: exportscheduleusage.
  - `id` (string) (**requerido**): Encoded JOB_ID returned by Create. Supply this same encoded ID to status, action and errors operations.
  - `trackingId` (string): Support tracking identifier. May be omitted for an UNKNOWN fallback list item.
  - `sourceUserId` (string): Encoded PEOPLE ID of the initiating user. May be omitted for an UNKNOWN fallback list item.
  - `sourceCustomerId` (string): Encoded ORGANIZATION ID of the initiating organization. May be omitted for an UNKNOWN fallback list item.
  - `targetCustomerId` (string): Encoded ORGANIZATION ID owning the job. May be omitted for an UNKNOWN fallback list item.
  - `instanceId` (integer/int64) (**requerido**): Numeric Batch job instance identifier. The UNKNOWN fallback leaves this at 0.
  - `jobExecutionStatus` (array): Execution history and step details when available.
    - `id` (number) (**requerido**): Unique identifier that identifies each instance of the job.
    - `startTime` (string): Job execution start time in UTC format.
    - `endTime` (string): Job execution end time in UTC format.
    - `lastUpdated` (string): Last updated time (in UTC format) post one of the step execution completion.
    - `statusMessage` (string): Displays status for overall steps that are part of the job.
    - `exitCode` (string): Exit Code for a job.
    - `createdTime` (string): Job creation time in UTC format.
    - `stepExecutionStatuses` (array): Status of each step within a job.
      - `id` (number) (**requerido**): Unique identifier that identifies each step in a job.
      - `startTime` (string): Step execution start time in UTC format.
      - `endTime` (string): Step execution end time in UTC format.
      - `lastUpdated` (string): Last updated time for a step in UTC format.
      - `statusMessage` (string): Displays status for a step.
      - `exitCode` (string): Exit Code for a step.
      - `name` (string): Step name.
      - `timeElapsed` (string): Time lapsed since the step execution started.
  - `latestExecutionStatus` (string) (**requerido**): State of the latest job execution.  - `STARTING`: The latest job execution is preparing to run. - `STARTED`: The latest job execution is running. - `STOPPING`: The latest job execution is processing a request to stop. - `STOPPED`: The latest job execution stopped before completion. The job can be resumed. - `COMPLETED`: The latest job execution finished successfully. - `FAILED`: The latest job execution ended with an error. - `ABANDONED`: The latest job execution was abandoned and cannot be restarted. - `UNKNOWN`: The state of the latest job execution could not be determined. In a job list, this can also mean that the full job status could not be retrieved. Valores: STARTING, STARTED, STOPPING, STOPPED, COMPLETED, FAILED, ABANDONED, UNKNOWN.
  - `latestExecutionExitCode` (string): Latest execution result. Common values are UNKNOWN, EXECUTING, COMPLETED, NOOP, FAILED and STOPPED; this is an open string.
  - `csvFile` (string): Generated CSV file reference when available. The file contains Name, Location and Type columns.
  - `csvFileDownloadUrl` (string): Temporary signed CSV download URL when available. The field is omitted or null when no usable URL is available. Get Job Status generates a fresh URL when a file is available. The list operation does not generate one; use Get Job Status to obtain a download URL.

### New organization schedule export — respuesta 202
```json
{
  "name": "exportscheduleusage",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC80NDQ0NDQ0NC00NDQ0LTQ0NDQtODQ0NC00NDQ0NDQ0NDQ0NDQ",
  "trackingId": "EXPORT_USAGE_EXAMPLE_1",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS81NTU1NTU1NS01NTU1LTQ1NTUtODU1NS01NTU1NTU1NTU1NTU",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xMTExMTExMS0xMTExLTQxMTEtODExMS0xMTExMTExMTExMTE",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xMTExMTExMS0xMTExLTQxMTEtODExMS0xMTExMTExMTExMTE",
  "instanceId": 238972,
  "jobExecutionStatus": [],
  "latestExecutionStatus": "STARTING"
}
```
- Cabecera `Location`: URL of the job status resource, containing its encoded JOB_ID. This is not the CSV download URL.

## Respuestas de error
- **400**: Bad Request. Request JSON or parameters are invalid. The request is rejected before a job starts or invalid pagination reaches storage.
- **401**: Unauthorized. Authentication credentials are missing or invalid.
- **403**: Forbidden. The caller lacks the required administrator role, scope or permission.
- **404**: Not Found. The target organization could not be found.
- **429**: Too Many Requests. The service-wide executing job limit has been reached. Wait at least 30 seconds, check the job status, and retry.
- **500**: Internal Server Error. The service could not complete the request.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs