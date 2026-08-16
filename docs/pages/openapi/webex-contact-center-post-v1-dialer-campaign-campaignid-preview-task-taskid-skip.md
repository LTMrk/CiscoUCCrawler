---
doc_id: webex-contact-center-post-v1-dialer-campaign-campaignid-preview-task-taskid-skip
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/dialer/campaign/{campaignId}/preview-task/{taskId}/skip
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.965175+00:00
---

# POST /v1/dialer/campaign/{campaignId}/preview-task/{taskId}/skip

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `skipPreviewCampaignTaskRoute`

## Resumen
Skip Preview Task

## Descripción
API to skip the preview campaign task offered to the agent.

## Parámetros
- `taskId` [path] (string) **(requerido)**: The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.
- `campaignId` [path] (string) **(requerido)**: The unique ID represents the campaign that the user is currently working on.

## Respuestas
- **202**: The request is accepted for processing
- **400**: Bad Request
- **401**: Invalid or absent authorization header
- **403**: Invalid OAuth 2.0 Bearer Token
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
