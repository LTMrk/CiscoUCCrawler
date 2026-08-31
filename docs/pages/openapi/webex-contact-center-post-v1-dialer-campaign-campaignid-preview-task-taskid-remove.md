---
doc_id: webex-contact-center-post-v1-dialer-campaign-campaignid-preview-task-taskid-remove
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/dialer/campaign/{campaignId}/preview-task/{taskId}/remove
operation_id: removePreviewCampaignTaskRoute
tags: Tasks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.145145+00:00
---

# POST /v1/dialer/campaign/{campaignId}/preview-task/{taskId}/remove

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `removePreviewCampaignTaskRoute`

## Resumen
Remove Preview Task

## Descripción
API to remove the preview campaign task offered to the agent

## Parámetros
- `taskId` [path] (string/UUID) (**requerido**): The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.
- `campaignId` [path] (string/UUID) (**requerido**): The unique ID represents the campaign that the user is currently working on.

## Ejemplo de invocación
```bash
curl -X POST '/v1/dialer/campaign/<campaignId>/preview-task/<taskId>/remove' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: The request is accepted for processing

## Respuestas de error
- **400**: Bad Request
- **401**: Invalid or absent authorization header
- **403**: Invalid OAuth 2.0 Bearer Token
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs