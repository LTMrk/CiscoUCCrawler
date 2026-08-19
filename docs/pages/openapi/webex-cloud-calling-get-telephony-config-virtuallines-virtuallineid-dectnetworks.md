---
doc_id: webex-cloud-calling-get-telephony-config-virtuallines-virtuallineid-dectnetworks
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/virtualLines/{virtualLineId}/dectNetworks
operation_id: Get List of DECT Networks Handsets for a Virtual Line
tags: Virtual Line Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.175271+00:00
---

# GET /telephony/config/virtualLines/{virtualLineId}/dectNetworks

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Get List of DECT Networks Handsets for a Virtual Line`

## Resumen
Get List of DECT Networks Handsets for a Virtual Line

## Descripción
<div><Callout type="warning">Not supported for Webex for Government (FedRAMP)</Callout></div>

Retrieve DECT Network details assigned for a virtual line.

Virtual line is a capability in Webex Calling that allows administrators to configure multiple lines to Webex Calling users.

Retrieving the assigned device detials for a virtual line requires a full, user, or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `virtualLineId` [path] (string) (**requerido**): Retrieve settings for a virtual line with the matching ID.
- `orgId` [query] (string): Retrieve virtual line settings from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/virtualLines/<virtualLineId>/dectNetworks' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `dectNetworks` (array): List of DECT networks assigned to a virtual line.
  - `id` (string) (**requerido**): Unique identifier for a DECT network.
  - `name` (string) (**requerido**): Identifier for device DECT network.
  - `primaryEnabled` (boolean) (**requerido**): Indicates whether the virtual profile is the primary line.
  - `numberOfHandsetsAssigned` (number) (**requerido**): Number of DECT handsets assigned to the virtual profile.
  - `location` (object) (**requerido**): Location details of virtual line.
    - `id` (string) (**requerido**): ID of location associated with virtual line.
    - `name` (string) (**requerido**): Name of location associated with virtual line.

### Ejemplo — respuesta 200
```json
{
  "dectNetworks": [
    {
      "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL0RFVklDRS9hNmYwYjhkMi01ZjdkLTQzZDItODAyNi0zM2JkNDg3NjYzMTg=",
      "name": "Dect Network1",
      "primaryEnabled": false,
      "numberOfHandsetsAssigned": 1,
      "location": {
        "name": "Main Location Test",
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzMxMTYx"
      }
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