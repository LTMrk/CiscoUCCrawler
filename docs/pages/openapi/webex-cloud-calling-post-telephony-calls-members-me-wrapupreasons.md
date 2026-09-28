---
doc_id: webex-cloud-calling-post-telephony-calls-members-me-wrapupreasons
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/calls/members/me/wrapupreasons
operation_id: setWrapupReasons
tags: Call Controls Members Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-28T16:31:32.398052+00:00
---

# POST /telephony/calls/members/me/wrapupreasons

**API:** Webex Cloud Calling
**Área:** Call Controls Members Me
**operationId:** `setWrapupReasons`

## Resumen
Set Wrap-up Reasons

## Descripción
Sets wrap-up reasons for the authenticated user's last completed call. The request must provide wrapupReasons.

## Cuerpo de la petición (application/json)
- `wrapupReasons` (array): Array of wrap-up reason names to apply to the agent's last completed call.

### Ejemplo — petición
```json
{
  "wrapupReasons": [
    "Reason1",
    "Reason2",
    "Reason3"
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/calls/members/me/wrapupreasons' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: No Content

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs