---
doc_id: webex-contact-center-post-flow-store-orgid-project-projectid-flows-import
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /flow-store/{orgId}/project/{projectId}/flows:import
operation_id: importFlowVersionUsingPOST
tags: Legacy Flows
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.811532+00:00
---

# POST /flow-store/{orgId}/project/{projectId}/flows:import

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Contact Center
**Área:** Legacy Flows
**operationId:** `importFlowVersionUsingPOST`

## Resumen
Import a Flow or Subflow

## Descripción
**Deprecated.** Use the Flow import endpoint (`POST /flow-store/{orgId}/project/{projectId}/v2/flows:import`, operationId `importFlowV2`) instead. The V1 Flow APIs operate on the raw FDL format and will continue to function but will not receive new features.

Returns the imported flow/subflow in response.

Scope: `cjp:config_write`. Roles: [`Organizational Full Admin`, `Supervisor`, `Contact Center Service Admin`, `User Admin`]

## Parámetros
- `Content-Length` [header] (integer/int32) (**requerido**): Content length value in number of bytes.
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `overwrite` [query] (string): Determines whether to overwrite the existing flow or not. Possible values: yes/no.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'.
- `associatedRcs` [query] (array): IDs of Resource Collections to associate with the imported flow. Por defecto: [].

## Cuerpo de la petición (multipart/form-data)
- `file` (string/binary) (**requerido**): Upload a file containing a `FlowVersionRes` object.

## Ejemplo de invocación
```bash
curl -X POST '/flow-store/<orgId>/project/<projectId>/flows:import' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"file": "<file>"}'
```

## Respuestas correctas
**201**: CREATED: Flow or Subflow is created.
- `associatedChannels` (array): Channels associated with the flow.
  - `channelType` (string): Channel type associated with the flow version.
  - `id` (string): Identifier of the associated channel.
  - `name` (string): Display name of the associated channel.
- `assignedRS` (array): Assigned Routing Strategy
- `createdBy` (string): Email of the account which created the flow
- `createdDate` (string/date-time): Date of creation of the flow
- `description` (string): Description of the flow
- `flowType` (string): Flow Type (FLOW/SUBFLOW). Default value is FLOW
- `id` (string): Flow/Subflow ID
- `lastModifiedBy` (string): Email of the account which modified the flow last
- `lastModifiedDate` (string/date-time): Date the flow object is last modified
- `lockedAt` (string/date-time): Moment at which a user began editing the flow and locked the flow for everyone else
- `lockedBy` (string): Email of the account which is currently editing the flow
- `name` (string): Name of the Flow
- `orgId` (string): Organization ID
- `status` (string): Indicates if this flow has ever been published - is one of 'Draft' or 'Published'
- `tagHistories` (object): Histories of the tags. Tracks how the tags have been assigned to versions chronologically
- `tags` (array): Tags used by the flow
  - `default` (boolean): Determines whether the tag is a default tag
  - `displayName` (string): Display name of the tag. It is one of 'Live', 'Test', 'Dev', 'Latest'
  - `flowVersionId` (string): Flow Version object ID to with which the tag is currently associated.
  - `id` (string): Identifier of the tag. It is one of 'Live', 'Test', 'Dev', 'Latest
  - `versionNumber` (integer/int32): Associated Flow Version object's version number
- `version` (integer/int32): Version Number

### Ejemplo — respuesta 201
```json
{
  "id": "65c28d9db2a2375974066579",
  "name": "TestFlow",
  "flowType": "FLOW",
  "status": "Draft",
  "orgId": "8eb7da9a-c81c-4d13-b08b-38fdeb7330d8",
  "version": 1
}
```

## Respuestas de error
- **400**: BAD REQUEST: Possible causes - Import file size exceeded the limit. File parse error. Flow name is empty. Invalid flow type. Invalid activity.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **409**: CONFLICT: A flow/subflow with the same name already exists.
- **500**: Internal Server Error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs