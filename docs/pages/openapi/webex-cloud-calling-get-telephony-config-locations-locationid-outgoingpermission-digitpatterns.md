---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-outgoingpermission-digitpatterns
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/outgoingPermission/digitPatterns
operation_id: Get Outgoing Permission Digit Pattern for a Location
tags: Location Call Settings: Call Handling
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.341416+00:00
---

# GET /telephony/config/locations/{locationId}/outgoingPermission/digitPatterns

**API:** Webex Cloud Calling
**Área:** Location Call Settings: Call Handling
**operationId:** `Get Outgoing Permission Digit Pattern for a Location`

## Resumen
Get Outgoing Permission Digit Pattern for a Location

## Descripción
Get the digit patterns for the outbound permission in a location.

Use Digit Patterns to bypass the set permissions for all persons/workspaces at this location.

Retrieving digit patterns requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve the digit patterns for this location.
- `orgId` [query] (string): Retrieve the digit patterns for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/outgoingPermission/digitPatterns' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `digitPatterns` (array) (**requerido**): List of digit pattern information.
  - `id` (string) (**requerido**): A unique identifier for the digit pattern.
  - `name` (string) (**requerido**): A unique name for the digit pattern.
  - `pattern` (string) (**requerido**): The digit pattern to be matched with the input number.
  - `action` (string) (**requerido**): Action to be performed on the input number that matches the digit pattern.  * `ALLOW` - Allow the designated call type.  * `BLOCK` - Block the designated call type.  * `AUTH_CODE` - Allow only via Authorization Code.  * `TRANSFER_NUMBER_1` - Transfer to Auto Transfer Number 1. The answering person can then approve the call and send it through or reject the call.  * `TRANSFER_NUMBER_2` - Transfer to Auto Transfer Number 2. The answering person can then approve the call and send it through or reject the call.  * `TRANSFER_NUMBER_3` - Transfer to Auto Transfer Number 3. The answering person can then approve the call and send it through or reject the call. Valores: ALLOW, BLOCK, AUTH_CODE, TRANSFER_NUMBER_1, TRANSFER_NUMBER_2, TRANSFER_NUMBER_3.
  - `transferEnabled` (boolean) (**requerido**): If `true`, allows transfer and forwarding for the call type.

### Ejemplo — respuesta 200
```json
{
  "digitPatterns": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFL1FWVlVUMEZVVkVWT1JFRk9WQzFDVlZOSlRrVlRVeTFJVDFWU1V3",
      "name": "DigitPattern1",
      "pattern": "2XXXX",
      "action": "ALLOW",
      "transferEnabled": false
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL1NDSEVEVUxFL1FWVlVUMEZVVkVWT1JFRk9WQzFDVlZOSlRrVlRVeTFJVDFWU1V5",
      "name": "DigitPattern2",
      "pattern": "1XXXX",
      "action": "ALLOW",
      "transferEnabled": false
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