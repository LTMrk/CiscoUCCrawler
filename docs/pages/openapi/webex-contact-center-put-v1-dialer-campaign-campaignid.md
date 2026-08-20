---
doc_id: webex-contact-center-put-v1-dialer-campaign-campaignid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PUT
path: /v1/dialer/campaign/{campaignId}
operation_id: updateCampaignRoute
tags: Campaign Manager
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.749069+00:00
---

# PUT /v1/dialer/campaign/{campaignId}

**API:** Webex Contact Center
**Área:** Campaign Manager
**operationId:** `updateCampaignRoute`

## Resumen
Update Campaign Request

## Descripción
By using an update campaign API, businesses can automate the process of modifying and managing outbound campaigns, and integrate campaign updates into their existing workflows or applications. This can help to improve efficiency and reduce errors, as well as allow for greater flexibility and control over outbound campaigns. Requires 'cjp.config_write' scope and one of the following roles: 'cjp.admin','id_full_admin','atlas-portal.partner.salesadmin','atlas-portal.partner.provision_admin' for authorization.

## Parámetros
- `campaignId` [path] (string) (**requerido**): The unique request id of the campaign that needs to be updated

## Cuerpo de la petición (application/json)
- `dialingRate` (number/float) (**requerido**): Number of contacts to be dialed out per available Agent. For Progressive 1:1 Dialer, it will support for only 1 contact and for Progressive 1:N Dialer it can support upto 10 contacts to be dialed out per available Agent
- `campaignName` (string): (Optional) Used if different than id, maximum length 64 characters.
- `authToken` (string): (Not in use) The token needed by the dialer for querying records.
- `dialingListFetchURL` (string) (**requerido**): URL the dialer will use to fetch the list of contacts to dial for the campaign from campaign manager, maximum length 1024 characters.
- `outdialANI` (string) (**requerido**): The ANI (E164)  that will be presented to the customer. These must be restricted to the configured outdial Eps in Webex Contact Center, maximum length 50 characters.
- `noAnswerRingLimit` (integer): (Optional) Number of seconds before a dialed call from the dialer is considered not answered. The range is from 16 to 80, default is 32. This field is not applicable for Direct preview campaigns.
- `maxDialingRate` (number/float): Caps the maximum dialing rate per agent at this value. The range is from 1.0 to 10.0, default is 1.0.
- `reservationPercentage` (integer): (Not in use) The percentage of agents to reserve within the queue associated with the campaign. The range is from 0 to 100 , default is 100.
- `previewOfferTimeout` (integer): (Required only if previewOfferTimeoutAutoAction is provided) The number of seconds dialer waits for an agent to act on a preview campaign record, before performing the provided previewOfferTimeoutAutoAction. The range is from 0 to 7200 seconds(2 hours) for ACCEPT auto-action, and from 10 to 7200 seconds(2 hours) for other auto-actions. The default value is 600 seconds(10 minutes).
- `previewOfferTimeoutAutoAction` (string): (Required only if previewOfferTimeout is provided) The automatic action to be performed after the previewOfferTimeout duration has elapsed, if agent takes no action on the preview campaign record offered. The action can be "ACCEPT", "SKIP" or "REMOVE". The default action is "SKIP".
- `previewActionsDisabled` (array): (Optional) The list of preview actions to be disabled for the agent when a preview campaign record is offered. The list can be empty if no action should be disabled, otherwise it can be either "SKIP" or "REMOVE" or both. The default is an empty list
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
curl -X PUT '/v1/dialer/campaign/<campaignId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"dialingRate": 0, "dialingListFetchURL": "<dialingListFetchURL>", "outdialANI": "<outdialANI>"}'
```

## Respuestas correctas
**202**: The campaign was updated successfully
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