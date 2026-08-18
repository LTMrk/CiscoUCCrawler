---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-features-hotdesking-members
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/features/hotDesking/members
operation_id: getHotDeskingMembers
tags: Features: Hot Desking Members, User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.388315+00:00
---

# GET /telephony/config/people/{personId}/features/hotDesking/members

**API:** Webex Cloud Calling
**Área:** Features: Hot Desking Members, User Call Settings (3/3)
**operationId:** `getHotDeskingMembers`

## Resumen
Get Hot Desking Members

## Descripción
Retrieve the primary and shared-line members assigned to a person's hot desking guest profile.

This API requires a full, user, device, read-only, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization, such as partners, may use this parameter. If not specified, the organization from the OAuth token is used.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/features/hotDesking/members' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `model` (string): Name of the hot desking guest profile endpoint.
- `members` (array) (**requerido**): List of primary and shared-line members assigned to the person's hot desking guest profile.
  - `id` (string) (**requerido**): Unique identifier for the assigned member.
  - `firstName` (string): First name of the assigned member.
  - `lastName` (string): Last name of the assigned member.
  - `phoneNumber` (string): Phone number of the assigned member.
  - `extension` (string): Extension of the assigned member.
  - `routingPrefix` (string): Routing prefix of the member's location.
  - `esn` (string): Enterprise significant number for the assigned member.
  - `primaryOwner` (boolean) (**requerido**): Indicates whether this member is the hot desking guest profile owner.
  - `port` (integer) (**requerido**): Port assigned to the member.
  - `t38FaxCompressionEnabled` (boolean): T.38 fax compression setting for the member line.
  - `lineType` (string) (**requerido**): Line type for the hot desking guest profile member.  * `HOTDESKING_GUEST` - Primary hot desking guest profile line.  * `SHARED_CALL_APPEARANCE` - Shared line assigned to the hot desking guest profile.  * `PRIMARY` - Primary line.  * `MOBILITY` - Mobility line. Valores: HOTDESKING_GUEST, SHARED_CALL_APPEARANCE, PRIMARY, MOBILITY.
  - `lineWeight` (integer) (**requerido**): Number of lines configured for the member on the hot desking guest profile endpoint.
  - `hostIP` (string): Registration home IP address for the line port.
  - `remoteIP` (string): Registration remote IP address for the line port.
  - `hotlineEnabled` (boolean): Whether this line automatically calls a predefined number when taken off-hook.
  - `hotlineDestination` (string): Preconfigured number for the hotline. Required when `hotlineEnabled` is `true`.
  - `allowCallDeclineEnabled` (boolean): When enabled, a call decline request is extended to all endpoints on the line. When disabled, the call is declined only at the current endpoint.
  - `memberType` (string) (**requerido**): Type of assigned or available member.  * `PEOPLE` - The member is a person.  * `PLACE` - The member is a workspace.  * `VIRTUAL_LINE` - The member is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `location` (object): Location associated with the hot desking member.
    - `id` (string) (**requerido**): Unique identifier for the location.
    - `name` (string) (**requerido**): Name of the location.
- `maxLineCount` (integer): Maximum number of lines that can be configured on the hot desking guest profile endpoint.

### Ejemplo — respuesta 200
```json
{
  "model": "Business Communicator - PC",
  "members": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wZTQ5NjAzNC1lNTQ1LTRmMmEtODI4ZC03MjhjYjJlNjNlMWQ",
      "firstName": "Alice",
      "lastName": "Gomez",
      "phoneNumber": "+12055552220",
      "extension": "2220",
      "routingPrefix": "1234",
      "esn": "12342220",
      "primaryOwner": true,
      "port": 1,
      "lineType": "HOTDESKING_GUEST",
      "lineWeight": 1,
      "hotlineEnabled": false,
      "allowCallDeclineEnabled": true,
      "memberType": "PEOPLE",
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzJiNDkyZmZkLTRjNGItNGVmNS04YzAzLWE1MDYyYzM4NDA5Mw",
        "name": "Main Office"
      }
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS83MGY2MzYzMC1mZjlmLTExZWItODU5YS0xZjhiYjRjNzc3OGg",
      "firstName": "Support",
      "lastName": "Line",
      "phoneNumber": "+12055552222",
      "extension": "2222",
      "routingPrefix": "1234",
      "esn": "12342222",
      "primaryOwner": false,
      "port": 2,
      "lineType": "SHARED_CALL_APPEARANCE",
      "lineWeight": 1,
      "hotlineEnabled": false,
      "allowCallDeclineEnabled": true,
      "memberType": "VIRTUAL_LINE",
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzJiNDkyZmZkLTRjNGItNGVmNS04YzAzLWE1MDYyYzM4NDA5Mw",
        "name": "Main Office"
      }
    }
  ],
  "maxLineCount": 10
}
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

**Documentación adicional:** https://developer.webex.com/docs/api/v1/webex-calling

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs