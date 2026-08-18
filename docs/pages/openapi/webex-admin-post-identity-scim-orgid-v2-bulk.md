---
doc_id: webex-admin-post-identity-scim-orgid-v2-bulk
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /identity/scim/{orgId}/v2/Bulk
operation_id: User bulk API
tags: Bulk Manage SCIM 2 Users and Groups
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.579903+00:00
---

# POST /identity/scim/{orgId}/v2/Bulk

**API:** Webex Admin
**Área:** Bulk Manage SCIM 2 Users and Groups
**operationId:** `User bulk API`

## Resumen
User bulk API

## Descripción
<br/>

**Authorization**

OAuth token rendered by Identity Broker.

<br/>

One of the following OAuth scopes is required:

- `identity:people_rw`

<br/>

**Usage**:

1. The input JSON must conform to the following schema: 'urn:ietf:params:scim:api:messages:2.0:BulkRequest'.

1. The request must be accompanied with a body in JSON format according to the standard SCIM schema definition.
   The maximum number of operations in a request is 100; an error is thrown if the limit is exceeded.

1. `failOnErrors` parameter

   An integer specifies the number of errors that the service provider will accept before the operation is terminated and an error response is returned.
   It is OPTIONAL in a request.
   Maximum number of operations allowed to fail before the server stops processing the request. The value must be between 1 and 100.

1. `operations` parameter

   Contains a list of bulk operations for POST/PATCH/DELETE operations. (REQUIRED)
    + `operations.method`

      The HTTP method of the current operation. Possible values are POST, PATCH or DELETE.
    + `operations.path`

      The Resource's relative path. If the method is POST the value must specify a Resource type endpoint;
      e.g., /Users or /Groups whereas all other method values must specify the path to a specific Resource;
      e.g., /Users/2819c223-7f76-453a-919d-413861904646.
    + `operations.data`

      The Resource data as it would appear for a single POST or PATCH Resource operation.
      It is REQUIRED in a request when method is POST and PATCH.
      Refer to corresponding wiki for SCIM 2.0 POST, PATCH and DELETE API.
    + `operations.bulkId`

      The transient identifier of a newly created resource, unique within a bulk request and created by the client.
      The bulkId serves as a surrogate resource id enabling clients to uniquely identify newly created resources in the response and cross-reference new resources in and across operations within a bulk request.
      It is REQUIRED when "method" is "POST".

## Parámetros
- `orgId` [path] (string) (**requerido**): Webex Identity assigned organization identifier for user's organization.

## Cuerpo de la petición (application/json)
- `schemas` (array) (**requerido**): Input JSON schemas.
- `failOnErrors` (number) (**requerido**): An integer specifying the maximum number of errors that the service provider will accept before the operation is terminated and an error response is returned.
- `operations` (array) (**requerido**): Contains a list of bulk operations for POST/PATCH/DELETE operations.
  - `method` (string) (**requerido**): The HTTP method of the current operation. Valores: POST, PATCH, DELETE.
  - `path` (string) (**requerido**): The resource's relative path. If the method is POST, the value must specify a resource type endpoint, for example `/Users` or `/Groups`. All other method values must specify the path to a specific resource.
  - `data` (string): The Resource JSON data as it appears for a single POST or PATCH resource operation.
  - `bulkId` (string): The transient identifier of a newly created resource, unique within a bulk request and created by the client.

### Ejemplo — petición
```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:BulkRequest"
  ],
  "failOnErrors": 99,
  "operations": [
    {
      "method": "PATCH",
      "path": "/Users/2819c223-7f76-453a-919d-413861904646",
      "data": "JSON text",
      "bulkId": "ytrewq"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/identity/scim/<orgId>/v2/Bulk' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"schemas": [], "failOnErrors": 0, "operations": []}'
```

## Respuestas correctas
**200**: OK
- `schemas` (array) (**requerido**): Input JSON schemas.
- `failOnErrors` (number) (**requerido**): An integer specifying the maximum number of errors that the service provider will accept before the operation is terminated and an error response is returned.
- `operations` (array) (**requerido**): Contains a list of bulk operations for POST/PATCH/DELETE operations.
  - `method` (string) (**requerido**): The HTTP method of the current operation. Valores: POST, PATCH, DELETE.
  - `path` (string) (**requerido**): The resource's relative path. If the method is POST, the value must specify a resource type endpoint, for example `/Users` or `/Groups`. All other method values must specify the path to a specific resource.
  - `data` (string): The Resource JSON data as it appears for a single POST or PATCH resource operation.
  - `bulkId` (string): The transient identifier of a newly created resource, unique within a bulk request and created by the client.

### Ejemplo — respuesta 200
```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:BulkResponse"
  ],
  "Operations": [
    {
      "location": "https://example.com/v2/Users/92b725cd-9465-4e7d-8c16-01f8e146b87a",
      "method": "POST",
      "bulkId": "qwerty",
      "version": "W/\"oY4m4wn58tkVjJxK\"",
      "status": "201"
    },
    {
      "location": "https://example.com/v2/Users/5d8d29d3-342c-4b5f-8683-a3cb6763ffcc",
      "method": "PATCH",
      "version": "W/\"huJj29dMNgu3WXPD\"",
      "status": "200"
    },
    {
      "location": "https://example.com/v2/Users/e9025315-6bea-44e1-899c-1e07454e468b",
      "method": "DELETE",
      "status": "204"
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
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs