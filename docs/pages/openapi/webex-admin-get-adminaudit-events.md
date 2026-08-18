---
doc_id: webex-admin-get-adminaudit-events
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /adminAudit/events
operation_id: List Admin Audit Events
tags: Admin Audit Events
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.558553+00:00
---

# GET /adminAudit/events

**API:** Webex Admin
**Área:** Admin Audit Events
**operationId:** `List Admin Audit Events`

## Resumen
List Admin Audit Events

## Descripción
List admin audit events in your organization. Several query parameters are available to filter the response.

Long result sets will be split into [pages](/docs/basics#pagination).

**NOTE**: A maximum of one year of audit events can be returned per request.

## Parámetros
- `orgId` [query] (string) (**requerido**): List events in this organization, by ID.
- `from` [query] (string) (**requerido**): List events which occurred after a specific date and time.
- `to` [query] (string) (**requerido**): List events which occurred before a specific date and time.
- `actorId` [query] (string): List events performed by this person, by ID.
- `max` [query] (number): Limit the maximum number of events in the response. The maximum value is `200`. Por defecto: 100.
- `offset` [query] (number): Offset from the first result that you want to fetch.
- `eventCategories` [query] (array): List events, by event categories.

## Ejemplo de invocación
```bash
curl -X GET '/adminAudit/events?orgId=<orgId>&from=<from>&to=<to>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of audit event objects. See [this article](https://help.webex.com/n3b0w6x/) for details about each event type.
  - `data` (object):
    - `actorOrgName` (string): The display name of the organization.
    - `targetName` (string): The name of the resource being acted upon.
    - `eventDescription` (string): A description for the event.
    - `actorName` (string): The name of the person who performed the action.
    - `actorEmail` (string): The email of the person who performed the action.
    - `adminRoles` (array): Admin roles for the person.
    - `trackingId` (string): A tracking identifier for the event.
    - `targetType` (string): The type of resource changed by the event.
    - `targetId` (string): The identifier for the resource changed by the event.
    - `eventCategory` (string): The category of resource changed by the event.
    - `actorUserAgent` (string): The browser user agent of the person who performed the action.
    - `actorIp` (string): The IP address of the person who performed the action.
    - `targetOrgId` (string): The `orgId` of the organization.
    - `actionText` (string): A more detailed description of the change made by the person.
    - `targetOrgName` (string): The name of the organization being acted upon.
    - `errorMessage` (string): User operation failure message.
    - `errorCode` (string): User operation failure code.
  - `created` (string): The date and time the event took place.
  - `actorOrgId` (string): The `orgId` of the person who made the change.
  - `id` (string): A unique identifier for the event.
  - `actorId` (string): The `personId` of the person who made the change.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "data": {
        "actorOrgName": "Acme Inc.",
        "targetName": "Acme Inc.",
        "eventDescription": "An Admin logged in",
        "actorName": "Joe Smith",
        "actorEmail": "joe@example.com",
        "adminRoles": [
          "User"
        ],
        "trackingId": "ATLAS_6f23a878-bcd4-c204-a4db-e701b42b0e5c_0",
        "targetType": "TargetResourceType.ORG",
        "targetId": "NWIzZTBiZDgtZjg4Ni00MjViLWIzMTgtYWNlYjliN2EwZGFj",
        "eventCategory": "EventCategory.LOGINS",
        "actorUserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "actorIp": "128.107.241.191",
        "targetOrgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
        "actionText": "Joe Smith logged into organization Acme Inc.",
        "targetOrgName": "Acme Inc."
      },
      "created": "2019-01-02T16:58:36.845Z",
      "actorOrgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
      "id": "MjQ0ODhiZTYtY2FiMS00ZGRkLTk0NWQtZDFlYjkzOGQ4NGUy",
      "actorId": "MjQ4Njg2OTYtYWMwZC00ODY4LWJkMjEtZGUxZDc4MzhjOTdm"
    }
  ]
}
```
- Cabecera `Content-Disposition`: 

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
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs