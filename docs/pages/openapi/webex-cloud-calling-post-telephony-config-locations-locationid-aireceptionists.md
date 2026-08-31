---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-aireceptionists
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/aiReceptionists
operation_id: createAiReceptionist
tags: AI Receptionist for Webex Calling, AI Receptionist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.121542+00:00
---

# POST /telephony/config/locations/{locationId}/aiReceptionists

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `createAiReceptionist`

## Resumen
Create an AI Receptionist

## Descripción
Create a new AI Receptionist for a location.

AI Receptionist is a Webex Calling feature that uses AI to greet callers and intelligently route calls to people or services.

This API requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location ID.
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Name of the AI Receptionist. This has to be unique across location. Long. max: 128.
- `enabled` (boolean) (**requerido**): Flag to indicate AI receptionist is enabled or not. When disabled, incoming calls to this AI receptionist will not be answered.
- `phoneNumber` (string): Phone number of the AI Receptionist. Either phoneNumber or extension is mandatory. At least one is required. Long. max: 23.
- `extension` (string): Extension of the AI Receptionist. Either phoneNumber or extension is mandatory. At least one is required. Long. max: 10.
- `directLineCallerIdName` (object): Direct line caller ID name configuration
- `dialByName` (string): A dial by name used for AI Receptionist name dialing. Characters of `%`, `+`, `\`, `"` and Unicode characters are not allowed. Long. max: 128.
- `defaultAction` (object) (**requerido**): Default action configuration for the AI Receptionist
- `aiAgent` (object) (**requerido**): AI Agent configuration

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/aiReceptionists' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "enabled": true, "defaultAction": "<defaultAction>", "aiAgent": "<aiAgent>"}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): AI Receptionist ID encoded using the Resource Type.

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