---
doc_id: webex-contact-center-get-v3-campaign-management-campaign-groups-campaigngroupname-campaigns
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v3/campaign-management/campaign-groups/{campaignGroupName}/campaigns
operation_id: getCampaignsByCampaignGroup
tags: Campaign Group
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.822759+00:00
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
- `campaignGroupName` [path] (string) (**requerido**): The name of the campaign group whose campaigns are to be retrieved. Case-insensitive matching.   **Allowed characters:** - `A-Z`, `a-z`, `0-9`, `_` (underscore), space  **Allowed Length** `1..64`
- `page` [query] (integer): The page number of the result set to retrieve (1-based). Por defecto: 1.
- `pageSize` [query] (integer): The number of campaigns to return per page. Must be between 1 and 100. Por defecto: 50.
- `campaignStatus` [query] (string): Optional filter for campaign status. Case-insensitive. Allowed values: `Draft`, `Running`, `Pending`, `Paused`, `Completed`, `Ended`. Valores: Draft, Running, Pending, Paused, Completed, Ended.

## Ejemplo de invocación
```bash
curl -X GET '/v3/campaign-management/campaign-groups/<campaignGroupName>/campaigns' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Campaigns successfully retrieved for the specified campaign group.
- `outcome` (string) (**requerido**): High-level outcome of the request.
- `statusCode` (integer) (**requerido**): Application-level status code. `0` indicates success.
- `campaigns` (array) (**requerido**): List of campaigns belonging to the campaign group for the requested page.
  - `campaignId` (string): Unique identifier of the campaign.
  - `campaignName` (string): Display name of the campaign.
  - `campaignGroupName` (string): Name of the campaign group to which the campaign belongs.
  - `channel` (string): Channel through which the campaign is executed.
  - `campaignType` (string): Type of campaign configuration. Valores: Basic, Advanced.
  - `campaignDialingMode` (string): Dialing mode of the campaign. Valores: Progressive, Predictive, ProgressiveIvr, PredictiveIvr, StandardPreview, DirectPreview.
  - `status` (string): Current status of the campaign. Valores: Draft, Running, Pending, Paused, Completed, Ended.
  - `createdTime` (string/date-time): Timestamp when the campaign was created (ISO 8601, UTC).
  - `lastUpdatedTime` (string): Timestamp when the campaign was last updated (ISO 8601, UTC).
  - `startDate` (string): Campaign schedule start date in `yyyy-MM-dd` format.
  - `endDate` (string): Campaign schedule end date in `yyyy-MM-dd` format. Returns `N/A` when the campaign has no configured end date.
  - `sourceCampaigns` (array): List of source campaigns in chaining from where the contacts are derived. Omitted from the response when empty.
  - `fieldMapping` (string): Name of the field mapping associated with the campaign.
  - `timezone` (string): Timezone configured for the campaign schedule.
  - `scheduleType` (string): Type of schedule configured for the campaign. `Basic` uses a single daily start/end window; `Advanced` provides per-day windows with named day-of-week entries. Valores: Basic, Advanced.
  - `scheduleInfo` (array): Schedule windows for the campaign. The shape of each entry depends on `scheduleType`: for `Basic`, entries are simple `startTime`/`endTime` windows; for `Advanced`, entries describe a specific day-of-week with one or more time slots.
    - (uno de:)
      - `startTime` (string) (**requerido**): Start time of the schedule slot in HH:mm (24-hour) format.
      - `endTime` (string) (**requerido**): End time of the schedule slot in HH:mm (24-hour) format.
      - `name` (string) (**requerido**): Day-of-week name. Valores: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday.
      - `day` (string) (**requerido**): Day-of-week index as a string. `1` = Sunday through `7` = Saturday. Valores: 1, 2, 3, 4, 5, 6, 7.
      - `slots` (array) (**requerido**): One or more start/end time slots active on this day.
        - `startTime` (string) (**requerido**): Start time of the schedule slot in HH:mm (24-hour) format.
        - `endTime` (string) (**requerido**): End time of the schedule slot in HH:mm (24-hour) format.
  - `safeCallingWindow` (array): Safe-calling windows for the campaign.
    - `scwStartTime` (string): Start time of the safe-calling window in HH:mm (24-hour) format.
    - `scwEndTime` (string): End time of the safe-calling window in HH:mm (24-hour) format.
  - `contactAttemptsStrategy` (object): Strategy that governs how many times and in what order contacts are attempted. May be null if not configured.
  - `contactFlowPriority` (object): Contact flow priority applied during dialing. Either a `Contact Attribute` priority or a `FreshVsRetry` priority.
  - `campaignCreatedBy` (string): User or system that created the campaign.
  - `controlHubChannelEntryPointID` (string/uuid): Control Hub Channel (a.k.a. Entry Point) associated with the campaign.
  - `outdialANI` (string): ANI used for outdial in E.164 format.
  - `dncLists` (array): DNC lists applied to the campaign.
  - `purposeTags` (array): Purpose tags applied to the campaign.
  - `pAndLTag` (string): P&L tag associated with the campaign.
  - `cpaEnabled` (string): Whether Call Progress Analysis (CPA) is enabled for the campaign. Valores: Yes, No.
  - `numberOfSFTPContactLists` (integer): Number of SFTP-sourced contact lists associated with the campaign.
  - `numberOfAPIContactLists` (integer): Number of API-sourced contact lists associated with the campaign.
  - `numberOfManualFileContactLists` (integer): Number of manually uploaded file contact lists associated with the campaign.
- `pagination` (object) (**requerido**): Pagination metadata for a paged response.
  - `page` (integer) (**requerido**): Current page number (1-based).
  - `pageSize` (integer) (**requerido**): Number of items returned per page.
  - `totalCount` (integer) (**requerido**): Total number of campaigns matching the query.
  - `totalPages` (integer) (**requerido**): Total number of pages available for the query.

### Ejemplo — respuesta 200
```json
{
  "outcome": "Success",
  "statusCode": 0,
  "campaigns": [
    {
      "campaignId": "CCV_1780403367475",
      "campaignName": "Auto_Loan_Collection Campaigns",
      "campaignGroupName": "Debt_Collection Campaigns",
      "channel": "Voice",
      "campaignType": "Basic",
      "campaignDialingMode": "StandardPreview",
      "status": "Running",
      "createdTime": "2026-06-02T07:59:27Z",
      "lastUpdatedTime": "2026-06-02T07:57:58Z",
      "startDate": "2026-06-01",
      "endDate": "2026-12-31",
      "fieldMapping": "Auto_Loans_Field_Mapping",
      "timezone": "UTC - 06:00 / USA / Central Time / Chicago, Dallas, Memphis, Nashville",
      "scheduleType": "Advanced",
      "scheduleInfo": [
        {
          "name": "Monday",
          "day": "2",
          "slots": [
            {
              "startTime": "08:00",
              "endTime": "12:00"
            },
            {
              "startTime": "13:00",
              "endTime": "17:00"
            },
            {
              "startTime": "18:00",
              "endTime": "20:00"
            }
          ]
        },
        {
          "name": "Tuesday",
          "day": "3",
          "slots": [
            {
              "startTime": "08:00",
              "endTime": "13:00"
            },
            {
              "startTime": "14:00",
              "endTime": "20:00"
            }
          ]
        },
        {
          "name": "Wednesday",
          "day": "4",
          "slots": [
        
  ... (truncado)
```

## Respuestas de error
- **400**: Bad Request: The request was invalid (e.g., invalid `page`, `pageSize`, or `campaignStatus`).
  Ejemplo:
```json
{
  "code": 1001,
  "message": "Invalid pageSize. Allowed range is 1 to 100.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f594b"
}
```
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
  Ejemplo:
```json
{
  "code": 401,
  "message": "Invalid or expired access token.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f591"
}
```
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed. The feature may not be enabled for this organization or the user lacks required permissions.
  Ejemplo:
```json
{
  "code": 403,
  "message": "Feature is not enabled for this organization.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f592"
}
```
- **404**: Not Found: The specified campaign group does not exist.
  Ejemplo:
```json
{
  "code": 1004,
  "message": "Campaign group 'Carshield_25May2026' not found.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f593"
}
```
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
  Ejemplo:
```json
{
  "code": 429,
  "message": "Too many requests. Rate limit exceeded.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f595"
}
```
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
  Ejemplo:
```json
{
  "code": 1006,
  "message": "An unexpected error occurred while processing your request.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f596"
}
```
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
  Ejemplo:
```json
{
  "code": 502,
  "message": "The server received an invalid response from an upstream server.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f597"
}
```
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
  Ejemplo:
```json
{
  "code": 503,
  "message": "Service is temporarily unavailable. Please try again later.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f598"
}
```
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.
  Ejemplo:
```json
{
  "code": 504,
  "message": "The server did not receive a timely response from an upstream server.",
  "trackingId": "GTWY_e6763c9a-71b2-4515-ad5b-89260f7f599"
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs