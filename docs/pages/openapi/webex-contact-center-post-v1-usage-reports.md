---
doc_id: webex-contact-center-post-v1-usage-reports
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/usage-reports
operation_id: createReport
tags: Usage Reports
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-02T12:35:57.593283+00:00
---

# POST /v1/usage-reports

**API:** Webex Contact Center
**Área:** Usage Reports
**operationId:** `createReport`

## Resumen
Create usage report

## Descripción
Creates a new usage report for the specified organization, resource type,
and date range. The report is generated asynchronously in the background.

A single **usage report (reportId)** is always created for each request.
Depending on the requested date range, the report may contain **one or more
report files**, each representing a sub-range of the overall time period.

When the requested date range spans **more than 30 days**, the overall range
is **automatically split by natural calendar months**, and **multiple report
files** are generated under the same report.

**Examples:**

- Requested range: **`2025-12-23`** ~ **`2026-03-20`**
  - Generated result:
    - Report ID: single report
    - Report files:
      - **`2025-12-23`** ~ **`2025-12-31`**
      - **`2026-01-01`** ~ **`2026-01-31`**
      - **`2026-02-01`** ~ **`2026-02-28`**
      - **`2026-03-01`** ~ **`2026-03-20`**
- Requested range: **`2025-12-23`** ~ **`2026-01-21`**
  - Generated result:
    - Report ID: single report
    - Report files:
      - **`2025-12-23`** ~ **`2026-01-21`**

**Concurrent file-generation limit:**

- The concurrency check is calculated by **report file**, not by usage report or `reportId`.
- Each item in `reportFiles[]` requires a separate file-generation task and counts as one
  active task while it is `queued` or `in progress`. Tasks in terminal states no longer
  count toward the limit.
- At request time, the service counts all active report-file generation tasks for the same
  organization across all reports. A report with four active files and another report with
  three active files count as **7 active tasks**, not 2 reports.
- The service checks the existing active task count **before creating the new report**.
  If this count is below 10, the request passes this concurrency check even when the new
  report creates enough files to bring the total above 10. The new report's files are
  not added to the count used for this check.

**Example:**

- Requested range: **`2025-01-01`** ~ **`2025-12-31`**
  - Existing active file-generation tasks: **0**
  - Generated result:
    - Request: **accepted**
    - Report ID: single report
    - Report files: **12 monthly report files**, one per calendar month
    - File-generation tasks created: **12**
    - Active tasks after creation: **12**, exceeding the threshold of 10
  - Subsequent report creation requests:
    - Existing active tasks **10 or more**: rejected with **HTTP 429**
    - Existing active tasks **below 10**: allowed by the concurrency check

## Cuerpo de la petición (application/json)
- `resourceType` (string): Type of resource this report contains.
- `startDate` (string): Report start date (inclusive), in yyyy-MM-dd format.
- `endDate` (string): Report end date (exclusive), in yyyy-MM-dd format.

### Ejemplo — petición
```json
{
  "resourceType": "ContactSessionRecord",
  "startDate": "2025-01-01",
  "endDate": "2025-01-31"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/v1/usage-reports' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- (array de:)
  - `reportId` (string): Unique report ID (UUID without hyphens). Use this ID to get the report status and generated file list. Do not use reportId to download files; use each file's fileId instead.
  - `createdTime` (string): Report creation timestamp in ISO 8601 format.

### Ejemplo — respuesta 200
```json
[
  {
    "reportId": "550e8400e29b41d4a716446655440000",
    "createdTime": "2026-02-01T09:31:04Z"
  }
]
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **429**: Too Many Requests: The organization already has 10 or more active report-file generation tasks before this request. The limit is calculated from report files whose generation tasks are queued or in progress, not from the number of reports or reportIds. If the existing count is below 10, the request passes this concurrency check even if its new files bring the total above 10.
- **500**: Internal Server Error: Something went wrong on the server
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs