---
doc_id: webex-cloud-calling-get-telephony-conference
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/conference
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.579110+00:00
---

# GET /telephony/conference

**API:** Webex Cloud Calling
**Área:** Conference Controls
**operationId:** `Get Conference Details`

## Resumen
Get Conference Details

## Descripción
Get the details of the conference.  An empty JSON object body is returned if there is no conference.

## Parámetros
- `lineOwnerId` [query] (string): The ID of a user, workspace, or virtual line for which there is a secondary line on a device owned by the user invoking the API.

## Respuestas
- **200**: OK
  - `state` (string) **(requerido)**: * `connected` - The controller is an active participant.  * `held` - The controller has held the conference and so is no longer an active participant.  * `disconnected` - The conference has been released. Valores: connected, held, disconnected.
  - `appearance` (number): The appearance index for the conference leg. Only present when the conference has an appearance value assigned.
  - `created` (string) **(requerido)**: The conference start time in ISO 8601 format.
  - `muted` (boolean) **(requerido)**: Indicates if the host of the conference has been muted.
  - `type` (string):  Valores: bargeIn, silentMonitoring, coaching.
  - `participants` (array): The participants in the conference.
    - `callId` (string) **(requerido)**: The callId of the call.
    - `muted` (boolean) **(requerido)**: Indicates if the participant has been muted.
    - `deafened` (boolean) **(requerido)**: Indicates if the participant has been deafened (i.e. media stream is not being transmitting to the participant)
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
