---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-dectnetworks-dectnetworkid-handsets-handsetid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/handsets/{handsetId}
operation_id: Update DECT Network Handset
tags: DECT Devices Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.549595+00:00
---

# PUT /telephony/config/locations/{locationId}/dectNetworks/{dectNetworkId}/handsets/{handsetId}

**API:** Webex Cloud Calling
**Área:** DECT Devices Settings
**operationId:** `Update DECT Network Handset`

## Resumen
Update DECT Network Handset

## Descripción
Update the line assignment on a handset.

A handset can have up to two lines, and a DECT network supports a total of 120 lines across all handsets.
A member on line1 of a DECT handset can be of type PEOPLE or PLACE while a member on line2 of a DECT handset can be of type PEOPLE, PLACE, or VIRTUAL_LINE.

Updating a DECT Network handset requires a full or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

<div><Callout type="warning">Adding a person with a Webex Calling Standard license to the DECT handset line1 will disable Webex Calling across their Webex mobile, tablet, desktop, and browser applications. 
Removing a person with a Webex Calling Standard license from the DECT handset line1 will enable Webex Calling across their Webex mobile, tablet, desktop, and browser applications.</Callout></div>

<div><Callout type="warning">Adding or removing handsets to the DECT network in less than 90 seconds may result in base station not having the latest configuration until the base station is rebooted.</Callout></div>

## Parámetros
- `locationId` [path] (string) (**requerido**): Location containing the DECT network.
- `dectNetworkId` [path] (string) (**requerido**): Update handset details in the specified DECT network.
- `handsetId` [path] (string) (**requerido**): A unique identifier for the handset.
- `orgId` [query] (string): Organization containing the DECT network.

## Cuerpo de la petición (application/json)
- `line1MemberId` (string) (**requerido**): ID of the member on line1 of the handset. Members can be PEOPLE or PLACE.
- `line2MemberId` (string): ID of the member on line2 of the handset. Members can be PEOPLE, PLACE, or VIRTUAL_LINE.
- `customDisplayName` (string) (**requerido**): Custom display name on the handset.

### Ejemplo — petición
```json
{
  "line1MemberId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMlm",
  "line2MemberId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMjk",
  "customDisplayName": "handsetDisplayName"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/dectNetworks/<dectNetworkId>/handsets/<handsetId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"line1MemberId": "<line1MemberId>", "customDisplayName": "<customDisplayName>"}'
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