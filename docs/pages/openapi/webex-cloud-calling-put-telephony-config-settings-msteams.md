---
doc_id: webex-cloud-calling-put-telephony-config-settings-msteams
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/settings/msTeams
operation_id: Update an Organization's MS Teams Setting
tags: Client Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.389535+00:00
---

# PUT /telephony/config/settings/msTeams

**API:** Webex Cloud Calling
**Área:** Client Call Settings
**operationId:** `Update an Organization's MS Teams Setting`

## Resumen
Update an Organization's MS Teams Setting

## Descripción
<div><Callout type="warning">Not supported for Webex for Government (FedRAMP)</Callout></div>

Update an MS Teams setting.

MS Teams setting can be updated at the organization level.

Requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Update MS Teams setting value for the organization.

## Cuerpo de la petición (application/json)
- `settingName` (string) (**requerido**): The enum value, either `HIDE_WEBEX_APP` or `PRESENCE_SYNC`, for the respective `settingName` to be updated.  * `HIDE_WEBEX_APP` - Webex will continue to run but its windows will be closed by default. Users can still access Webex from the system tray on Windows or the Menu Bar on Mac.  * `PRESENCE_SYNC` - Sync presence status between Microsoft Teams and Webex. Valores: HIDE_WEBEX_APP, PRESENCE_SYNC.
- `value` (boolean) (**requerido**): The boolean value, either `true` or `false`, for the respective `settingName` to be updated.

### Ejemplo — petición
```json
{
  "settingName": "HIDE_WEBEX_APP",
  "value": true
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/settings/msTeams' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"settingName": "<settingName>", "value": true}'
```

## Respuestas correctas
**204**: No Content

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