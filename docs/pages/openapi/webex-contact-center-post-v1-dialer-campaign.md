---
doc_id: webex-contact-center-post-v1-dialer-campaign
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/dialer/campaign
operation_id: startCampaignRoute
tags: Campaign Manager
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.820429+00:00
---

# POST /v1/dialer/campaign

**API:** Webex Contact Center
**Área:** Campaign Manager
**operationId:** `startCampaignRoute`

## Resumen
Start Campaign Request

## Descripción
A start campaign API allows businesses to programmatically start outbound campaigns using their own software applications. This type of API typically allows businesses to set up the parameters for a campaign, such as the list of phone numbers to call, the message or script to deliver, and the time of day or day of the week to call. Requires 'cjp.config_write' scope and one of the following roles: 'cjp.admin','id_full_admin','atlas-portal.partner.salesadmin','atlas-portal.partner.provision_admin' for authorization.

## Cuerpo de la petición (application/json)
- `id` (string) (**requerido**): The id represents the unique id with which the Campaign Request will be started, maximum length 64 characters.
- `vendorVersion` (string) (**requerido**): Vendor specific information, maximum length 32 characters.
- `campaignType` (string) (**requerido**): Type of campaign and campaignType should be one of "progressive", "campaign", "predictive", "progressive_ivr", "predictive_ivr" , "preview_standard", "preview_direct"
- `campaignName` (string): (Optional) Used if different than id, maximum length 64 characters.
- `authToken` (string): (Not in use) The token needed by the dialer for querying records.
- `dialingRate` (number/float) (**requerido**): Number of contacts to be dialed out per available Agent. For Progressive 1:1 Dialer, it will support for only 1 contact and for Progressive 1:N Dialer it can support upto 10 contacts to be dialed out per available Agent
- `entryPointId` (string) (**requerido**): Webex Contact Center outdial entry point, maximum length 36 characters.
- `dialingListFetchURL` (string) (**requerido**): URL the dialer will use to fetch the list of contacts to dial for the campaign from campaign manager, maximum length 1024 characters.
- `outdialANI` (string) (**requerido**): The ANI (E164)  that will be presented to the customer. These must be restricted to the configured outdial Eps in Webex Contact Center, maximum length 50 characters.
- `recordCount` (integer) (**requerido**): Value to indicate the recordCount the Campaign Manager expects the dialer to be able to request, the maximum is 400. If the value is greater than 400 it will be set to the maximum when the request is processed.
- `noAnswerRingLimit` (integer): (Optional) Number of seconds before a dialed call from the dialer is considered not answered, The range is from 16 to 80, default is 32. This field is not applicable for Direct preview campaigns.
- `maxDialingRate` (number/float): Caps the maximum dialing rate per agent at this value. The range is from 1.0 to 10.0 , default is 1.0.
- `abandonRatePercentage` (number/float): The percentage of calls that are allowed to be abandoned. The range is from 1.0 to 100.0 with a granularity of 0.1. The Default is 3.0
- `predictiveCorrectionPace` (integer): A count of the number of live voice connections that must occur before the dialer adjusts. Increasing this number results in less frequent adjustments based on a larger sample size. The range is from 10 to 5000 , default is 70.
- `predictiveGain` (number/float): The size of the adjustment to lines per agent each time an adjustment is made. Increasing this number results in larger per-agent adjustments. The range is 0.1 to 3.0 , default is 1.0.
- `reservationPercentage` (integer): (Not in use) The percentage of agents to reserve within the queue associated with the campaign. The range is from 0 to 100 , default is 100
- `callProgressAnalysisParams` (object): (Optional) Call Progressive Params details. This is used for Progressive 1:N Dialer.
  - `cpaEnabled` (boolean): (Optional) Determines if CPA should execute the campaign, default is false.
  - `amdEnabled` (boolean): (Optional) Determines if CPA should enable answering machine detection algorithm. cpaEnabled must be true when amdEnabled is set to true, default is false.
  - `minSilencePeriod` (integer): (Optional) The minimum silence period (in ms) is required to classify a call as voice detected. The range is from 100 to 1000, default is 608.
  - `analysisPeriod` (integer): (Optional) The number of ms spent analyzing the call. The range is 1000 to 10000, default is 1000.
  - `minimumValidSpeech` (integer): (Optional) The minimum number of ms of voice required to classify a call as voice detected. The range is from 50 to 500, default is 112.
  - `maxTimeAnalysis` (integer): (Optional) The maximum number of ms allowed for analysis before identifying a problem as dead air. The range is from 1000 to 10000, default is 3000.
  - `maxTermToneAnalysis` (integer): (Optional) The maximum number of ms the dialer analyzes an answering machine voice message looking for a termination tone. The range is 1000 to 60000, default is 30000.
  - `terminatingToneDetect` (boolean): (Optional) Determines if CPA should wait for the terminating tone of a voicemail before concluding. amdEnabled must be true when terminatingToneDetect is set to true, default is false.
