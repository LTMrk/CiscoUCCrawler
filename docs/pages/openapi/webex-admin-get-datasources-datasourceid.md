---
doc_id: webex-admin-get-datasources-datasourceid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /dataSources/{dataSourceId}
operation_id: Retrieve Data Source Details
tags: Data Sources
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.560715+00:00
---

# GET /dataSources/{dataSourceId}

**API:** Webex Admin
**Área:** Data Sources
**operationId:** `Retrieve Data Source Details`

## Resumen
Retrieve Data Source Details

## Descripción
Retrieves details for a data source by ID. Use a Service App token with the `spark-admin:datasource_read` scope.

## Parámetros
- `dataSourceId` [path] (string) (**requerido**): The unique identifier for the data source.

## Ejemplo de invocación
```bash
curl -X GET '/dataSources/<dataSourceId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `audience` (string): The JWT `aud` (audience) claim. This is usually the DAP application's name.
- `errorMessage` (string): The error message shown in Control Hub when `status` is set to `disabled`.
- `id` (string): The data source ID.
- `nonce` (string): A unique nonce used when encrypting the JWT.
- `schemaId` (string): The schema ID used for the data exchange.
- `status` (string): The data source status: `active` or `disabled`.
- `subject` (string): The JWT `sub` (subject) claim. This usually describes the application's function.
- `tokenLifetimeMinutes` (number): The JWT lifetime, in minutes. Before the token expires, provide a new token or Webex will stop delivering data.
- `url` (string): The URL of the endpoint where Webex will send the data.

### response — respuesta 200
```json
{
  "audience": "MedDocVirtualAgent",
  "errorMessage": "down for maintenance",
  "id": "f29bb291-5db0-411b-834a-e64f8dee0658",
  "nonce": "jeieu38udue83u398",
  "schemaId": "78efc775-dccb-45ca-9acf-989a4a59f788",
  "status": "active",
  "subject": "callAudioData",
  "tokenLifetimeMinutes": 60,
  "url": "https://www.byods.com/service1"
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