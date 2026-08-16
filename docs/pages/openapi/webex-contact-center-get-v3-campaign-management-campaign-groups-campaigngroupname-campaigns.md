---
doc_id: webex-contact-center-get-v3-campaign-management-campaign-groups-campaigngroupname-campaigns
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v3/campaign-management/campaign-groups/{campaignGroupName}/campaigns
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.975095+00:00
---

# GET /v3/campaign-management/campaign-groups/{campaignGroupName}/campaigns

**API:** Webex Contact Center
**Área:** Campaign Group
**operationId:** `getCampaignsByCampaignGroup`

## Resumen
List Campaigns by Campaign Group

## Descripción
Retrieves the list of campaigns that belong to the specified campaign group. Results are paginated and can optionally be filtered by campaign status.

**Note:** The `campaignStatus` filter is case-insensitive. Allowed values are `Draft`, `Running`, `Pending`, `Paused`, `Completed`, `Ended`. Unknown values will result in a 400 response.

## Parámetros
- `campaignGroupName` [path] (string) **(requerido)**: The name of the campaign group whose campaigns are to be retrieved. Case-insensitive matching.   **Allowed characters:** - `A-Z`, `a-z`, `0-9`, `_` (underscore), space  **Allowed Length** `1..64`
- `page` [query] (integer): The page number of the result set to retrieve (1-based).
- `pageSize` [query] (integer): The number of campaigns to return per page. Must be between 1 and 100.
- `campaignStatus` [query] (string): Optional filter for campaign status. Case-insensitive. Allowed values: `Draft`, `Running`, `Pending`, `Paused`, `Completed`, `Ended`.

## Respuestas
- **200**: Campaigns successfully retrieved for the specified campaign group.
  - `outcome` (string) **(requerido)**: High-level outcome of the request.
  - `statusCode` (integer) **(requerido)**: Application-level status code. `0` indicates success.
  - `campaigns` (array) **(requerido)**: List of campaigns belonging to the campaign group for the requested page.
    - `campaignId` (string): Unique identifier of the campaign.
    - `campaignName` (string): Display name of the campaign.
    - `campaignGroupName` (string): Name of the campaign group to which the campaign belongs.
    - `channel` (string): Channel through which the campaign is executed.
    - `campaignType` (string): Type of campaign configuration. Valores: Basic, Advanced.
    - `campaignDialingMode` (string): Dialing mode of the campaign. Valores: Progressive, Predictive, ProgressiveIvr, PredictiveIvr, StandardPreview, DirectPreview.
    - `status` (string): Current status of the campaign. Valores: Draft, Running, Pending, Paused, Completed, Ended.
    - `createdTime` (string): Timestamp when the campaign was created (ISO 8601, UTC).
    - `lastUpdatedTime` (string): Timestamp when the campaign was last updated (ISO 8601, UTC).
    - `startDate` (string): Campaign schedule start date in `yyyy-MM-dd` format.
    - `endDate` (string): Campaign schedule end date in `yyyy-MM-dd` format. Returns `N/A` when the campaign has no configured end date.
    - `sourceCampaigns` (array): List of source campaigns in chaining from where the contacts are derived. Omitted from the response when empty.
    - `fieldMapping` (string): Name of the field mapping associated with the campaign.
    - `timezone` (string): Timezone configured for the campaign schedule.
    - `scheduleType` (string): Type of schedule configured for the campaign. `Basic` uses a single daily start/end window; `Advanced` provides per-day windows with named day-of-week entries. Valores: Basic, Advanced.
    - `scheduleInfo` (array): Schedule windows for the campaign. The shape of each entry depends on `scheduleType`: for `Basic`, entries are simple `startTime`/`endTime` windows; for `Advanced`, entries describe a specific day-of-week with one or more time slots.
    - `safeCallingWindow` (array): Safe-calling windows for the campaign.
      - `scwStartTime` (string): Start time of the safe-calling window in HH:mm (24-hour) format.
      - `scwEndTime` (string): End time of the safe-calling window in HH:mm (24-hour) format.
    - `contactAttemptsStrategy` (object): Strategy that governs how many times and in what order contacts are attempted. May be null if not configured.
    - `contactFlowPriority` (object): Contact flow priority applied during dialing. Either a `Contact Attribute` priority or a `FreshVsRetry` priority.
    - `campaignCreatedBy` (string): User or system that created the campaign.
    - `controlHubChannelEntryPointID` (string): Control Hub Channel (a.k.a. Entry Point) associated with the campaign.
    - `outdialANI` (string): ANI used for outdial in E.164 format.
    - `dncLists` (array): DNC lists applied to the campaign.
    - `purposeTags` (array): Purpose tags applied to the campaign.
    - `pAndLTag` (string): P&L tag associated with the campaign.
    - `cpaEnabled` (string): Whether Call Progress Analysis (CPA) is enabled for the campaign. Valores: Yes, No.
    - `numberOfSFTPContactLists` (integer): Number of SFTP-sourced contact lists associated with the campaign.
    - `numberOfAPIContactLists` (integer): Number of API-sourced contact lists associated with the campaign.
    - `numberOfManualFileContactLists` (integer): Number of manually uploaded file contact lists associated with the campaign.
  - `pagination` (object) **(requerido)**: Pagination metadata for a paged response.
    - `page` (integer) **(requerido)**: Current page number (1-based).
    - `pageSize` (integer) **(requerido)**: Number of items returned per page.
    - `totalCount` (integer) **(requerido)**: Total number of campaigns matching the query.
    - `totalPages` (integer) **(requerido)**: Total number of pages available for the query.
- **400**: Bad Request: The request was invalid (e.g., invalid `page`, `pageSize`, or `campaignStatus`).
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed. The feature may not be enabled for this organization or the user lacks required permissions.
- **404**: Not Found: The specified campaign group does not exist.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
