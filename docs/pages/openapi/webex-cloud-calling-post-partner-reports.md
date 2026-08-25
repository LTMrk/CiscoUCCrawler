---
doc_id: webex-cloud-calling-post-partner-reports
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /partner/reports
operation_id: createAReport
tags: Partner Reports/Templates
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.529542+00:00
---

# POST /partner/reports

**API:** Webex Cloud Calling
**Área:** Partner Reports/Templates
**operationId:** `createAReport`

## Resumen
Create a Report

## Descripción
Create a new report. A new report can be created using `templateId` available from the _List Report Templates_ API. For each `templateId`, there are a set of validation rules that need to be followed.

The `templateId` parameter is a number. However, it is a limitation of developer.webex.com platform that it is passed as a string when you try to test the API from here.

To access this endpoint, you must use an administrator token with `spark-admin:reports_write` and `identity:people_read` scopes.

**Notes**:

<div><Callout type="info">CSV reports for Webex suite services are only created for organizations in the specified region. Organizations based in a different region will require a separate request with region specified.</Callout></div>

<div><Callout type="info">When no region is specified, the request defaults to Partner organization's home region. A request against a region where there are no organizations will return blank CSV files.</Callout></div>

## Parámetros
- `onBehalfOfSubPartnerOrgId` [query] (string): The encoded organization ID for the sub partner.

## Cuerpo de la petición (application/json)
- `templateId` (number) (**requerido**): Unique ID representing valid report templates.
- `startDate` (string) (**requerido**): Data in the report will be from this date onwards.
- `endDate` (string) (**requerido**): Data in the report will be until this date.
- `regionId` (string): Data in the report will be from organizations in this region, for example, US, CA, or EU.

### Ejemplo — petición
```json
{
  "templateId": 5,
  "startDate": "2024-05-01",
  "endDate": "2024-05-05",
  "regionId": "US"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/partner/reports' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"templateId": 0, "startDate": "<startDate>", "endDate": "<endDate>"}'
```

## Respuestas correctas
**200**: OK
- `reportId` (string): The unique identifier for the report.
- `createdTime` (string): The time of report creation.

### Ejemplo — respuesta 200
```json
{
  "reportId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9SRVBPUlQvYWQwZDIwNTc1ZGEwNDVhNDhmYWQ0N2Q5NzRhYjQxZjI",
  "createdTime": "2024-05-27 17:02:43"
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