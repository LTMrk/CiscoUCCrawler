---
doc_id: webex-contact-center-get-v4-campaign-management-campaigns-campaignid-contact-lists
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v4/campaign-management/campaigns/{campaignId}/contact-lists
operation_id: getContactListsInACampaign
tags: Contact List Management
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.775766+00:00
---

# GET /v4/campaign-management/campaigns/{campaignId}/contact-lists

**API:** Webex Contact Center
**Área:** Contact List Management
**operationId:** `getContactListsInACampaign`

## Resumen
Get Contact Lists within a Campaign

## Descripción
Retrieves all contact lists within a campaign. Use the optional `status` and `source` query parameters to filter results.

Each contact list in the response includes the source file name, the time contact counts were last updated, and a breakdown of contact counts by processing and dialer status (for example, processed, invalid, valid, eligible, fresh, open, closed, and ready for dialer).

Responses may reflect the same data for up to 30 seconds when the same campaign and filters are requested repeatedly.

## Parámetros
- `campaignId` [path] (string) (**requerido**): Campaign ID.
- `status` [query] (string): Contact List Status filter (Active, Expired, UploadFailed, etc.) Valores: Active, Expired, UploadFailed.
- `source` [query] (string): Contact List Source filter (API, SFTP, ManualFile) Valores: API, SFTP, ManualFile.

## Ejemplo de invocación
```bash
curl -X GET '/v4/campaign-management/campaigns/<campaignId>/contact-lists' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Contact lists retrieved successfully
- `outcome` (string) (**requerido**): Outcome of the operation Valores: Success, Failure.
- `statusCode` (integer) (**requerido**): 0 for success, non-zero for failure or validation failure
- `contactLists` (array) (**requerido**): List of contact lists
  - `contactListId` (string): Contact list ID within the campaign.
  - `contactListStatus` (string): Contact list status (for example: Active, Expired, UploadFailed).
  - `contactListSource` (string): How the contact list was created (for example, API, SFTP, ManualFile).
  - `contactListSourceFileName` (string): Source file name for the contact list upload.
  - `contactListCountsTimestampUtc` (string/date-time): UTC timestamp when the counts were last updated.
  - `processedContactsCount` (integer): Total contacts processed for this contact list.
  - `invalidContactsCount` (integer): Number of invalid contacts.
  - `validContactsCount` (integer): Derived: `processedContactsCount` − `invalidContactsCount`.
  - `eligibleContactsCount` (integer): Derived: `processedContactsCount` − `invalidContactsCount` − DNC-suppressed contacts.
  - `freshContactsCount` (integer): Number of contacts in Fresh state.
  - `openContactsCount` (integer): Number of contacts in Open state.
  - `closedContactsCount` (integer): Number of contacts in Closed state.
  - `errorsContactsCount` (integer): Number of contacts in Error state.
  - `readyForDialerContactsCount` (integer): Number of contacts ready to be sent to the dialer.
  - `sentToDialerAwaitingOutcomeContactsCount` (integer): Number of contacts sent to the dialer and awaiting an outcome.
  - `expiredContactsCount` (integer): Number of expired contacts.
  - `blockedContactsCount` (integer): Number of blocked contacts.
  - `closedTransferredToChainedCampaignContactsCount` (integer): Number of contacts closed and transferred to a chained campaign.
  - `dateOfCreation` (string/date-time): Date and time the contact list was created, in the campaign time zone.
  - `dateOfActivation` (string/date-time): Date and time the contact list was activated.
  - `dateOfExpiry` (string/date-time): Date and time the contact list expires.

### Ejemplo — respuesta 200
```json
{
  "outcome": "Success",
  "statusCode": 0,
  "contactLists": [
    {
      "contactListId": "501",
      "contactListStatus": "Active",
      "contactListSource": "API",
      "contactListSourceFileName": "contacts.csv",
      "contactListCountsTimestampUtc": "2025-08-01T14:30:00Z",
      "processedContactsCount": 100,
      "invalidContactsCount": 2,
      "validContactsCount": 98,
      "eligibleContactsCount": 95,
      "freshContactsCount": 40,
      "openContactsCount": 30,
      "closedContactsCount": 20,
      "errorsContactsCount": 0,
      "readyForDialerContactsCount": 5,
      "sentToDialerAwaitingOutcomeContactsCount": 3,
      "expiredContactsCount": 0,
      "blockedContactsCount": 0,
      "closedTransferredToChainedCampaignContactsCount": 0,
      "dateOfCreation": "2025-08-01T10:00:00",
      "dateOfActivation": "2025-08-01T12:00:00",
      "dateOfExpiry": "2025-09-01T00:00:00"
    }
  ]
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