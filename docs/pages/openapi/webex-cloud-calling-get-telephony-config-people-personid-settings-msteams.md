---
doc_id: webex-cloud-calling-get-telephony-config-people-personid-settings-msteams
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/settings/msTeams
operation_id: getPersonMSTeamsSettings
tags: User Call Settings (2/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.768659+00:00
---

# GET /telephony/config/people/{personId}/settings/msTeams

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `getPersonMSTeamsSettings`

## Resumen
Retrieve a Person's MS Teams Settings

## Descripción
<div><Callout type="warning">Not supported for Webex for Government (FedRAMP)</Callout></div>

Retrieve a person's MS Teams settings.

At a person level, MS Teams settings allow access to retrieving the `HIDE WEBEX APP` and `PRESENCE SYNC` settings.

To retrieve a person's MS Teams settings requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter since the default is the same organization as the token used to access the API.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/settings/msTeams' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `personId` (string) (**requerido**): Unique identifier for the person.
- `orgId` (string) (**requerido**): Unique identifier for the organization in which the person resides.
- `settings` (array) (**requerido**): Array of `SettingsObject`.
  - `settingName` (string) (**requerido**): Name of the setting retrieved.  * `HIDE_WEBEX_APP` - Webex will continue to run but its windows will be closed by default. Users can still access Webex from the system tray on Windows or the Menu Bar on Mac.  * `PRESENCE_SYNC` - Sync presence status between Microsoft Teams and Webex. Valores: HIDE_WEBEX_APP, PRESENCE_SYNC.
  - `level` (string) (**requerido**): Level at which the `settingName` has been set.  * `GLOBAL` - `settingName` configured at the `GLOBAL` `level`.  * `ORGANIZATION` - `settingName` configured at the `ORGANIZATION` `level`.  * `GROUP` - `settingName` configured at the `GROUP` `level`.  * `PEOPLE` - `settingName` configured at the `PEOPLE` `level`. Valores: GLOBAL, ORGANIZATION, GROUP, PEOPLE.
  - `value` (boolean) (**requerido**): Either `true` or `false` for the respective `settingName` to be retrieved.
  - `lastModified` (string) (**requerido**): The date and time when the respective `settingName` was last updated.

### Ejemplo — respuesta 200
```json
{
  "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xMWEzZjk5MC1hNjg5LTQ3N2QtYmU2Yi03MTIwMDI1ZDhhYmI",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "settings": [
    {
      "settingName": "HIDE_WEBEX_APP",
      "level": "PEOPLE",
      "value": true,
      "lastModified": "2024-02-24T07:22:23.494198Z"
    },
    {
      "settingName": "PRESENCE_SYNC",
      "level": "ORGANIZATION",
      "value": false,
      "lastModified": "2024-02-24T07:21:23.494198Z"
    }
  ]
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