---
doc_id: webex-wholesale-get-wholesale-billing-reports
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
method: GET
path: /wholesale/billing/reports
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.730689+00:00
---

# GET /wholesale/billing/reports

**API:** Webex Wholesale
**Área:** Wholesale Billing Reports
**operationId:** `List Wholesale Billing Reports`

## Resumen
List Wholesale Billing Reports

## Descripción
Search for associated wholesale billing reconciliation reports.

## Parámetros
- `billingStartDate` [query] (string): Only include billing reports having this billing `startDate`.
- `billingEndDate` [query] (string): Only include billing reports having this billing `endDate`.
- `type` [query] (string): Only include reports of this type.
- `sortBy` [query] (string): Sort the reports.
- `status` [query] (string): The status of the billing report
- `max` [query] (integer): Limit the maximum number of reports returned in the response, up to 100 per page. Refer to the [Pagination](/docs/basics#pagination) section of [Webex REST API Basics](/docs/api/basics).
- `subPartnerOrgId` [query] (string): The Organization ID of the sub partner on Cisco Webex.

## Respuestas
- **200**: OK
  - `items` (array): An array of report objects.
    - `id` (string): A unique report id that corresponds to a billing report.
    - `billingStartDate` (string): Billing report startDate.
    - `billingEndDate` (string): Billing report endDate.
    - `status` (string): The status of the billing report  * `IN_PROGRESS` - Report generation is in progress.  * `COMPLETED` - Report generation is complete.  * `FAILED` - Report generation failed. Valores: IN_PROGRESS, COMPLETED, FAILED.
    - `type` (string): Billing Report Type. Valores: USER, CUSTOMER, PARTNER.
    - `category` (string): The category of the billing report. Valores: RECONCILIATION, POINT_IN_TIME.
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
