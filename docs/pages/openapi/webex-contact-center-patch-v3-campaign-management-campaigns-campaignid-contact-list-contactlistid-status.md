---
doc_id: webex-contact-center-patch-v3-campaign-management-campaigns-campaignid-contact-list-contactlistid-status
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PATCH
path: /v3/campaign-management/campaigns/{campaignId}/contact-list/{contactListId}/status
operation_id: updateContactListStatus
tags: Contact List Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.873573+00:00
---

# PATCH /v3/campaign-management/campaigns/{campaignId}/contact-list/{contactListId}/status

**API:** Webex Contact Center
**Área:** Contact List Management
**operationId:** `updateContactListStatus`

## Resumen
Update contact list status

## Descripción
Updates the status of a contact list (e.g., EXPIRED). Note: This value is not case-sensitive.

## Parámetros
- `campaignId` [path] (string) (**requerido**): Campaign ID.
- `contactListId` [path] (string) (**requerido**): Contact List ID (as a number string).

## Cuerpo de la petición (application/json)
- `contactListStatus` (string): Contact List Status (e.g., EXPIRED). Note: This value is not case-sensitive.

### Ejemplo — petición
```json
{
  "contactListStatus": "EXPIRED"
}
```

## Ejemplo de invocación
```bash
curl -X PATCH '/v3/campaign-management/campaigns/<campaignId>/contact-list/<contactListId>/status' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: Contact list status updated successfully
- `outcome` (string): Outcome of the operation Valores: Success, Failure.
- `statusCode` (integer): 0 for success, non-zero for failure or validation failure
- `contactLists` (array): List of contact lists
  - `contactListId` (string): Contact List ID
  - `contactListStatus` (string): Contact List Status
  - `contactListRecordCount` (integer): Number of records in the contact list
  - `contactListSource` (string): Source of the contact list
  - `dateOfCreation` (string/date-time): Date of creation
  - `dateOfActivation` (string/date-time): Date of activation
  - `dateOfExpiry` (string/date-time): Date of expiry

### Ejemplo — respuesta 200
```json
{
  "outcome": "Success",
  "statusCode": 0,
  "summary": "Contact list status updated successfully"
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