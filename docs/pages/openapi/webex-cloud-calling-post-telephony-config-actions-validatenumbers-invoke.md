---
doc_id: webex-cloud-calling-post-telephony-config-actions-validatenumbers-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/actions/validateNumbers/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.631990+00:00
---

# POST /telephony/config/actions/validateNumbers/invoke

**API:** Webex Cloud Calling
**Área:** Numbers
**operationId:** `Validate phone numbers`

## Resumen
Validate Phone Numbers

## Descripción
Validate the list of phone numbers in an organization. Each phone number's availability is indicated in the response.

Each location has a set of phone numbers that can be assigned to people, workspaces, or features. Phone numbers must follow the E.164 format for all countries, except for the United States, which can also follow the National format. Active phone numbers are in service.

Validating a phone number in an organization requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Organization of the Route Group.

## Cuerpo de la petición (application/json)
- `phoneNumbers` (array) **(requerido)**: List of phone numbers that need to be added.

## Respuestas
- **200**: OK
  - `status` (string) **(requerido)**: * `OK` - Everything is good.  * `ERRORS` - Validation has failed with errors. Valores: OK, ERRORS.
  - `numbers` (array) **(requerido)**: An array of number objects with number details.
    - `number` (string) **(requerido)**: Phone numbers that need to be validated.
    - `state` (string) **(requerido)**: * `Available` - The phone number is available.  * `Duplicate` - Duplicate phone number.  * `Duplicate In List` - Duplicate phone number in the list.  * `Invalid` - The phone number is invalid.  * `Unavailable` - The phone number is unavailable and cannot be used. Valores: Available, Duplicate, Duplicate In List, Invalid, Unavailable.
    - `tollFreeNumber` (boolean) **(requerido)**: If `true`, it's a toll-free number.
    - `detail` (array): Error details if the number is unavailable.
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
