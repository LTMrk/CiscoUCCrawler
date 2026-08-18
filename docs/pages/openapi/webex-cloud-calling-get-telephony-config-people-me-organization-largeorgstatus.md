---
doc_id: webex-cloud-calling-get-telephony-config-people-me-organization-largeorgstatus
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/organization/largeOrgStatus
operation_id: getMyOrganizationLargeOrgStatus
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.252199+00:00
---

# GET /telephony/config/people/me/organization/largeOrgStatus

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyOrganizationLargeOrgStatus`

## Resumen
Get Large Organization Status

## Descripción
Get whether the authenticated person's organization is considered as a large organization.

Large organization status is used to determine how certain Webex Calling features behave, such as pagination limits and search capabilities, to optimize performance for organizations with many people.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/organization/largeOrgStatus' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `isLargeOrg` (boolean) (**requerido**): Indicates whether the caller's organization exceeds the large organization threshold percentage.

### Ejemplo — respuesta 200
```json
{
  "isLargeOrg": false
}
```

## Respuestas de error
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs