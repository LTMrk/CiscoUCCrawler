---
doc_id: webex-contact-center-patch-v3-campaign-management-campaigns-campaignid-contact-list-contactlistid-contacts-contactid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PATCH
path: /v3/campaign-management/campaigns/{campaignId}/contact-list/{contactListId}/contacts/{contactId}
operation_id: updateContactStatusInContactList
tags: Contact List Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.774831+00:00
---

# PATCH /v3/campaign-management/campaigns/{campaignId}/contact-list/{contactListId}/contacts/{contactId}

**API:** Webex Contact Center
**Área:** Contact List Management
**operationId:** `updateContactStatusInContactList`

## Resumen
Update a contact's status within a contact list

## Descripción
Updates a contact's status within a contact list. After update, system overwrites 'Latest Telephony Outcome' to blank and 'Latest Business Outcome' to 'Closed via API call' if status is CLOSED. This is an Asynchronous operation.

## Parámetros
- `campaignId` [path] (string) (**requerido**): Campaign ID.
- `contactListId` [path] (string) (**requerido**): Contact List ID (as a number string).
- `contactId` [path] (string) (**requerido**): Contact Unique ID (Contact Phone or Customer Unique ID or Account Unique ID)

## Cuerpo de la petición (application/json)
- `contactStatus` (string): Contact status (CLOSED) Valores: CLOSED.

### Ejemplo — petición
```json
{
  "contactStatus": "CLOSED"
}
```

## Ejemplo de invocación
```bash
curl -X PATCH '/v3/campaign-management/campaigns/<campaignId>/contact-list/<contactListId>/contacts/<contactId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**202**: Request queued
- `outcome` (string): Outcome of the operation Valores: Queued, Failed.
- `statusCode` (integer): 0 for Queued, non-zero for Failed
- `summary` (string): Summary of the operation

### Ejemplo — respuesta 202
```json
{
  "outcome": "Queued",
  "statusCode": 0,
  "summary": "Queued for updating the contact status"
}
```

## Respuestas de error
- **400**: Invalid request
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs