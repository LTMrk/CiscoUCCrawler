---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-applications-applicationid-members
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/applications/{applicationId}/members
operation_id: getSharedLineAppearanceMembers
tags: User Call Settings (2/2)
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.374221+00:00
---

# GET /telephony/config/people/{personId}/applications/{applicationId}/members

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getSharedLineAppearanceMembers`

## Resumen
Get Shared-Line Appearance Members

## Descripción
Retrieve primary and secondary members assigned to a shared line on a Webex Calling Apps Desktop device.

This API requires a full, user, or location administrator auth token with the `spark-admin:people_read` scope.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `applicationId` [path] (string) (**requerido**): Unique identifier for the application.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/applications/<applicationId>/members' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `model` (string) (**requerido**): Model name of device.
- `members` (array): List of members.
  - `id` (string) (**requerido**): Unique identifier for the member.
  - `firstName` (string): First name of the person or workspace.
  - `lastName` (string): Last name of the person or workspace.
  - `phoneNumber` (string): Phone number of the person or workspace. Currently, E.164 format is not supported. This will be supported in a future update.
  - `extension` (string): Phone extension of the person or workspace.
  - `routingPrefix` (string): Routing prefix of the location.
  - `esn` (string): Routing prefix plus extension of a person or workspace.
  - `port` (number) (**requerido**): Device port number assigned to the person or workspace.
  - `t38FaxCompressionEnabled `true`` (boolean): T.38 Fax Compression setting. Valid only for ATA Devices. Overrides user-level compression options.
  - `primaryOwner` (string) (**requerido**): If `true`, the person or workspace is the owner of the device. Points to the primary line/port of the device.
  - `lineType` (string) (**requerido**): * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
  - `lineWeight` (number) (**requerido**): Number of lines that have been configured for the person on the device.
  - `hostIP` (string): Registration home IP for the line port.
  - `remoteIP` (string): Registration remote IP for the line port.
  - `hotlineEnabled` (boolean) (**requerido**): Configure this line to automatically call a predefined number whenever taken off-hook. Once enabled, the line can only make calls to the predefined number set in `hotlineDestination`.
  - `hotlineDestination` (string) (**requerido**): Preconfigured number for the hotline. Required only if `hotlineEnabled` is set to `true`.
  - `allowCallDeclineEnabled` (boolean) (**requerido**): Set how a device behaves when a call is declined. When set to `true`, a call decline request is extended to all endpoints on the device. When set to `false`, a call decline request is only declined at the current endpoint.
  - `lineLabel` (string): Device line label.
  - `memberType` (string) (**requerido**): * `PEOPLE` - The associated member is a person.  * `PLACE` - The associated member is a workspace.  * `VIRTUAL_LINE` - The associated member is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `location` (object):
    - `id` (string) (**requerido**): Location identifier associated with the members.
    - `name` (string) (**requerido**): Location name associated with the member.
- `maxLineCount` (number) (**requerido**): Maximum number of device ports.

### Ejemplo — respuesta 200
```json
{
  "model": "Business Communicator - PC",
  "members": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85ODhiYTQyOC0zMjMyLTRmNjItYjUyNS1iZDUzZmI4Nzc0MWE",
      "firstName": "John",
      "lastName": "Doe",
      "phoneNumber": "+2056852221",
      "extension": "1111",
      "routingPrefix": "1234",
      "esn": "12341111",
      "port": 1,
      "primaryOwner": "true",
      "lineType": "SHARED_CALL_APPEARANCE",
      "lineWeight": 1,
      "hostIP": "198.168.0.1",
      "remoteIP": "198.168.0.2",
      "hotlineEnabled": true,
      "hotlineDestination": "1234",
      "allowCallDeclineEnabled": true,
      "lineLabel": "share line label",
      "memberType": "PEOPLE",
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzJiNDkyZmZkLTRjNGItNGVmNS04YzAzLWE1MDYyYzM4NDA5Mw",
        "name": "MainOffice"
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs