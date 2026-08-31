---
doc_id: webex-cloud-calling-get-telephony-config-redsky-status
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/redSky/status
operation_id: Get the Organization Compliance Status for a RedSky Account
tags: Emergency Services Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.241487+00:00
---

# GET /telephony/config/redSky/status

**API:** Webex Cloud Calling
**Área:** Emergency Services Settings
**operationId:** `Get the Organization Compliance Status for a RedSky Account`

## Resumen
Get the Organization Compliance Status for a RedSky Account

## Descripción
Get the organization compliance status for a RedSky account. The `locationStatus.state` in the response will show the state for the location that is in the earliest stage of configuration.

The enhanced emergency (E911) service for Webex Calling provides an emergency service designed for organizations with a hybrid or nomadic workforce. It provides dynamic location support and a network that routes emergency calls to Public Safety Answering Points (PSAP) around the US, its territories, and Canada.

To retrieve organization compliance status requires a full, user or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): Retrieve the compliance status for the organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/redSky/status' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `orgStatus` (string) (**requerido**): * `INITIALISE` - RedSky account configuration process is in progress.  * `ENABLED` - RedSky account configuration process is complete.  * `OPTED_OUT` - Customer has opted out of the E911 service. Valores: INITIALISE, ENABLED, OPTED_OUT.
- `complianceStatus` (string) (**requerido**): * `OPTED_OUT` - Customer has opted out of the E911 service.  * `EXEMPTED` - RedSky account compliance status has been exempted.  * `NON_COMPLIANT` - RedSky account is non-compliant.  * `COMPLIANT` - RedSky account is compliant. Valores: OPTED_OUT, EXEMPTED, NON_COMPLIANT, COMPLIANT.
- `companyId` (string): The RedSky held token from the secret response.
- `redSkyOrgId` (string): The RedSky organization ID for the organization which can be found in the RedSky portal.
- `adminExists` (boolean): `true` if an Admin has been created in RedSky.
- `locationsStatus` (object):
  - `state` (string): * `LOCATION_SETUP` - RedSky account is pending location setup.  * `ALERTS` - RedSky account is pending email notification configuration.  * `NETWORK_ELEMENTS` - RedSky account is pending network element setup.  * `ROUTING_ENABLE` - RedSky account is pending the routing enable setup stage. Valores: LOCATION_SETUP, ALERTS, NETWORK_ELEMENTS, ROUTING_ENABLE.
  - `count` (number): Total count of locations available in the organization.
  - `locations` (array): List of locations that have completed the least amount of setup. Only 4 locations are included in this list.
    - `id` (string) (**requerido**): Unique identifier for the location.
    - `name` (string) (**requerido**): Name of the location.

### Ejemplo — respuesta 200
```json
{
  "orgStatus": "INITIALISE",
  "complianceStatus": "NON_COMPLIANT",
  "companyId": "ddd1424c-5b48-433d-9bab-061cdfb84c90",
  "redSkyOrgId": "2ff43e05-af11-41ff-91b6-87a3b509f4z4",
  "adminExists": true,
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