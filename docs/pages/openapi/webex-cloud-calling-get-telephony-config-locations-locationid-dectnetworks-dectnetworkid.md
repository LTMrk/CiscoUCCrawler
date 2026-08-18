---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-dectnetworks-dectnetworkid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}
operation_id: Get DECT Network Details
tags: DECT Devices Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.147575+00:00
---

# GET /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}

**API:** Webex Cloud Calling
**Área:** DECT Devices Settings
**operationId:** `Get DECT Network Details`

## Resumen
Get DECT Network Details

## Descripción
Retrieves the details of a DECT network.

DECT Networks provide roaming voice services via base stations and wireless handsets. A DECT network can be provisioned up to 1000 lines across up to 254 base stations.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Details of the DECT network at this location.
- `dectNetworkId` [path] (string) (**requerido**): Details of the specified DECT network.
- `orgId` [query] (string): Details of the DECT network in this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/dectNetworks/<dectNetworkId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for the DECT network.
- `name` (string) (**requerido**): Name of the DECT network. This should be unique across the location.
- `displayName` (string): DECT network name displayed on the handset.
- `chainId` (number) (**requerido**): Chain ID of the DECT network.
- `model` (string) (**requerido**): * `DMS Cisco DBS210` - Cisco DBS210 base station model.  * `DMS Cisco DBS110` - Cisco DBS110 base station model. Valores: DMS Cisco DBS210, DMS Cisco DBS110.
- `defaultAccessCodeEnabled` (boolean) (**requerido**): Default access code is enabled. If true, the default access code is mandatory. If false, auto-generated access code is used.
- `defaultAccessCode` (string) (**requerido**): Default access code for the DECT network. The default access code should be unique within the same location to avoid the handset accidentally registering with base stations from different DECT networks in range. This is mandatory when `defaultAccessCodeEnabled` is true.
- `numberOfBaseStations` (number) (**requerido**): Number of base stations in the DECT network.
- `numberOfHandsetsAssigned` (number) (**requerido**): Number of handsets assigned to the DECT network.
- `numberOfLines` (number) (**requerido**): Number of lines in the DECT network.
- `location` (object) (**requerido**):
  - `id` (string) (**requerido**): Location identifier associated with the members.
  - `name` (string) (**requerido**): Location name associated with the member.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "name": "Demo-DectNetwork",
  "displayName": "Demo-DectNetwork",
  "chainId": 122456789,
  "model": "DMS Cisco DBS210",
  "defaultAccessCodeEnabled": true,
  "defaultAccessCode": "1234",
  "numberOfBaseStations": 2,
  "numberOfHandsetsAssigned": 5,
  "numberOfLines": 2,
  "location": {
    "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTA5OA",
    "name": "Cisco-HQ"
  }
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