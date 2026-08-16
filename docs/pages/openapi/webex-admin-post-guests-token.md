---
doc_id: webex-admin-post-guests-token
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: POST
path: /guests/token
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.150332+00:00
---

# POST /guests/token

**API:** Webex Admin
**Área:** Guest Management
**operationId:** `Create a Guest`

## Resumen
Create a Guest

## Descripción
Create a new token for a single guest user. The Service App that creates the guest must have the scope `guest-issuer:write`.

Guests are implicitly created by retrieving the guest access token.

Repeated calls to this API with the same `subject` will create additional tokens without invalidating previous ones. Tokens are valid until the `expiresIn`.

Guests can be renamed by supplying the same `subject` and changing the `displayName.`

To retrieve a new token for an existing guest, please provide the existing guest's `subject`. Tokens are valid until `expiresIn`.

## Cuerpo de la petición (application/json)
- `subject` (string) **(requerido)**: The unique and external identifier of the guest.
- `displayName` (string) **(requerido)**: The display name shown in the Webex application.

## Respuestas
- **200**: OK
  - `id` (string): The unique id of the guest. This is a `personId`
  - `subject` (string): The external unique identifier of the guest.
  - `displayName` (string): The guest’s display name shown in Webex applications
  - `email` (string): The person’s synthetic email in Webex.
  - `accessToken` (string): The guests access token. Guest tokens usually are over 2000 characters in length.
  - `expiresIn` (number): The token expiration in seconds from the time of issuance.
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
