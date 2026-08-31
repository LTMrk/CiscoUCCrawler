---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-receptionistcontacts-directories
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/receptionistContacts/directories
operation_id: Create a Receptionist Contact Directory
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.298214+00:00
---

# POST /telephony/config/locations/{locationId}/receptionistContacts/directories

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Create a Receptionist Contact Directory`

## Resumen
Create a Receptionist Contact Directory

## Descripción
Create a new Receptionist Contact Directory for a location.

Receptionist Contact Directories can be used to create named directories of users and/or location features (Auto Attendant, Call Queue, Hunt Group, Single Number Reach, and Paging Group).

Adding a directory requires a full or write-only administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Add a Receptionist Contact Directory to this location.
- `orgId` [query] (string): Add a Receptionist Contact Directory to this organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Receptionist Contact Directory name. The directory name should be greater than 0 and less than 41 characters in length.
- `contacts` (array) (**requerido**): Non-empty array of users or location features assigned to this Receptionist Contact Directory.
  - `personId` (string): Person ID.
  - `featureId` (string): Location feature ID.
  - `type` (string): Types of users supported in receptionist contacts are People, Auto Attendant, Call Queue, Hunt Group, Single Number Reach, and Paging Group.

### Ejemplo — petición
```json
{
  "name": "test_directory",
  "contacts": [
    {
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8wNTUyZjY3Yi01OWE5LTQxYmItODczNi0xYjA0MWQxZGRkNWU"
    },
    {
      "featureId": "Y2lzY29zcGFyazovL3VzL0FVVE9fQVRURU5EQU5ULzA1NTJmNjdiLTU5YTktNDFiYi04NzM2LTFiMDQxZDFkZGQ1ZQ",
      "type": "AUTO_ATTENDANT"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/receptionistContacts/directories' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "contacts": []}'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Receptionist Contact Directory ID.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1NDSU1fR1JPVVAvZEdWemRGOWthWEpsWTNSdmNuaz06OTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh"
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