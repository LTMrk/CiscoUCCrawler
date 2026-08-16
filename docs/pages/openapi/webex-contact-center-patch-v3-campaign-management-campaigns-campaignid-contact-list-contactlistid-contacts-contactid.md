---
doc_id: webex-contact-center-patch-v3-campaign-management-campaigns-campaignid-contact-list-contactlistid-contacts-contactid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /v3/campaign-management/campaigns/{campaignId}/contact-list/{contactListId}/contacts/{contactId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.975437+00:00
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
- `campaignId` [path] (string) **(requerido)**: Campaign ID.
- `contactListId` [path] (string) **(requerido)**: Contact List ID (as a number string).
- `contactId` [path] (string) **(requerido)**: Contact Unique ID (Contact Phone or Customer Unique ID or Account Unique ID)

## Cuerpo de la petición (application/json)
- `contactStatus` (string): Contact status (CLOSED) Valores: CLOSED.

### Ejemplo de petición
```json
{
  "contactStatus": "CLOSED"
}
```

## Respuestas
- **202**: Request queued
  - `outcome` (string): Outcome of the operation Valores: Queued, Failed.
  - `statusCode` (integer): 0 for Queued, non-zero for Failed
  - `summary` (string): Summary of the operation
- **400**: Invalid request

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
