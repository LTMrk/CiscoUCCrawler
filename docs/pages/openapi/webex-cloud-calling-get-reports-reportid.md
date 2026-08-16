---
doc_id: webex-cloud-calling-get-reports-reportid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /reports/{reportId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.635983+00:00
---

# GET /reports/{reportId}

**API:** Webex Cloud Calling
**Área:** Reports
**operationId:** `getReportDetails`

## Resumen
Get Report Details

## Descripción
Shows details for a report, by report ID.

Specify the report ID in the `reportId` parameter in the URI.

**Notes**:
CSV reports for Webex suite services are only supported for organizations based in the North American region. Organizations based in a different region will return blank CSV files for any Teams reports.

Reports are usually provided in zip format. A Content-header `application/zip` or `application/octet-stream` does indicate the zip     format. There is usually no .zip file extension.

## Parámetros
- `reportId` [path] (string) **(requerido)**: The unique identifier for the report.

## Respuestas
- **200**: OK
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
