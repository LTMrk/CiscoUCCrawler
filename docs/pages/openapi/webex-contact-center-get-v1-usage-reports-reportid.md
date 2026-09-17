---
doc_id: webex-contact-center-get-v1-usage-reports-reportid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/usage-reports/{reportId}
operation_id: getReport
tags: Usage Reports
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-17T19:59:29.926727+00:00
---

# GET /v1/usage-reports/{reportId}

**API:** Webex Contact Center
**Área:** Usage Reports
**operationId:** `getReport`

## Resumen
Get usage report details

## Descripción
Retrieves detailed information for a specific usage report.

## Parámetros
- `reportId` [path] (string) (**requerido**): Usage report ID

## Ejemplo de invocación
```bash
curl -X GET '/v1/usage-reports/<reportId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `reportId` (string): Unique report ID (UUID without hyphens). A single usage report may contain multiple report files, especially for long date ranges that are split by calendar month. Use reportId to get or delete the report. Use each report file's fileId to download that file.
- `resourceType` (string): Type of resource this usage report contains.
- `orgId` (string): Organization ID whose data is included in this report file.
- `status` (string): Overall status of the usage report.  This status represents the aggregated state of all report files generated under this report. A report may contain multiple files, each with its own individual status.  Typical rules: - queued：All report files are pending - in progress: At least one report file is still being processed - completed: All report files have completed successfully - failed: All report files failed Valores: queued, in progress, completed, failed.
- `createdTime` (string): Timestamp when the usage report was created, in ISO 8601 format.
- `completedTime` (string): Timestamp when the all usage report files were completed, in ISO 8601 format.
- `expiryTime` (string): Expiration time of the usage report, in ISO 8601 format.  After this timestamp, the entire usage report will be permanently deleted, including all associated report files. Once expired, the report and its files can no longer be queried or downloaded.  The report expiration time is typically 7 days after the report was completed.
- `reportFiles` (array): List of report files generated for this usage report.  Depending on the requested date range, the report may contain one or more report files.  When the requested date range spans more than 30 days, the overall range is automatically split by natural calendar months. Each report file represents one such time slice within the original requested range.  Report files are processed independently and may have different statuses. The overall report status is derived from the statuses of these files.
  - `startDate` (string): Report file start date (inclusive), in yyyy-MM-dd format.
  - `endDate` (string): Report file end date (exclusive), in yyyy-MM-dd format.
  - `status` (string): Current status of this report file.  Each report file represents a specific time range within the overall usage report. File statuses are independent from each other and may differ within the same report.  Possible values: - queued: File generation is pending - in progress: File is currently being generated - completed: File has been generated successfully and is available for download - failed: File generation failed Valores: queued, in progress, completed, failed.
  - `fileId` (string): Unique file ID (UUID without hyphens). Use this ID with the Download Usage Report File API to download this individual generated file.
  - `fileName` (string): Name of the generated CSV file. Format: resourceType_reportId_orgId_startDate_endDate.csv
  - `fileSize` (integer/int64): Size of the generated file in bytes. Available only when the file status is completed.
  - `checksum` (string): MD5 checksum of the generated file for integrity verification. Available only when the file status is completed.
  - `downloadUrl` (string): Customer-facing API Gateway download URL for this individual file. Available only when the file status is completed. The URL contains the fileId, not the reportId, and still requires authorization.

### Ejemplo — respuesta 200
```json
{
  "reportId": "550e8400e29b41d4a716446655440000",
  "resourceType": "ContactSessionRecord",
  "orgId": "1eb65fdf-9643-417f-9974-ad72cae0e10f",
  "status": "completed",
  "createdTime": "2026-01-22T09:31:04Z",
  "completedTime": "2026-01-22T10:15:30Z",
  "expiryTime": "2026-01-29T10:15:30Z",
  "reportFiles": [
    {
      "startDate": "2025-12-23",
      "endDate": "2025-12-31",
      "status": "completed",
      "fileId": "0f49a30b66f9415382ce2251f2ee194d",
      "fileName": "ContactSessionRecord_550e8400e29b41d4a716446655440000_1eb65fdf-9643-417f-9974-ad72cae0e10f_2025-12-23_2025-12-31.csv",
      "fileSize": 102400,
      "checksum": "a1b2c3d4e5f67890",
      "downloadUrl": "https://api.intgus1.ciscoccservice.com/v1/usage-reports/0f49a30b66f9415382ce2251f2ee194d/download"
    },
    {
      "startDate": "2026-01-01",
      "endDate": "2026-01-22",
      "status": "completed",
      "fileId": "782ae11e495b4b6d9c6a9d9a2469e7c4",
      "fileName": "ContactSessionRecord_550e8400e29b41d4a716446655440000_1eb65fdf-9643-417f-9974-ad72cae0e10f_2026-01-01_2026-01-22.csv",
      "fileSize": 204800,
      "checksum": "b1c2d3e4f5a67890",
      "downloadUrl": "https://api.intgus1.ciscoccservice.com/v1/usage-reports/782ae11e495b4b6d9c6a9d9a2469e7c4/download"
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **404**: The URI requested is invalid or the resource requested, such as a report does not exist. Also returned when the requested format is not supported by the requested method.
- **500**: Internal Server Error: Something went wrong on the server
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs