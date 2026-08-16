---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-queues-queueid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/locations/{locationId}/queues/{queueId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.603094+00:00
---

# PUT /telephony/config/locations/{locationId}/queues/{queueId}

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `updateCallQueue`

## Resumen
Update a Call Queue

## Descripción
Update the designated Call Queue.

Call queues temporarily hold calls in the cloud when all agents, which
can be users or agents, assigned to receive calls from the queue are
unavailable. Queued calls are routed to an available agent when not on an
active call. Each call queue is assigned a Lead Number, which is a telephone
number outside callers can dial to reach users assigned to the call queue.
Call queues are also assigned an internal extension, which can be dialed
internally to reach users assigned to the call queue.

Updating a call queue requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Location in which this call queue exists.
- `queueId` [path] (string) **(requerido)**: Update setting for the call queue with the matching ID.
- `orgId` [query] (string): Update call queue settings from this organization.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): Whether or not the call queue is enabled.
- `name` (string): Unique name for the call queue.
- `languageCode` (string): Language code.
- `firstName` (string): First name to be shown when calls are forwarded out of this call queue. Defaults to `.`. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name to be shown when calls are forwarded out of this call queue. Defaults to the `phoneNumber` if set, otherwise defaults to call group name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `timeZone` (string): Time zone for the hunt group.
- `phoneNumber` (string): Primary phone number of the call queue.
- `extension` (string): Extension of the call queue.
- `alternateNumberSettings` (object): The alternate numbers feature allows you to assign multiple phone numbers or extensions to a call queue. Each number will reach the same greeting and each menu will function identically to the main number. The alternate numbers option enables you to have up to ten (10) phone numbers ring into the call queue.
  - `distinctiveRingEnabled` (boolean): Distinctive Ringing selected for the alternate numbers in the call queue overrides the normal ringing patterns set for Alternate Numbers.
  - `alternateNumbers` (array): Allows up to 10 numbers, each with an optional distinctive ring setting override.
    - `phoneNumber` (string) **(requerido)**: Alternate phone number for the hunt group.
    - `ringPattern` (string): * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a short ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
- `callPolicies` (object):
  - `routingType` (string) **(requerido)**: * `PRIORITY_BASED` - Default routing type which directly uses the routing policy to dispatch calls to the agents.  * `SKILL_BASED` - This option uses skill level as the criteria to route calls to agents. When there is more than one agent with the same skill level, the selected `policy` helps dispatch the calls to the agents. Valores: PRIORITY_BASED, SKILL_BASED.
  - `policy` (string): * `CIRCULAR` - This option cycles through all agents after the last agent that took a call. It sends calls to the next available agent. This is supported for `SKILL_BASED`.  * `REGULAR` - Send the call through the queue of agents in order, starting from the top each time. This is supported for `SKILL_BASED`.  * `SIMULTANEOUS` - Sends calls to all agents at once  * `UNIFORM` - Sends calls to the agent that has been idle the longest. If they don't answer, proceed to the next agent who has been idle the second longest, and so on until the call is answered. This is supported for `SKILL_BASED`.  * `WEIGHTED` - Sends calls to idle agents based on percentages you assign to each agent (up to 100%). Valores: CIRCULAR, REGULAR, SIMULTANEOUS, UNIFORM, WEIGHTED.
  - `callBounce` (object): Settings for when the call is not answered.
    - `callBounceEnabled` (boolean): If enabled, bounce calls after the set number of rings.
    - `callBounceMaxRings` (number): Number of rings after which to bounce call, if call bounce is enabled.
    - `agentUnavailableEnabled` (boolean): Bounce if agent becomes unavailable.
    - `alertAgentEnabled` (boolean): Alert agent if call on hold more than `alertAgentMaxSeconds`.
    - `alertAgentMaxSeconds` (number): Number of second after which to alert agent if `alertAgentEnabled.`
    - `callBounceOnHoldEnabled` (boolean): Bounce if call on hold more than `callBounceMaxSeconds`.
    - `callBounceOnHoldMaxSeconds` (number): Number of second after which to bounce if `callBounceEnabled`.
  - `distinctiveRing` (object): Whether or not the call queue has the `distinctiveRing` option enabled.
    - `enabled` (boolean): Whether or not the `distinctiveRing` is enabled.
    - `ringPattern` (string): * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a short ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
