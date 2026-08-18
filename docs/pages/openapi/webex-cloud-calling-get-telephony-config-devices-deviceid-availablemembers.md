---
doc_id: webex-cloud-calling-get-telephony-config-devices-deviceid-availablemembers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/devices/{deviceId}/availableMembers
operation_id: searchMembers
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.259408+00:00
---

# GET /telephony/config/devices/{deviceId}/availableMembers

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `searchMembers`

## Resumen
Search Members

## Descripción
Search members that can be assigned to the device.

A device member can be either a person or a workspace. A admin can access the list of member details, modify member details and
search for available members on a device.

This requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `deviceId` [path] (string) (**requerido**): Unique identifier for the device.
- `orgId` [query] (string): Retrieves the list of available members on the device in this organization.
- `start` [query] (number): Specifies the offset from the first result that you want to fetch.
- `max` [query] (number): Specifies the maximum number of records that you want to fetch. Por defecto: 2000.
- `memberName` [query] (string): Search (Contains) numbers based on member name.
- `phoneNumber` [query] (string): Search (Contains) based on number.
- `locationId` [query] (string): Unique identifier for the location.
- `extension` [query] (string): Search (Contains) based on extension.
- `usageType` [query] (string): Search for members eligible to become the owner of the device, or share line on the device. Valores: DEVICE_OWNER, SHARED_LINE.
- `order` [query] (string): Sort the list of available members on the device in ascending order by name, use either last name `lname` or first name `fname`. Default: last name in ascending order.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/devices/<deviceId>/availableMembers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `members` (array): List of members available for the device.
  - `id` (string) (**requerido**): Unique identifier for the member.
  - `firstName` (string): First name of a person or workspace.
  - `lastName` (string): Last name of a person or workspace.
  - `phoneNumber` (string): Phone Number of a person or workspace.
  - `t38FaxCompressionEnabled` (boolean): T.38 Fax Compression setting and available only for ATA Devices. Choose T.38 fax compression if the device requires this option. this will override user level compression options.
  - `lineType` (string) (**requerido**): * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
  - `allowCallDeclineEnabled` (boolean) (**requerido**): Set how a person's device behaves when a call is declined. When set to true, a call decline request is extended to all the endpoints on the device. When set to false, a call decline request only declines the current endpoint.
  - `memberType` (string) (**requerido**): * `PEOPLE` - Indicates the associated member is a person.  * `PLACE` - Indicates the associated member is a workspace. Valores: PEOPLE, PLACE.
  - `location` (object):
    - `id` (string) (**requerido**): Location identifier associated with the members.
    - `name` (string) (**requerido**): Location name associated with the member.

### Ejemplo — respuesta 200
```json
{
  "members": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMjk",
      "firstName": "John",
      "lastName": "Smith",
      "phoneNumber": "+12055552221",
      "t38FaxCompressionEnabled": false,
      "lineType": "SHARED_CALL_APPEARANCE",
      "allowCallDeclineEnabled": true,
      "memberType": "PEOPLE",
      "location": {
        "name": "MainOffice",
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzJiNDkyZmZkLTRjNGItNGVmNS04YzAzLWE1MDYyYzM4NDA5Mw"
      }
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMjk",
      "firstName": "Bob",
      "lastName": "Smith-ws",
      "phoneNumber": "+12055552221",
      "t38FaxCompressionEnabled": false,
      "lineType": "SHARED_CALL_APPEARANCE",
      "allowCallDeclineEnabled": true,
      "memberType": "PLACE",
      "location": {
        "name": "MainOffice",
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzJiNDkyZmZkLTRjNGItNGVmNS04YzAzLWE1MDYyYzM4NDA5Mw"
      }
    }
  ]
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs