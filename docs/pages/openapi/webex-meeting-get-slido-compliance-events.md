---
doc_id: webex-meeting-get-slido-compliance-events
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /slido/compliance/events
operation_id: listComplianceEvents
tags: slidoSecurePremium
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.499998+00:00
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
- `sessionOrgId` [query] (string) (**requerido**): Webex organization UUID.
- `sessionId` [query] (string) (**requerido**): Webex meeting instance ID (`{meetingSeriesId}_I_{conferenceId}`).
- `start` [query] (string): Pagination token. Returned in the response body as the `next` property.

## Ejemplo de invocación
```bash
curl -X GET '/slido/compliance/events?sessionOrgId=<sessionOrgId>&sessionId=<sessionId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Default Response
- `items` (array) (**requerido**):
  - `createdAtMs` (number) (**requerido**):
  - `sessionId` (string) (**requerido**): Webex meeting instance ID (`{meetingSeriesId}_I_{conferenceId}`). Long. max: 128.
  - `sessionOrgId` (string) (**requerido**): Webex organization UUID. Long. max: 128.
  - `userId` (string) (**requerido**):  Long. max: 128.
  - `data` (object) (**requerido**):
- `next` (string):

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "createdAtMs": 0,
      "sessionId": "abcdef0123456789abcdef0123456789_I_000000000000000000",
      "sessionOrgId": "a1111111-1a11-111a-1a11-1a1111a1111a",
      "userId": "u1111111-1u11-111u-1u11-1u1111u1111u",
      "data": {
        "type": "qaaQuestion",
        "sessionId": "abcdef0123456789abcdef0123456789_I_000000000000000000",
        "questionId": "q1111111-1q11-111q-1q11-1q1111q1111q",
        "createdAtMs": 0,
        "modifiedAtMs": 0,
        "isDeleted": false,
        "text": "What are we having for breakfast tonight?",
        "isAnonymous": false,
        "user": {
          "userId": "u1111111-1u11-111u-1u11-1u1111u1111u",
          "name": "John Doe",
          "unverifiedName": null
        },
        "status": "public"
      }
    }
  ],
  "next": "MTIzNDU2Nzg5MDEyMzQ1Ng"
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
The Webex Meetings APIs enable developers to schedule, manage, and retrieve information about Webex meetings, webinars, and events. They provide endpoints for meeting creation, participant management, recordings, transcripts, in-meeting features such as chat and closed captions, and post-meeting analytics. Common use cases include integrating meeting scheduling into calendar apps, automating follow-ups with recordings and transcripts, embedding meeting controls in custom portals, and extracting insights for compliance or productivity analysis. The APIs support both real-time and asynchronous w...

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs