---
doc_id: webex-wholesale-post-subscribers-subscriberid-emails-consentmove
source: webex-openapi-specs/public-spec/webex-wholesale.json
api: Webex Wholesale
method: POST
path: /subscribers/{subscriberId}/emails/consentMove
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.733240+00:00
---

# POST /subscribers/{subscriberId}/emails/consentMove

**API:** Webex Wholesale
**Área:** Wholesale Provisioning
**operationId:** `Send Consent User Move Email to Pending Wholesale Subscribers`

## Resumen
Send Consent User Move Email to Pending Wholesale Subscribers

## Descripción
Allows a Service Provider to send the user consent move email to a subscriber who is currently in `pending_user_migration` state.

## Parámetros
- `subscriberId` [path] (string) **(requerido)**: A unique identifier for the subscriber in question.
- `onBehalfOfSubPartnerOrgId` [query] (string): The encoded organization ID for the sub partner.

## Respuestas
- **204**: No Content
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
