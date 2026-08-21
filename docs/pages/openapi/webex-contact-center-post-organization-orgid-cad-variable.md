---
doc_id: webex-contact-center-post-organization-orgid-cad-variable
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/cad-variable
operation_id: createConfig_21
tags: Global Variables
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.755698+00:00
---

# POST /organization/{orgid}/cad-variable

**API:** Webex Contact Center
**Área:** Global Variables
**operationId:** `createConfig_21`

## Resumen
Create a new Global Variable

## Descripción
Create a new Global Variable in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A name for the Global Variable. Long. max: 80.
- `description` (string): A the description for the Global Variable created. Long. max: 256.
- `active` (boolean) (**requerido**): Indicates whether the Global Variable is active or not.
- `agentEditable` (boolean) (**requerido**): Indicates whether the Global Variable is editable in the Agent Desktop by the agent or not.
- `variableType` (string) (**requerido**): A valid Global Variable Type. The valid types are: String, Integer, DateTime, Boolean, Decimal. Valores: STRING, INTEGER, DATE_TIME, BOOLEAN, DECIMAL, String, Integer, DateTime, Boolean, Decimal.
- `defaultValue` (string) (**requerido**): A default value for the Global Variable. Long. max: 256.
- `reportable` (boolean) (**requerido**): Indicates whether the Global Variable is reportable or not.
- `agentViewable` (boolean) (**requerido**): Indicates whether the agent can view the Global Variable in Agent Desktop or not.
- `sensitive` (boolean): Indicates whether the Global Variable is sensitive or not.
- `desktopLabel` (string): A desktop label for the Global Variable created. Long. max: 50.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/cad-variable' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"active": true, "agentEditable": true, "agentViewable": true, "defaultValue": "<defaultValue>", "name": "<name>", "reportable": true}'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A name for the Global Variable. Long. max: 80.
- `description` (string): A the description for the Global Variable created. Long. max: 256.
- `active` (boolean) (**requerido**): Indicates whether the Global Variable is active or not.
- `agentEditable` (boolean) (**requerido**): Indicates whether the Global Variable is editable in the Agent Desktop by the agent or not.
- `variableType` (string) (**requerido**): A valid Global Variable Type. The valid types are: String, Integer, DateTime, Boolean, Decimal. Valores: STRING, INTEGER, DATE_TIME, BOOLEAN, DECIMAL, String, Integer, DateTime, Boolean, Decimal.
- `defaultValue` (string) (**requerido**): A default value for the Global Variable. Long. max: 256.
- `reportable` (boolean) (**requerido**): Indicates whether the Global Variable is reportable or not.
- `agentViewable` (boolean) (**requerido**): Indicates whether the agent can view the Global Variable in Agent Desktop or not.
- `sensitive` (boolean): Indicates whether the Global Variable is sensitive or not.
- `desktopLabel` (string): A desktop label for the Global Variable created. Long. max: 50.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
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