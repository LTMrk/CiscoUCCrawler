---
doc_id: webex-cloud-calling-get-telephony-config-aireceptionists-templates-templateid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/aiReceptionists/templates/{templateId}
operation_id: getAiReceptionistTemplate
tags: AI Receptionist for Webex Calling, AI Receptionist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.120979+00:00
---

# GET /telephony/config/aiReceptionists/templates/{templateId}

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `getAiReceptionistTemplate`

## Resumen
Get AI Receptionist Template Details

## Descripción
Get AI Receptionist template details.

AI Receptionist is a Webex Calling feature that uses AI to greet callers and intelligently route calls. Use templates to define goals, messages, and guidelines.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `templateId` [path] (string) (**requerido**): Template Id.
- `orgId` [query] (string): Optional target organization identifier. Defaults to token's organization if not provided.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/aiReceptionists/templates/<templateId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for the AI receptionist template.
- `name` (string) (**requerido**): Name of the AI Receptionist template.
- `goal` (string): Goal of the AI Receptionist.
- `welcomeMessage` (string) (**requerido**): Welcome message to be played before the call handling.
- `guideline` (string): Guidelines for the AI receptionist to follow. This includes information like identity, role definition, context, behavior, etc.
- `defaultTransparencyMessage` (string): Default transparency disclosure message for AI Receptionist. This message explicitly informs callers they are interacting with an AI system, ensuring compliance with EU AI Act transparency obligations for Limited Risk AI systems.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1RFTVBMQVRFL2EyYjNjNDU2LTc4OTAtMTIzNC01Njc4LTkwYWJjZGVmMTIzNA",
  "name": "Clinic",
  "goal": "As an AI receptionist for Shine Healthcare Clinic, your role is to help callers with necessary information regarding our services.",
  "welcomeMessage": "Hello I am your AI Receptionist. How can I help you today?",
  "guideline": "1. Role Definition: You are a friendly assistant\n2. Context: User can only book or cancel appointment",
  "defaultTransparencyMessage": "Hi, I'm an AI receptionist. This interaction may be recorded and transcribed for troubleshooting purposes."
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