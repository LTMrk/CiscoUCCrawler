---
doc_id: webex-contact-center-put-organization-orgid-cad-variable-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /organization/{orgid}/cad-variable/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.943868+00:00
---

# PUT /organization/{orgid}/cad-variable/{id}

**API:** Webex Contact Center
**Área:** Global Variables
**operationId:** `updateConfig_22`

## Resumen
Update specific Global Variable by ID

## Descripción
Update an existing Global Variable by ID in a given organization. Required fields in payload are agentEditable, variableType, agentViewable, reportable, active, defaultValue.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: ID of the Global Variable.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: A name for the Global Variable.
- `description` (string): A the description for the Global Variable created.
- `active` (boolean) **(requerido)**: Indicates whether the Global Variable is active or not.
- `agentEditable` (boolean) **(requerido)**: Indicates whether the Global Variable is editable in the Agent Desktop by the agent or not.
- `variableType` (string) **(requerido)**: A valid Global Variable Type. The valid types are: String, Integer, DateTime, Boolean, Decimal. Valores: STRING, INTEGER, DATE_TIME, BOOLEAN, DECIMAL, String, Integer, DateTime, Boolean, Decimal.
- `defaultValue` (string) **(requerido)**: A default value for the Global Variable.
- `reportable` (boolean) **(requerido)**: Indicates whether the Global Variable is reportable or not.
- `agentViewable` (boolean) **(requerido)**: Indicates whether the agent can view the Global Variable in Agent Desktop or not.
- `sensitive` (boolean): Indicates whether the Global Variable is sensitive or not.
- `desktopLabel` (string): A desktop label for the Global Variable created.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the Global Variable.
  - `description` (string): A the description for the Global Variable created.
  - `active` (boolean) **(requerido)**: Indicates whether the Global Variable is active or not.
  - `agentEditable` (boolean) **(requerido)**: Indicates whether the Global Variable is editable in the Agent Desktop by the agent or not.
  - `variableType` (string) **(requerido)**: A valid Global Variable Type. The valid types are: String, Integer, DateTime, Boolean, Decimal. Valores: STRING, INTEGER, DATE_TIME, BOOLEAN, DECIMAL, String, Integer, DateTime, Boolean, Decimal.
  - `defaultValue` (string) **(requerido)**: A default value for the Global Variable.
  - `reportable` (boolean) **(requerido)**: Indicates whether the Global Variable is reportable or not.
  - `agentViewable` (boolean) **(requerido)**: Indicates whether the agent can view the Global Variable in Agent Desktop or not.
  - `sensitive` (boolean): Indicates whether the Global Variable is sensitive or not.
  - `desktopLabel` (string): A desktop label for the Global Variable created.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `createdTime` (integer): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
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
