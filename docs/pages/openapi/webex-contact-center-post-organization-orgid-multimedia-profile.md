---
doc_id: webex-contact-center-post-organization-orgid-multimedia-profile
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/multimedia-profile
operation_id: createConfig_11
tags: Multimedia Profile
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.704525+00:00
---

# POST /organization/{orgid}/multimedia-profile

**API:** Webex Contact Center
**Área:** Multimedia Profile
**operationId:** `createConfig_11`

## Resumen
Create a new Multimedia Profile

## Descripción
Create a new Multimedia Profile in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Enter the name for the multimedia profile. Generally, use names that indicate the type of the profile, such as Default Telephony Profile. Long. max: 80.
- `description` (string): Enter a description for the multimedia profile. Long. max: 255.
- `chat` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 or 1(depends on the 'BlendingMode') to 5.
- `email` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 5.
- `telephony` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should be either 0 or 1(depends on the 'BlendingMode').
- `social` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 5.
- `active` (boolean) (**requerido**): Specify whether the multimedia profile is active or not.
- `blendingModeEnabled` (boolean) (**requerido**): Specify whether the blending mode is enabled or not for a multimedia profile.
- `blendingMode` (string) (**requerido**): Blending mode can be one the following:  BLENDED: This mode allows agents to handle multiple contacts of different channel types simultaneously. Number of contacts that you can set for Voice: 0â€“1 and for Chat, Email, and Social Channel: 0â€“5  BLENDED_REALTIME: This allows agents to handle a contact of one real-time channel at a time - either voice or chat. Along with this they can handle non-realtime contacts which include email and social channels. Number of contacts that you can set for Voice: 1 (mandatory), Chat: 1â€“5, Email and Social Channel: 0â€“5  EXCLUSIVE: This mode allows agents to focus on one customer contact at a time.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `manuallyAssignable` (object):
  - `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `telephony` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should be either 0 or 1.
  - `chat` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 5.
  - `email` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 10.
  - `social` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 5.
  - `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.
- `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/multimedia-profile' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"active": true, "blendingMode": "<blendingMode>", "blendingModeEnabled": true, "chat": 0, "email": 0, "name": "<name>"}'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Enter the name for the multimedia profile. Generally, use names that indicate the type of the profile, such as Default Telephony Profile. Long. max: 80.
- `description` (string): Enter a description for the multimedia profile. Long. max: 255.
- `chat` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 or 1(depends on the 'BlendingMode') to 5.
- `email` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 5.
- `telephony` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should be either 0 or 1(depends on the 'BlendingMode').
- `social` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 5.
- `active` (boolean) (**requerido**): Specify whether the multimedia profile is active or not.
- `blendingModeEnabled` (boolean) (**requerido**): Specify whether the blending mode is enabled or not for a multimedia profile.
- `blendingMode` (string) (**requerido**): Blending mode can be one the following:  BLENDED: This mode allows agents to handle multiple contacts of different channel types simultaneously. Number of contacts that you can set for Voice: 0â€“1 and for Chat, Email, and Social Channel: 0â€“5  BLENDED_REALTIME: This allows agents to handle a contact of one real-time channel at a time - either voice or chat. Along with this they can handle non-realtime contacts which include email and social channels. Number of contacts that you can set for Voice: 1 (mandatory), Chat: 1â€“5, Email and Social Channel: 0â€“5  EXCLUSIVE: This mode allows agents to focus on one customer contact at a time.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `manuallyAssignable` (object):
  - `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `telephony` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should be either 0 or 1.
  - `chat` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 5.
  - `email` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 10.
  - `social` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 5.
  - `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.
- `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.

## Respuestas de error
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs