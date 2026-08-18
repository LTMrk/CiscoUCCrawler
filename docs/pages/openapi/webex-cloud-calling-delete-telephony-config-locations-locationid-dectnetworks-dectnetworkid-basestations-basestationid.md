---
doc_id: webex-cloud-calling-delete-telephony-config-locations-locationid-dectnetworks-dectnetworkid-basestations-basestationid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: DELETE
path: /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/baseStations/{baseStationId}
operation_id: Delete a Specific DECT Network Base Station
tags: DECT Devices Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.149000+00:00
---

# DELETE /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/baseStations/{baseStationId}

**API:** Webex Cloud Calling
**Área:** DECT Devices Settings
**operationId:** `Delete a Specific DECT Network Base Station`

## Resumen
Delete a Specific DECT Network Base Station

## Descripción
Delete a specific base station in the DECT Network.

A DECT network supports 2 types of base stations, DECT DBS-110 Single-Cell and DECT DBS-210 Multi-Cell.
A DECT DBS-110 allows up to 30 lines of registration and supports 1 base station only. A DECT DBS-210 can have up to 254 base stations and supports up to 1000 lines of registration.

This API requires a full or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location containing the DECT network.
- `dectNetworkId` [path] (string) (**requerido**): Delete a specific base station in the specified DECT network ID.
- `baseStationId` [path] (string) (**requerido**): Delete the specific DECT base station ID.
- `orgId` [query] (string): Organization containing the DECT network.

## Ejemplo de invocación
```bash
curl -X DELETE '/telephony/config/locations/<locationId>/dectNetworks/<dectNetworkId>/baseStations/<baseStationId>' \
  -H 'Authorization: Bearer <TOKEN>'
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