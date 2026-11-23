---
doc_id: webex-cloud-calling-delete-telephony-config-people-personid-priorityalert-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: DELETE
path: /telephony/config/people/{personId}/priorityAlert/criteria/{id}
operation_id: deletePersonPriorityAlertCriteria
tags: User Call Settings (3/3)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:16.062739+00:00
---

# DELETE /telephony/config/people/{personId}/priorityAlert/criteria/{id}

**API:** Webex Cloud Calling
**Área:** User Call Settings (3/3)
**operationId:** `deletePersonPriorityAlertCriteria`

## Resumen
Delete a Priority Alert Criterion for a Person

## Descripción
Delete a Priority Alert criterion for a person.

Priority alert allows setting up a distinctive ringtone based on predefined criteria. This API removes a specific criterion by its unique identifier.

This API requires a full, user, or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `personId` [path] (string) (**requerido**): A unique identifier for the person.
- `id` [path] (string) (**requerido**): Unique identifier for the priority alert criterion.
- `orgId` [query] (string): Optional target organization identifier. Defaults to the token's organization if not provided. A partner administrator must provide this value to specify the target organization.

## Ejemplo de invocación
```bash
curl -X DELETE '/telephony/config/people/<personId>/priorityAlert/criteria/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: Priority Alert criterion deleted successfully. No content is returned.

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a person, does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs