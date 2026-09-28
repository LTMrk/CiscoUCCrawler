---
doc_id: webex-wholesale-get-wholesale-billing-reports
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
api_version: 1.0.0
method: GET
path: /wholesale/billing/reports
operation_id: List Wholesale Billing Reports
tags: Wholesale Billing Reports
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-27T10:51:20.831346+00:00
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
- `type` [query] (string): Only include reports of this type. Valores: PARTNER, CUSTOMER, USER.
- `sortBy` [query] (string): Sort the reports. Valores: id, billingStartDate, billingEndDate, status. Por defecto: billingStartDate.
- `status` [query] (string): The status of the billing report Valores: IN_PROGRESS, COMPLETED, FAILED.
- `max` [query] (integer): Limit the maximum number of reports returned in the response, up to 100 per page. Refer to the [Pagination](/docs/basics#pagination) section of [Webex REST API Basics](/docs/api/basics). Por defecto: 100.
- `subPartnerOrgId` [query] (string): The Organization ID of the sub partner on Cisco Webex.

## Ejemplo de invocación
```bash
curl -X GET '/wholesale/billing/reports' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of report objects.
  - `id` (string): A unique report id that corresponds to a billing report.
  - `billingStartDate` (string): Billing report startDate.
  - `billingEndDate` (string): Billing report endDate.
  - `status` (string): The status of the billing report  * `IN_PROGRESS` - Report generation is in progress.  * `COMPLETED` - Report generation is complete.  * `FAILED` - Report generation failed. Valores: IN_PROGRESS, COMPLETED, FAILED.
  - `type` (string): Billing Report Type. Valores: USER, CUSTOMER, PARTNER.
  - `category` (string): The category of the billing report. Valores: RECONCILIATION, POINT_IN_TIME. Por defecto: RECONCILIATION.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0JJTExJTkdfUkVQT1JULzViOGQ1MThhLThmMDAtNDUxYi1hNDA2LWVhZjQ5YjRhN2ZhOA",
      "billingStartDate": "2021-05-21",
      "billingEndDate": "2021-05-30",
      "status": "COMPLETED",
      "type": "PARTNER"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0JJTExJTkdfUkVQT1JULzViOGQ1MThhLThmMDAtNDUxYi1hNDA2LWVhZjQ5YjRhN2Zh2B",
      "billingStartDate": "2021-05-21",
      "billingEndDate": "2021-05-30",
      "status": "COMPLETED",
      "type": "PARTNER"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0JJTExJTkdfUkVQT1JULzViOGQ1MThhLThmMDAtNDUxYi1hNDA2LWVhZjQ5YjRhN2Zh5D",
      "billingStartDate": "2021-05-21",
      "billingEndDate": "2021-05-30",
      "status": "COMPLETED",
      "type": "PARTNER"
    }
  ]
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
The Webex Wholesale APIs are designed for service providers to manage wholesale Webex offerings, including customer onboarding, provisioning, billing, reporting, and lifecycle management. These APIs enable automation and integration with provider systems to deliver scalable, multi-tenant collaboration solutions. Use cases include automated partner onboarding, real-time usage reporting, integration with billing platforms, and management of customer entitlements across large portfolios.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs