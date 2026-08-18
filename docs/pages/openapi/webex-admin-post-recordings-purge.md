---
doc_id: webex-admin-post-recordings-purge
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /recordings/purge
operation_id: bulkPurgeRecordings
tags: Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.576394+00:00
---

# POST /recordings/purge

**API:** Webex Admin
**Área:** Recordings
**operationId:** `bulkPurgeRecordings`

## Resumen
Purge Recordings from Recycle Bin

## Descripción
Purge recordings from recycle bin with recording IDs or purge all the recordings that are in the recycle bin.

Only recordings of meetings hosted by the authenticated user can be purged from recycle bin.

* If `purgeAll` is `true`, `recordingIds` should be empty.

* If `purgeAll` is `false`, `recordingIds` should not be empty and its maximum size is `100`.

* All the IDs of `recordingIds` should belong to the site of `siteUrl` or the user's preferred site if `siteUrl` is not specified.

## Parámetros
- `hostEmail` [query] (string): Email address for the meeting host. Only used if the user or application calling the API has the required [admin-level meeting scopes](/docs/meetings#adminorganization-level-authentication-and-scopes). If set, the admin may specify the email of a user in a site they manage and the API will purge recordings from recycle bin of that user.

## Cuerpo de la petición (application/json)
- `purgeAll` (boolean): If not specified or `false`, purges the recordings specified by `recordingIds`. If `true`, purges all recordings from the recycle bin.
- `recordingIds` (array): Recording IDs for purging recordings from the recycle bin in batch. Note that all the recording IDs should belong to the site of `siteUrl` or the user's preferred site if `siteUrl` is not specified.
- `siteUrl` (string): URL of the Webex site from which the API purges recordings. If not specified, the API purges recordings from user's preferred site. All available Webex sites and preferred sites of the user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

### Ejemplo — petición
```json
{
  "purgeAll": false,
  "recordingIds": [
    "4f914b1dfe3c4d11a61730f18c0f5387"
  ],
  "siteUrl": "example.webex.com"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/recordings/purge' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**204**: No Content

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