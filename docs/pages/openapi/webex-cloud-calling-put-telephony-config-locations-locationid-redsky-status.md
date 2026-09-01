---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-redsky-status
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/redSky/status
operation_id: Update a Location's RedSky Compliance Status
tags: Emergency Services Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.672042+00:00
---

# PUT /telephony/config/locations/{locationId}/redSky/status

**API:** Webex Cloud Calling
**Área:** Emergency Services Settings
**operationId:** `Update a Location's RedSky Compliance Status`

## Resumen
Update a Location's RedSky Compliance Status

## Descripción
Update the compliance status for a specific location.

The Enhanced Emergency (E911) Service for Webex Calling provides dynamic location support and a network that routes emergency calls to Public Safety Answering Points (PSAP) around the US, its territories, and Canada. E911 services are provided in conjunction with a RedSky account.

Updating the RedSky account's compliance status requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Update the E911 compliance status for this location.
- `orgId` [query] (string): Update the E911 compliance status for the location in this organization.

## Cuerpo de la petición (application/json)
- `complianceStatus` (string) (**requerido**): * `OPTED_OUT` - Customer has opted out of the E911 service.  * `LOCATION_SETUP` - Building and locations stage of the RedSky account creation has been completed.  * `ALERTS` - Email notification configuration stage of the RedSky account creation has been completed.  * `NETWORK_ELEMENTS` - Network wire map configuration stage of the RedSky account creation process has been completed and Webex Calling will begin routing emergency test number calls (933) to RedSky.  * `ROUTING_ENABLED` - Emergency calls for devices in the specified locations will begin to route to RedSky. Valores: OPTED_OUT, LOCATION_SETUP, ALERTS, NETWORK_ELEMENTS, ROUTING_ENABLED.

### Ejemplo — petición
```json
{
  "complianceStatus": "LOCATION_SETUP"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/redSky/status' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"complianceStatus": "<complianceStatus>"}'
```

## Respuestas correctas
**200**: OK
- `locationsStatus` (object):
  - `state` (string): * `OPTED_OUT` - Customer has opted out of the E911 service.  * `EXEMPTED` - RedSky account compliance status has been exempted.  * `LOCATION_SETUP` - RedSky account is pending location setup.  * `ALERTS` - RedSky account is pending email notification configuration.  * `NETWORK_ELEMENTS` - RedSky account is pending network element setup.  * `ROUTING_ENABLE` - RedSky account is pending the routing enable setup stage.  * `COMPLIANT` - RedSky account is compliant. Valores: OPTED_OUT, EXEMPTED, LOCATION_SETUP, ALERTS, NETWORK_ELEMENTS, ROUTING_ENABLE, COMPLIANT.
  - `count` (number): Total count of the `locations` list.
  - `locations` (array): Object that contains the `id` and the `name` for the location in the request.
    - `id` (string) (**requerido**): Unique identifier for the location.
    - `name` (string) (**requerido**): Name of the location.

### Ejemplo — respuesta 200
```json
{
  "locationsStatus": {
    "state": "LOCATION_SETUP",
    "count": 2,
    "locations": [
      {
        "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTA5OA",
        "name": "MainOffice"
      }
    ]
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