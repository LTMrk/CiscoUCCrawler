---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-callcaptions
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/callCaptions
operation_id: getMyCallCaptionsSettings
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.967865+00:00
---

# GET /telephony/config/people/me/settings/callCaptions

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyCallCaptionsSettings`

## Resumen
Get my call captions settings

## Descripción
Retrieve the effective call captions settings of the authenticated user.

**NOTE**: The call captions feature is not supported for Webex Calling Standard users or users assigned to locations in India.

The call caption feature allows the customer to enable and manage closed captions and transcript functionality (rolling caption panel) in Webex Calling, without requiring the user to escalate the call to a meeting.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/callCaptions' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `userClosedCaptionsEnabled` (boolean) (**requerido**): User-level closed captions are enabled or disabled.
- `userTranscriptsEnabled` (boolean) (**requerido**): User-level transcripts are enabled or disabled.
- `locationClosedCaptionsEnabled` (boolean) (**requerido**): Location closed captions are enabled or disabled. If `useOrgSettingsEnabled` is `true`, these are organization-level settings. Otherwise, location-level settings are used.
- `locationTranscriptsEnabled` (boolean) (**requerido**): Location transcripts are enabled or disabled. If `useOrgSettingsEnabled` is `true`, these are organization-level settings. Otherwise, location-level settings are used.
- `useLocationSettingsEnabled` (boolean) (**requerido**): If `useLocationSettingsEnabled` is `true`, location settings will control the user's closed captions and transcripts. Otherwise, user-level settings are used.

### Ejemplo — respuesta 200
```json
{
  "userClosedCaptionsEnabled": true,
  "userTranscriptsEnabled": true
}
```

## Respuestas de error
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

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs