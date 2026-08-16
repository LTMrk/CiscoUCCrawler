---
doc_id: webex-contact-center-delete-v1-dialer-campaign-campaignid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /v1/dialer/campaign/{campaignId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.974478+00:00
---

# DELETE /v1/dialer/campaign/{campaignId}

**API:** Webex Contact Center
**Área:** Campaign Manager
**operationId:** `stopCampaignRoute`

## Resumen
Stop Campaign Request

## Descripción
The stop campaign API enables businesses to automate the process of managing outbound campaigns and integrate campaign deletion into their existing workflows or applications. Requires 'cjp.config_write' scope and one of the following roles: 'cjp.admin','id_full_admin','atlas-portal.partner.salesadmin','atlas-portal.partner.provision_admin' for authorization.

## Parámetros
- `campaignId` [path] (string) **(requerido)**: The unique request id of the campaign that needs to be stopped

## Respuestas
- **204**: The campaign was stopped.
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
