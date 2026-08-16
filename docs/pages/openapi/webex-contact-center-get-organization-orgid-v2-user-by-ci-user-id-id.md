---
doc_id: webex-contact-center-get-organization-orgid-v2-user-by-ci-user-id-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/v2/user/by-ci-user-id/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.958015+00:00
---

# GET /organization/{orgid}/v2/user/by-ci-user-id/{id}

**API:** Webex Contact Center
**Área:** Users
**operationId:** `getUserByCiUserIdWithUserProfileGranularAccessUser`

## Resumen
Get specific User by CI User ID

## Descripción
Retrieve an existing User using the CI ID  in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: CI ID of the User.
- `includeUserProfile` [query] (boolean): Specifiy whether to include user profile data
- `includeNames` [query] (boolean): Specifiy whether to include resource collection names
- `includeSkillDetails` [query] (boolean): If set to true, the response includes skill information for each dynamic skill assignment.

## Respuestas
- **200**: OK
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
