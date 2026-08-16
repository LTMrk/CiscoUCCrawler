---
doc_id: webex-meeting-post-meetingparticipants-cancelcallout
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: POST
path: /meetingParticipants/cancelCallout
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.387203+00:00
---

# POST /meetingParticipants/cancelCallout

**API:** Webex Meetings
**Área:** Participants
**operationId:** `Cancel Calling Out a SIP Participant`

## Resumen
Cancel Calling Out a SIP Participant

## Descripción
Cancel the call to a SIP participant before the ringing on the invited SIP device stops. The ringing on the invited SIP device stops in 30 seconds if there is no response.

If a user invoking the API is not a [Service App](/docs/service-apps), the user must join the meeting before invoking the API. If a user is a [Service App](/docs/service-apps), the service app can invoke the API without joining the meeting. In both cases, the normal user or the service app that invokes the API must be the meeting host or cohost. If the meeting is created by the service app on behalf of the real host, the service app cannot use the admin on behalf function to invoke this API. Instead the host or cohost must execute the action.

The authenticated user calling this API must have the `meeting:participants_write` scope.

## Cuerpo de la petición (application/json)
- `participantId` (string) **(requerido)**: ID of the SIP participant on whom the callout is to be cancelled. It can be retrieved from the response of the "Call Out a SIP Participant" API.

### Ejemplo de petición
```json
{
  "participantId": "d8c3347d7ec04242ba9b856184b334ac_I_630641605678082408_57514861-50f7-3f5b-864f-ce0e308bf653"
}
```

## Respuestas
- **204**: No Content
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
