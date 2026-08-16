---
doc_id: webex-contact-center-put-organization-orgid-dial-plan-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /organization/{orgid}/dial-plan/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.941486+00:00
---

# PUT /organization/{orgid}/dial-plan/{id}

**API:** Webex Contact Center
**Área:** Dial Plan
**operationId:** `updateConfigDialPlan`

## Resumen
Update specific Dial Plan by ID

## Descripción
Update an existing Dial Plan by ID in a given organization.

**Deprecated:** Dial Plan configuration is deprecated. Dial Plan is no longer available as an Agent Profile setting, so agents can no longer  use them for agent dial number validation.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Dial Plan.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: Enter the name for the dial plan.
- `description` (string): A short description of the dial plan.
- `regularExpression` (string) **(requerido)**: A regular expression specifies the format of the phone number and the characters that you can use while dialing a number.
- `prefix` (string): (Optional) Enter a prefix that the system automatically adds to the phone number that the agent enters. For example, digit 1 for long-distance calls within the United States.
- `strippedChars` (string): Enter the characters that system removes from the phone number that the agent dials.For example, left and right parentheses, space, and hyphen.
- `active` (boolean) **(requerido)**: Specify whether the dial plan is active or not
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer): This is the created time of the entity.
- `lastUpdatedTime` (integer): This is the updated time of the entity.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: Enter the name for the dial plan.
  - `description` (string): A short description of the dial plan.
  - `regularExpression` (string) **(requerido)**: A regular expression specifies the format of the phone number and the characters that you can use while dialing a number.
  - `prefix` (string): (Optional) Enter a prefix that the system automatically adds to the phone number that the agent enters. For example, digit 1 for long-distance calls within the United States.
  - `strippedChars` (string): Enter the characters that system removes from the phone number that the agent dials.For example, left and right parentheses, space, and hyphen.
  - `active` (boolean) **(requerido)**: Specify whether the dial plan is active or not
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