- `callingLineIdPolicy` (string): Which type of Calling Line ID Policy Selected for Call Queue.  * `DIRECT_LINE` - Calling Line ID Policy will show the caller's direct line number.  * `LOCATION_NUMBER` - Calling Line ID Policy will show the main number for the location.  * `CUSTOM` - Calling Line ID Policy will show the value from the `callingLineIdPhoneNumber` field. Valores: DIRECT_LINE, LOCATION_NUMBER, CUSTOM.
- `callingLineIdPhoneNumber` (string): Calling line ID Phone number which will be shown if CUSTOM is selected.
- `queueSettings` (object) **(requerido)**:
  - `queueSize` (number) **(requerido)**: The maximum number of calls for this call queue. Once this number is reached, the `overflow` settings are triggered.
  - `callOfferToneEnabled` (boolean): Play ringing tone to callers when their call is set to an available agent.
  - `resetCallStatisticsEnabled` (boolean): Reset caller statistics upon queue entry.
  - `overflow` (object) **(requerido)**: Settings for incoming calls exceed queueSize.
    - `action` (string) **(requerido)**: Indicates how to handle new calls when the queue is full.  * `PERFORM_BUSY_TREATMENT` - The caller hears a fast-busy tone.  * `PLAY_RINGING_UNTIL_CALLER_HANGS_UP` - The caller hears ringing until they disconnect.  * `TRANSFER_TO_PHONE_NUMBER` - Number where you want to transfer overflow calls. Valores: PERFORM_BUSY_TREATMENT, PLAY_RINGING_UNTIL_CALLER_HANGS_UP, TRANSFER_TO_PHONE_NUMBER.
    - `sendToVoicemail` (boolean): When `true`, forwards all calls to a voicemail service of an internal number. This option is ignored when an external `transferNumber` is entered.
    - `transferNumber` (string): Destination number for overflow calls when `action` is set to `TRANSFER_TO_PHONE_NUMBER`.
    - `overflowAfterWaitEnabled` (boolean): After calls wait for the configured number of seconds and no agent is available, the overflow treatment is triggered.
    - `overflowAfterWaitTime` (number): Number of seconds to wait before the overflow treatment is triggered when no agent is available. The minimum value 0, The maximum value is 7200 seconds.
    - `playOverflowGreetingEnabled` (boolean): Indicate overflow audio to be played, otherwise, callers will hear the hold music until the call is answered by a user.
    - `greeting` (string) **(requerido)**: Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
    - `audioAnnouncementFiles` (array): Array of announcement files to be played as `overflow` greetings. These files are from the list of announcement files associated with this call queue. For `CUSTOM` announcement, a minimum of 1 file is mandatory, and the maximum is 4.
      - `id` (string): Unique identifier of the Announcement file.
      - `name` (string): Name of the announcement file. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
      - `mediaFileType` (string): Media file type of announcement file.
      - `level` (string): The level at which this announcement exists. Valores: LOCATION, ORGANIZATION, ENTITY.
  - `welcomeMessage` (object): Play a message when callers first reach the queue. For example, “Thank you for calling. An agent will be with you shortly.” It can be set as mandatory. If the mandatory option is not selected and a caller reaches the call queue while there is an available agent, the caller will not hear this announcement and is transferred to an agent. The welcome message feature is enabled by default.
    - `enabled` (boolean): If enabled play entrance message. The default value is `true`.
    - `alwaysEnabled` (boolean): Mandatory entrance message. The default value is `false`.
    - `greeting` (string) **(requerido)**: Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
    - `audioAnnouncementFiles` (array): Array of announcement files to be played as `welcomeMessage` greetings. These files are from the list of announcement files associated with this call queue. For `CUSTOM` announcement, a minimum of 1 file is mandatory, and the maximum is 4.
      - `id` (string): Unique identifier of the Announcement file.
      - `name` (string): Name of the announcement file. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
      - `mediaFileType` (string): Media file type of announcement file.
      - `level` (string): The level at which this announcement exists. Valores: LOCATION, ORGANIZATION, ENTITY.
  - `waitMessage` (object): Notify the caller with either their estimated wait time or position in the queue. If this option is enabled, it plays after the welcome message and before the comfort message. By default, it is not enabled.
    - `enabled` (boolean): If enabled play Wait Message.
    - `waitMode` (string) **(requerido)**: Estimated wait message operating mode. Supported values `TIME` and `POSITION`.  * `TIME` - Announce the waiting time.  * `POSITION` - Announce queue position. Valores: TIME, POSITION.
    - `handlingTime` (number): The number of minutes for which the estimated wait is played. The minimum time is 10 minutes. The maximum time is 100 minutes.
    - `defaultHandlingTime` (number): The default number of call handling minutes. The minimum time is 1 minutes, The maximum time is 100 minutes.
    - `queuePosition` (number): The number of the position for which the estimated wait is played. The minimum positions are 10, The maximum positions are 100.
    - `highVolumeMessageEnabled` (boolean): Play time / Play position High Volume.
    - `estimatedWaitingTime` (number): The number of estimated waiting times in seconds. The minimum time is 10 seconds. The maximum time is 600 seconds.
    - `callbackOptionEnabled` (boolean): Callback options enabled/disabled. Default value is false.
    - `minimumEstimatedCallbackTime` (number): The minimum estimated callback times in minutes. The default value is 30.
    - `internationalCallbackEnabled` (boolean): The international numbers for callback is enabled/disabled. The default value is `false`.
    - `playUpdatedEstimatedWaitMessage` (boolean): Play updated estimated wait message.
  - `comfortMessage` (object): Play a message after the welcome message and before hold music. This is typically a `CUSTOM` announcement that plays information, such as current promotions or information about products and services.
    - `enabled` (boolean): If enabled play periodic comfort message.
    - `timeBetweenMessages` (number): The interval in seconds between each repetition of the comfort message played to queued users. The minimum time is 10 seconds.The maximum time is 600 seconds.
    - `greeting` (string) **(requerido)**: Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
    - `audioAnnouncementFiles` (array): Array of announcement files to be played as `comfortMessage` greetings. These files are from the list of announcement files associated with this call queue. For `CUSTOM` announcement, a minimum of 1 file is mandatory, and the maximum is 4.
      - `id` (string): Unique identifier of the Announcement file.
      - `name` (string): Name of the announcement file. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
      - `mediaFileType` (string): Media file type of announcement file.
      - `level` (string): The level at which this announcement exists. Valores: LOCATION, ORGANIZATION, ENTITY.
  - `comfortMessageBypass` (object): Play a shorter comfort message instead of the usual Comfort or Music On Hold announcement to all the calls that should be answered quickly. This feature prevents a caller from hearing a short portion of the standard comfort message that abruptly ends when they are connected to an agent.
    - `enabled` (boolean): If enabled play comfort bypass message.
    - `callWaitingAgeThreshold` (number): The interval in seconds between each repetition of the comfort bypass message played to queued users. The minimum time is 1 seconds. The maximum time is 120 seconds.
    - `greeting` (string) **(requerido)**: Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
    - `audioAnnouncementFiles` (array): Array of announcement files to be played as `comfortMessageBypass` greetings. These files are from the list of announcements files associated with this call queue. For `CUSTOM` announcement, a minimum of 1 file is mandatory, and the maximum is 4.
      - `id` (string): Unique identifier of the Announcement file.
      - `name` (string): Name of the announcement file. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
      - `mediaFileType` (string): Media file type of announcement file.
      - `level` (string): The level at which this announcement exists. Valores: LOCATION, ORGANIZATION, ENTITY.
  - `mohMessage` (object): Play music after the comforting message in a repetitive loop.
    - `normalSource` (object) **(requerido)**:
      - `enabled` (boolean): Enable media on hold for queued calls.
      - `greeting` (string) **(requerido)**: Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
      - `audioAnnouncementFiles` (array): Array of announcement files to be played as `mohMessage` greetings. These files are from the list of announcement files associated with this call queue. For `CUSTOM` announcement, a minimum of 1 file is mandatory, and the maximum is 4.
        - `id` (string): Unique identifier of the Announcement file.
        - `name` (string): Name of the announcement file. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
        - `mediaFileType` (string): Media file type of announcement file.
        - `level` (string): The level at which this announcement exists. Valores: LOCATION, ORGANIZATION, ENTITY.
      - `audioPlaylistId` (string): Identifier of the playlist used for this MOH source.
    - `alternateSource` (object) **(requerido)**:
      - `enabled` (boolean): Enable media on hold for queued calls.
      - `greeting` (string) **(requerido)**: Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
      - `audioAnnouncementFiles` (array): Array of announcement files to be played as `mohMessage` greetings. These files are from the list of announcement files associated with this call queue. For `CUSTOM` announcement, a minimum of 1 file is mandatory, and the maximum is 4.
        - `id` (string): Unique identifier of the Announcement file.
        - `name` (string): Name of the announcement file. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
        - `mediaFileType` (string): Media file type of announcement file.
        - `level` (string): The level at which this announcement exists. Valores: LOCATION, ORGANIZATION, ENTITY.
      - `audioPlaylistId` (string): Identifier of the playlist used for this MOH source.
  - `whisperMessage` (object): Play a message to the agent immediately before the incoming call is connected. The message typically announces the identity of the call queue from which the call is coming.
    - `enabled` (boolean): If enabled play the Whisper Message.
    - `greeting` (string) **(requerido)**: Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
    - `audioAnnouncementFiles` (array): Array of announcement files to be played as `whisperMessage` greetings. These files are from the list of announcement files associated with this call queue. For `CUSTOM` announcement, a minimum of 1 file is mandatory, and the maximum is 4.
      - `id` (string): Unique identifier of the Announcement file.
      - `name` (string): Name of the announcement file. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
      - `mediaFileType` (string): Media file type of announcement file.
      - `level` (string): The level at which this announcement exists. Valores: LOCATION, ORGANIZATION, ENTITY.
  - `useEnterprisePlayToneToAgentSettingsEnabled` (boolean): When `true`, the call queue uses the organization-level play tone settings and ignores the queue-level `playToneToAgent*` values. When `false`, the queue-level `playToneToAgent*` values are used.
  - `playToneToAgentForBargeInEnabled` (boolean): Queue-specific setting that plays a tone to agents when a supervisor joins an active call using barge in. Applies only when `useEnterprisePlayToneToAgentSettingsEnabled` is `false`.
  - `playToneToAgentForSilentMonitoringEnabled` (boolean): Queue-specific setting that plays a tone to agents when a supervisor monitors their active call without joining. Applies only when `useEnterprisePlayToneToAgentSettingsEnabled` is `false`.
  - `playToneToAgentForSupervisorCoachingEnabled` (boolean): Queue-specific setting that plays a tone to agents when a supervisor coaches an agent during an active call. Applies only when `useEnterprisePlayToneToAgentSettingsEnabled` is `false`.
- `allowCallWaitingForAgentsEnabled` (boolean): Flag to indicate whether call waiting is enabled for agents.
- `agents` (array): People, workspaces and virtual lines that are eligible to receive calls.
  - `id` (string) **(requerido)**: ID of person, workspace or virtual line.
  - `weight` (string): Weight of person, workspace or virtual line. Only applied when call policy is `WEIGHTED`.
  - `skillLevel` (number): Skill level of person, workspace or virtual line. Only applied when call routing type is `SKILL_BASED`.
  - `joinEnabled` (boolean): Indicates the join status of the agent for this queue. The default value for newly added agents is `true`.
- `allowAgentJoinEnabled` (boolean): Whether or not to allow agents to join or unjoin a queue.
- `phoneNumberForOutgoingCallsEnabled` (boolean): When `true`, indicates that the agent's configuration allows them to use the queue's Caller ID for outgoing calls.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this workspace.
  - `selection` (string): * `DISPLAY_NAME` - When this option is selected, `displayName` is to be shown for this workspace.  * `CUSTOM_NAME` - When this option is selected, `customName` is to be shown for this workspace. Valores: CUSTOM_NAME, DISPLAY_NAME.
  - `customName` (string): Sets or clears the custom direct line caller ID name.  To clear the `customName`, the attribute must be set to null or empty string. Required if `selection` is set to `CUSTOM_NAME`.
- `dialByName` (string): Sets or clears the name to be used for dial by name functions. To clear the `dialByName`, the attribute must be set to null or empty string. Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.
- `digitalInboxEnabled` (boolean): Digital Inbox enabled for Queue. This field is applicable for queue which has `hasCxEssentials=true`.

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
