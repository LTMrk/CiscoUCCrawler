---
doc_id: webex-cloud-calling-get-partner-reports-reportid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /partner/reports/{reportId}
operation_id: getReportDetails
tags: Partner Reports/Templates
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.353045+00:00
---

# GET /partner/reports/{reportId}

**API:** Webex Cloud Calling
**Área:** Partner Reports/Templates
**operationId:** `getReportDetails`

## Resumen
Get Report Details

## Descripción
Shows details for a report by report ID.

Specify the report ID in the `reportId` parameter in the URI.

To access this endpoint, you must use an administrator token with `spark-admin:reports_read` and `identity:people_read` scopes.

**Notes**:

<div><Callout type="info">Reports are usually provided in zip format. A content-header application/zip or application/octet-stream does indicate the zip format. There is usually no .zip file extension.</Callout></div>

## Parámetros
- `reportId` [path] (string) (**requerido**): The unique identifier for the report.
- `onBehalfOfSubPartnerOrgId` [query] (string): The encoded organization ID for the sub partner.

## Ejemplo de invocación
```bash
curl -X GET '/partner/reports/<reportId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string): Unique identifier for the report.
- `title` (string): Name of the template to which this report belongs.
- `service` (string): The service to which the report belongs.
- `startDate` (string): The data in this report belongs to dates greater than or equal to this.
- `endDate` (string): The data in this report belongs to dates smaller than or equal to this.
- `siteList` (string): The site to which this report belongs to. This only exists if the report belongs to service `Webex`.
- `timeZone` (string): Time zone used for report date and time values. Use an IANA time zone name. The default value is `UTC` when not specified.
- `created` (string): Time of creation for this report.
- `createdBy` (string): The person who created the report.
- `scheduledFrom` (string): Whether this report was scheduled from API or Control Hub.
- `status` (string): Completion status of this report.
- `downloadURL` (string): The link from which the report can be downloaded.

### Ejemplo — respuesta 200
```json
{
  "reportId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9SRVBPUlQvYWQwZDIwNTc1ZGEwNDVhNDhmYWQ0N2Q5NzRhYjQxZjI",
  "templateId": 5,
  "title": "Calling Usage Reports",
  "service": "Teams",
  "startDate": "2024-02-23",
  "endDate": "2024-03-24",
  "regionId": "US",
  "createdTime": "2024-03-24 17:13:39",
  "status": "done",
  "fileName": "Calling Usage_12345_Org_2024-05-01_2024-05-05.csv",
  "fileSize": 0,
  "checksum": "12345",
  "downloadURL": "https://downloadservicebts.webex.com/api?reportId=Y2lzY29zcGFyazovL3VzL1JFUE9SVC9hZDBkMjA1NzVkYTA0NWE0OGZhZDQ3ZDk3NGFiNDFmMg",
  "downloadUrlExpiryTime": "3600"
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs