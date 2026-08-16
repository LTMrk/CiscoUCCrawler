---
doc_id: webex-contact-center-get-v3-campaign-management-campaigns-campaignid-contact-lists
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v3/campaign-management/campaigns/{campaignId}/contact-lists
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.975805+00:00
---

# GET /v3/campaign-management/campaigns/{campaignId}/contact-lists

**API:** Webex Contact Center
**Área:** Contact List Management
**operationId:** `getContactListsInCampaign`

## Resumen
Get Contact Lists within a Campaign

## Descripción
Retrieves all contact lists within a campaign, with optional filters for status and source.

This is the **v3** endpoint. Each contact list entry includes `contactListRecordsProcessed` (total processed records). For dialer counts, source file name, and per-status contact counts, use the **v4** endpoint (`GET /v4/campaign-management/campaigns/{campaignId}/contact-lists`).

**Caching:** Responses are cached for up to 30 seconds per campaign and filter combination.

## Parámetros
- `campaignId` [path] (string) **(requerido)**: Campaign ID.
- `status` [query] (string): Contact List Status filter (Active, Expired, UploadFailed, etc.)
- `source` [query] (string): Contact List Source filter (API, SFTP, ManualFile)

## Respuestas
- **200**: Contact lists retrieved successfully
  - `outcome` (string) **(requerido)**: Outcome of the operation Valores: Success, Failure.
  - `statusCode` (integer) **(requerido)**: 0 for success, non-zero for failure or validation failure
  - `contactLists` (array) **(requerido)**: List of contact lists
    - `contactListId` (string): Contact list ID within the campaign.
    - `contactListStatus` (string): Contact list status (for example: Active, Expired, UploadFailed).
    - `contactListSource` (string): How the contact list was created (for example, API, SFTP, ManualFile).
    - `contactListSourceFileName` (string): Source file name for the contact list upload.
    - `contactListCountsTimestampUtc` (string): UTC timestamp when the counts were last updated.
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
    - `dateOfCreation` (string): Date and time the contact list was created, in the campaign time zone.
    - `dateOfActivation` (string): Date and time the contact list was activated.
    - `dateOfExpiry` (string): Date and time the contact list expires.
- **400**: Invalid request

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
