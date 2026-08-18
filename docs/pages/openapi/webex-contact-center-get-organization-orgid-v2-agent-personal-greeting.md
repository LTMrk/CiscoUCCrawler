---
doc_id: webex-contact-center-get-organization-orgid-v2-agent-personal-greeting
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v2/agent-personal-greeting
operation_id: getAllConfigWithMetaDataAgentPersonalGreeting
tags: Agent Personal Greeting Files
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.774026+00:00
---

# GET /organization/{orgid}/v2/agent-personal-greeting

**API:** Webex Contact Center
**Área:** Agent Personal Greeting Files
**operationId:** `getAllConfigWithMetaDataAgentPersonalGreeting`

## Resumen
List Greeting Files

## Descripción
Retrieve a list of Greeting Files in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. Supported fields are: firstName, lastName, email, ciUserId, and attributeTag.  The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(firstName, lastName, email, attributeTag)  The examples below show some search queries - "Cisco" - field=="firstName";value=="Cisco" - fields=in=("firstName","email");value=="Cisco"
- `attributes` [query] (string/string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `includeAgentDetails` [query] (boolean): If includeAgentDetails is set to true, projection, filtering, searching, and sorting on the agent's firstName, lastName, and email will be enabled. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v2/agent-personal-greeting' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object): Metadata of response with paging information
  - `orgid` (string/uuid): Organization ID. Long. max: 36.
  - `page` (integer/int32): Current page number.
  - `pageSize` (integer/int32): Page size for current data set.
  - `totalPages` (integer/int32): Number of pages.
  - `totalRecords` (integer/int32): Total number of items.
  - `links` (object): Map of pagination links with `self`, `next`, `prev`, `last`, and `first`.
- `data` (array):
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) (**requerido**): A name for the Agent's personal greeting file. It should have valid extension i.e. .wav Long. max: 80.
  - `contentType` (string) (**requerido**): Indicates Content-Type of the Audio file. It can take one of these values: AUDIO_WAV, AUDIO_X_WAV Valores: AUDIO_WAV, TEXT_HTML, TEXT_PHP, AUDIO_X_WAV, APPLICATION_OCTET_STREAM.
  - `blobId` (string): Identifier for the audio file.
  - `url` (string/url): Audio file download url.
  - `agentId` (string) (**requerido**): Agent Id with which this greeting file is to be associated with.
  - `attributeTag` (string): This is used to identify the purpose of a greeting. Long. max: 80.
  - `firstName` (string): First Name of the Agent with whom this greeting file is to be associated with.
  - `lastName` (string): Last Name of the Agent with whom this greeting file is to be associated with.
  - `email` (string): Email of the Agent with whom this greeting file is to be associated with.
  - `agentActive` (boolean): Indicates whether the Agent with whom this greeting file is to be associated with is active or not active
  - `ciUserId` (string): Id of the Agent in common identity with whom this greeting file is to be associated with.
  - `audioFile` (string/binary): Audio File.
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

## Respuestas de error
- **401**: Unauthorized Operation
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "401",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "401",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **403**: Operation is forbidden
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "403",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "403",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **404**: Resource not found or URI is invalid
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "404",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "404",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "429",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "429",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **500**: An Unexpected Error Occurred
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "500",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "500",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs