---
doc_id: webex-cloud-calling-get-partner-reports
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /partner/reports
operation_id: listReports
tags: Partner Reports/Templates
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.352659+00:00
---

# GET /partner/reports

**API:** Webex Cloud Calling
**Área:** Partner Reports/Templates
**operationId:** `listReports`

## Resumen
List Reports

## Descripción
Lists all reports previously generated from a given region. Use query parameters to filter the response. The parameters are optional.

To access this endpoint, you must use an administrator token with `spark-admin:reports_read` and `identity:people_read` scopes.

<div><Callout type="info">CSV reports for Webex suite services are only supported for organizations based in one region per API request. Organizations based in a different region will require a separate request with region specified.</Callout></div>

<div><Callout type="info">When no region is specified, the request defaults to Partner organization's home region.</Callout></div>

<div><Callout type="info">Reports are usually provided in zip format. A content-header application/zip or application/octet-stream does indicate the zip format. There is usually no .zip file extension.</Callout></div>

## Parámetros
- `service` [query] (string): List reports which use this service.
- `templateId` [query] (number): List reports with this report template ID.
- `from` [query] (string): List reports that were created on or after this date.
- `to` [query] (string): List reports that were created before this date.
- `regionId` [query] (string): Data in the report will be from organizations in this region, for example, US, CA, or EU.
- `onBehalfOfSubPartnerOrgId` [query] (string): The encoded organization ID for the sub partner.

## Ejemplo de invocación
```bash
curl -X GET '/partner/reports' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `Report Attributes` (array): An array of report objects.
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