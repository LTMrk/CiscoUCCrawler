---
doc_id: webex-wholesale-get-wholesale-billing-reports-id
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
api_version: 1.0.0
method: GET
path: /wholesale/billing/reports/{id}
operation_id: Get a Wholesale Billing Report
tags: Wholesale Billing Reports
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-27T10:51:20.832124+00:00
---

# GET /wholesale/billing/reports/{id}

**API:** Webex Wholesale
**Área:** Wholesale Billing Reports
**operationId:** `Get a Wholesale Billing Report`

## Resumen
Get a Wholesale Billing Report

## Descripción
Retrieve a specific wholesale billing reconciliation report.

## Parámetros
- `id` [path] (string) (**requerido**): A unique identifier for the report being requested.

## Ejemplo de invocación
```bash
curl -X GET '/wholesale/billing/reports/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string): A unique report ID that corresponds to a billing report.
- `billingStartDate` (string): Billing report `startDate`.
- `billingEndDate` (string): Billing report `endDate`.
- `type` (string): Billing Report Type Valores: USER, CUSTOMER, PARTNER.
- `category` (string): The category of the billing report. Valores: RECONCILIATION, POINT_IN_TIME.
- `created` (string): The date and time the report was generated.
- `createdBy` (string): The person ID of the partner administrator who created the report.
- `status` (string): The status of the billing report.  * `IN_PROGRESS` - Report generation is in progress  * `COMPLETED` - Report generation is complete  * `FAILED` - Report generation failed Valores: IN_PROGRESS, COMPLETED, FAILED.
- `tempDownloadURL` (string): The URL for partners to download the billing report.
- `errors` (array): List of errors that occurred during report generation.  **Note:**  * This list captures errors that occurred during asynchronous or background report generation, after the request has been accepted and a `202 OK` response is returned.
  - `code` (number): An error code that identifies the reason for the error.
  - `description` (string): A textual representation of the error code.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0JJTExJTkdfUkVQT1JULzViOGQ1MThhLThmMDAtNDUxYi1hNDA2LWVhZjQ5YjRhN2ZhOA",
  "billingStartDate": "2021-05-21",
  "billingEndDate": "2021-05-30",
  "type": "PARTNER",
  "created": "2021-06-16T12:40:33.109Z",
  "createdBy": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wYWNkMzg3NS00ZTEyLTRkNzctYjk4MS1lMzg5ZmQ4ODQ2YzA",
  "status": "COMPLETED",
  "tempDownloadURL": "https://billing-reports-int-us-east-1.webexcontent.com/a366de9b-3204-4140-8181-25808d360e36/WHOLESALE/340177d1-7f25-41e1-a39f-ad63ec1103a5.csv?Expires=1624978489&Signature=Syp3vrVeMx4P6MeMtm8e1bQaeAdHFe-c7NeHERWh5-qJGLZ1T8Dvl2ee-M8OsFf~z6Yepz94e2Hh1HDVailD0Uryl8SgiM~jl0cBh7L0PmSe~i9oFA0eJ0MulkqGSMVf7ZHhxY55xYMgIBZIERkWm3CqQNDg5BS4EaXapKfOnmFegf36OokCM63m5uOK8-csk08IkZhwo2Z0l1JMtuWYEaLh4dgMHoe~xgH3YmDSSCWInFYaEifUAfgi2YAYS6nP9Zq4BTliBq62XBaehOE1gBrhy4RdwD-3WSs2oD-BdpoRpuGzo3FZzDLVEvd0S2D6gTcHljOHodQKxe-u0BXPWQ__&Key-Pair-Id=APKAJADAKLCI2FW2U32Q"
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