---
doc_id: webex-cloud-calling-get-telephony-config-moh-settings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/moh/settings
operation_id: Get the organization Music on Hold configuration
tags: Calling Service Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.984377+00:00
---

# GET /telephony/config/moh/settings

**API:** Webex Cloud Calling
**Área:** Calling Service Settings
**operationId:** `Get the organization Music on Hold configuration`

## Resumen
Get the organization Music on Hold configuration

## Descripción
Retrieve the organization's Music on Hold settings.

## Parámetros
- `orgId` [query] (string): Retrieve Music on Hold settings for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/moh/settings' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `mohEnabled` (boolean) (**requerido**): Music on hold enabled or disabled for the workspace.
- `mohLocationEnabled` (boolean) (**requerido**): Music on hold enabled or disabled for the location. The music on hold setting returned in the response is used only when music on hold is enabled at the location level. When `mohLocationEnabled` is false and `mohEnabled` is true, music on hold is disabled for the workspace. When `mohLocationEnabled` is true and `mohEnabled` is false, music on hold is turned off for the workspace. In both cases, music on hold will not be played.
- `greeting` (string) (**requerido**): Greeting type for the workspace.  * `DEFAULT` - Play music configured at location level.  * `CUSTOM` - Play previously uploaded custom music when call is placed on hold or parked. Valores: DEFAULT, CUSTOM.
- `audioAnnouncementFile` (object):
  - `id` (string) (**requerido**): A unique identifier for the announcement.
  - `fileName` (string) (**requerido**): Audio announcement file name.
  - `mediaFileType` (string) (**requerido**): Audio announcement file type.  * `WAV` - WAV File Extension. Valores: WAV.
  - `level` (string) (**requerido**): Audio announcement file type location.  * `ORGANIZATION` - Specifies this audio file is configured across the organization.  * `LOCATION` - Specifies this audio file is configured across the location. Valores: ORGANIZATION, LOCATION.

### Ejemplo — respuesta 200
```json
{
  "defaultOrgMoh": "OPUS"
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