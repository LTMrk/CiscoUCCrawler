---
doc_id: webex-cloud-calling-get-telephony-config-virtualextensions
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/virtualExtensions
operation_id: Read the List of Virtual Extensions
tags: Features: Virtual Extensions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.290056+00:00
---

# GET /telephony/config/virtualExtensions

**API:** Webex Cloud Calling
**Área:** Features: Virtual Extensions
**operationId:** `Read the List of Virtual Extensions`

## Resumen
Read the List of Virtual Extensions

## Descripción
Retrieve virtual extensions associated with a specific customer.

The GET Virtual Extensions API allows administrators to retrieve a list of virtual extensions configured within their organization. Virtual extensions enable users to dial extension numbers that route to external phone numbers, such as those of remote workers or frequently contacted clients.
This API returns key information including the  extension, associated  phone number (in E.164 format), display name, and the location to which the virtual extension belongs
The API supports filtering by various parameters, such as extension number, phone number, and location name. The results can be paginated using the `max` and `start` parameters, and the order of the results can be specified using the `order` parameter.

Retrieving a Virtual Extension requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Unique identifier for the organization.
- `max` [query] (number): Limit the number of virtual extensions returned to this maximum count. Default is 10.
- `start` [query] (number): Start at the zero-based offset in the list of matching virtual extensions. Default is 0.
- `order` [query] (string): Order the list of virtual extensions in ascending or descending order. Default is ascending.
- `extension` [query] (string): Filter the list of virtual extensions by extension number.
- `phoneNumber` [query] (string): Filter the list of virtual extensions by phone number.
- `name` [query] (string): Filter the list of virtual extensions by name. This can be either first name or last name.
- `locationName` [query] (string): Filter the list of virtual extensions by location name.(Only one of the locationName, locationId, and OrgLevelOnly query parameters is allowed at the same time.)
- `locationId` [query] (string): Filter the list of virtual extensions by location ID.
- `orgLevelOnly` [query] (boolean): Filter the list of virtual extensions by organization level. If orgLevelOnly is true, return only the organization level virtual extensions.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/virtualExtensions' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `virtualExtensions` (array) (**requerido**): List of virtual extensions.
  - `id` (string) (**requerido**): ID of the virtual extension.
  - `extension` (string) (**requerido**): Extension of the virtual extension.
  - `routingPrefix` (string): Routing prefix of the virtual extension's location.
  - `esn` (string) (**requerido**): ESN of the virtual extension.
  - `phoneNumber` (string) (**requerido**): Directory number of the virtual extension.
  - `firstName` (string): First name of the person at the virtual extension.
  - `lastName` (string): Last name of the person at the virtual extension.
  - `level` (string) (**requerido**): Level of the virtual extension. It can be either `ORGANIZATION` or `LOCATION`.  * `ORGANIZATION` - Organization level.  * `LOCATION` - Location level. Valores: ORGANIZATION, LOCATION.
  - `locationId` (string): ID of the location to which the virtual extension is assigned. The location ID is a unique identifier for the location in Webex Calling.
  - `locationName` (string): Name of the location to which the virtual extension is assigned.
  - `displayName` (string): Display name of the person at the virtual extension.

### Ejemplo — respuesta 200
```json
{
  "virtualExtensions": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfRVhURU5TSU9OLzZkNmYwNmVlLTdkNDEtNDQ4Yy05MjgwLWZkM2ZiMDhmOGUyMA",
      "extension": "5001",
      "routingPrefix": "4321",
      "esn": "43215001",
      "phoneNumber": "+16692515287",
      "firstName": "Bob",
      "level": "LOCATION",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2QzYjA4MGMwLWU1MjctNDQ1Zi04NTk5LTU5OWJmNzQ2MjViNg",
      "locationName": "TestLocation",
      "displayName": "Bob Smith"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfRVhURU5TSU9OL2JhNTE0MGExLWM0MjItNDRhMC05MmUyLTRkNDQ0ZTg1NDc5NQ",
      "extension": "5001",
      "esn": "5001",
      "phoneNumber": "+12135536387",
      "firstName": "John",
      "lastName": "Smith",
      "level": "ORGANIZATION",
      "displayName": "John Smith"
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