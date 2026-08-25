---
doc_id: webex-cloud-calling-get-telephony-config-supervisors-availablesupervisors
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/supervisors/availableSupervisors
operation_id: listAvailableCallQueueSupervisors
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.478563+00:00
---

# GET /telephony/config/supervisors/availableSupervisors

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `listAvailableCallQueueSupervisors`

## Resumen
List Available Supervisors for Call Queue or Customer Assist

## Descripción
Get list of available supervisors for an organization.

Agents in a call queue can be associated with a supervisor who can silently monitor, coach, barge in or to take over calls that their assigned agents are currently handling.

This operation requires a full, user or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List the available supervisors in this organization.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `name` [query] (string): Only return the supervisors that match the given name.
- `phoneNumber` [query] (string): Only return the supervisors that match the given phone number, extension, or ESN.
- `order` [query] (string): Sort results alphabetically by supervisor name, in ascending or descending order.
- `hasCxEssentials` [query] (boolean): Returns only the list of available supervisors with Customer Assist license, when `true`. When ommited or set to 'false', will return the list of available supervisors with Customer Experience Basic license.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/supervisors/availableSupervisors' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `supervisors` (array) (**requerido**): Array of available supervisors.
  - `id` (string) (**requerido**): A unique identifier for the supervisor.
  - `firstName` (string): First name of the supervisor.
  - `lastName` (string): Last name of the supervisor.
  - `displayName` (string): (string, optional) - Display name of the supervisor.
  - `phoneNumber` (string): Primary phone number of the supervisor.
  - `extension` (string): Primary phone extension of the supervisor.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person.

### Ejemplo — respuesta 200
```json
{
  "supervisors": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YzVlODRhMS0wZmEwLTQzNDAtODVkZC1mMzM1ZGQ4MTkxMmI",
      "lastName": "Adam",
      "firstName": "Sandler",
      "displayName": "Adam Sandler",
      "extension": "0200",
      "routingPrefix": "34543",
      "esn": "345430200",
      "phoneNumber": "+19845550200",
      "hasCxEssentials": true
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82ZmYyYTkxNi1hYWRhLTQwZTYtOTkzMC0xZmFmYmNiMzQwODU",
      "lastName": "Steven",
      "firstName": "Robert",
      "displayName": "Steven Robert",
      "extension": "9906",
      "routingPrefix": "34",
      "esn": "349906",
      "hasCxEssentials": true
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