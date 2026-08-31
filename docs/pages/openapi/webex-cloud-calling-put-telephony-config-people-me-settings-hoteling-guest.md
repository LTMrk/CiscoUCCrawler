---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-hoteling-guest
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/me/settings/hoteling/guest
operation_id: updateHotelingGuestSettings
tags: Call Settings For Me Phase 5
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.173354+00:00
---

# PUT /telephony/config/people/me/settings/hoteling/guest

**API:** Webex Cloud Calling
**Área:** Call Settings For Me Phase 5
**operationId:** `updateHotelingGuestSettings`

## Resumen
Update Hoteling Guest Settings

## Descripción
Update hoteling guest settings for a person. Allows enabling or disabling the ability to use hoteling as a guest, configuring whether an association will be removed automatically after a specified time period, and associating with a hoteling host.

Hoteling is a feature of Webex Calling that enables flexible workspace solutions by allowing users to log into shared devices.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Cuerpo de la petición (application/json)
- `enabled` (boolean) (**requerido**): Enable/Disable hoteling guest functionality for the person. When enabled, the person can associate themselves with a hoteling host device.
- `associationLimitEnabled` (boolean): When enabled, the person's hoteling guest association will be automatically removed after the specified time period.
- `associationLimitHours` (integer): Time limit in hours for the hoteling guest association (1-999). Applicable when associationLimitEnabled is true.
- `hostId` (string): Unique identifier of the hoteling host person or workspace to associate with. Required when enabling hoteling guest functionality.

### Ejemplo — petición
```json
{
  "enabled": true,
  "associationLimitEnabled": true,
  "associationLimitHours": 12,
  "hostId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hYmNkZWYxMi0zNDU2LTc4OTAtYWJjZC1lZjEyMzQ1Njc4OTA"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/me/settings/hoteling/guest' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"enabled": true}'
```

## Respuestas correctas
**204**: No Content: Hoteling guest settings successfully updated.

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