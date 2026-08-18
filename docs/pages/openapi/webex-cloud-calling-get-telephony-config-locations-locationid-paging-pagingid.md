---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-paging-pagingid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/paging/{pagingId}
operation_id: Get Details for a Paging Group
tags: Features:  Paging Group
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.325065+00:00
---

# GET /telephony/config/locations/{locationId}/paging/{pagingId}

**API:** Webex Cloud Calling
**Área:** Features:  Paging Group
**operationId:** `Get Details for a Paging Group`

## Resumen
Get Details for a Paging Group

## Descripción
Retrieve Paging Group details.

Group Paging allows a person, place or virtual line a one-way call or group page to up to 75 people and/or workspaces and/or virtual line by
dialing a number or extension assigned to a specific paging group. The Group Paging service makes a simultaneous call to all the assigned targets.

Retrieving paging group details requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve settings for a paging group in this location.
- `pagingId` [path] (string) (**requerido**): Retrieve settings for the paging group with this identifier.
- `orgId` [query] (string): Retrieve paging group settings from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/paging/<pagingId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for the paging group.
- `enabled` (boolean) (**requerido**): Whether or not the paging group is enabled.
- `name` (string) (**requerido**): Unique name for the paging group. Minimum length is 1. Maximum length is 30.
- `phoneNumber` (string): Paging group phone number. Minimum length is 1. Maximum length is 23. Either `phoneNumber` or `extension` is mandatory.
- `extension` (string): Paging group extension. Minimum length is 2. Maximum length is 10. Either `phoneNumber` or `extension` is mandatory.
- `tollFreeNumber` (boolean): Flag to indicate toll free number.
- `language` (string) (**requerido**): Paging language. Minimum length is 1. Maximum length is 40.
- `languageCode` (string) (**requerido**): Language code.
- `firstName` (string): First name that displays when a group page is performed. Minimum length is 1. Maximum length is 64. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name that displays when a group page is performed. Minimum length is 1. Maximum length is 64. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `originatorCallerIdEnabled` (boolean) (**requerido**): Determines what is shown on target users caller ID when a group page is performed. If true shows page originator ID.
- `originators` (array): An array of people, workspaces and virtual lines ID's who may originate pages to this paging group.
  - `id` (string) (**requerido**): Agents ID.
  - `firstName` (string): Agent's first name. Minimum length is 1. Maximum length is 64.
  - `lastName` (string): Agent's last name. Minimum length is 1. Maximum length is 64.
  - `type` (string) (**requerido**): Type of the person, workspace or virtual line.  * `PEOPLE` - Indicates that this object is a person.  * `PLACE` - Indicates that this object is a workspace, formerly known as a place.  * `VIRTUAL_LINE` - Indicates that this object is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `phoneNumber` (string): Agent's phone number. Minimum length is 1. Maximum length is 23. Either phoneNumber or extension is mandatory.
  - `extension` (string): Agent's extension. Minimum length is 2. Maximum length is 10. Either phoneNumber or extension is mandatory.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person or workspace.
- `targets` (array): An array of people, workspaces and virtual lines ID's that are added to paging group as paging call targets.
  - `id` (string) (**requerido**): Agents ID.
  - `firstName` (string): Agent's first name. Minimum length is 1. Maximum length is 64.
  - `lastName` (string): Agent's last name. Minimum length is 1. Maximum length is 64.
  - `type` (string) (**requerido**): Type of the person, workspace or virtual line.  * `PEOPLE` - Indicates that this object is a person.  * `PLACE` - Indicates that this object is a workspace, formerly known as a place.  * `VIRTUAL_LINE` - Indicates that this object is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `phoneNumber` (string): Agent's phone number. Minimum length is 1. Maximum length is 23. Either phoneNumber or extension is mandatory.
  - `extension` (string): Agent's extension. Minimum length is 2. Maximum length is 10. Either phoneNumber or extension is mandatory.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person or workspace.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this workspace.
  - `selection` (string): * `DISPLAY_NAME` - When this option is selected, `displayName` is to be shown for this workspace.  * `CUSTOM_NAME` - When this option is selected, `customName` is to be shown for this workspace. Valores: CUSTOM_NAME, DISPLAY_NAME.
  - `customName` (string): The custom direct line caller ID name. Required if `selection` is set to `CUSTOM_NAME`.
- `dialByName` (string): The name to be used for dial by name functions.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1BBR0lOR19HUk9VUC9hSFpoWlROMk1HOHliMEEyTkRrME1USTVOeTVwYm5ReE1DNWlZMnhrTG5kbFltVjRMbU52YlE",
  "enabled": true,
  "name": "PagingGroup-1",
  "phoneNumber": "+15558675309",
  "extension": "7781",
  "language": "English",
  "languageCode": "en_us",
  "firstName": "John",
  "lastName": "Doe",
  "originatorCallerIdEnabled": true,
  "originators": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YTc2ZmVmNC1mZjlmLTExZWItYWYwZC00M2YwZjY1NTdjYWI",
      "firstName": "John",
      "lastName": "Doe",
      "type": "PEOPLE",
      "phoneNumber": "+15558675310",
      "extension": "7781",
      "routingPrefix": "567",
      "esn": "5677781"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS83MGY2MzYzMC1mZjlmLTExZWItODU5YS0xZjhiYjRjNzc3OGg=",
      "firstName": "Alice",
      "lastName": "Smith",
      "type": "VIRTUAL_LINE",
      "phoneNumber": "+15558675311",
      "extension": "7782",
      "routingPrefix": "567",
      "esn": "5677781"
    }
  ],
  "targets": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BMQUNFLzg0YjQ1OTIyLWZmOWYtMTFlYi1hNGI4LTMzNjI3YmVkNjdiNQ",
      "firstName": "Alaska Office",
      "lastName": "Second Floor",
      "type": "PLACE",
      "phoneNumber": "+15558675311",
      "extension": "7781",
      "routingPrefix": "567",
      "esn": "5677781"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS83MGY2MzYzMC1mZjlmLTExZWItODU5YS0xZjhiYjRjNzc3OGg=",
      "firstName": "Alice",
      "lastName": "Smith",

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