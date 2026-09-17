---
doc_id: webex-contact-center-get-v1-usage-reports-fileid-download
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/usage-reports/{fileId}/download
operation_id: downloadReport
tags: Usage Reports
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-17T19:59:29.926880+00:00
---

# GET /v1/usage-reports/{fileId}/download

**API:** Webex Contact Center
**Área:** Usage Reports
**operationId:** `downloadReport`

## Resumen
Download usage report file

## Descripción
Downloads one completed report file as a binary stream.

Use the `fileId` returned in the report's `reportFiles` array. A `reportId` identifies the overall report and cannot be used with this endpoint. Usage Reports can cover up to 36 months of raw data, so large date ranges may be split into one file per calendar month. This keeps individual compressed files more manageable and avoids requiring customers to download a single very large file. If a report contains multiple files, call this endpoint once for each `fileId`.

Passing a `reportId` to this endpoint returns `404` because the path parameter expects a file-level identifier.

The Developer Portal may not handle binary downloads reliably. Use Postman, curl, or a programmatic API client to download the file.

**Note:** Both file and download URLs expire 7 days after report completion.

## Parámetros
- `fileId` [path] (string) (**requerido**): ID of the specific report file to download. Use fileId, not reportId.

## Ejemplo de invocación
```bash
curl -X GET '/v1/usage-reports/<fileId>/download' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Binary stream containing the generated CSV report file

### Ejemplo — respuesta 200
```json
"<binary file content>"
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: The URI requested is invalid or the resource requested, such as a report does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many download times
- **500**: Internal Server Error: Something went wrong on the server
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs