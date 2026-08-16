---
doc_id: webex-meeting-get-meeting-qualities
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meeting/qualities
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.389959+00:00
---

# GET /meeting/qualities

**API:** Webex Meetings
**Área:** Meeting Qualities
**operationId:** `getMeetingQualities`

## Resumen
Get Meeting Qualities

## Descripción
Get quality data for a meeting, by `meetingId`. Only organization administrators can retrieve meeting quality data.

## Parámetros
- `meetingId` [query] (string) **(requerido)**: Unique identifier for the specific meeting instance. **Note:** The `meetingId` can be obtained via the Meeting List API when meetingType=meeting. The `id` attribute in the Meeting List Response is what is needed, for example, `e5dba9613a9d455aa49f6ffdafb6e7db_I_191395283063545470`.
- `max` [query] (number): Limit the maximum number of media sessions in the response.
- `offset` [query] (number): Offset from the first result that you want to fetch.

## Respuestas
- **200**: OK
  - `items` (array):
    - `meetingInstanceId` (string) **(requerido)**: The meeting identifier for the specific meeting instance.
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
