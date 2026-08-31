---
doc_id: webex-contact-center-post-v3-campaign-management-campaigns-campaignid-contact-list-contactlistid-contacts
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v3/campaign-management/campaigns/{campaignId}/contact-list/{contactListId}/contacts
operation_id: createContactsInContactList
tags: Contact List Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.774293+00:00
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
- `campaignId` [path] (string) (**requerido**): Campaign ID to which the contact list belongs.
- `contactListId` [path] (string) (**requerido**): Contact List ID (as a number string).

## Cuerpo de la petición (application/json)
- `contacts` (array): Array of contact attributes, max 10 contacts per request
  - `contactAttributes` (array) (**requerido**): Array of field mapping field name & value pairs.
    - `fieldName` (string): Field name
    - `value` (string): Field value

## Ejemplo de invocación
```bash
curl -X POST '/v3/campaign-management/campaigns/<campaignId>/contact-list/<contactListId>/contacts' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**202**: Request accepted
- `outcome` (string): Outcome of the operation Valores: Queued, Failed.
- `statusCode` (integer): 0 for Queued, non-zero for Failed
- `summary` (string): Summary of the operation

### Ejemplo — respuesta 202
```json
{
  "outcome": "Queued",
  "statusCode": 0,
  "summary": "Queued for adding to the contact list"
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