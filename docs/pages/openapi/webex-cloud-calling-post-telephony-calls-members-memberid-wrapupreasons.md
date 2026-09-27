---
doc_id: webex-cloud-calling-post-telephony-calls-members-memberid-wrapupreasons
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/calls/members/{memberId}/wrapupreasons
operation_id: setWrapupReasonsByMemberId
tags: Call Controls Members
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-27T10:51:19.271737+00:00
---

# POST /telephony/calls/members/{memberId}/wrapupreasons

**API:** Webex Cloud Calling
**Área:** Call Controls Members
**operationId:** `setWrapupReasonsByMemberId`

## Resumen
Set Wrap-up Reasons by Member ID

## Descripción
Sets wrap-up reasons for the specified member's last completed call. This API is for admins/service apps to perform actions on behalf of a user. The request must provide wrapupReasons.

## Parámetros
- `memberId` [path] (string) (**requerido**): Unique identifier for the member.
- `orgId` [query] (string): Organization ID.

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
curl -X POST '/telephony/calls/members/<memberId>/wrapupreasons' \
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