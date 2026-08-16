---
doc_id: webex-contact-center-patch-v3-campaign-management-campaigns-campaignid-contact-list-contactlistid-status
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /v3/campaign-management/campaigns/{campaignId}/contact-list/{contactListId}/status
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.975693+00:00
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
- `campaignId` [path] (string) **(requerido)**: Campaign ID.
- `contactListId` [path] (string) **(requerido)**: Contact List ID (as a number string).

## Cuerpo de la petición (application/json)
- `contactListStatus` (string): Contact List Status (e.g., EXPIRED). Note: This value is not case-sensitive.

### Ejemplo de petición
```json
{
  "contactListStatus": "EXPIRED"
}
```

## Respuestas
- **200**: Contact list status updated successfully
  - `outcome` (string): Outcome of the operation Valores: Success, Failure.
  - `statusCode` (integer): 0 for success, non-zero for failure or validation failure
  - `contactLists` (array): List of contact lists
    - `contactListId` (string): Contact List ID
    - `contactListStatus` (string): Contact List Status
    - `contactListRecordCount` (integer): Number of records in the contact list
    - `contactListSource` (string): Source of the contact list
    - `dateOfCreation` (string): Date of creation
    - `dateOfActivation` (string): Date of activation
    - `dateOfExpiry` (string): Date of expiry
- **400**: Invalid request

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
