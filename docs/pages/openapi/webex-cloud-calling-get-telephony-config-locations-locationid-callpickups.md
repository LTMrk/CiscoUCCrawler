---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-callpickups
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/callPickups
operation_id: Read the List of Call Pickups
tags: Features:  Call Pickup
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.687776+00:00
---

# GET /telephony/config/locations/{locationId}/callPickups

**API:** Webex Cloud Calling
**Área:** Features:  Call Pickup
**operationId:** `Read the List of Call Pickups`

## Resumen
Read the List of Call Pickups

## Descripción
List all Call Pickups for the organization.

Call Pickup enables a user (agent) to answer any ringing line within their pickup group.

Retrieving this list requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

**NOTE**: The Call Pickup ID will change upon modification of the Call Pickup name.

## Parámetros
- `locationId` [path] (string) (**requerido**): Return the list of call pickups for this location.
- `orgId` [query] (string): List call pickups for this organization.
- `max` [query] (number): Limit the number of call pickups returned to this maximum count. Default is 2000.
- `start` [query] (number): Start at the zero-based offset in the list of matching call pickups. Default is 0.
- `order` [query] (string): Sort the list of call pickups by name, either ASC or DSC. Default is ASC.
- `name` [query] (string): Return the list of call pickups that contains the given name. The maximum length is 80.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/callPickups' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `callPickups` (array) (**requerido**): Array of call pickups.
  - `name` (string) (**requerido**): Unique name for the call pickup. The maximum length is 80.
  - `id` (string) (**requerido**): A unique identifier for the call pickup.
  - `locationName` (string) (**requerido**): Name of the location for call pickup.
  - `locationId` (string) (**requerido**): ID of the location for call pickup.

### Ejemplo — respuesta 200
```json
{
  "callPickups": [
    {
      "name": "North Alaska-Group",
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUElDS1VQL1kyRnNiRkJwWTJ0MWNERT0",
      "locationName": "Alaska",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzEyMzQ1"
    },
    {
      "name": "South Alaska-Group",
      "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUElDS1VQL1kyRnNiRkJwWTJ0MWNEST0",
      "locationName": "Alaska",
      "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzEyMzQ1"
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