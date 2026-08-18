---
doc_id: webex-admin-get-authorizations
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /authorizations
operation_id: listAuthorizationsForUser
tags: Authorizations
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.559077+00:00
---

# GET /authorizations

**API:** Webex Admin
**Área:** Authorizations
**operationId:** `listAuthorizationsForUser`

## Resumen
List authorizations for a user

## Descripción
Lists all authorizations for a user. Either `personId` or `personEmail` must be provided. This API does not support pagination.

## Parámetros
- `personId` [query] (string): List authorizations for this user id.
- `personEmail` [query] (string): List authorizations for this user email.

## Ejemplo de invocación
```bash
curl -X GET '/authorizations' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):
  - `id` (string): The unique authorization identifier.
  - `applicationId` (string): The unique identifier for the application.
  - `applicationName` (string): The name of the Integration.
  - `personId` (string): The person Id of the user. Can be used in the /people API.
  - `clientId` (string): The unique oAuth client id.
  - `created` (string): The date and time the authorization was created.
  - `type` (string): The type of token associated with the authorization.  * `refresh` - refresh authorization used to create `access` tokens  * `access` - `access` token authorization Valores: refresh, access.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FVVEhPUklaQVRJT04vZjI3MDM0ZTMtMDA5ZS00ODA4LTk5MDQtNTNkMDQ0OGJlNDVk",
      "applicationId": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL0NmMzkyNWU5NDFmMzhhYTc0M2Y0MmFiNzcwZmZhZjFhNTIyMjcxZDI5OTQ4NDhjNjk2YWMwYTEwN2Q2YTg5MjI3",
      "applicationName": "Developer Portal",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lYjIyYjNiZC03NGNiLTRjMjktYjA3Zi1lYWQwMmU1NjgyZDI",
      "clientId": "C80fb9c7096bd8474627317ee1d7a817eff372ca9c9cee3ce43c3ea3e8d1511ec",
      "created": "2015-10-18T14:26:16+00:00",
      "type": "refresh"
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