---
doc_id: webex-messaging-get-events-eventid
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: GET
path: /events/{eventId}
operation_id: Get Event Details
tags: Events
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.804015+00:00
---

# GET /events/{eventId}

**API:** Webex Messaging
**Área:** Events
**operationId:** `Get Event Details`

## Resumen
Get Event Details

## Descripción
Shows details for an event, by event ID.

Specify the event ID in the `eventId` parameter in the URI.

## Parámetros
- `eventId` [path] (string) (**requerido**): The unique identifier for the event.

## Ejemplo de invocación
```bash
curl -X GET '/events/<eventId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): The unique identifier for the event.
- `resource` (string) (**requerido**): * `attachmentActions` - State changed on a card attachment  * `businessTexts` - A user sent or received a SMS message  * `call_records` - A Webex call was made to/from a user  * `convergedRecordings` - A Webex call was recorded for a user  * `file_transcodings` - State change on a file preview  * `files` - State changed on a file download  * `meetingMessages` - State changed on a meeting message, i.e. message exchanged as part of a meeting  * `meetings` - State change on a meeting ( here combined with type = 'ended' )  * `meetingTranscripts` - State change on a automatic transcript resource for Webex Assistant  * `memberships` - State changed on a memberships resource  * `messages` - State changed on a messages resource  * `rooms` - State changed on a space classification  * `tabs` - State changed on a room tabs in a space Valores: attachmentActions, businessTexts, call_records, convergedRecordings, file_transcodings, files, meetingMessages, meetings, meetingTranscripts, memberships, messages, rooms, tabs.
- `type` (string) (**requerido**): * `created` - The resource has been created  * `updated` - A property on the resource has been updated  * `deleted` - The resource has been deleted  * `ended` - The meeting has ended Valores: created, updated, deleted, ended.
- `appId` (string): The ID of the application for the event.
- `actorId` (string) (**requerido**): The ID of the person who performed the action.
- `orgId` (string) (**requerido**): The ID of the organization for the event.
- `created` (string) (**requerido**): The date and time of the event.
- `data` (object) (**requerido**): The event's data representation. This object will contain the event's `resource`, such as [memberships](/docs/api/v1/memberships/get-membership-details), [messages](/docs/api/v1/messages/get-message-details), [meetings](/docs/api/v1/meetings), [meetingMessages](/docs/api/v1/meetingMessages), [tabs](/docs/api/v1/room-tabs), [rooms](/docs/api/v1/space-classifications) or [attachmentActions](/docs/api/v1/attachment-actions) at the time the event took place.
  - `id` (string):
  - `roomId` (string):
  - `roomType` (string):
  - `orgId` (string):
  - `text` (string):
  - `personId` (string):
  - `personEmail` (string):
  - `meetingId` (string):
  - `creatorId` (string):
  - `host` (object): The meeting's host data.
  - `attendees` (array): Common Identity (CI) authenticated meeting attendees.
  - `transcriptionEnabled` (string): Indicates whether or not the Voice Assistant was enabled during the meeting. If `true` a transcript should be available a couple minutes after the meeting ended at the [meetingTranscripts resource](/docs/api/v1/meeting-transcripts).
  - `recordingEnabled` (string): Indicates if recording was enabled for all or parts of the meeting. If `true` a recording should be available shortly after the meeting ended at the [recordings resource](/docs/api/v1/recordings).
  - `hasPostMeetingsChat` (string): Indicates if chat messages were exchanged during the meeting in the meetings client (not the unified client). If `true` these messages can be accessed by a compliance officer at the [postMeetingsChat](/docs/api/v1/meetings-chat) resource. Meetings chat collection must be custom enabled.
  - `corelationId` (string): Telephony; The corelation id.
  - `callType` (string): Telephony; call types (examples `VIDEO_DIALIN`,`VIDEO_DIALOUT`,`CASCADE`,`HYBRID_CASCADE`,`PSTN_SIP`,`PSTN_DIALIN`,`PSTN_DIALOUT`,`PSTN_ONLY_DIALIN`,`PSTN_ONLY_DIALOUT`,`H323`,`H323_IP`,`SIP_ENTERPRISE`,`SIP_MOBILE`,`SIP_NATIONAL`,`SIP_INTERNATIONAL`,`SIP_EMERGENCY`,`SIP_OPERATOR`,`SIP_SHORTCODE`,`SIP_TOLLFREE`,`SIP_PREMIUM`,`SIP_URI`,`SIP_INBOUND`,`UNKNOWN`,`ZTM`,`SIP_MEETING`).
  - `userId` (string): Telephony; user id of the CDR owner.
  - `userType` (string): Telephony; The type of user (`User`,`Anchor`,`AutomatedAttendantBasic`,`AutomatedAttendantStandard`,`AutomatedAttendantVideo`,`BroadworksAnywhere`,`CallCenterBasic`,`CallCenterPremium`,`CallCenterStandard`,`CollaborateBridge`,`ContactCenterAdaptor`,`FindMeFollowMe`,`FlexibleSeatingHost`,`GroupCall`,`GroupPaging`,`HuntGroup`,`LocalGateway`,`MeetMeConference`,`Place`,`RoutePoint`,`SystemVoicePortal`,`VoiceMailGroup`,`VoiceMailRetrieval`,`VoiceXML`,`VirtualLine`,`Unknown`).
  - `callDirection` (string): Telephony; `ORIGINATING` or `TERMINATING`.
  - `isCallAnswered` (string): Telephony; indicates if the call was answered.
  - `callDurationSeconds` (string): Telephony; duration of call in seconds.
  - `callStartTime` (string): Telephony; ISO 8601.
  - `callAnswerTime` (string): Telephony; ISO 8601.
  - `callTransferTime` (string): Telephony; ISO 8601.
  - `callingNumber` (string): Telephony; originating number.
  - `callingLineId` (string): Telephony.
  - `calledNumber` (string): Telephony; destination number.
  - `calledLineId` (string): Telephony
  - `dialedDigits` (string): Telephony
  - `callRedirectingNumber` (string): Telephony
  - `callRedirectedReason` (string): Telephony
  - `created` (string):
  - `type` (string): Message type `direct` or `group` message.
  - `breakoutSessionId` (string): The breakout session Id in cases where the action happened in a meeting's brakout session, for example a `meetingMessage`.
  - `recipients` (array): The recipients list for directed meetingMessages.
    - `personId` (string): The personId of the recipient
    - `personEmail` (string): The personEmail
    - `guestDisplayName` (string): Guests, who are unauthenticated users, have a guestDisplayName
    - `guestEmail` (string): Guests, who are unauthenticated users, have a guestEmail

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0VWRU5UL2JiY2ViMWFkLTQzZjEtM2I1OC05MTQ3LWYxNGJiMGM0ZDE1NAo",
  "resource": "messages",
  "type": "created",
  "appId": "null",
  "actorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
  "orgId": "OTZhYmMyYWEtM2RjYy0xMWU1LWExNTItZmUzNDgxOWNkYzlh",
  "created": "2016-05-16T21:34:59.324Z",
  "data": {
    "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
    "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
    "roomType": "group",
    "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9jZTg2MWZiYS02ZTJmLTQ5ZjktOWE4NC1iMzU0MDA4ZmFjOWU",
    "text": "PROJECT UPDATE - A new project plan has been published on Box: http://box.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
    "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
    "personEmail": "matt@example.com",
    "meetingId": "16ce696f75844d24b2d4fab04b4419af_I_183979003076423608",
    "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YWE2ZGE5OS0xYzdlLTQ4MWItODY3YS03MWY2NTIwNDk0MzM",
    "transcriptionEnabled": "yes",
    "recordingEnabled": "yes",
    "hasPostMeetingsChat": "yes",
    "corelationId": "fdda8613-d34b-424c-8c6a-44ff2e19379c",
    "callType": "SIP_ENTERPRISE",
    "userId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zZjEwMTU1NC04ZGJjLTQyMmUtOGEzZC1kYTk1YTI3NWZlNzU",
    "userType": "User",
    "call
  ... (truncado)
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
The Webex Messaging APIs offer robust programmatic access to messaging features within Webex, including sending and receiving messages, managing spaces, memberships, attachments, and moderating content. These APIs enable integration with bots, workflow automation, notification systems, and custom messaging solutions to enhance team collaboration and productivity. Use cases include building chatbots, integrating with ticketing or alerting platforms, automating onboarding flows, and creating custom collaboration experiences tailored to business needs.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs