---
doc_id: webex-broadworks-post-broadworks-enterprises-id-broadworksdirectorysync-externaluser
source: webex-openapi-specs/public-spec/webex-broadworks.json
api: Webex Broadworks Calling
method: POST
path: /broadworks/enterprises/{id}/broadworksDirectorySync/externalUser
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.284977+00:00
---

# POST /broadworks/enterprises/{id}/broadworksDirectorySync/externalUser

**API:** Webex Broadworks Calling
**Área:** BroadWorks Enterprises
**operationId:** `Trigger Directory Sync for a User`

## Resumen
Trigger Directory Sync for a User

## Descripción
This API lets a Partner Admin trigger a directory sync for an external user (real or virtual user) on Broadworks enterprise with Webex.

## Parámetros
- `id` [path] (string) **(requerido)**: A unique identifier for the enterprise in question.

## Cuerpo de la petición (application/json)
- `userId` (string): The user ID of the Broadworks user to be synced (A non-webex user).

### Ejemplo de petición
```json
{
  "userId": "john_anderson@acme.com"
}
```

## Respuestas
- **200**: OK
  - `userResponse` (object): User Directory sync response
    - `userId` (string): The UserID of the user on Broadworks (A non-webex user).
    - `firstName` (string): First name of the user on Broadworks.
    - `lastName` (string): Last name of the user on Broadworks.
    - `extension` (string): Extension of the user on Broadworks.
    - `number` (string): Phone number of the user on Broadworks.
    - `mobile` (string): Mobile number of the user on Broadworks.
  - `status` (string): The Status of the operation being performed.  * `ADD` - The external user is added in this sync  * `UPDATE` - The external user is updated in this sync  * `DELETE` - The external user is deleted in this sync  * `NO_OPERATION` - No changes made on the external user in this sync Valores: ADD, UPDATE, DELETE, NO_OPERATION.
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
