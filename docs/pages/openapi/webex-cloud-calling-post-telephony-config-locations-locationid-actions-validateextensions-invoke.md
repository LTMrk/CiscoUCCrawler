---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-actions-validateextensions-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/actions/validateExtensions/invoke
operation_id: Validate Extensions
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.723779+00:00
---

# POST /telephony/config/locations/{locationId}/actions/validateExtensions/invoke

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Validate Extensions`

## Resumen
Validate Extensions

## Descripción
Validate extensions for a specific location.

Validating extensions requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Validate extensions for this location.
- `orgId` [query] (string): Validate extensions for this organization.

## Cuerpo de la petición (application/json)
- `extensions` (array) (**requerido**): Array of extensions that will be validated.

### Ejemplo — petición
```json
{
  "extensions": [
    "407721",
    "507721",
    "507721",
    "9111",
    "a234"
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/actions/validateExtensions/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"extensions": []}'
```

## Respuestas correctas
**200**: OK
- `status` (string) (**requerido**): Status of the validated array of extensions.  * `OK` - Indicates that all extensions were validated.  * `ERRORS` - Indicates that not all extensions were validated. Valores: OK, ERRORS.
- `extensionStatus` (array): Array of extensions statuses.
  - `extension` (string): Unique extension which will be validated at the location level.
  - `state` (string) (**requerido**): State of the extension after it was validated.  * `VALID` - Extension is valid.  * `DUPLICATE` - Extension already assigned to another group.  * `DUPLICATE_IN_LIST` - Extension already exists in the request body and was already verified.  * `INVALID` - Extension is invalid. Valores: VALID, DUPLICATE, DUPLICATE_IN_LIST, INVALID.
  - `errorCode` (number): Error code of the state in case extension is not valid.
  - `message` (string): Message assigned to the error code.

### Ejemplo — respuesta 200
```json
{
  "status": "ERRORS",
  "extensionStatus": [
    {
      "extension": "407721",
      "state": "DUPLICATE",
      "errorCode": 9495,
      "message": "[Error 9495] The extension is not available. It is already assigned as a Call Park Extension: 407721."
    },
    {
      "extension": "507721",
      "state": "VALID"
    },
    {
      "extension": "507721",
      "state": "DUPLICATE_IN_LIST",
      "errorCode": 9498
    },
    {
      "extension": "911",
      "state": "INVALID",
      "errorCode": 4911,
      "message": "[Error 4911] Invalid extension.  The extension cannot be an emergency number."
    },
    {
      "extension": "a234",
      "state": "INVALID",
      "errorCode": 4910,
      "message": "[Error 4910] Invalid extension.  The extension can only contain characters 0-9."
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