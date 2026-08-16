---
doc_id: webex-wholesale-post-wholesale-billing-reports
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
method: POST
path: /wholesale/billing/reports
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.730913+00:00
---

# POST /wholesale/billing/reports

**API:** Webex Wholesale
**Área:** Wholesale Billing Reports
**operationId:** `Create a Wholesale Billing Report`

## Resumen
Create a Wholesale Billing Report

## Descripción
Generate a wholesale billing reconciliation report.

## Cuerpo de la petición (application/json)
- `billingStartDate` (string) **(requerido)**: The `startDate` (`YYYY-MM-DD`) for which the partner requests the billing report.
- `billingEndDate` (string) **(requerido)**: The `endDate` (`YYYY-MM-DD`) for which the partner requests the billing report.
- `type` (string): Create report of the given type, `PARTNER`, `CUSTOMER`, or `USER`. Default: `PARTNER`.
- `subPartnerOrgId` (string): The Organization ID of the sub partner on Cisco Webex.
- `internal` (boolean): If true or selected, internal orgs will be included in the billing report. Default: false.

### Ejemplo de petición
```json
{
  "billingStartDate": "2020-05-21",
  "billingEndDate": "2020-05-30",
  "type": "PARTNER",
  "subPartnerOrgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi81MmNmNTc2ZC02MGE4LTQwN2EtYjIyYy00NjdjNTE1OTE5MDg"
}
```

## Respuestas
- **200**: OK
  - `id` (string): A unique report ID that corresponds to a billing report.
  - `billingStartDate` (string): Billing report startDate.
  - `billingEndDate` (string): Billing report endDate.
  - `type` (string): Billing Report Type Valores: USER, CUSTOMER, PARTNER.
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
