---
doc_id: webex-cloud-calling-get-telephony-pstn-locations-locationid-connection
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/pstn/locations/{locationId}/connection
operation_id: Retrieve PSTN Connection for a Location
tags: PSTN
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.745424+00:00
---

# GET /telephony/pstn/locations/{locationId}/connection

**API:** Webex Cloud Calling
**Área:** PSTN
**operationId:** `Retrieve PSTN Connection for a Location`

## Resumen
Retrieve PSTN Connection for a Location

## Descripción
Retrieves the current configured PSTN connection details for a location.

PSTN location connection settings enables the admin to configure or change the PSTN provider for a location.

Retrieving the PSTN connection details for a location requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_pstn_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve PSTN location connection details for this location.
- `orgId` [query] (string): Retrieve PSTN location connection details for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/pstn/locations/<locationId>/connection' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for the connection.
- `displayName` (string): The display name of the PSTN connection.
- `pstnServices` (array): The PSTN services available for this connection.
- `pstnConnectionType` (string) (**requerido**): * `LOCAL_GATEWAY` - PSTN connection type for a premises-based connection.  * `NON_INTEGRATED_CCP` - PSTN connection type for a Non-Integrated Cloud Connected PSTN connection.  * `INTEGRATED_CCP` - PSTN connection type for an Integrated Cloud Connected PSTN connection. Updating the location with this connection type is currently not supported using the API.  * `CISCO_PSTN` - PSTN connection type for a Cisco PSTN connection. Updating the location with this connection type is currently not supported using the API. Valores: LOCAL_GATEWAY, NON_INTEGRATED_CCP, INTEGRATED_CCP, CISCO_PSTN.
- `routeType` (string): * `ROUTE_GROUP` - A route group has been selected for premises-based PSTN.  * `TRUNK` - A trunk group has been selected for premises-based PSTN. Valores: ROUTE_GROUP, TRUNK.
- `routeId` (string): Premise route ID. This refers to either a Trunk ID or a Route Group ID. This field is optional but required if the connection type is LOCAL_GATEWAY.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1BTVE5fQ09OTkVDVElPTi81MWRlNDg5Yy1hYTYwLTRjMjUtOWFmNi1jYzRjYjE3MTczMGU",
  "displayName": "Premises-based PSTN",
  "pstnServices": [
    "GEOGRAPHIC_NUMBERS"
  ],
  "pstnConnectionType": "LOCAL_GATEWAY",
  "routeType": "TRUNK",
  "routeId": "Y2lzY29zcGFyazovL3VzL1RSVU5LL2Y1YTU4MzAwLTVmZTYtNGNjMS1hODA3LTRlN2E5OTMzN2Q0ZA"
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