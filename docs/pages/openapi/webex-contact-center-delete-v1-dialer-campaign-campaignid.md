---
doc_id: webex-contact-center-delete-v1-dialer-campaign-campaignid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /v1/dialer/campaign/{campaignId}
operation_id: stopCampaignRoute
tags: Campaign Manager
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.772686+00:00
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
- `campaignId` [path] (string) (**requerido**): The unique request id of the campaign that needs to be stopped

## Ejemplo de invocación
```bash
curl -X DELETE '/v1/dialer/campaign/<campaignId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: The campaign was stopped.

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