---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-monitoring-availablemembers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/monitoring/availableMembers
operation_id: getAvailableMembersForPersonMonitoring
tags: User Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.541437+00:00
---

# GET /telephony/config/people/{personId}/monitoring/availableMembers

**API:** Webex Cloud Calling
**Área:** User Call Settings
**operationId:** `getAvailableMembersForPersonMonitoring`

## Resumen
Get Available Members for Person Monitoring

## Descripción
Get available members for person monitoring. This API allows administrators to retrieve a list of members that can be added to the monitoring list for a specific person.

Webex Calling monitoring allows a person to watch the line status of selected people, workspaces, and virtual lines. Configuring a monitoring list helps the person quickly see whether monitored members are on a call.

This API requires a full, user, or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): ID of the organization within which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access the API.
- `locationId` [query] (string): Search for the available members in the location ID.
- `memberName` [query] (string): Search for available members by name.
- `phoneNumber` [query] (string): Search for available members by number or extension.
- `order` [query] (array): Sort response based on `firstName` or `lastName` with sort direction `asc` or `desc`. Example: `lastName-asc` or `firstName-desc`. Default sort is ascending order.
- `start` [query] (integer): Number of records to skip for pagination.
- `max` [query] (integer): Number of records per page for pagination. Default: 2000. Maximum: 2000. Por defecto: 2000.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/monitoring/availableMembers' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `members` (array): List of available members.
  - `id` (string): The identifier of the available member.
  - `firstName` (string): The first name of the available member.
  - `lastName` (string): The last name of the available member.
  - `displayName` (string): The display name of the available member.
  - `phoneNumber` (string): The phone number of the available member.
  - `extension` (string): The extension of the available member.
  - `type` (string): The type of the available member.  * `PEOPLE` - Object is a user.  * `PLACE` - Object is a workspace.  * `VIRTUAL_LINE` - Object is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `location` (object):
    - `id` (string): The ID of the location.
    - `name` (string): The name of the location.

### Ejemplo — respuesta 200
```json
{
  "members": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS85ODhiYTQyOC0zMjMyLTRmNjItYjUyNy1hZGEyNTRlMTk0MjE",
      "firstName": "John",
      "lastName": "Doe",
      "displayName": "John Doe",
      "phoneNumber": "+14085551234",
      "extension": "1234",
      "type": "PEOPLE",
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzEyMzQ1Njc4OTAxMjM0NTY3ODkw",
        "name": "San Jose"
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