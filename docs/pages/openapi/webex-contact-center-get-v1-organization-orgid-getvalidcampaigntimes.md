---
doc_id: webex-contact-center-get-v1-organization-orgid-getvalidcampaigntimes
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/organization/{orgId}/getValidCampaignTimes
operation_id: getValidCampaignTimesRoute
tags: Campaign Manager
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.772383+00:00
---

# GET /v1/organization/{orgId}/getValidCampaignTimes

**API:** Webex Contact Center
**Área:** Campaign Manager
**operationId:** `getValidCampaignTimesRoute`

## Resumen
Get Valid Campaign Times

## Descripción
Gets valid campaign times for a campaign and agent. This request is accepted for asynchronous processing. Requires 'cjp:user','cjp.config_write' scope and one of the following roles: 'cjp.admin','id_full_admin','atlas-portal.partner.salesadmin','atlas-portal.partner.provision_admin' for authorization.

## Parámetros
- `orgId` [path] (string/uuid) (**requerido**): The organization ID for which valid campaign times are being requested.
- `campaignId` [query] (string) (**requerido**): The campaign ID for which valid campaign times are being requested.
- `interactionId` [query] (string/uuid) (**requerido**): The unique identifier of the interaction associated with this request.
- `agentId` [query] (string/uuid) (**requerido**): The agent ID for whom valid campaign times are being requested.
- `trackingId` [query] (string/uuid): Optional tracking identifier for request tracing.

## Ejemplo de invocación
```bash
curl -X GET '/v1/organization/<orgId>/getValidCampaignTimes?campaignId=<campaignId>&interactionId=<interactionId>&agentId=<agentId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: The valid campaign times request was accepted for processing.

## Respuestas de error
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs