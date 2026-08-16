---
doc_id: webex-contact-center-post-organization-orgid-cad-variable-bulk
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/cad-variable/bulk
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.943358+00:00
---

# POST /organization/{orgid}/cad-variable/bulk

**API:** Webex Contact Center
**Área:** Global Variables
**operationId:** `saveAllConfig_18`

## Resumen
Bulk save Global Variable(s)

## Descripción
Export all Global Variable(s) in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `items` (array):
  - `itemIdentifier` (integer): Unique item identifier for a bulk operation.
  - `item` (object):
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
  - `requestAction` (string): Identifier for action type. Possible values can be SAVE and DELETE.

## Respuestas
- **207**: Multi-Status
  - `items` (array):
    - `itemIdentifier` (integer): Unique item identifier for a bulk operation.
    - `status` (integer): Indicates the error status code.
    - `operationType` (string): The kind of operation desired of an entity. Valores: CREATE, UPDATE, DELETE, GET.
    - `href` (string): The resource URI of an entity.
    - `apiError` (object): Response body for an API error.
      - `trackingId` (string): An opaque identifier for mapping protocol failures to service internal codes.   When specified in a request, it can be used for co-relating events across services
      - `error` (object): Details of an error.
        - `key` (string): An application defined error code.
        - `message` (array): A message providing details about the error.
          - `description` (string): A human readable explanation for the occurrence of an error.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
