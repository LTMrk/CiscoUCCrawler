---
doc_id: webex-contact-center-post-organization-orgid-multimedia-profile
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/multimedia-profile
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.944451+00:00
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
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: Enter the name for the multimedia profile. Generally, use names that indicate the type of the profile, such as Default Telephony Profile.
- `description` (string): Enter a description for the multimedia profile.
- `chat` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 or 1(depends on the 'BlendingMode') to 5.
- `email` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 5.
- `telephony` (integer) **(requerido)**: Define the upper limits for this channel type. It should be either 0 or 1(depends on the 'BlendingMode').
- `social` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 5.
- `active` (boolean) **(requerido)**: Specify whether the multimedia profile is active or not.
- `blendingModeEnabled` (boolean) **(requerido)**: Specify whether the blending mode is enabled or not for a multimedia profile.
- `blendingMode` (string) **(requerido)**: Blending mode can be one the following:  BLENDED: This mode allows agents to handle multiple contacts of different channel types simultaneously. Number of contacts that you can set for Voice: 0â€“1 and for Chat, Email, and Social Channel: 0â€“5  BLENDED_REALTIME: This allows agents to handle a contact of one real-time channel at a time - either voice or chat. Along with this they can handle non-realtime contacts which include email and social channels. Number of contacts that you can set for Voice: 1 (mandatory), Chat: 1â€“5, Email and Social Channel: 0â€“5  EXCLUSIVE: This mode allows agents to focus on one customer contact at a time.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `manuallyAssignable` (object):
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `telephony` (integer) **(requerido)**: Define the upper limits for this channel type. It should be either 0 or 1.
  - `chat` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 5.
  - `email` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 10.
  - `social` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 5.
  - `createdTime` (integer): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
- `createdTime` (integer): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: Enter the name for the multimedia profile. Generally, use names that indicate the type of the profile, such as Default Telephony Profile.
  - `description` (string): Enter a description for the multimedia profile.
  - `chat` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 or 1(depends on the 'BlendingMode') to 5.
  - `email` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 5.
  - `telephony` (integer) **(requerido)**: Define the upper limits for this channel type. It should be either 0 or 1(depends on the 'BlendingMode').
  - `social` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 5.
  - `active` (boolean) **(requerido)**: Specify whether the multimedia profile is active or not.
  - `blendingModeEnabled` (boolean) **(requerido)**: Specify whether the blending mode is enabled or not for a multimedia profile.
  - `blendingMode` (string) **(requerido)**: Blending mode can be one the following:  BLENDED: This mode allows agents to handle multiple contacts of different channel types simultaneously. Number of contacts that you can set for Voice: 0â€“1 and for Chat, Email, and Social Channel: 0â€“5  BLENDED_REALTIME: This allows agents to handle a contact of one real-time channel at a time - either voice or chat. Along with this they can handle non-realtime contacts which include email and social channels. Number of contacts that you can set for Voice: 1 (mandatory), Chat: 1â€“5, Email and Social Channel: 0â€“5  EXCLUSIVE: This mode allows agents to focus on one customer contact at a time.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `manuallyAssignable` (object):
    - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `telephony` (integer) **(requerido)**: Define the upper limits for this channel type. It should be either 0 or 1.
    - `chat` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 5.
    - `email` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 10.
    - `social` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 5.
    - `createdTime` (integer): Creation time(in epoch millis) of this resource.
    - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
  - `createdTime` (integer): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
