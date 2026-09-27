---
doc_id: webex-broadworks-get-broadworks-billing-reports-id
source: webex-openapi-specs/public-spec/webex-broadworks.json
api: Webex Broadworks Calling
api_version: 1.0.0
method: GET
path: /broadworks/billing/reports/{id}
operation_id: Get a BroadWorks Billing Report
tags: BroadWorks Billing Reports
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-27T10:51:18.910502+00:00
---

# GET /broadworks/billing/reports/{id}

**API:** Webex Broadworks Calling
**Área:** BroadWorks Billing Reports
**operationId:** `Get a BroadWorks Billing Report`

## Resumen
Get a BroadWorks Billing Report

## Descripción
Retrieve a specific billing reconciliation report.

## Parámetros
- `id` [path] (string) (**requerido**): A unique identifier for the report in request.

## Ejemplo de invocación
```bash
curl -X GET '/broadworks/billing/reports/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string): A unique report ID that corresponds to a billing report.
- `billingPeriod` (string): The year and month (`YYYY-MM`) for which the billing report was generated.
- `status` (string): The status of the billing report.  * `IN_PROGRESS` - Report generation is in progress.  * `COMPLETED` - Report generation is complete.  * `FAILED` - Report generation failed. Valores: IN_PROGRESS, COMPLETED, FAILED.
- `created` (string): The date and time the report was generated.
- `createdBy` (string): The person ID of the partner administrator who created the report.
- `tempDownloadURL` (string): The URL for partners to download the billing report.
- `errors` (array): List of errors that occurred during report generation.  **Note:**  * Captures errors that occurred during asynchronous or background report generation, after the request has been accepted and a `202 OK` response is returned.
  - `code` (number): The error code itself.
  - `description` (string): A textual representation of the error code.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0JJTExJTkdfUkVQT1JULzViOGQ1MThhLThmMDAtNDUxYi1hNDA2LWVhZjQ5YjRhN2ZhOA",
  "billingPeriod": "2021-05",
  "status": "COMPLETED",
  "created": "2021-06-16T12:40:33.109Z",
  "createdBy": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wYWNkMzg3NS00ZTEyLTRkNzctYjk4MS1lMzg5ZmQ4ODQ2YzA",
  "tempDownloadURL": "https://billing-reports-example.webexcontent.com/a366de9b-3204-4140-8181-25808d360e36/2021/06/16/340177d1-7f25-41e1-a39f-ad63ec1103a5.csv?Expires=1624978489&Signature=Syp3vrVeMx4P6MeMtm8e1bQaeAdHFe-c7NeHERWh5-qJGLZ1T8Dvl2ee-M8OsFf~z6Yepz94e2Hh1HDVailD0Uryl8SgiM~jl0cBh7L0PmSe~i9oFA0eJ0MulkqGSMVf7ZHhxY55xYMgIBZIERkWm3CqQNDg5BS4EaXapKfOnmFegf36OokCM63m5uOK8-csk08IkZhwo2Z0l1JMtuWYEaLh4dgMHoe~xgH3YmDSSCWInFYaEifUAfgi2YAYS6nP9Zq4BTliBq62XBaehOE1gBrhy4RdwD-3WSs2oD-BdpoRpuGzo3FZzDLVEvd0S2D6gTcHljOHodQKxe-u0BXPWQ__&Key-Pair-Id=APKAJADAKLCI2FW2U32Q"
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
The Webex BroadWorks Calling APIs provide access to advanced calling features and user management for BroadWorks-powered Webex Calling deployments. These APIs support provisioning of users and devices, call control, feature management, device inventory, and detailed reporting. Service providers and enterprises can automate onboarding, integrate with OSS/BSS systems, manage user entitlements, and monitor call quality. The APIs are designed for scalable, multi-tenant environments and support seamless integration with existing telephony infrastructure.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs