---
doc_id: webex-contact-center-get-organization-orgid-skill
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/skill
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.949128+00:00
---

# GET /organization/{orgid}/skill

**API:** Webex Contact Center
**Área:** Skill
**operationId:** `getAllConfig_2`

## Resumen
List Skill(s)

## Descripción
Retrieve a list of Skill(s) in a given organization.
 Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. Supported filterable fields:  id.   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported. except (enumSkillValues)
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.
- `singleObjectResponse` [query] (boolean): Specifiy whether to include array fields in the response, This query param should use only if the response contain single record, if we are using for multiple objects response query param not supported and throws an exception.

## Respuestas
- **200**: OK
  - (array de:)
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) **(requerido)**: Indicates the name of the skill. Once created, name cannot be modified.
    - `description` (string): Indicates the description of the skill.
    - `serviceLevelThreshold` (integer) **(requerido)**: Allows to set the time that a customer request can be in a queue before the system flags it as outside the service level.    If the agent completes a customer service request within this time interval, the system considers it within the service level.  It is required only for a create or an update operation.
    - `enumSkillValues` (array):
      - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `name` (string) **(requerido)**: Indicates the name of the enumSkillValue.
      - `description` (string): Indicates the description of the enumSkillValue.
      - `skillId` (string): Represents the skillId of the enumSkillValue.
      - `createdTime` (integer): This is the created time of the entity.
      - `lastUpdatedTime` (integer): This is the updated time of the entity.
    - `active` (boolean) **(requerido)**: Indicates the status of the skill whether it is active(when true) or not active(when false). It is required only during a create or an update operation.
    - `dynamicSkill` (boolean): Indicates whether the skill is a dynamic skill or not. Default value is false.
    - `skillType` (string) **(requerido)**: This can be of the following types  PROFICIENCY: id = 0  BOOLEAN: id = 1  TEXT: id = 2  ENUM: id = 3  Once created, skillType cannot be modified. Valores: Proficiency, Boolean, Text, enum.
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
