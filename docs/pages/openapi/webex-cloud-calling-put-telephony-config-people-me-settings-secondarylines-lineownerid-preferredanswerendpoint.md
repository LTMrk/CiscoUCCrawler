---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-secondarylines-lineownerid-preferredanswerendpoint
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/me/settings/secondaryLines/{lineOwnerId}/preferredAnswerEndpoint
operation_id: modifyMySecondaryLinesPreferredAnswerEndpoint
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.142907+00:00
---

# PUT /telephony/config/people/me/settings/secondaryLines/{lineOwnerId}/preferredAnswerEndpoint

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `modifyMySecondaryLinesPreferredAnswerEndpoint`
**Autenticación:** bearer-key

## Resumen
Modify My Secondary Line Owner's Preferred Answer Endpoint

## Descripción
Sets or clears the preferred answer endpoint for the secondary line owner of the authenticated person. To clear the preferred answer endpoint the `id` attribute must be set to null.

 A Webex Calling user may be associated with multiple endpoints such as Webex App (desktop or mobile), Cisco desk IP phone, Webex Calling-supported analog devices or third-party endpoints. Preferred answering endpoints allow users to specify which of these devices should be prioritized for answering calls, particularly when a person's extension (or a virtual line assigned to them) rings on multiple devices. This helps ensure that calls are answered on the most convenient or appropriate device for the person.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Parámetros
- `lineOwnerId` [path] (string) (**requerido**): Unique identifier for the secondary line owner (applicable only for Virtual Lines).

## Cuerpo de la petición (application/json)
- `preferredAnswerEndpointId` (string) (**requerido**): Person’s preferred answer endpoint.

### Ejemplo — petición
```json
{
  "id": "Y2lzY29z..."
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/me/settings/secondaryLines/<lineOwnerId>/preferredAnswerEndpoint' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"preferredAnswerEndpointId": "<preferredAnswerEndpointId>"}'
```

## Respuestas correctas
**204**: No Content: The preferred answering endpoint was successfully updated.

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs