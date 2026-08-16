---
doc_id: webex-broadworks-get-broadworks-billing-reports
source: webex-openapi-specs/public-spec/webex-broadworks.json
api: Webex Broadworks Calling
method: GET
path: /broadworks/billing/reports
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.283905+00:00
---

# GET /broadworks/billing/reports

**API:** Webex Broadworks Calling
**Área:** BroadWorks Billing Reports
**operationId:** `List BroadWorks Billing Reports`

## Resumen
List BroadWorks Billing Reports

## Descripción
Search for reports. There are a number of filter options which can be combined in a single request.

## Parámetros
- `before` [query] (string): Only include billing reports created before this date.
- `after` [query] (string): Only include billing reports created after this date.
- `sortBy` [query] (string): Sort the reports.  + Members:     + id     + status     + billingPeriod

## Respuestas
- **200**: OK
  - `items` (array): An array of reports objects.
    - `id` (string): A unique report ID that corresponds to a billing report.
    - `billingPeriod` (string): The year and month (`YYYY-MM`) for which the billing report was generated.
    - `status` (string): The status of the billing report.  * `IN_PROGRESS` - Report generation is in progress.  * `COMPLETED` - Report generation is complete.  * `FAILED` - Report generation failed. Valores: IN_PROGRESS, COMPLETED, FAILED.
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
