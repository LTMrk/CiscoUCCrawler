---
doc_id: webex-cloud-calling-post-telephony-config-virtualextensions
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/virtualExtensions
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.619266+00:00
---

# POST /telephony/config/virtualExtensions

**API:** Webex Cloud Calling
**Área:** Features: Virtual Extensions
**operationId:** `Create a Virtual Extension`

## Resumen
Create a Virtual Extension

## Descripción
Create new Virtual Extension for the given organization or location.

You can set up virtual extensions at the organization or location level. The organization level enables everyone across your organization to dial the same extension number to reach someone.
You can use the location level virtual extension like any other extension assigned to the specific location.
Users at the specific location can dial the extension. However, users at other locations can reach the virtual extension by dialing the ESN.

Creating a virtual extension requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write` and `identity:contacts_rw`.

## Parámetros
- `orgId` [query] (string): Unique identifier for the organization.

## Cuerpo de la petición (application/json)
- `firstName` (string): First name of the person at the virtual extension.
- `lastName` (string): Last name of the person at the virtual extension.
- `displayName` (string) **(requerido)**: Display name of the person at the virtual extension.
- `phoneNumber` (string) **(requerido)**: Directory number of the virtual extension.
- `extension` (string) **(requerido)**: Extension of the virtual extension.
- `locationId` (string): ID of the location to which the virtual extension is assigned. The location ID is a unique identifier for the location in Webex Calling.

### Ejemplo de petición
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "displayName": "JohnSmith",
  "phoneNumber": "+17011558169",
  "extension": "9133",
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTA5OA"
}
```

## Respuestas
- **201**: Created
  - `id` (string) **(requerido)**: ID of the newly created virtual extension.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
