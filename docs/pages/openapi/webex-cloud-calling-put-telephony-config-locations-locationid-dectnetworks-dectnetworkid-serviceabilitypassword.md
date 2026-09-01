---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-dectnetworks-dectnetworkid-serviceabilitypassword
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/serviceabilityPassword
operation_id: Update DECT Serviceability Password Status
tags: DECT Devices Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.551337+00:00
---

# PUT /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/serviceabilityPassword

**API:** Webex Cloud Calling
**Área:** DECT Devices Settings
**operationId:** `Update DECT Serviceability Password Status`

## Resumen
Update DECT Serviceability Password Status

## Descripción
Enables or disables the DECT serviceability password.

<div><Callout type="warning">Enabling or disabling the password and transmitting it to the DECT network can reboot the entire network. Be sure you choose an appropriate time for this action.</Callout></div>

<div><Callout type="info">If enabling is requested, but the serviceability password has not been generated, we will not actively reject the request even though there is no serviceability password.</Callout></div>

The DECT serviceability password, also known as the admin override password, provides read/write access to DECT base stations for performing system serviceability and troubleshooting functions.

This API requires a full or location administrator auth token with the scope of `spark-admin:telephony_config_write`, or a device administrator token with the scope of `spark-admin:devices_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Unique identifier for the location.
- `dectNetworkId` [path] (string) (**requerido**): Unique identifier for the DECT network.
- `orgId` [query] (string): Unique identifier for the organization.

## Cuerpo de la petición (application/json)
- `enabled` (boolean) (**requerido**): DECT serviceability password status. When `enabled` is set to `true`, the serviceability password can be used to manage DECT. When `enabled` is set to `false`, the serviceability password is disabled and the password owned and known by Cisco is required to perform serviceability and troubleshooting.

### Ejemplo — petición
```json
{
  "enabled": "true"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/dectNetworks/<dectNetworkId>/serviceabilityPassword' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"enabled": true}'
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