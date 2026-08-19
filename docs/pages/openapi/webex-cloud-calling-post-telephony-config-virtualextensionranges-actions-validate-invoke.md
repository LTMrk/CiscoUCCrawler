---
doc_id: webex-cloud-calling-post-telephony-config-virtualextensionranges-actions-validate-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/virtualExtensionRanges/actions/validate/invoke
operation_id: Validate the prefix and extension pattern for a Virtual Extension Range
tags: Features: Virtual Extensions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.060441+00:00
---

# POST /telephony/config/virtualExtensionRanges/actions/validate/invoke

**API:** Webex Cloud Calling
**Área:** Features: Virtual Extensions
**operationId:** `Validate the prefix and extension pattern for a Virtual Extension Range`

## Resumen
Validate the prefix and extension pattern for a Virtual Extension Range

## Descripción
Validate the prefix and extension pattern for a Virtual Extension Range.

Virtual extension ranges integrate remote workers on a separate telephony system into Webex Calling and enable extension dialing. Using these ranges, you can define patterns that can be used to route calls at a location level or an organization level. You are allowed to define virtual extensions ranges in addition to individual virtual extensions.
This works in both Standard and Enhanced modes

Validating a prefix and extension pattern for a Virtual Extension Range requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Unique identifier for the organization.

## Cuerpo de la petición (application/json)
- `locationId` (string): ID of the location to which the virtual extension range is assigned. The location ID is a unique identifier for the location in Webex Calling.
- `name` (string): Name of the virtual extension range. This is a unique name for the virtual extension range.
- `prefix` (string): Prefix used for a virtual extension range.
- `patterns` (array): List of virtual extension patterns. The maximum number of patterns supported at a time is 100.
- `rangeId` (string): ID of the virtual extension range. This is mandatory when validating for an existing virtual extension range, not present when validating a new virtual extension range before adding it.

### Ejemplo — petición
```json
{
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTA5OA",
  "name": "SalesVirtualExtensionRange",
  "prefix": "+14089",
  "patterns": [
    "12XXXX"
  ],
  "rangeId": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfRVhURU5TSU9OLzZkNmYwNmVlLTdkNDEtNDQ4Yy05MjgwLWZkM2ZiMDhmOGUyMA"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/virtualExtensionRanges/actions/validate/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `status` (string) (**requerido**): Virtual extension range validation status.  * `OK` - Validation is successful.  * `ERRORS` - Validation failed. Valores: OK, ERRORS.
- `virtualExtensionRangeValidationStatus` (array): Array of virtual extension range validation status. This is set only when the `status` is `ERRORS`.
  - `name` (string): Name used for virtual extension range validation.
  - `prefix` (string): Prefix used for a virtual extension range validation.
  - `pattern` (string): Pattern used for a virtual extension range validation.
  - `errorCode` (string) (**requerido**): Error code for the virtual extension range validation.
  - `message` (string) (**requerido**): Error message for the virtual extension range validation.
  - `status` (string) (**requerido**): * `VALID` - Validation is successful.  * `DUPLICATE` - Duplicate patterns for virtual extension range.  * `DUPLICATE_IN_LIST` - Duplicate routing number in the pattern list.  * `INVALID` - Invalid prefix length.  * `LIMIT_EXCEEDED` - Exceeding pattern limit of 100 in the request. Valores: VALID, DUPLICATE, DUPLICATE_IN_LIST, INVALID, LIMIT_EXCEEDED.

### Ejemplo — respuesta 200
```json
{
  "status": "OK"
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