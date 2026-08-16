---
doc_id: webex-cloud-calling-delete-telephony-config-people-me-settings-selectiveaccept-criteria-id
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: DELETE
path: /telephony/config/people/me/settings/selectiveAccept/criteria/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.571857+00:00
---

# DELETE /telephony/config/people/me/settings/selectiveAccept/criteria/{id}

**API:** Webex Cloud Calling
**Área:** Call Settings For Me With UserHub Phase2
**operationId:** `deleteMySelectiveCallAcceptCriteria`

## Resumen
Delete a Selective Call Accept Criteria

## Descripción
Delete a Selective Call Accept Criteria for the authenticated user.



Selective Call Accept allows you to create customized rules to accept specific calls for users based on the phone number,identity and the time or day of the call.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Parámetros
- `id` [path] (string) **(requerido)**: The `id` parameter specifies the unique identifier for the selective call accept criteria. Example: `Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL1oxNzU0MzgzODQzNTA5NzY`.

## Respuestas
- **204**: Selective Call Accept Criteria deleted successfully. No content is returned.
- **400**: Bad Request: The request was invalid or cannot be otherwise served.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
