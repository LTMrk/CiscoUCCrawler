---
doc_id: webex-contact-center-post-v3-campaign-management-campaigns-campaignid-contact-list
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v3/campaign-management/campaigns/{campaignId}/contact-list
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.975194+00:00
---

# POST /v3/campaign-management/campaigns/{campaignId}/contact-list

**API:** Webex Contact Center
**Área:** Contact List Management
**operationId:** `createContactList`

## Resumen
Create contact list

## Descripción
Creates and activates a contact list for a campaign. The system can activate a contact list even if there are no contact records within it.

## Parámetros
- `campaignId` [path] (string) **(requerido)**: Campaign ID to which the contact list belongs.

## Cuerpo de la petición (application/json)
- `supportedChannels` (array) **(requerido)**: Supported channels for the contact list
- `activationTimeLagMinutes` (integer): Contact list activation time lag in minutes (0 = immediate activation, 180 = 3 hours delay). Required if activationDateTime is not provided.
- `activationDateTime` (string): Contact list activation DateTimeStamp (format: YYYY-MM-DDTHH:MM). Required if activationTimeLagMinutes is not provided.

## Respuestas
- **201**: Contact list created successfully
  - `outcome` (string): Outcome of the operation Valores: Success, Failure.
  - `statusCode` (integer): 0 for success, non-zero for failure or validation failure
  - `contactListId` (string): Contact List ID within the campaign (number only)
- **400**: Invalid request

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
