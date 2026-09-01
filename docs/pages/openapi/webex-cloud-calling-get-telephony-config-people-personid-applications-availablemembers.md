---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-applications-availablemembers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/applications/availableMembers
operation_id: searchSharedLineAppearanceMembersNew
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.773591+00:00
---

# GET /telephony/config/people/{personId}/applications/availableMembers

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `searchSharedLineAppearanceMembersNew`

## Resumen
Search Shared-Line Appearance Members New

## Descripción
Get members available for shared-line assignment to a Webex Calling Apps.

Like most hardware devices, applications support assigning additional shared lines which can monitored and utilized by the application.

This API requires a full, user, or location administrator auth token with the `spark-admin:telephony_config_read` scope.

## Parámetros
- `personId` [path] (string) (**requerido**): A unique identifier for the person.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `order` [query] (string): Order the Route Lists according to number, ascending or descending.
- `location` [query] (string): Location ID for the user.
- `name` [query] (string): Search for users with names that match the query.
- `phoneNumber` [query] (string): Search for users with numbers that match the query.
- `extension` [query] (string): Search for users with extensions that match the query.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/applications/availableMembers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `members` (array): List of members available for shared-line assignment to a Webex Calling Apps.
  - `id` (string) (**requerido**): A unique member identifier.
  - `firstName` (string) (**requerido**): First name of member.
  - `lastName` (string) (**requerido**): Last name of member.
  - `phoneNumber` (string): Phone number of member. Currently, E.164 format is not supported.
  - `extension` (string): Phone extension of member.
  - `lineType` (string) (**requerido**): * `PRIMARY` - Primary line for the member.  * `SHARED_CALL_APPEARANCE` - Shared line for the member. A shared line allows users to receive and place calls to and from another user's extension, using their own device. Valores: PRIMARY, SHARED_CALL_APPEARANCE.
  - `location` (object):
    - `id` (string) (**requerido**): Location identifier associated with the members.
    - `name` (string) (**requerido**): Location name associated with the member.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person or workspace.

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
      "esn": "12348080",
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