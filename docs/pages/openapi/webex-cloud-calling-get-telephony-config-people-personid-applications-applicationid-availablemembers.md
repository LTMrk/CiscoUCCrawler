---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-applications-applicationid-availablemembers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/applications/{applicationId}/availableMembers
operation_id: searchSharedLineAppearanceMembers
tags: User Call Settings (2/2)
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.764530+00:00
---

# GET /telephony/config/people/{personId}/applications/{applicationId}/availableMembers

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `searchSharedLineAppearanceMembers`

## Resumen
Search Shared-Line Appearance Members

## Descripción
Retrieve members available for shared-line assignment to a Webex Calling Apps Desktop device.

This API requires a full, user, or location administrator auth token with the `spark-admin:people_read` scope.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `applicationId` [path] (string) (**requerido**): Unique identifier for the application.
- `max` [query] (number): Number of records per page.
- `start` [query] (number): Page number.
- `location` [query] (string): Location ID for the user.
- `name` [query] (string): Search for users whose names match the query.
- `number` [query] (string): Search for users whose numbers match the query.
- `order` [query] (string): Sort by first name (`fname`) or last name (`lname`).
- `extension` [query] (string): Search for users whose extensions match the query.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/applications/<applicationId>/availableMembers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `members` (array):
  - `id` (string) (**requerido**): Unique identifier for the member.
  - `firstName` (string): First name of the member.
  - `lastName` (string): Last name of the member.
  - `phoneNumber` (string): Phone number of the member. Currently, E.164 format is not supported.
  - `extension` (string): Phone extension of the member.
  - `routingPrefix` (string): Routing prefix of the location.
  - `esn` (string): Routing prefix plus extension of a person or workspace.
  - `lineType` (string) (**requerido**): * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
  - `location` (object):
    - `id` (string) (**requerido**): Location identifier associated with the members.
    - `name` (string) (**requerido**): Location name associated with the member.

### Ejemplo — respuesta 200
```json
{
  "members": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85ODhiYTQyOC0zMjMyLTRmNjItYjUyNS1iZDUzZmI4Nzc0MWE",
      "firstName": "John",
      "lastName": "Doe",
      "phoneNumber": "+1234567890",
      "extension": "0000",
      "routingPrefix": "1234",
      "esn": "12340000",
      "lineType": "SHARED_CALL_APPEARANCE",
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzJiNDkyZmZkLTRjNGItNGVmNS04YzAzLWE1MDYyYzM4NDA5Mw",
        "name": "MainOffice"
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