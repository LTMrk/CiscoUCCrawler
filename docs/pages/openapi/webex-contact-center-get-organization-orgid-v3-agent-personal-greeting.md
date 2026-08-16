---
doc_id: webex-contact-center-get-organization-orgid-v3-agent-personal-greeting
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/v3/agent-personal-greeting
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.930907+00:00
---

# GET /organization/{orgid}/v3/agent-personal-greeting

**API:** Webex Contact Center
**Área:** Agent Personal Greeting Files
**operationId:** `getAllV2ConfigWithMetaDataAgentPersonalGreeting`

## Resumen
List Greeting Files

## Descripción
Retrieve a list of Greeting Files in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. Supported fields are: firstName, lastName, email, ciUserId, and attributeTag.  The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(firstName, lastName, email, attributeTag)  The examples below show some search queries - "Cisco" - field=="firstName";value=="Cisco" - fields=in=("firstName","email");value=="Cisco"
- `attributes` [query] (string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.
- `includeAgentDetails` [query] (boolean): If includeAgentDetails is set to true, projection, filtering, searching, and sorting on the agent's firstName, lastName, and email will be enabled.

## Respuestas
- **200**: OK
  - `meta` (object): Metadata of response with paging information
    - `orgid` (string): Organization ID.
    - `page` (integer): Current page number.
    - `pageSize` (integer): Page size for current data set.
    - `totalPages` (integer): Number of pages.
    - `totalRecords` (integer): Total number of items.
    - `links` (object): Map of pagination links with `self`, `next`, `prev`, `last`, and `first`.
  - `data` (array):
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) **(requerido)**: A name for the Agent's personal greeting file. It should have valid extension i.e. .wav
    - `contentType` (string) **(requerido)**: Indicates Content-Type of the Audio file. It can take one of these values: AUDIO_WAV, AUDIO_X_WAV Valores: AUDIO_WAV, TEXT_HTML, TEXT_PHP, AUDIO_X_WAV, APPLICATION_OCTET_STREAM.
    - `blobId` (string): Identifier for the audio file.
    - `url` (string): Audio file download url.
    - `agentId` (string) **(requerido)**: Agent Id with which this greeting file is to be associated with.
    - `firstName` (string): First Name of the Agent with whom this greeting file is to be associated with.
    - `lastName` (string): Last Name of the Agent with whom this greeting file is to be associated with.
    - `email` (string): Email of the Agent with whom this greeting file is to be associated with.
    - `agentActive` (boolean): Indicates whether the Agent with whom this greeting file is to be associated with is active or not active
    - `ciUserId` (string): Id of the Agent in common identity with whom this greeting file is to be associated with.
    - `greetingPurposeId` (string): Id of the greeting purpose
    - `greetingPurposeName` (string): Name of the greeting purpose
    - `audioFile` (string): Audio File.
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
