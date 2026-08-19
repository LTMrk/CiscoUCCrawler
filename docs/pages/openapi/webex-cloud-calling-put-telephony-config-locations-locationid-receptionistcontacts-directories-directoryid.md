---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-receptionistcontacts-directories-directoryid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/receptionistContacts/directories/{directoryId}
operation_id: Modify a Receptionist Contact Directory
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.117430+00:00
---

# PUT /telephony/config/locations/{locationId}/receptionistContacts/directories/{directoryId}

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Modify a Receptionist Contact Directory`

## Resumen
Modify a Receptionist Contact Directory

## Descripción
Modify Receptionist Contact Directories attached to a location. This modification will replace the existing list of contacts with the new incoming contacts list from the request body. The API does not support incremental updates.

Receptionist Contact Directories can be used to create named groups of Persons, Auto Attendants, Call Queues, Hunt Groups, Single Number Reaches, and Paging Groups.

Modifying a directory requires a full or write-only administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Modify list of Receptionist Contact Directories for this location.
- `directoryId` [path] (string) (**requerido**): Get details for the Receptionist Contact Directory with this identifier.
- `orgId` [query] (string): Modify list of Receptionist Contact Directories for this organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Receptionist Contact Directory name. The directory name should be greater than 0 and less than 41 characters in length.
- `contacts` (array) (**requerido**): Non-empty array of users or location features assigned to this Receptionist Contact Directory.

### Ejemplo — petición
```json
{
  "name": "test_directory",
  "contacts": [
    "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMjk"
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/receptionistContacts/directories/<directoryId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "contacts": []}'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): ID of the newly created Receptionist directory name.

### Ejemplo — respuesta 200
```json
{
  "name": "test_directory",
  "contacts": [
    "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jODhiZGIwNC1jZjU5LTRjMjMtODQ4OC00NTNhOTE3ZDFlMjk"
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