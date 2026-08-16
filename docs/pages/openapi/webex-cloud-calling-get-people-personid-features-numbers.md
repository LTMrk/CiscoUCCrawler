---
doc_id: webex-cloud-calling-get-people-personid-features-numbers
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /people/{personId}/features/numbers
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.640218+00:00
---

# GET /people/{personId}/features/numbers

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `Get a List of Phone Numbers for a Person`

## Resumen
Get a List of Phone Numbers for a Person

## Descripción
Get a person's phone numbers including alternate numbers.

A person can have one or more phone numbers and/or extensions via which they can be called.

This API requires a full or user administrator or location administrator auth token with the `spark-admin:people_read` scope.

<br/>

<div><Callout type="warning">The `preferE164Format` query parameter can be used to get phone numbers either in E.164 format or in their legacy format. The support for getting phone numbers in non-E.164 format in some geographies will be removed in the future.</Callout></div>

## Parámetros
- `personId` [path] (string) **(requerido)**: Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
- `preferE164Format` [query] (boolean): Return phone numbers in E.164 format.

## Respuestas
- **200**: OK
  - `distinctiveRingEnabled` (boolean): Enable/disable a distinctive ring pattern that identifies calls coming from a specific phone number.
  - `phoneNumbers` (array) **(requerido)**: Information about the number.
    - `primary` (boolean): Flag to indicate if the number is primary or not.
    - `directNumber` (string): Phone number.
    - `extension` (string): Extension.
    - `routingPrefix` (string): Routing prefix of location.
    - `esn` (string): Routing prefix + extension of a person or workspace.
    - `ringPattern` (string): Optional ring pattern. Applicable only for alternate numbers.  * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a long ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
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
