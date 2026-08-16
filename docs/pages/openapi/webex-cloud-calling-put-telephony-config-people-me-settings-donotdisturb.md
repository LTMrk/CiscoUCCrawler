---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-donotdisturb
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/people/me/settings/doNotDisturb
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.567888+00:00
---

# PUT /telephony/config/people/me/settings/doNotDisturb

**API:** Webex Cloud Calling
**Área:** Beta Call Settings For Me With Userhub Phase1
**operationId:** `updateMyDoNotDisturbSettings`

## Resumen
Modify Do Not Disturb Settings for User

## Descripción
Update Do Not Disturb settings for the authenticated user.

Do Not Disturb (DND) enables users to block or silence incoming calls on their phone. When activated, the phone either stops ringing or rejects calls depending on the configured option, but users can still see call information and answer calls if desired.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): `true` if the Do Not Disturb feature is enabled.
- `ringSplashEnabled` (boolean): Enables a Ring Reminder to play a brief tone on your desktop phone when you receive incoming calls.
- `webexGoOverrideEnabled` (boolean) **(requerido)**: `true` if a mobile device will still ring even if Do Not Disturb is enabled.

### Ejemplo de petición
```json
{
  "enabled": true,
  "ringSplashEnabled": false,
  "webexGoOverrideEnabled": false
}
```

## Respuestas
- **204**: Do Not Disturb settings updated successfully for the authenticated user.
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
