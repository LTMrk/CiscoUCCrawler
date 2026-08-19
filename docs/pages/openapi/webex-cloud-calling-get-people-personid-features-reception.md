---
doc_id: webex-cloud-calling-get-people-personid-features-reception
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /people/{personId}/features/reception
operation_id: Read Receptionist Client Settings for a Person
tags: User Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.147715+00:00
---

# GET /people/{personId}/features/reception

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `Read Receptionist Client Settings for a Person`

## Resumen
Read Receptionist Client Settings for a Person

## Descripción
Retrieve a person's Receptionist Client settings.

To help support the needs of your front-office personnel, you can set up people, workspaces or virtual lines as telephone attendants so that they can screen all incoming calls to certain numbers within your organization.

This API requires a full, user, or read-only administrator or location administrator auth token with a scope of `spark-admin:people_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Ejemplo de invocación
```bash
curl -X GET '/people/<personId>/features/reception' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `receptionEnabled` (boolean) (**requerido**): Set to `true` to enable the Receptionist Client feature.
- `monitoredMembers` (array): List of people, workspaces or virtual lines to monitor.
  - `id` (string) (**requerido**): Unique identifier of the person, workspace or virtual line to be monitored.
  - `lastName` (string): Last name of the monitored person, workspace or virtual line.
  - `firstName` (string): First name of the monitored person, workspace or virtual line.
  - `displayName` (string): Display name of the monitored person, workspace or virtual line.
  - `type` (string) (**requerido**): * `PEOPLE` - Person or list of people.  * `PLACE` - Workspace that is not assigned to a specific person such as for a shared device in a common area.  * `VIRTUAL_LINE` - Virtual line or list of virtual lines. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `email` (string): Email address of the monitored person, workspace or virtual line.
  - `numbers` (array): List of phone numbers of the monitored person, workspace or virtual line.
    - `external` (string): External phone number of the monitored person, workspace or virtual line.
    - `extension` (string): Extension number of the monitored person, workspace or virtual line.
    - `routingPrefix` (string): Routing prefix of location.
    - `esn` (string): Routing prefix + extension of a person or workspace.
    - `primary` (boolean): Indicates whether phone number is a primary number.

### Ejemplo — respuesta 200
```json
{
  "receptionEnabled": true,
  "monitoredMembers": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82MWU3MDlkNy1hM2IxLTQ2MDctOTBiOC04NmE5MDgxYWFkNmE",
      "lastName": "Little",
      "firstName": "Alice",
      "displayName": "Alice Little",
      "type": "PEOPLE",
      "email": "alice@example.com",
      "location": {
        "name": "Paragville",
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzhjOWZkMjg1LTY1MDAtNDUxOC04NTZlLWViODM2YzY3NjFkOA"
      },
      "numbers": [
        {
          "external": "+19845551088",
          "extension": "1088",
          "routingPrefix": "1234",
          "esn": "12341088",
          "primary": true
        }
      ]
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jMTQzMzhkNS02YTdjLTRiZjYtOTFiMS0zYmM2ZWMzMGJiMTE",
      "lastName": "Johnson",
      "firstName": "Bob",
      "displayName": "Bob Johnson",
      "type": "PEOPLE",
      "email": "bob@example.com",
      "numbers": [
        {
          "external": "+198455501099",
          "extension": "1099",
          "routingPrefix": "1234",
          "esn": "12341099",
          "primary": true
        }
      ]
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS83MGY2MzYzMC1mZjlmLTExZWItODU5YS0xZjhiYjRjNzc3OGg",
      "lastName": "Alice",
      "firstName": "Smith",
      "displayName": "AliceSmith",
      "type": "VIRTUAL_LINE",
      "numbers": [
        {
          "external": "+19075552859",
          "extension": "8083",
          "routingPrefix": "12
  ... (truncado)
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs