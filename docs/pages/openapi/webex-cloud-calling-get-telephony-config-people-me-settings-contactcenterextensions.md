---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-contactcenterextensions
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/contactCenterExtensions
operation_id: readTheContactCenterExtensions
tags: 
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T14:22:47.277671+00:00
---

# GET /telephony/config/people/me/settings/contactCenterExtensions

**API:** Webex Cloud Calling
**operationId:** `readTheContactCenterExtensions`

## Resumen
Read the Contact Center Extensions

## Descripción
Retrieves the Contact Center phone number, extension, virtual numbers, endpoints, and endpoints registration status associated with the authenticated user. This API returns all primary and secondary endpoints, the hot desk guest profiles currently hosted on the agent's own devices, if any, and registration status of those endpoints. Only virtual line extensions hosted exclusively on the agent's devices and the registration status of those virtual line endpoints will be retrieved. Any virtual lines shared with devices not owned by the current user will be excluded.

 A Webex Calling Contact Center extension is a calling extension assigned to a user or device within the Webex Contact Center for internal dialing.

This API requires a user auth token with a scope of spark:telephony_config_read.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/contactCenterExtensions' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `ccExtensions` (array) (**requerido**): List of user extensions.
  - `directNumber` (string) (**requerido**): Direct number of the user.
  - `extension` (string) (**requerido**): Extension of the user.
  - `type` (object) (**requerido**): Type of User Extension.
  - `lineOwnerType` (object) (**requerido**): Type of the line owner. Indicates whether the line is owned by a person, workspace, or virtual line.
  - `lineOwnerId` (string) (**requerido**): Unique identifier of the line owner.
  - `preferredAnsweringEndPointId` (string) (**requerido**): Unique identifier of the set preferred answering endpoint.
  - `endpoints` (array) (**requerido**): List of user endpoints with type.
    - `id` (string) (**requerido**): Unique identifier of the endpoint.
    - `type` (object) (**requerido**): Type of the endpoint.
- `endpoints` (array) (**requerido**): List of user endpoints details.
  - `id` (string) (**requerido**): Unique identifier of the endpoint.
  - `type` (object) (**requerido**): Type of the endpoint.
  - `name` (string) (**requerido**): Name of the endpoint.
  - `status` (object) (**requerido**): SIP Registration status of the device.

### Ejemplo — respuesta 200
```json
{
  "ccExtensions": [
    {
      "directNumber": "+13374831550",
      "extension": "1550",
      "type": "PRIMARY",
      "lineOwnerType": "PEOPLE",
      "lineOwnerId": "Y2lzY29zcGFyazovL3VzL1ZJUlRVQUxfTElORS85NWM4MGY0My1mNjBlLTQzYTAtYTkwMy1iNWQ3ZDg0MThiNDU",
      "preferredAnsweringEndPointId": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL2Q0OTE3ZWFiLTQ4Y2EtNGRlZC1iOTczLWQzNTFhOTU5OWZhZB",
      "endpoints": [
        {
          "id": "Y2lzY29zcGFyazovL3VzL0hPVERFU0tJTkdfR1VFU1QvNDE1YjFkODUtZDA3NS00ZTNmLWExMGItMGVjOGExMjRjMWQ4",
          "type": "HOTDESKING_GUEST"
        },
        {
          "id": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL2Q0OTE3ZWFiLTQ4Y2EtNGRlZC1iOTczLWQzNTFhOTU5OWZhZB",
          "type": "CALLING_DEVICE"
        },
        {
          "id": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL2QxYzM5M2QwLTg1M2ItNDc3MC1iZjA1LWQyMDU2MWRhM2NjZh",
          "type": "APPLICATION"
        }
      ]
    }
  ],
  "endpoints": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0hPVERFU0tJTkdfR1VFU1QvNDE1YjFkODUtZDA3NS00ZTNmLWExMGItMGVjOGExMjRjMWQ4",
      "type": "HOTDESKING_GUEST",
      "name": "Cisco HotDesking",
      "status": "CONNECTED"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL2Q0OTE3ZWFiLTQ4Y2EtNGRlZC1iOTczLWQzNTFhOTU5OWZhZB",
      "type": "CALLING_DEVICE",
      "name": "Cisco 9841",
      "status": "CONNECTED"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL2QxYzM5M2QwLTg1M2ItNDc3MC1iZjA1LWQyMDU2MWRhM2NjZh",
      "type": "APPLICATION",
     
  ... (truncado)
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