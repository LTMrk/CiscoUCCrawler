---
doc_id: webex-cloud-calling-post-telephony-config-jobs-schedules-exportusage-jobid-actions-pause-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/jobs/schedules/exportUsage/{jobId}/actions/pause/invoke
operation_id: pauseExportScheduleUsageJob
tags: Export Schedule Usage Jobs
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:15.806019+00:00
---

# POST /telephony/config/jobs/schedules/exportUsage/{jobId}/actions/pause/invoke

**API:** Webex Cloud Calling
**Área:** Export Schedule Usage Jobs
**operationId:** `pauseExportScheduleUsageJob`

## Resumen
Pause Export Schedule Usage Job

## Descripción
Pauses a job that exports the people and services using a business hours or holiday schedule. Use the encoded job ID returned when the export job was created. The request asks the job to stop processing so that it can be resumed later. Check the job status to confirm that it has stopped.

A schedule can be used by different people and calling services. Schedule usage export creates a CSV report showing which ones use the selected schedule. For an organization-level schedule, the report can include usage across the organization or be limited to one location. For a location-level schedule, it includes usage within that location.

A full administrator token with spark-admin:telephony_config_write is required.

For STARTING or STARTED, the job normally moves through STOPPING to STOPPED. Repeating a pause for STOPPING or STOPPED is accepted. For COMPLETED, FAILED, ABANDONED or UNKNOWN, the request is accepted without changing the state. Racing state changes can return 409.

A 202 response does not guarantee that distributed processing has already stopped. Poll Get Job Status.

## Parámetros
- `jobId` [path] (string) (**requerido**): Encoded JOB_ID returned when the export job was created.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization, such as partners, may use this parameter because the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/jobs/schedules/exportUsage/<jobId>/actions/pause/invoke' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: Accepted. The pause request was accepted. No response body.

## Respuestas de error
- **401**: Unauthorized. Authentication credentials are missing or invalid.
- **403**: Forbidden. The caller lacks the required administrator role, scope or permission.
- **404**: Not Found. The job does not exist or is unavailable to the target organization.
- **409**: Conflict. The job state changed or the job lock prevents the requested action.
- **500**: Internal Server Error. The service could not complete the request.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs