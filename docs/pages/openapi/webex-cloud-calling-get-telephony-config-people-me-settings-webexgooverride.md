---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-webexgooverride
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/webexGoOverride
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.560239+00:00
---

# GET /telephony/config/people/me/settings/webexGoOverride

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyWebexGoOverrideSettings`

## Resumen
Get My WebexGoOverride Settings

## Descripción
Retrieve "Mobile User Aware" override setting for Do Not Disturb feature.

When enabled, a mobile device will still ring even if Do Not Disturb, Quiet Hours, or Presenting Status are enabled.

When disabled, a mobile device will return busy for all incoming calls if Do Not Disturb, Quiet Hours, or Presenting Status are enabled.

It requires a user auth token with `spark:telephony_config_read` scope.

## Respuestas
- **200**: OK
  - `enabled` (boolean) **(requerido)**: True if the "Mobile User Aware" override setting for Do Not Disturb feature is enabled.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
