---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-callparkextensions-callparkextensionid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/callParkExtensions/{callParkExtensionId}
operation_id: Get Details for a Call Park Extension
tags: Features:  Call Park
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.468511+00:00
---

# GET /telephony/config/locations/{locationId}/callParkExtensions/{callParkExtensionId}

**API:** Webex Cloud Calling
**Área:** Features:  Call Park
**operationId:** `Get Details for a Call Park Extension`

## Resumen
Get Details for a Call Park Extension

## Descripción
Retrieve Call Park Extension details.

The Call Park service, enabled for all users by default, allows a user to park a call against an available user's extension or to a Call Park Extension. Call Park Extensions are extensions defined within the Call Park service for holding parked calls.

Retrieving call park extension details requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve details for a call park extension in this location.
- `callParkExtensionId` [path] (string) (**requerido**): Retrieve details for a call park extension with the matching ID.
- `orgId` [query] (string): Retrieve call park extension details from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/callParkExtensions/<callParkExtensionId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `extension` (string) (**requerido**): The extension for the call park extension.
- `routingPrefix` (string): Routing prefix of location.
- `esn` (string): Routing prefix + extension of a person or workspace.
- `name` (string) (**requerido**): Unique name for the call park extension.

### Ejemplo — respuesta 200
```json
{
  "extension": "1415",
  "routingPrefix": "1234",
  "esn": "12341415",
  "name": "14159265"
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