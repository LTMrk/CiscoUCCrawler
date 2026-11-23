---
doc_id: webex-cloud-calling-get-telephony-config-jobs-schedules-exportusage-jobid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/schedules/exportUsage/{jobId}
operation_id: getExportScheduleUsageJobStatus
tags: Export Schedule Usage Jobs
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:15.805728+00:00
---

# GET /telephony/config/jobs/schedules/exportUsage/{jobId}

**API:** Webex Cloud Calling
**Área:** Export Schedule Usage Jobs
**operationId:** `getExportScheduleUsageJobStatus`

## Resumen
Get Export Schedule Usage Job Status

## Descripción
Gets the current status of a job that exports the people and services using a business hours or holiday schedule. Use the encoded job ID returned when the export job was created. When the export is complete and the CSV is available, the response includes a signed URL to download it.

A schedule can be used by different people and calling services. Schedule usage export creates a CSV report showing which ones use the selected schedule. For an organization-level schedule, the report can include usage across the organization or be limited to one location. For a location-level schedule, it includes usage within that location.

An authorized administrator token with spark-admin:telephony_config_read is required.

The Location response header identifies this job status resource. Query parameters are not included in that header. csvFileDownloadUrl is temporary; request status again to obtain a fresh URL when the CSV is available.

## Parámetros
- `jobId` [path] (string) (**requerido**): Encoded JOB_ID returned when the export job was created.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization, such as partners, may use this parameter because the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/schedules/exportUsage/<jobId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK. Current job status and a fresh download URL when the CSV is available.
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

### Completed export with execution history and CSV — respuesta 200
```json
{
  "name": "exportscheduleusage",
  "id": "Y2lzY29zcGFyazovL3VzL0pPQl9JRC80NDQ0NDQ0NC00NDQ0LTQ0NDQtODQ0NC00NDQ0NDQ0NDQ0NDQ",
  "trackingId": "EXPORT_USAGE_EXAMPLE_1",
  "sourceUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS81NTU1NTU1NS01NTU1LTQ1NTUtODU1NS01NTU1NTU1NTU1NTU",
  "sourceCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xMTExMTExMS0xMTExLTQxMTEtODExMS0xMTExMTExMTExMTE",
  "targetCustomerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xMTExMTExMS0xMTExLTQxMTEtODExMS0xMTExMTExMTExMTE",
  "instanceId": 238972,
  "jobExecutionStatus": [
    {
      "id": 436272,
      "createdTime": "2026-10-14T12:00:00.000Z",
      "startTime": "2026-10-14T12:00:01.000Z",
      "endTime": "2026-10-14T12:00:05.000Z",
      "lastUpdated": "2026-10-14T12:00:05.000Z",
      "timeElapsed": "PT4S",
      "statusMessage": "COMPLETED",
      "exitCode": "COMPLETED",
      "stepExecutionStatuses": [
        {
          "id": 436273,
          "name": "exportScheduleUsageStep",
          "startTime": "2026-10-14T12:00:01.000Z",
          "endTime": "2026-10-14T12:00:05.000Z",
          "lastUpdated": "2026-10-14T12:00:05.000Z",
          "timeElapsed": "PT4S",
          "statusMessage": "COMPLETED",
          "exitCode": "COMPLETED"
        }
      ]
    }
  ],
  "latestExecutionStatus": "COMPLETED",
  "latestExecutionExitCode": "COMPLETED",
  "csvFile": "schedule-usage.csv",
  "csvFileDownloadUrl": "https://example.com/schedule-usage.csv?signature=example"
}
```
- Cabecera `Location`: URL of the job status resource, containing its encoded JOB_ID. This is not the CSV download URL.

## Respuestas de error
- **401**: Unauthorized. Authentication credentials are missing or invalid.
- **403**: Forbidden. The caller lacks the required administrator role, scope or permission.
- **404**: Not Found. The job does not exist or is unavailable to the target organization.
- **500**: Internal Server Error. The service could not complete the request.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs