---
doc_id: webex-cloud-calling-get-recordingreport-meetingarchives-archiveid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /recordingReport/meetingArchives/{archiveId}
operation_id: Get Meeting Archive Details
tags: Recording Report
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.357928+00:00
---

# GET /recordingReport/meetingArchives/{archiveId}

**API:** Webex Cloud Calling
**Área:** Recording Report
**operationId:** `Get Meeting Archive Details`

## Resumen
Get Meeting Archive Details

## Descripción
Retrieves details for a meeting archive report with a specified archive ID, which contains recording metadata.

Meeting archive details are only available to full administrators, not even the meeting host.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.

## Parámetros
- `archiveId` [path] (string) (**requerido**): A unique identifier for the meeting archive summary.
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/recordingReport/meetingArchives/<archiveId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `archiveId` (string): A unique identifier for the meeting archive summary.
- `serviceType` (string): Recording achrive report's service-type. Valores: MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
- `title` (string): Meeting title.
- `start` (string): Start time for meeting in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
- `end` (string): End time for a meeting in ISO 8601 compliant format.
- `hostDisplayName` (string): Display name for the meeting host.
- `hostEmail` (string): Email address for the meeting host.
- `participants` (array): The participants of the meeting archive.
  - `correlationId` (number): An internal ID that is associated with each join.
  - `displayName` (string): Display name for the meeting participant.
  - `joinedTime` (string): The time the participant joined the meeting.
  - `leftTime` (string): The time the participant left the meeting.
  - `email` (string): Email address for the meeting participant.
- `chats` (array): The chats of the meeting archive.
  - `type` (string): Whether the type of the chat is private, public or group. Private chat is for the 1:1 chat. Public chat is for the message which is sent to all the people in the meeting. Group chat is for the message which is sent to a small group of people, like a message to the "host and presenter".
  - `senderName` (string): Display name for the sender of the chat snippet.
  - `chatTime` (string): Chat time for the chat snippet in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
  - `target` (string): Information of the receivers of the chat snippet.
  - `text` (string): The text of the chat snippet.
- `polls` (array): The polls of the meeting archive.
  - `type` (string): The type of the question.
  - `startTime` (string): The date and time the poll started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
  - `endTime` (string): The date and time the poll ended in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
  - `content` (object): The content of the meeting archive poll;
    - `questionCount` (number): The total number of questions.
    - `userCount` (number): The total number of users.
    - `votedUserCount` (number): The number of voters among users.
    - `questions` (array): Poll's questions.
      - `voteUsers` (array): The voters among users.
        - `correlationId` (number): An internal ID that is associated with each join.
        - `displayName` (string): Display name for the meeting participant.
        - `email` (string): Email address for the meeting participant.
      - `question` (object): The poll's question.
        - `choiceCount` (number): The number of choices in the questions.
        - `type` (string): The type of the question.
        - `text` (string): The text of the question.
      - `answerSummary` (array): The answer summary of the archive poll.
        - `totalRespondents` (number): The total number of people who selected this answer.
        - `isCorrect` (boolean): Whether the answer is correct.
        - `text` (string): The text of the answer.
        - `voteUsers` (array): The voters among users.
      - `respondents` (array): The question's respondents.
        - `correlationId` (number): An internal ID that is associated with the respondent's each join.
        - `displayName` (string): Display name for the poll respondent.
        - `email` (string): Email address for the poll respondent.
        - `answers` (array): An array of answers to the question.
- `qas` (array): Meeting meeting archive's Q and A.
  - `priority` (string): The priority of the Q and A.
  - `type` (string): Whether the type of the Q and A is private, public, or group. Private Q and A is for the 1:1 chat. Public Q and A are for the message which is sent to all the people in the meeting. Group Q and A are for the message which is sent to a small group of people, like a Q and A to "host and presenter".
  - `displayName` (string): The email of the user who asked the question.
  - `questionTime` (string): The date and time the question was created in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
  - `target` (string): Information of the user who asked the question.
  - `question` (string): The question that was asked.
  - `answers` (array): Question's answers.
    - `responseMode` (string): The answer's response mode.
    - `displayName` (string): The name of the person who answered the question.
    - `correlationId` (number): An internal ID that is associated with the answer's each join.
    - `email` (string): The email of the person who answered the question.
    - `answerTime` (string): The date and time the question answered in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
    - `text` (string): The text of the answer.

### Ejemplo — respuesta 200
```json
{
  "archiveId": "4E3254897D3A2E24E05386CA24AD93A6_R_1000637312",
  "serviceType": "MeetingCenter",
  "title": "Marcos Alonso's Personal Room",
  "start": "2022-11-03T10:37:32+08:00",
  "end": "2022-11-03T10:37:32+08:00",
  "hostDisplayName": "Marcos Alonso",
  "hostEmail": "marcos@example.com",
  "participants": [
    {
      "correlationId": -25516827,
      "displayName": "Marcos Alonso",
      "joinedTime": "2022-11-03T10:32:09+08:00",
      "leftTime": "2022-11-03T10:37:32+08:00"
    },
    {
      "correlationId": 10947662,
      "displayName": "Antoine Griezmann",
      "joinedTime": "2022-11-03T10:32:09+08:00",
      "leftTime": "2022-11-03T10:37:32+08:00",
      "email": "linzhou@example.com"
    },
    {
      "correlationId": -25516842,
      "displayName": "Marco Reus",
      "joinedTime": "2022-11-03T10:32:09+08:00",
      "leftTime": "2022-11-03T10:37:32+08:00"
    }
  ],
  "chats": [
    {
      "type": "public",
      "senderName": "Marcos Alonso",
      "chatTime": "2022-11-03T10:32:48+08:00",
      "target": "All Participants",
      "text": "Hi everyone!"
    }
  ],
  "polls": [
    {
      "type": "public",
      "startTime": "2022-11-03T10:33:40+08:00",
      "endTime": "2022-11-03T10:37:32+08:00",
      "content": {
        "questionCount": 1,
        "userCount": 1,
        "votedUserCount": 3,
        "questions": [
          {
            "voteUsers": [
              {
                "correlationId": -25516827,
                "displayName": "Marcos 
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs