---
doc_id: webex-cloud-calling-put-telephony-config-people-me-settings-executive-callfiltering
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/people/me/settings/executive/callFiltering
operation_id: updateMyExecutiveCallFilteringSettings
tags: Beta Call Settings For Me With Userhub Phase1
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.364542+00:00
---

# PUT /telephony/config/people/me/settings/executive/callFiltering

**API:** Webex Cloud Calling
**Área:** Beta Call Settings For Me With Userhub Phase1
**operationId:** `updateMyExecutiveCallFilteringSettings`

## Resumen
Modify User Executive Call Filtering Settings

## Descripción
Update executive call filtering settings for the authenticated user.

Executive Call Filtering in Webex allows you to control which calls are allowed to reach the executive assistant based on custom criteria, such as specific phone numbers or call types. You can enable or disable call filtering and configure filter rules to manage incoming calls.

This API requires a user auth token with a scope of `spark:telephony_config_write`.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): Set to `true` to enable executive call filtering or `false` to disable it.
- `filterType` (string): * `CUSTOM_CALL_FILTERS` - Choose this option to ensure that only specific calls are sent to the executive assistant.  * `ALL_CALLS` - Choose this option to send both internal and external calls to the executive assistant.  * `ALL_INTERNAL_CALLS` - Choose this option to send all internal calls to the executive assistant.  * `ALL_EXTERNAL_CALLS` - Choose this option to send all external calls to the executive assistant. Valores: CUSTOM_CALL_FILTERS, ALL_CALLS, ALL_INTERNAL_CALLS, ALL_EXTERNAL_CALLS.
- `criteriaActivation` (array): The list of criteria activation settings to update for executive call filtering.
  - `id` (string) (**requerido**): Unique identifier for the filter criteria.
  - `activationEnabled` (boolean) (**requerido**): Controls whether this filter criteria is active. When `true`, the criteria is evaluated for incoming calls. When `false`, the criteria is completely ignored and has no effect on call filtering.

### Ejemplo — petición
```json
{
  "enabled": true,
  "filterType": "CUSTOM_CALL_FILTERS",
  "criteriaActivation": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0NSSVRFUklBL2RHVnpkRjltYVd4MFpYST0",
      "activationEnabled": true
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/people/me/settings/executive/callFiltering' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: Executive call filtering settings modified successfully.

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