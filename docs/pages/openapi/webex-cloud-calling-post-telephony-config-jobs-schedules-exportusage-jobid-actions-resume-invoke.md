---
doc_id: webex-cloud-calling-post-telephony-config-jobs-schedules-exportusage-jobid-actions-resume-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/jobs/schedules/exportUsage/{jobId}/actions/resume/invoke
operation_id: resumeExportScheduleUsageJob
tags: Export Schedule Usage Jobs
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.655503+00:00
---

# POST /telephony/config/jobs/schedules/exportUsage/{jobId}/actions/resume/invoke

**API:** Webex Cloud Calling
**Área:** Export Schedule Usage Jobs
**operationId:** `resumeExportScheduleUsageJob`

## Resumen
Resume Export Schedule Usage Job

## Descripción
Resumes a paused job that exports the people and services using a business hours or holiday schedule. Use the encoded job ID returned when the export job was created. Resuming requests that the stopped export continue processing.

A schedule can be used by different people and calling services. Schedule usage export creates a CSV report showing which ones use the selected schedule. For an organization-level schedule, the report can include usage across the organization or be limited to one location. For a location-level schedule, it includes usage within that location.

A full administrator token with spark-admin:telephony_config_write is required.

A STOPPED or FAILED job can be restarted. A 202 response means a new execution was submitted; it may not yet be running. Poll Get Job Status.

Lock contention returns 409. The service-wide executing job limit returns 429 with Retry-After: 30. Repeated or racing requests can return 409 or 500 depending on when the state is checked. Active, completed, abandoned or unknown executions, or missing execution history, can currently return 500. Check job status before retrying.

## Parámetros
- `jobId` [path] (string) (**requerido**): Encoded JOB_ID returned when the export job was created.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization, such as partners, may use this parameter because the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/jobs/schedules/exportUsage/<jobId>/actions/resume/invoke' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: Accepted. A new execution was submitted. No response body.

## Respuestas de error
- **401**: Unauthorized. Authentication credentials are missing or invalid.
- **403**: Forbidden. The caller lacks the required administrator role, scope or permission.
- **404**: Not Found. The job does not exist or is unavailable to the target organization.
- **409**: Conflict. The job state changed or the job lock prevents the requested action.
- **429**: Too Many Requests. The service-wide executing job limit has been reached. Wait at least 30 seconds, check the job status, and retry.
- **500**: Internal Server Error. The service could not complete the request.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs