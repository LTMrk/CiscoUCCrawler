---
doc_id: webex-meeting-get-slido-compliance-events
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /slido/compliance/events
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.404515+00:00
---

# GET /slido/compliance/events

**API:** Webex Meetings
**Área:** slidoSecurePremium
**operationId:** `listComplianceEvents`

## Resumen
List Compliance Events

## Descripción
Lists events representing actions that occurred during a Slido Secure Premium session (creating a poll, modifying a poll, activating a poll, posting an answer, etc.)

Events capture who performed the action and on what resource.

The events are paginated by the server into pages of max 256 items per page without any order.

The events are available within 15 minutes after they happened.

Every resource has properties:
* type - event type

* ... event specific ids

* ... event specific properties

## Parámetros
- `sessionOrgId` [query] (string) **(requerido)**: Webex organization UUID.
- `sessionId` [query] (string) **(requerido)**: Webex meeting instance ID (`{meetingSeriesId}_I_{conferenceId}`).
- `start` [query] (string): Pagination token. Returned in the response body as the `next` property.

## Respuestas
- **200**: Default Response
  - `items` (array) **(requerido)**:
    - `createdAtMs` (number) **(requerido)**:
    - `sessionId` (string) **(requerido)**: Webex meeting instance ID (`{meetingSeriesId}_I_{conferenceId}`).
    - `sessionOrgId` (string) **(requerido)**: Webex organization UUID.
    - `userId` (string) **(requerido)**:
    - `data` (object) **(requerido)**:
  - `next` (string):
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
