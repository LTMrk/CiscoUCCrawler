---
doc_id: webex-cloud-calling-post-telephony-config-virtuallines
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/virtualLines
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.655852+00:00
---

# POST /telephony/config/virtualLines

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Create a Virtual Line`

## Resumen
Create a Virtual Line

## Descripción
Create new Virtual Line for the given location.

Virtual line is a capability in Webex Calling that allows administrators to configure multiple lines to Webex Calling users.

Creating a virtual line requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Create the virtual line for this organization.

## Cuerpo de la petición (application/json)
- `firstName` (string) **(requerido)**: First name defined for a virtual line. Minimum length is 1. Maximum length is 30.
- `lastName` (string) **(requerido)**: Last name defined for a virtual line. Minimum length is 1. Maximum length is 30.
- `displayName` (string): Display name defined for a virtual line.
- `phoneNumber` (string): Phone number of a virtual line. Minimum length is 1. Maximum length is 23. Either `phoneNumber` or `extension` is mandatory.
- `extension` (string): Extension of a virtual line. Minimum length is 2. Maximum length is 10. Either `phoneNumber` or `extension` is mandatory.
- `locationId` (string) **(requerido)**: ID of location for virtual line.
- `callerIdLastName` (string): Last name used in the Calling Line ID and for dial-by-name functions. Minimum length is 1. Maximum length is 30.
- `callerIdFirstName` (string): First name used in the Calling Line ID and for dial-by-name functions. Minimum length is 1. Maximum length is 30.
- `callerIdNumber` (string): Phone number to appear as the CLID for all calls. Minimum length is 1. Maximum length is 23.

### Ejemplo de petición
```json
{
  "firstName": "Bob",
  "lastName": "Smith",
  "displayName": "Bob Smith",
  "phoneNumber": "+15558675309",
  "extension": "5309",
  "locationId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YTc2ZmVmNC1mZjlmLTExZWItYWYwZC00M2YwZjY1NTdjYWI",
  "callerIdFirstName": "Bob",
  "callerIdLastName": "Smith",
  "callerIdNumber": "+15558675309"
}
```

## Respuestas
- **201**: Created
  - `id` (string) **(requerido)**: ID of the newly created virtual line.
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
