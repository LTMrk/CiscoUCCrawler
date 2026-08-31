---
doc_id: webex-cloud-calling-get-telephony-config-premisepstn-trunks
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/premisePstn/trunks
operation_id: Read the List of Trunks
tags: Call Routing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.135537+00:00
---

# GET /telephony/config/premisePstn/trunks

**API:** Webex Cloud Calling
**Área:** Call Routing
**operationId:** `Read the List of Trunks`

## Resumen
Read the List of Trunks

## Descripción
List all Trunks for the organization.

A Trunk is a connection between Webex Calling and the premises, which terminates on the premises with a local gateway or other supported device.
The trunk can be assigned to a Route Group - a group of trunks that allow Webex Calling to distribute calls over multiple trunks or to provide redundancy.

Retrieving this list requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List trunks for this organization.
- `name` [query] (array): Return the list of trunks matching the local gateway names.
- `locationName` [query] (array): Return the list of trunks matching the location names.
- `trunkType` [query] (string): Return the list of trunks matching the trunk type.
- `max` [query] (number): Limit the number of objects returned to this maximum count.
- `start` [query] (number): Start at the zero-based offset in the list of matching objects.
- `order` [query] (string): Order the trunks according to the designated fields.  Available sort fields: name, locationName. Sort order is ascending by default

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/premisePstn/trunks' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `trunks` (array) (**requerido**): Array of trunks.
  - `id` (string) (**requerido**): Unique identifier for the trunk.
  - `name` (string) (**requerido**): A unique name for the trunk.
  - `location` (object): Location associated with the hot desking member.
    - `id` (string) (**requerido**): Unique identifier for the location.
    - `name` (string) (**requerido**): Name of the location.
  - `inUse` (boolean): Trunk in use flag.
  - `trunkType` (string): * `REGISTERING` - For Cisco CUBE Local Gateway.  * `CERTIFICATE_BASED` - For Cisco Unified Border Element, Oracle ACME Session Border Controller, AudioCodes Session Border Controller, Ribbon Session Border Controller. Valores: REGISTERING, CERTIFICATE_BASED.
  - `isRestrictedToDedicatedInstance` (boolean): Flag to indicate if the trunk is restricted to a dedicated instance.

### Ejemplo — respuesta 200
```json
{
  "trunks": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0RJQUxfUExBTi8wNTlhMjczZS1iYmIwLTExZWMtODQyMi0wMjQyYWMxMjAwMDI",
      "name": "trunkName",
      "location": {
        "id": "Y2lzY29zcGFyazovL3VzL0RJQUxfUExBTi8wNTlhMjczZS1iYmIwLTExZWMtODQyMi0wMjQyYWMxMjAwMDI",
        "name": "locationName"
      },
      "inUse": true,
      "trunkType": "REGISTERING",
      "isRestrictedToDedicatedInstance": true
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