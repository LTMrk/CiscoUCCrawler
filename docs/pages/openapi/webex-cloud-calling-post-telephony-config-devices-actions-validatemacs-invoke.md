---
doc_id: webex-cloud-calling-post-telephony-config-devices-actions-validatemacs-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/devices/actions/validateMacs/invoke
operation_id: validateAListOfMACAddress
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.620136+00:00
---

# POST /telephony/config/devices/actions/validateMacs/invoke

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `validateAListOfMACAddress`

## Resumen
Validate a list of MAC address

## Descripción
Validate a list of MAC addresses.

Validating this list requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Validate the mac address(es) for this organization.

## Cuerpo de la petición (application/json)
- `macs` (array) (**requerido**): MAC addresses to be validated.

### Ejemplo — petición
```json
{
  "macs": [
    "ab125678cdef",
    "00005E0053B4"
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/devices/actions/validateMacs/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"macs": []}'
```

## Respuestas correctas
**200**: OK
- `status` (string) (**requerido**): Status of MAC address. Valores: OK, ERRORS.
- `macStatus` (array) (**requerido**): Contains an array of all the MAC address provided and their statuses.
  - `mac` (string) (**requerido**): MAC address.
  - `state` (string) (**requerido**): State of the MAC address.  * `AVAILABLE` - The requested MAC address is available.  * `UNAVAILABLE` - The requested MAC address is unavailable.  * `DUPLICATE_IN_LIST` - The requested MAC address is duplicated.  * `INVALID` - The requested MAC address is invalid. Valores: AVAILABLE, UNAVAILABLE, DUPLICATE_IN_LIST, INVALID.
  - `errorCode` (number): MAC address validation error code.
  - `message` (string): Provides a status message about the MAC address.

### Ejemplo — respuesta 200
```json
{
  "status": "ERRORS",
  "macStatus": [
    {
      "mac": "ab125678cdef",
      "state": "AVAILABLE"
    },
    {
      "mac": "00005E0053B4",
      "state": "UNAVAILABLE",
      "errorCode": 5675,
      "message": "[Error 5675] MAC Address is in use."
    }
  ]
}
```
- Cabecera `Link`: 

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