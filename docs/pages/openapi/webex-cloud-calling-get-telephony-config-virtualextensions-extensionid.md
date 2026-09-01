---
doc_id: webex-cloud-calling-get-telephony-config-virtualextensions-extensionid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/virtualExtensions/{extensionId}
operation_id: Get a Virtual Extension
tags: Features: Virtual Extensions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.718403+00:00
---

# GET /telephony/config/virtualExtensions/{extensionId}

**API:** Webex Cloud Calling
**Área:** Features: Virtual Extensions
**operationId:** `Get a Virtual Extension`

## Resumen
Get a Virtual Extension

## Descripción
Retrieve Virtual Extension details for the given extension ID.

Virtual extensions integrate remote workers on separate telephony systems into Webex Calling, enabling users to reach them via extension dialing.
This endpoint allows administrators to retrieve configuration details for a specific virtual extension, ensuring visibility into the mapping between extensions and external phone numbers.

Retrieving a Virtual Extension requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `extensionId` [path] (string) (**requerido**): ID of the virtual extension.
- `orgId` [query] (string): Unique identifier for the organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/virtualExtensions/<extensionId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
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
  "id": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfRVhURU5TSU9OLzZkNmYwNmVlLTdkNDEtNDQ4Yy05MjgwLWZkM2ZiMDhmOGUyMA",
  "extension": "5001",
  "routingPrefix": "4321",
  "esn": "43215001",
  "phoneNumber": "+6692515287",
  "firstName": "John",
  "level": "LOCATION",
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2QzYjA4MGMwLWU1MjctNDQ1Zi04NTk5LTU5OWJmNzQ2MjViNg",
  "locationName": "Test1",
  "displayName": "JohnSmith"
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