- `ivrPorts` (integer): The number of IVR ports to use for this campaign. IVR ports are in use when calling a customer until the call is either ended or transferred to an agent. One IVR port can be considered equivalent to an agent in an agent based campaign.The range is from 1 to 1000.
- `previewOfferTimeout` (integer): (Required if previewOfferTimeoutAutoAction is provided, optional otherwise) The number of seconds dialer waits for an agent to act on a preview campaign record, before performing the provided previewOfferTimeoutAutoAction. The range is from 0 to 7200(2 hours) for ACCEPT auto-action and 10 to 7200(2 hours) for other auto-actions. The default is 600(10 minutes).
- `previewOfferTimeoutAutoAction` (string): (Required if previewOfferTimeout is provided, optional otherwise) The automatic action to be performed after the previewOfferTimeout duration has elapsed, if agent takes no action on the preview campaign record offered. Should be one of "ACCEPT", "SKIP", "REMOVE". The default is "SKIP".
- `previewActionsDisabled` (array): (Optional) The list of preview actions to be disabled for the agent when a preview campaign record is offered. Can be empty if no action should be disabled, otherwise should be one of "SKIP", "REMOVE" or both. The default is an empty list
- `validCampaignTimes` (object): (Optional) Defines the valid operating hours for the campaign based on a weekly schedule and optional date-specific overrides. The campaign will only be active during the specified time windows.
  - `timeZone` (string) (**requerido**): The IANA timezone name (e.g., 'America/New_York') that defines the timezone for all shift times in the schedule. This timezone is used to interpret the start and end times in the weekly schedule and date overrides.
  - `weeklySchedule` (object) (**requerido**):
    - `monday` (array) (**requerido**): List of shift times for Monday. Can be empty if no shifts are scheduled.
      - `start` (string) (**requerido**): The start time of the shift in 24-hour format (HH:MM). Must be earlier than the end time.
      - `end` (string) (**requerido**): The end time of the shift in 24-hour format (HH:MM). Must be later than the start time.
    - `tuesday` (array) (**requerido**): List of shift times for Tuesday. Can be empty if no shifts are scheduled.
      - `start` (string) (**requerido**): The start time of the shift in 24-hour format (HH:MM). Must be earlier than the end time.
      - `end` (string) (**requerido**): The end time of the shift in 24-hour format (HH:MM). Must be later than the start time.
    - `wednesday` (array) (**requerido**): List of shift times for Wednesday. Can be empty if no shifts are scheduled.
      - `start` (string) (**requerido**): The start time of the shift in 24-hour format (HH:MM). Must be earlier than the end time.
      - `end` (string) (**requerido**): The end time of the shift in 24-hour format (HH:MM). Must be later than the start time.
    - `thursday` (array) (**requerido**): List of shift times for Thursday. Can be empty if no shifts are scheduled.
      - `start` (string) (**requerido**): The start time of the shift in 24-hour format (HH:MM). Must be earlier than the end time.
      - `end` (string) (**requerido**): The end time of the shift in 24-hour format (HH:MM). Must be later than the start time.
    - `friday` (array) (**requerido**): List of shift times for Friday. Can be empty if no shifts are scheduled.
      - `start` (string) (**requerido**): The start time of the shift in 24-hour format (HH:MM). Must be earlier than the end time.
      - `end` (string) (**requerido**): The end time of the shift in 24-hour format (HH:MM). Must be later than the start time.
    - `saturday` (array) (**requerido**): List of shift times for Saturday. Can be empty if no shifts are scheduled.
      - `start` (string) (**requerido**): The start time of the shift in 24-hour format (HH:MM). Must be earlier than the end time.
      - `end` (string) (**requerido**): The end time of the shift in 24-hour format (HH:MM). Must be later than the start time.
    - `sunday` (array) (**requerido**): List of shift times for Sunday. Can be empty if no shifts are scheduled.
      - `start` (string) (**requerido**): The start time of the shift in 24-hour format (HH:MM). Must be earlier than the end time.
      - `end` (string) (**requerido**): The end time of the shift in 24-hour format (HH:MM). Must be later than the start time.
  - `dateOverrides` (array): Optional list of date-specific schedule overrides that take precedence over the weekly schedule for particular dates (e.g., holidays, special events).
    - `date` (string) (**requerido**): The specific date for which the shift schedule should be overridden, in YYYY-MM-DD format.
    - `shiftTimes` (array) (**requerido**): The list of shift times that apply on this specific date, overriding the weekly schedule. An empty array indicates no shifts are scheduled for this date (e.g., holidays, company closures).
      - `start` (string) (**requerido**): The start time of the shift in 24-hour format (HH:MM). Must be earlier than the end time.
      - `end` (string) (**requerido**): The end time of the shift in 24-hour format (HH:MM). Must be later than the start time.

## Ejemplo de invocación
```bash
curl -X POST '/v1/dialer/campaign' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"id": "<id>", "vendorVersion": "<vendorVersion>", "campaignType": "<campaignType>", "dialingRate": 0, "entryPointId": "<entryPointId>", "dialingListFetchURL": "<dialingListFetchURL>"}'
```

## Respuestas correctas
**202**: The campaign was started for processing.
- `data` (string) (**requerido**):
- `meta` (object) (**requerido**):
  - `orgId` (string/uuid): Organization ID used for this operation.

## Respuestas de error
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs