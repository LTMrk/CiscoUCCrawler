---
doc_id: webex-contact-center-delete-v1-usage-reports-reportid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /v1/usage-reports/{reportId}
operation_id: deleteReport
tags: Usage Reports
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-17T19:59:29.926807+00:00
---

# DELETE /v1/usage-reports/{reportId}

**API:** Webex Contact Center
**Área:** Usage Reports
**operationId:** `deleteReport`

## Resumen
Delete usage report

## Descripción
Deletes the specified usage report and its associated file. This operation cannot be undone.

## Parámetros
- `reportId` [path] (string) (**requerido**): Usage report ID

## Ejemplo de invocación
```bash
curl -X DELETE '/v1/usage-reports/<reportId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: OK

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **500**: Internal Server Error: Something went wrong on the server
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs