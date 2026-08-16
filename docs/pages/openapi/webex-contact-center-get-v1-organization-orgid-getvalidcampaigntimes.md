---
doc_id: webex-contact-center-get-v1-organization-orgid-getvalidcampaigntimes
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v1/organization/{orgId}/getValidCampaignTimes
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.974257+00:00
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
- `orgId` [path] (string) **(requerido)**: The organization ID for which valid campaign times are being requested.
- `campaignId` [query] (string) **(requerido)**: The campaign ID for which valid campaign times are being requested.
- `agentId` [query] (string) **(requerido)**: The agent ID for whom valid campaign times are being requested.
- `trackingId` [query] (string): Optional tracking identifier for request tracing.

## Respuestas
- **200**: The valid campaign times request was accepted for processing.
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
