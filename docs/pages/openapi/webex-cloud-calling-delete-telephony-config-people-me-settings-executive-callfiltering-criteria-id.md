---
doc_id: webex-cloud-calling-delete-telephony-config-people-me-settings-executive-callfiltering-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: DELETE
path: /telephony/config/people/me/settings/executive/callFiltering/criteria/{id}
operation_id: deleteMyExecutiveCallFilteringCriteria
tags: Beta Call Settings For Me With Userhub Phase1
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.188236+00:00
---

# DELETE /telephony/config/people/me/settings/executive/callFiltering/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Beta Call Settings For Me With Userhub Phase1
**operationId:** `deleteMyExecutiveCallFilteringCriteria`

## Resumen
Delete User Executive Call Filtering Criteria

## Descripción
Delete a specific executive call filtering criteria for the authenticated user.

Executive Call Filtering Criteria in Webex allows you to manage detailed filter rules for incoming calls. This API removes a specific filter rule by its unique identifier.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Parámetros
- `id` [path] (string) (**requerido**): The `id` parameter specifies the unique identifier for the executive call filtering criteria. Example: `Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL2RHVnpkRjltYVd4MFpYST0`.

## Ejemplo de invocación
```bash
curl -X DELETE '/telephony/config/people/me/settings/executive/callFiltering/criteria/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: Executive call filtering criteria deleted successfully. No content is returned.

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
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