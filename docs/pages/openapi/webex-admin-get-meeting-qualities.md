---
doc_id: webex-admin-get-meeting-qualities
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /meeting/qualities
operation_id: getMeetingQualities
tags: Meeting Qualities
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.567730+00:00
---

# GET /meeting/qualities

**API:** Webex Admin
**Área:** Meeting Qualities
**operationId:** `getMeetingQualities`

## Resumen
Get Meeting Qualities

## Descripción
Get quality data for a meeting, by `meetingId`. Only organization administrators can retrieve meeting quality data.

## Parámetros
- `meetingId` [query] (string) (**requerido**): Unique identifier for the specific meeting instance. **Note:** The `meetingId` can be obtained via the Meeting List API when meetingType=meeting. The `id` attribute in the Meeting List Response is what is needed, for example, `e5dba9613a9d455aa49f6ffdafb6e7db_I_191395283063545470`.
- `max` [query] (number): Limit the maximum number of media sessions in the response. Por defecto: 100.
- `offset` [query] (number): Offset from the first result that you want to fetch.

## Ejemplo de invocación
```bash
curl -X GET '/meeting/qualities?meetingId=<meetingId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):
  - `meetingInstanceId` (string) (**requerido**): The meeting identifier for the specific meeting instance.
  - `webexUserName` (string): The display name of the participant of this media session.
  - `webexUserEmail` (string): The email address of the participant of this media session.
  - `joinTime` (string): The date and time when this participant joined the meeting.
  - `leaveTime` (string): The date and time when this participant left the meeting.
  - `joinMeetingTime` (string): The join meeting time of the participant.
  - `clientType` (string): The type of the client (and OS) used by this media session.
  - `clientVersion` (string): The version of the client used by this media session.
  - `osType` (string): The operating system used for the client.
  - `osVersion` (string): The version of the operating system used for the client.
  - `hardwareType` (string): The type of hardware used to attend the meeting
  - `speakerName` (string): A description of the speaker used in the meeting.
  - `networkType` (string): The type of network. Valores: wifi, cellular, ethernet, unknown.
  - `localIP` (string): The local IP address of the client.
  - `publicIP` (string): The public IP address of the client.
  - `maskedLocalIP` (string): The masked local IP address of the client.
  - `maskedPublicIP` (string): The masked public IP address of the client.
  - `camera` (string): A description of the camera used in the meeting.
  - `microphone` (string): A description of the microphone used in the meeting.
  - `serverRegion` (string): The server region.
  - `videoMeshCluster` (string): The video mesh cluster name.
  - `videoMeshServer` (string): The video mesh server name.
  - `participantId` (string): Identifies the participant.
  - `participantSessionId` (string): Identifies a specific session the participant has in a given meeting.
  - `videoIn` (array): The collection of downstream (sent to the client) video quality data.
    - `samplingInterval` (number): The sampling interval, in seconds, of the downstream video quality data.
    - `startTime` (string): The date and time when this video session started.
    - `endTime` (string): The date and time when this video session ended.
    - `packetLoss` (array): The percentage of video packet loss, as a float between 0.0 and 100.0, during each sampling interval.
    - `latency` (array): The average latency, in milliseconds, during each sampling interval.
    - `resolutionHeight` (array): The pixel height of the incoming video.
    - `frameRate` (array): The frames per second of the incoming video.
    - `mediaBitRate` (array): The bit rate of the incoming video.
    - `codec` (string): The incoming video codec.
    - `jitter` (array): The incoming video jitter.
    - `transportType` (string): The network protocol used for video transmission. Valores: UDP, TCP.
  - `videoOut` (array): The collection of upstream (sent from the client) video quality data.
    - `samplingInterval` (number): The sampling interval, in seconds, of the upstream video quality data.
    - `startTime` (string): The date and time when this video session started.
    - `endTime` (string): The date and time when this video session ended.
    - `packetLoss` (array): The percentage of video packet loss, in float between 0.0 and 100.0, during each sampling interval.
    - `latency` (array): The average latency, in milliseconds, during each sampling interval.
    - `resolutionHeight` (array): The pixel height of the outgoing video.
    - `frameRate` (array): The frames per second of the outgoing video.
    - `mediaBitRate` (array): The bit rate of the outgoing video.
    - `codec` (string): The outgoing video codec.
    - `jitter` (array): The outgoing video jitter.
    - `transportType` (string): The network protocol used for video transmission. Valores: UDP, TCP.
  - `audioIn` (array): The collection of downstream (sent to the client) audio quality data.
    - `samplingInterval` (number): The sampling interval, in seconds, of the downstream audio quality data.
    - `startTime` (string): The date and time when this audio session started.
    - `endTime` (string): The date and time when this audio session ended.
    - `packetLoss` (array): The percentage of audio packet loss, as a float between 0.0 and 100.0, during each sampling interval.
    - `latency` (array): The average latency, in milliseconds, during each sampling interval.
    - `resolutionHeight` (array): Not applicable to audio.
    - `frameRate` (array): Not applicable to audio.
    - `mediaBitRate` (array): The bitrate of the incoming audio.
    - `codec` (string): The codec of the incoming audio.
    - `jitter` (array): The incoming audio jitter.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "meetingInstanceId": "e5dba9613a9d455aa49f6ffdafb6e7db_I_191395283063545470",
      "webexUserName": "John Andersen",
      "webexUserEmail": "john.andersen@example.com",
      "joinTime": "2020-04-10T17:00:00.000Z",
      "leaveTime": "2020-04-10T17:02:00.000Z",
      "joinMeetingTime": "5.793",
      "clientType": "Teams_Mobile_Client (iOS)",
      "clientVersion": "40.5.0.210",
      "osType": "mac",
      "osVersion": "Version 10.14.6 (Build 18G3020)",
      "hardwareType": "mac book",
      "speakerName": "MacBook Pro Speakers",
      "networkType": "wifi",
      "localIP": "10.24.72.54",
      "publicIP": "10.24.72.54",
      "maskedLocalIP": "10.24.72.54",
      "maskedPublicIP": "10.24.72.54",
      "camera": "FaceTime HD Camera",
      "microphone": "External Microphone",
      "serverRegion": "San Jose, USA",
      "videoMeshCluster": "Mesh Cluster One",
      "videoMeshServer": "server.example.com",
      "participantId": "8635cbf0ca1a4573b27348e560679b25_I_158174534545967299_57",
      "participantSessionId": "3324C9D0-9EA7-45A2-B249-5B62A384AFEF",
      "videoIn": [
        {
          "samplingInterval": 60,
          "startTime": "2020-04-10T17:00:00.000Z",
          "endTime": "2020-04-10T18:00:00.000Z",
          "packetLoss": [],
          "latency": [],
          "resolutionHeight": [],
          "frameRate": [
            25.940001
          ],
          "mediaBitRate": [],
          "codec": "H.264 BP",
          "jitter": [
   
  ... (truncado)
```
- Cabecera `Link`: 

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
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs