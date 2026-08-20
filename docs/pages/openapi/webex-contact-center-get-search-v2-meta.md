---
doc_id: webex-contact-center-get-search-v2-meta
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /search/v2/meta
operation_id: getSearchMetadataV2
tags: Search Metadata
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.728556+00:00
---

# GET /search/v2/meta

**API:** Webex Contact Center
**Área:** Search Metadata
**operationId:** `getSearchMetadataV2`

## Resumen
Get Search Metadata

## Descripción
Returns schema metadata for the Webex Contact Center Search GraphQL API, describing supported queries, fields, nested structures, data types, filters, sorting options, grouping capabilities, and aggregation operations.

**Authentication & Authorization:**
- **Required Scopes:** `cjp:config` or `cjp:config_read`

An asterisk (*) in the rendered response schema indicates a required property.

## Parámetros
- `X-ORGANIZATION-ID` [header] (string/uuid): Organization ID to use for this operation. If unspecified, inferred from token. Token must have permission to interact with this organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes.

## Ejemplo de invocación
```bash
curl -X GET '/search/v2/meta' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `queries` (array) (**requerido**): Required list of GraphQL query types and their nested fields.
  - `name` (string) (**requerido**): GraphQL query or nested object field name.
  - `deprecated` (boolean) (**requerido**): Indicates whether the field is deprecated.
  - `type` (object) (**requerido**): GraphQL introspection type, including wrapped list and non-null types.
    - `name` (string): GraphQL type name when present.
    - `kind` (string) (**requerido**): GraphQL introspection type kind. Valores: SCALAR, OBJECT, INTERFACE, UNION, ENUM, INPUT_OBJECT, LIST, NON_NULL.
    - `ofType` (object): Wrapped GraphQL type for list and non-null kinds.
  - `systemField` (boolean) (**requerido**): Indicates whether the field is managed by the Search API.
  - `description` (string) (**requerido**): Description from the GraphQL schema.
  - `fields` (array) (**requerido**): Nested objects and leaf fields.
    - (uno de:)
      - (referencia circular a SearchMetadataObject)
      - `name` (string) (**requerido**): Fully qualified GraphQL field path.
      - `deprecated` (boolean) (**requerido**): Indicates whether the field is deprecated.
      - `type` (object) (**requerido**): GraphQL introspection type, including wrapped list and non-null types.
        - `name` (string): GraphQL type name when present.
        - `kind` (string) (**requerido**): GraphQL introspection type kind. Valores: SCALAR, OBJECT, INTERFACE, UNION, ENUM, INPUT_OBJECT, LIST, NON_NULL.
        - `ofType` (object): Wrapped GraphQL type for list and non-null kinds.
      - `systemField` (boolean) (**requerido**): Indicates whether the field is managed by the Search API.
      - `sortable` (boolean) (**requerido**): Indicates whether the field can be used for sorting.
      - `fieldType` (string) (**requerido**): Search data category for the field. Valores: COMMON, GRANULAR, SUMMARY.
      - `filter` (string) (**requerido**): GraphQL filter input supported by the field. Valores: filter, extFilter.
      - `groupBy` (boolean) (**requerido**): Indicates whether the field can be used for grouping.
      - `description` (string) (**requerido**): Description from the GraphQL schema.
      - `aggregation` (object) (**requerido**): Aggregation capabilities for a Search field.
        - `aggregationType` (string) (**requerido**): Aggregation data category when aggregation is supported. Valores: SUMMARY, GRANULAR.
        - `operations` (array) (**requerido**): Supported aggregation operations.

### Ejemplo — respuesta 200
```json
{
  "queries": [
    {
      "name": "task",
      "deprecated": false,
      "type": {
        "name": "Task",
        "kind": "OBJECT"
      },
      "systemField": false,
      "description": "Represents the customer workflow for a contact session or a task.",
      "fields": [
        {
          "name": "id",
          "deprecated": false,
          "type": {
            "name": "String",
            "kind": "SCALAR"
          },
          "systemField": false,
          "sortable": true,
          "fieldType": "SUMMARY",
          "filter": "filter",
          "groupBy": true,
          "description": "ID of the task.",
          "aggregation": {
            "aggregationType": "SUMMARY",
            "operations": [
              "count",
              "cardinality"
            ]
          }
        }
      ]
    }
  ]
}
```

## Respuestas de error
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden
- **500**: An Unexpected Error Occurred
- **503**: The service is currently unavailable to serve the requests

**Documentación adicional:** https://developer.webex.com/docs/getting-started-with-search-api

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs