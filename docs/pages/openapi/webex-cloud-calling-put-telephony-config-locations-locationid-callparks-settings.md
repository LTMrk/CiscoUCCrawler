---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-callparks-settings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/callParks/settings
operation_id: updateCallParkSettings
tags: Features:  Call Park
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T14:22:47.297292+00:00
---

# PUT /telephony/config/locations/{locationId}/callParks/settings

**API:** Webex Cloud Calling
**Área:** Features:  Call Park
**operationId:** `updateCallParkSettings`

## Resumen
Update Call Park settings

## Descripción
Update Call Park settings for the designated location.

Call Park allows call recipients to place a call on hold so that it can be retrieved from another device.

Updating call park settings requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location for which call park settings will be updated.
- `orgId` [query] (string): Update call park settings from this organization.

## Cuerpo de la petición (application/json)
- `callParkRecall` (object): Recall options that are added to call park.
- `callParkSettings` (object): Setting controlling call park behavior.

### Ejemplo — petición
```json
{
  "callParkRecall": {
    "huntGroupId": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvZEdWamFHNXBZMkZzTFhOMWNIQnZjblF0TlRVMU9EWTNOVE13T1VCbmJXRnBiQzVqYjIwPQ",
    "huntGroupName": "Technical Support Group - 5558675309",
    "option": "ALERT_HUNT_GROUP_ONLY"
  },
  "callParkSettings": {
    "ringPattern": "NORMAL",
    "recallTime": 45,
    "huntWaitTime": 45
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/callParks/settings' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
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