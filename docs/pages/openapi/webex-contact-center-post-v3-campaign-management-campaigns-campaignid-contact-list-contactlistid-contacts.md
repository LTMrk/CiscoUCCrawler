---
doc_id: webex-contact-center-post-v3-campaign-management-campaigns-campaignid-contact-list-contactlistid-contacts
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v3/campaign-management/campaigns/{campaignId}/contact-list/{contactListId}/contacts
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.975324+00:00
---

# POST /v3/campaign-management/campaigns/{campaignId}/contact-list/{contactListId}/contacts

**API:** Webex Contact Center
**Área:** Contact List Management
**operationId:** `createContactsInContactList`

## Resumen
Create contacts within a contact list

## Descripción
Creates contacts within a contact list (only if that contact list was created using API method). If the contact record is invalid, it will be added as INVALID and reflected in the 'Processed' and 'Invalid' counts. This is an Asynchronous operation. The values within the 'contactAttributes' param should conform to datatypes of the contact attributes as specified in the 'Field mapping' associated with the campaign.

## Parámetros
- `campaignId` [path] (string) **(requerido)**: Campaign ID to which the contact list belongs.
- `contactListId` [path] (string) **(requerido)**: Contact List ID (as a number string).

## Cuerpo de la petición (application/json)
- `contacts` (array): Array of contact attributes, max 10 contacts per request
  - `contactAttributes` (array) **(requerido)**: Array of field mapping field name & value pairs.
    - `fieldName` (string): Field name
    - `value` (string): Field value

## Respuestas
- **202**: Request accepted
  - `outcome` (string): Outcome of the operation Valores: Queued, Failed.
  - `statusCode` (integer): 0 for Queued, non-zero for Failed
  - `summary` (string): Summary of the operation
- **400**: Invalid request

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
