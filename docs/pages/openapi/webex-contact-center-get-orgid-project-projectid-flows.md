---
doc_id: webex-contact-center-get-orgid-project-projectid-flows
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /{orgId}/project/{projectId}/flows
operation_id: findFlowsUsingGET
tags: Flows
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.804760+00:00
---

# GET /{orgId}/project/{projectId}/flows

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `findFlowsUsingGET`

## Resumen
List Flows or Subflows

## Descripción
Returns a list of flows in response. Channel-based filtering can be applied with the `searchBy` query parameter (for example, `channelType|telephony`, `channelType|workItem`, `channelType|customMessaging`, `channelType|genericAction`). Channel visibility may be constrained by organization feature flags.

Scope: `cjp:config_read`. Roles: [`Organizational Full Admin`, `Supervisor`, `Contact Center Service Admin`, `User Admin`]

## Parámetros
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'. Por defecto: FLOW.
- `ids` [query] (array): Filters results based on a comma-separated list of flow IDs. If provided, only flows with those IDs will be fetched in the response.
- `orgId` [path] (string) (**requerido**): Organization ID.
- `page` [query] (integer/int32): Defines the number of the displayed page. The page number starts from 0. Por defecto: 0.
- `partialNameSearch` [query] (string): Performs a partial string match on the name of the flow. If the flow name contains the given string it will be fetched in the response.
- `searchBy` [query] (string): Filter expression in the format `<field>|<value>`. Supports searching by `channelType` (for example, `channelType|telephony`, `channelType|workItem`, `channelType|customMessaging`, `channelType|genericAction`).
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `size` [query] (integer/int32): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 10.
- `includePagination` [query] (boolean): If set to true then a different paginated response object containing the page metadata (currentPage, totalRecords, pageSize, totalPages) will be returned. The flow objects will be in an array named "data". Por defecto: False.
- `isValidation` [query] (boolean): If true, validates the existence of flows by ID regardless of the caller's RBAC access. Intended for internal Task Management use cases. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/<orgId>/project/<projectId>/flows' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- (array de:)
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

### Ejemplo — respuesta 200
```json
[
  {
    "id": "65c28d9db2a2375974066579",
    "name": "TestFlow",
    "flowType": "FLOW",
    "status": "Draft",
    "orgId": "8eb7da9a-c81c-4d13-b08b-38fdeb7330d8",
    "version": 1
  }
]
```

## Respuestas de error
- **400**: Bad request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs