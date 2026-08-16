---
doc_id: webex-admin-put-datasources-datasourceid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: PUT
path: /dataSources/{dataSourceId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.147782+00:00
---

# PUT /dataSources/{dataSourceId}

**API:** Webex Admin
**Área:** Data Sources
**operationId:** `Update a Data Source`

## Resumen
Update a Data Source

## Descripción
Updates a data source. The fields you can update are `audience`, `subject`, `nonce`, `url`, and `tokenLifetimeMinutes`.
You can set `status` from `active` to `disabled` only if you provide an `errorMessage`, which may be shown to the customer administrator in Control Hub.
Update tokens before they expire to prevent service interruption.

## Parámetros
- `dataSourceId` [path] (string) **(requerido)**: The unique identifier for the data source.

## Cuerpo de la petición (application/json)
- `audience` (string): The JWT `aud` (audience) claim. This is usually the DAP application's name.
- `errorMessage` (string): The error message shown in Control Hub when `status` is set to `disabled`.
- `nonce` (string): A unique nonce used when encrypting the JWT.
- `schemaId` (string): The schema ID used for the data exchange.
- `status` (string): The data source status: `active` or `disabled`.
- `subject` (string): The JWT `sub` (subject) claim. This usually describes the application's function.
- `tokenLifetimeMinutes` (number): The JWT lifetime, in minutes. Before the token expires, provide a new token or Webex will stop delivering data. Must be 1440 or less.
- `url` (string): The URL of the endpoint where Webex will send the data.

## Respuestas
- **200**: OK
  - `audience` (string): The JWT `aud` (audience) claim. This is usually the DAP application's name.
  - `errorMessage` (string): The error message shown in Control Hub when `status` is set to `disabled`.
  - `id` (string): The data source ID.
  - `nonce` (string): A unique nonce used when encrypting the JWT.
  - `schemaId` (string): The schema ID used for the data exchange.
  - `status` (string): The data source status: `active` or `disabled`.
  - `subject` (string): The JWT `sub` (subject) claim. This usually describes the application's function.
  - `tokenLifetimeMinutes` (number): The JWT lifetime, in minutes. Before the token expires, provide a new token or Webex will stop delivering data.
  - `url` (string): The URL of the endpoint where Webex will send the data.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
