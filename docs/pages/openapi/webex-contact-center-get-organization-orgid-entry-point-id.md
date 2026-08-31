---
doc_id: webex-contact-center-get-organization-orgid-entry-point-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/entry-point/{id}
operation_id: getConfig_15
tags: Entry Point
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.701380+00:00
---

# GET /organization/{orgid}/entry-point/{id}

**API:** Webex Contact Center
**Área:** Entry Point
**operationId:** `getConfig_15`

## Resumen
Get specific Entry Point by ID

## Descripción
Retrieve an existing Entry Point by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the Entry Point.
- `includeNames` [query] (boolean): Specifiy whether to include flow override settings reference variable names. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/entry-point/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A unique name for the entry point within the organization. It is required only during a create or an update operation. Long. max: 80.
- `description` (string): A short description of the entry point. Long. max: 255.
- `entryPointType` (string) (**requerido**): Setting to indicate if this entry point is meant for incoming or outgoing contacts. Use uppercase. Can be set to either `INBOUND` or `OUTBOUND`. With Outbound Type, Only Telephony channel is supported. It is required only during a create or an update operation. Valores: INBOUND, OUTBOUND.
- `channelType` (string) (**requerido**): Setting to indicate the channel type. Use uppercase. Supported channel types are:    TELEPHONY, EMAIL, VIDEO, SOCIAL_CHANNEL, FAX, CHAT and OTHERS.  It is required only during a create or an update operation. Valores: TELEPHONY, EMAIL, FAX, CHAT, VIDEO, OTHERS, SOCIAL_CHANNEL.
- `socialChannelType` (string) (**requerido**): Setting to indicate the type of Social Channel.This setting is available only when channel type is SOCIAL_CHANNEL.Use uppercase. Can be set to either `MESSAGEBIRD` or `MESSENGER`. Valores: MESSAGEBIRD, MESSENGER, WHATSAPP, APPLE_BUSINESS_CHAT, GOOGLE_BUSINESS_MESSAGES.
- `active` (boolean) (**requerido**): Used to toggle the state of the entrypoint from active to inactive and vice-versa. It is required only during a create or an update operation.
- `serviceLevelThreshold` (integer/int32) (**requerido**): Allows to set the time that a customer request can be in a queue before the system flags it as outside the service level.    If the agent completes a customer service request within this time interval, the system considers it within the service level.  It is required only for a create or an update operation.
- `maximumActiveContacts` (integer/int32) (**requerido**): Caps the maximum number of simultaneous calls for this entry point.  The system busies out any additional calls when the number of active calls exceeds this number.  It is required only for a create or an update operation.
- `controlFlowScriptUrl` (string) (**requerido**): The system automatically populates this field with the URL for this entry point or the default control script of the queue.It happens when you don’t configure the control script using the Webex Contact Center Routing Strategy module.This setting is available for the Telephony channel type.
- `overflowNumber` (string) (**requerido**): Allows to set the destination phone number to which the system diverts the customer calls when they exceed the Maximum Time in Queue   that has been set in the routing strategy.  This setting is applicable only for the Telephony channel type. Long. max: 40.
- `timezone` (string): (Optional) Any routing strategy for this entry point uses the time zone that you select here.
- `imiOrgType` (string) (**requerido**): Refers to the type of digital channels used by the org. It takes two values: IMI (if all channels used are IMI) and MIXED_MODE (if both native and IMI channels are used). Valores: MIXED_MODE, IMI.
- `assetId` (string) (**requerido**): ID of the asset in IMI that corresponds to this entrypoint.
- `xspVersion` (string): (Optional) Used to subscribe for recording events. Long. max: 80.
- `subscriptionId` (string): (Optional) Used to subscribe for recording events. Long. max: 80.
- `routePointId` (string): The identifier of a route point of WxC which is similar to entry point of WxCC
- `flowId` (string):
- `flowTagId` (string):
- `musicOnHoldId` (string):
- `outdialQueueId` (string):
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `callbackEnabled` (boolean): Indicates whether the created resource is call back enabled or not
- `outdialTransferToQueueEnabled` (boolean): Indicates whether the resource is Default Outdial Transfer to Queue.
- `dnEpMappingCount` (integer/int64):
- `flowOverrideSettings` (array): Add a Flow override settings to entry-point. This feature enables non-flow developers and designers including Contact Center Supervisors and other Contact Center personnel to modify settings such as business hours and audio prompts within Control Hub using configurable parameters, bypassing the complexity of flow editing. Note that flow override settings are applicable only for telephony entry-point.
  - `name` (string) (**requerido**):
  - `type` (string) (**requerido**):
  - `entityType` (string):
  - `entityId` (string):
  - `value` (string):
- `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.

## Respuestas de error
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs