---
doc_id: webex-contact-center-patch-v3-campaign-management-campaigns-campaignid-contacts-contactid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /v3/campaign-management/campaigns/{campaignId}/contacts/{contactId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.975551+00:00
---

# PATCH /v3/campaign-management/campaigns/{campaignId}/contacts/{contactId}

**API:** Webex Contact Center
**Área:** Contact List Management
**operationId:** `updateContactStatusInCampaignChain`

## Resumen
Update contact status across the campaign chain

## Descripción
Synchronously closes the specified contacts and returns the outcome in the same response. Contacts are identified using the same unique identifiers configured in your campaign field mappings, such as Contact Phone (format as per the associated field mapping) or Customer Unique ID or Account Unique ID (For more info, please refer to the [global variables help documentation](https://docs-campaign-for-contact-centers.webexcampaign.com/docs/global-variables)).

 By default, the API searches the specified campaign and any of its downstream target campaigns in the chain (across all active contact-lists associated with these campaigns), and closes the contact wherever it is found in a closeable state. Set `searchAcrossTheCampaignChain` to `no` to close the contact only in the campaign specified in the request path.

**Optional query parameters**

- `contactListId` - Search only the specific contact-list within the campaign specified in the request path. If `searchAcrossTheCampaignChain` is set to `yes` then all active contact-lists in the other downstream target campaigns in the chain are also searched.
- `fields` - Return specified contact field values in the response for the matching contact records (for example: FirstName, LastName, AmountDue).

## Parámetros
- `campaignId` [path] (string) **(requerido)**: Campaign ID (as a string). All downstream target campaigns in the chain are included in the search.
- `contactId` [path] (string) **(requerido)**: Contact Unique ID (Contact Phone or Customer Unique ID or Account Unique ID)
- `contactListId` [query] (string): Optional. Search only the specific contact-list within the campaign specified in the request path. If `searchAcrossTheCampaignChain` is set to `yes`, then all active contact-lists in the other downstream target campaigns in the chain are also searched. When omitted, all active contact lists in that campaign are searched.
- `fields` [query] (string): Optional. Contact field names to include in the response (comma-separated names).

## Cuerpo de la petición (application/json)
- `contactStatus` (string) **(requerido)**: Contact status to apply. Only CLOSED is supported. Valores: CLOSED.
- `searchAcrossTheCampaignChain` (string): Whether to close the contact across all campaigns in the chain. When omitted, all campaigns in the chain are included by default. Set to `no` to close only in the campaign specified in the request path. Valores: yes, no.

## Respuestas
- **200**: Contact closed. See `outcome` and `records` for per-campaign details.
  - `outcome` (string) **(requerido)**: Overall result: `Success` if closed everywhere a match was found; `PartialSuccess` if some matching contact records were closed but others were non-closeable; `NoChange` if none of the matching contact records could be closed; `Matching contact record not found.` if no match (HTTP 404). Valores: Success, PartialSuccess, NoChange, Matching contact record not found..
  - `statusCode` (integer) **(requerido)**: 0 for a completed API response.
  - `records` (array) **(requerido)**: Per-campaign close outcome.
    - `updated` (boolean): True when the contact was closed in this campaign.
    - `campaignId` (string): Campaign ID for this record.
    - `campaignName` (string): Campaign Name.
    - `contactListId` (string): Contact list ID within the campaign where the contact was matched.
    - `matchedBy` (object): Field header and value used to match the contact in this campaign.
    - `fields` (object): Optional map of requested field names to values, present when the `fields` query parameter was supplied. Omitted when no fields were requested.
    - `comment` (string): Per-record result message. `Closed.` when the contact was successfully closed (`updated: true`). When matched but in sent-to-dialer status, `Cannot close; already sent to dialer.` (`updated: false`).
- **400**: Invalid request (for example, unsupported contactStatus, missing contactStatus, invalid contactListId, or malformed fields query parameter).
- **403**: This operation is not enabled for your organization.
- **404**: No matching contact record found in any campaign in scope.
- **429**: Rate limit exceeded.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
