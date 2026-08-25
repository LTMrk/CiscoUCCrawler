---
doc_id: webex-cloud-calling-get-telephony-config-virtualextensions-settings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/virtualExtensions/settings
operation_id: Get Virtual extension settings
tags: Features: Virtual Extensions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.503605+00:00
---

# GET /telephony/config/virtualExtensions/settings

**API:** Webex Cloud Calling
**Área:** Features: Virtual Extensions
**operationId:** `Get Virtual extension settings`

## Resumen
Get Virtual extension settings

## Descripción
Retrieve Virtual Extension settings for the given Org.

This API retrieves the virtual extension mode settings configured for a given organization. Virtual extensions can operate in two modes: STANDARD and ENHANCED. The selected mode determines how the system handles routing and signaling for virtual extensions.
By default, the virtual extensions that you create use the Standard mode. Another mode, enhanced signaling mode, is available to all customers, however, virtual extensions won't function properly in this mode unless your PSTN provider supports special network signaling extensions and there aren't many PSTN providers that do.

Retrieving a Virtual Extension settings requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Unique identifier for the organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/virtualExtensions/settings' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `mode` (string) (**requerido**): Mode of the virtual extension. It can be either `STANDARD` or `ENHANCED`.      + `STANDARD` -  Standard virtual extension mode in which virtual extensions must be associated with a valid E.164 number, but this requires no enhanced signaling support from the PSTN provider.     + `ENHANCED` - Enhanced signaling mode: only a few PSTN providers support this special network signaling extension. Valores: STANDARD.

### Ejemplo — respuesta 200
```json
{
  "mode": "STANDARD"
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