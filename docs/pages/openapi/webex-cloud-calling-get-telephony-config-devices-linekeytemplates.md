---
doc_id: webex-cloud-calling-get-telephony-config-devices-linekeytemplates
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/devices/lineKeyTemplates
operation_id: readListOfLineKeyTemplates
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.995953+00:00
---

# GET /telephony/config/devices/lineKeyTemplates

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `readListOfLineKeyTemplates`

## Resumen
Read the list of Line Key Templates

## Descripción
List all Line Key Templates available for this organization.

Line Keys also known as Programmable Line Keys (PLK) are the keys found on either sides of a typical desk phone display.
A Line Key Template is a definition of actions that will be performed by each of the Line Keys for a particular device model.
This API allows users to retrieve the list of Line Key Templates that are available for the organization.

Retrieving this list requires a full, user or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List line key templates for this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/devices/lineKeyTemplates' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `lineKeyTemplates` (array) (**requerido**): Array of Line Key Templates.
  - `id` (string) (**requerido**): Unique identifier for the Line Key Template.
  - `templateName` (string) (**requerido**): Name of the Line Key Template.
  - `deviceModel` (string) (**requerido**): The Device Model for which the Line Key Template is applicable.
  - `modelDisplayName` (string) (**requerido**): The friendly display name used to represent the device model in Control Hub.

### Ejemplo — respuesta 200
```json
{
  "lineKeyTemplates": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0RFVklDRV9MSU5FX0tFWV9URU1QTEFURS9lYzVmMjg0Ni1iMDQ2LTQ5OGEtOWU2Mi04ZTg4ZWFlZmQyMGQ",
      "templateName": "template-for-8845",
      "deviceModel": "DMS Cisco 8845",
      "modelDisplayName": "Cisco 8845"
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