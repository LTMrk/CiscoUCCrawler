---
doc_id: webex-meeting-get-meetings-postmeetingchats
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetings/postMeetingChats
operation_id: List Meeting Chats
tags: Chats
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.462933+00:00
---

# GET /meetings/postMeetingChats

**API:** Webex Meetings
**Área:** Chats
**operationId:** `List Meeting Chats`

## Resumen
List Meeting Chats

## Descripción
Lists the meeting chats of a finished [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) specified by `meetingId`. You can set a maximum number of chats to return.

Use this operation to list the chats of a finished [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) when they are ready. Please note that only **meeting instances** in state `ended` are supported for `meetingId`. **Meeting series**, **scheduled meetings** and `in-progress` **meeting instances** are not supported.

## Parámetros
- `meetingId` [query] (string) (**requerido**): A unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the chats belong. The meeting ID of a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting is not supported.
- `max` [query] (number): Limit the maximum number of meeting chats in the response, up to 100. Por defecto: 10.
- `offset` [query] (number): Offset from the first result that you want to fetch.

## Ejemplo de invocación
```bash
curl -X GET '/meetings/postMeetingChats?meetingId=<meetingId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): Chat array
  - `id` (string): A unique identifier for the chat snippet.
  - `chatTime` (string): Chat time for the chat snippet in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
  - `text` (string): The text of the chat snippet.
  - `meetingId` (string): A unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the chat belongs.
  - `type` (string): Whether the type of the chat is private, public or group. Private chat is for the 1:1 chat. Public chat is for the message which is sent to all the people in the meeting. Group chat is for the message which is sent to a small group of people, like a message to "host and presenter".
  - `sender` (object): Information of the sender of the chat snippet.
    - `email` (string): Email address of the sender of the meeting chat snippet.
    - `displayName` (string): Display name for the sender.
    - `personId` (string): A unique identifier for the sender.
    - `orgId` (string): The ID of the organization to which the sender belongs.
  - `receivers` (array): Information of the receivers of the chat snippet.
    - `email` (string): Email address of the receiver of the meeting chat snippet.
    - `displayName` (string): Display name for the receiver.
    - `personId` (string): A unique identifier for the receiver.
    - `orgId` (string): The ID of the organization to which the receiver belongs.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "1aea8390-e375-4547-b7ff-58ecd9e0b03d",
      "chatTime": "2021-07-06T09:22:34Z",
      "text": "hi",
      "meetingId": "a2f95f5073e347489f7611492dbd6ad5_I_199075330905867928",
      "type": "private",
      "sender": {
        "email": "john.andersen@example.com",
        "displayName": "John Andersen",
        "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jN2ZkNzNmMi05ZjFlLTQ3ZjctYWEwNS05ZWI5OGJiNjljYzY=",
        "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9jMmUyMjE4Zi00ZDZhLTQwODEtYTc1MS0yOWIyZTk3MDRiZGU="
      },
      "receivers": [
        {
          "email": "catherine.sinu@example.com",
          "displayName": "Catherine Sinu",
          "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hYmEwZDRjYi02MGVkLTQzYjctYTkyNy1mZTc2MmIyZTRiODY=",
          "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9jMmUyMjE4Zi00ZDZhLTQwODEtYTc1MS0yOWIyZTk3MDRiZGU="
        }
      ]
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request
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