---
doc_id: webex-cloud-calling-delete-telephony-config-people-me-settings-callnotify-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: DELETE
path: /telephony/config/people/me/settings/callNotify/criteria/{id}
operation_id: deleteMyCallNotifyCriteria
tags: Call Settings For Me With UserHub Phase2
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.161545+00:00
---

# DELETE /telephony/config/people/me/settings/callNotify/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `deleteMyCallNotifyCriteria`

## Resumen
Delete a Call Notify Criteria

## Descripción
Delete a Call Notify criteria for the authenticated user.

Call Notify allows you to set up a unique ringtone based on predefined criteria. This API removes a specific criteria rule by its unique identifier.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Parámetros
- `id` [path] (string) (**requerido**): The `id` parameter specifies the unique identifier for the call notify criteria. Example: `Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1oxNzU0MzgzODQzNTA5NzY`.

## Ejemplo de invocación
```bash
curl -X DELETE '/telephony/config/people/me/settings/callNotify/criteria/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: Call Notify criteria deleted successfully. No content is returned.

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs