---
doc_id: webex-cloud-calling-post-reports
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /reports
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.635889+00:00
---

# POST /reports

**API:** Webex Cloud Calling
**Área:** Reports
**operationId:** `createaReport`

## Resumen
Create a Report

## Descripción
Create a new report. For each `templateId`, there are a set of validation rules that need to be followed. For example, for templates belonging to Webex, the user needs to provide `siteUrl`. These validation rules can be retrieved via the [Report Templates API](/docs/api/v1/report-templates).

The 'templateId' parameter is a number. However, it is a limitation of developer.webex.com platform that it is passed as a string when you try to test the API from here.

CSV reports for Webex suite services are only supported for organizations based in the North American region. Organizations based in a different region will return blank CSV files for any Teams reports.

## Cuerpo de la petición (application/json)
- `templateId` (number) **(requerido)**: Unique ID representing valid report templates.
- `startDate` (string): Data in the report will be from this date onwards.
- `endDate` (string): Data in the report will be until this date.
- `siteList` (string): Sites belonging to user's organization. This attribute is needed for site-based templates.
- `timeZone` (string): Time zone used for report date and time values. Use an IANA time zone name. This field is optional.

## Respuestas
- **200**: OK
  - `id` (string): The unique identifier for the report.
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
