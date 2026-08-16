---
doc_id: webex-cloud-calling-post-telephony-config-virtualextensions-actions-validatenumbers-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/virtualExtensions/actions/validateNumbers/invoke
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.620046+00:00
---

# POST /telephony/config/virtualExtensions/actions/validateNumbers/invoke

**API:** Webex Cloud Calling
**Área:** Features: Virtual Extensions
**operationId:** `Validate an external phone number`

## Resumen
Validate an external phone number

## Descripción
Validate external phone number for the given organization.

This API is designed to validate external phone numbers before they are assigned as virtual extensions for a customer.
It ensures that the provided numbers are properly formatted, eligible for use, and not already in use within the system.
This validation is typically part of a pre-check process during provisioning or number assignment workflows, helping administrators or systems prevent conflicts or errors related to number reuse or format issues.

Creating a virtual extension requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Unique identifier for the organization.

## Cuerpo de la petición (application/json)
- `phoneNumbers` (array) **(requerido)**: List of external phone numbers to be validated.

### Ejemplo de petición
```json
{
  "phoneNumbers": [
    "+1234567890",
    "+1987654321"
  ]
}
```

## Respuestas
- **200**: OK
  - `status` (string) **(requerido)**: status of external phone number.
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
