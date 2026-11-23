---
doc_id: webex-cloud-calling-get-telephony-config-jobs-schedules-exportusage-jobid-errors
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/jobs/schedules/exportUsage/{jobId}/errors
operation_id: listExportScheduleUsageJobErrors
tags: Export Schedule Usage Jobs
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:15.806942+00:00
---

# GET /telephony/config/jobs/schedules/exportUsage/{jobId}/errors

**API:** Webex Cloud Calling
**Área:** Export Schedule Usage Jobs
**operationId:** `listExportScheduleUsageJobErrors`

## Resumen
List Export Schedule Usage Job Errors

## Descripción
Returns itemized errors reported while exporting schedule usage for an organization. Clients can use these errors to identify schedule records that could not be processed and determine what needs to be corrected.

A schedule can be used by different people and calling services. Schedule usage export creates a CSV report showing which ones use the selected schedule. For an organization-level schedule, the report can include usage across the organization or be limited to one location. For a location-level schedule, it includes usage within that location.

An authorized administrator token with spark-admin:telephony_config_read is required.

Use max to choose the page size. The response always contains an items array; items is empty when no errors were recorded. When a Link header with rel="next" is returned, follow the complete URL unchanged. Its storage continuation values are opaque; do not construct or modify them. Numeric start offsets are not supported by this operation.

## Parámetros
- `jobId` [path] (string) (**requerido**): Encoded JOB_ID returned when the export job was created.
- `orgId` [query] (string): ID of the organization within which the workspace resides. Only admin users of another organization, such as partners, may use this parameter because the default is the same organization as the token used to access the API.
- `max` [query] (integer): Maximum number of records to return. Values outside 1 through 250 return HTTP 400. Por defecto: 50.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/jobs/schedules/exportUsage/<jobId>/errors' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK. Itemized export errors.
- `items` (array) (**requerido**): Recorded errors. An empty array means that no errors were recorded.
  - `itemNumber` (integer) (**requerido**): Record or line number associated with the error. Job-level errors use 0.
  - `item` (string) (**requerido**): Generated identifier of the stored error record.
  - `errorType` (string) (**requerido**): Severity of the recorded issue.  - `ERROR`: An error recorded while processing the export. - `WARN`: A warning recorded while processing the export. Valores: ERROR, WARN. Por defecto: ERROR.
  - `error` (object) (**requerido**): Error key and messages recorded for an export failure.
    - `key` (string) (**requerido**): HTTP-style key associated with the failed operation.
    - `message` (array) (**requerido**): Messages recorded for the error. The array can be empty if stored message details could not be decoded.
      - `description` (string) (**requerido**): Human-readable failure description.
      - `code` (string): Batch error category when available, such as NOT_FOUND, INVALID_JOB_DATA, AUTHORIZATION_FAILURE, DEPENDENT_APPLICATION_ERROR, RESOURCE_UNDER_LOAD or SERVICE_COMMUNICATION_ERROR.
  - `trackingId` (string) (**requerido**): Tracking identifier captured for the failed request.

### Schedule was not found — respuesta 200
```json
{
  "items": [
    {
      "itemNumber": 0,
      "item": "44444444-4444-4444-8444-444444444444_0_66666666-6666-4666-8666-666666666666",
      "errorType": "ERROR",
      "error": {
        "key": "404",
        "message": [
          {
            "description": "The requested schedule was not found for this organization or location.",
            "code": "NOT_FOUND"
          }
        ]
      },
      "trackingId": "EXPORT_USAGE_EXAMPLE_1"
    }
  ]
}
```

### No recorded errors — respuesta 200
```json
{
  "items": []
}
```
- Cabecera `Link`: Next-page URL with rel="next", when more errors are available. Follow the complete URL unchanged; continuation values are opaque.

## Respuestas de error
- **400**: Bad Request. Request JSON or parameters are invalid. The request is rejected before a job starts or invalid pagination reaches storage.
- **401**: Unauthorized. Authentication credentials are missing or invalid.
- **403**: Forbidden. The caller lacks the required administrator role, scope or permission.
- **404**: Not Found. The job does not exist or is unavailable to the target organization.
- **500**: Internal Server Error. The service could not complete the request.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs