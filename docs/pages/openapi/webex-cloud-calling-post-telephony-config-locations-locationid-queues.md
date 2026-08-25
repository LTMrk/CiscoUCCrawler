---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-queues
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/queues
operation_id: createCallQueue
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.471451+00:00
---

# POST /telephony/config/locations/{locationId}/queues

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `createCallQueue`

## Resumen
Create Call Queue or Customer Assist Queue

## Descripción
Create new Call Queues for the given location.

Call queues temporarily hold calls in the cloud, when all agents assigned to receive calls from the queue are unavailable.
Queued calls are routed to an available agent, when not on an active call. Each call queue is assigned a lead number, which is a telephone
number that external callers can dial to reach the users assigned to the call queue. Call queues are also assigned an internal extension,
which can be dialed internally to reach the users assigned to the call queue.

Creating a call queue requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): The location ID where the call queue needs to be created.
- `orgId` [query] (string): The organization ID where the call queue needs to be created.
- `hasCxEssentials` [query] (boolean): Creates a Customer Assist call queue, when `true`. This requires Customer Assist licensed agents.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Unique name for the call queue.
- `phoneNumber` (string): Primary phone number of the call queue. Either a `phoneNumber` or `extension` is mandatory.
- `extension` (string): Primary phone extension of the call queue. Either a `phoneNumber` or extension is mandatory.
- `languageCode` (string): Language code.
- `firstName` (string): First name to be shown when calls are forwarded out of this call queue. Defaults to ".". This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name to be shown when calls are forwarded out of this call queue. Defaults to `phoneNumber` if set, otherwise defaults to call group name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `timeZone` (string): Time zone for the call queue.
- `callPolicies` (object) (**requerido**):
  - `routingType` (string) (**requerido**): * `PRIORITY_BASED` - Default routing type which directly uses the routing policy to dispatch calls to the agents.  * `SKILL_BASED` - This option uses skill level as the criteria to route calls to agents. When there is more than one agent with the same skill level, the selected `policy` helps dispatch the calls to the agents. Valores: PRIORITY_BASED, SKILL_BASED.
  - `policy` (string) (**requerido**): * `CIRCULAR` - This option cycles through all agents after the last agent that took a call. It sends calls to the next available agent.  * `REGULAR` - Send the call through the queue of agents in order, starting from the top each time.  * `SIMULTANEOUS` - Sends calls to all agents at once  * `UNIFORM` - Sends calls to the agent that has been idle the longest. If they don't answer, proceed to the next agent who has been idle the second longest, and so on until the call is answered.  * `WEIGHTED` - Sends call to idle agents based on percentages you assign to each agent (up to 100%). Valores: CIRCULAR, REGULAR, SIMULTANEOUS, UNIFORM, WEIGHTED.
  - `callBounce` (object) (**requerido**): Settings for when the call into the hunt group is not answered.
    - `callBounceEnabled` (boolean): If enabled, bounce calls after the set number of rings.
    - `callBounceMaxRings` (number): Number of rings after which to bounce call, if `callBounce` is enabled.
    - `agentUnavailableEnabled` (boolean): Bounce if agent becomes unavailable.
    - `alertAgentEnabled` (boolean): Alert agent if call on hold more than `alertAgentMaxSeconds`.
    - `alertAgentMaxSeconds` (number): Number of second after which to alert agent if `alertAgentEnabled`.
    - `callBounceOnHoldEnabled` (boolean): Bounce if call on hold more than `callBounceMaxSeconds`.
    - `callBounceOnHoldMaxSeconds` (number): Number of second after which to bounce if `callBounceEnabled`.
  - `distinctiveRing` (object) (**requerido**): Whether or not the call queue has the `distinctiveRing` option enabled.
    - `enabled` (boolean) (**requerido**): Whether or not the `distinctiveRing` is enabled.
    - `ringPattern` (string): * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a short ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
- `queueSettings` (object) (**requerido**):
  - `queueSize` (number) (**requerido**): The maximum number of calls for this call queue. Once this number is reached, the `overflow` settings are triggered.
  - `callOfferToneEnabled` (boolean): Play ringing tone to callers when their call is set to an available agent.
  - `resetCallStatisticsEnabled` (boolean): Reset caller statistics upon queue entry.
  - `overflow` (object) (**requerido**): Settings for incoming calls exceed queueSize.
    - `action` (string) (**requerido**): Indicates how to handle new calls when the queue is full.  * `PERFORM_BUSY_TREATMENT` - The caller hears a fast-busy tone.  * `PLAY_RINGING_UNTIL_CALLER_HANGS_UP` - The caller hears ringing until they disconnect.  * `TRANSFER_TO_PHONE_NUMBER` - Number where you want to transfer overflow calls. Valores: PERFORM_BUSY_TREATMENT, PLAY_RINGING_UNTIL_CALLER_HANGS_UP, TRANSFER_TO_PHONE_NUMBER.
    - `sendToVoicemail` (boolean): When `true`, forwards all calls to a voicemail service of an internal number. This option is ignored when an external `transferNumber` is entered.
    - `transferNumber` (string): Destination number for overflow calls when `action` is set to `TRANSFER_TO_PHONE_NUMBER`.
    - `overflowAfterWaitEnabled` (boolean): After calls wait for the configured number of seconds and no agent is available, the overflow treatment is triggered.
    - `overflowAfterWaitTime` (number): Number of seconds to wait before the overflow treatment is triggered when no agent is available. The minimum value 0, The maximum value is 7200 seconds.
    - `playOverflowGreetingEnabled` (boolean): Indicate overflow audio to be played, otherwise, callers will hear the hold music until the call is answered by a user.
    - `greeting` (string) (**requerido**): Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
    - `audioAnnouncementFiles` (array): Array of announcement files to be played as `overflow` greetings. These files are from the list of announcement files associated with this call queue. For `CUSTOM` announcement, a minimum of 1 file is mandatory, and the maximum is 4.
      - `id` (string): Unique identifier of the Announcement file.
      - `name` (string): Name of the announcement file. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
      - `mediaFileType` (string): Media file type of announcement file.
      - `level` (string): The level at which this announcement exists. Valores: LOCATION, ORGANIZATION, ENTITY.
  - `welcomeMessage` (object): Play a message when callers first reach the queue. For example, “Thank you for calling. An agent will be with you shortly.” It can be set as mandatory. If the mandatory option is not selected and a caller reaches the call queue while there is an available agent, the caller will not hear this announcement and is transferred to an agent. The welcome message feature is enabled by default.
    - `enabled` (boolean): If enabled play entrance message. The default value is `true`.
    - `alwaysEnabled` (boolean): Mandatory entrance message. The default value is `false`.
    - `greeting` (string) (**requerido**): Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
    - `audioAnnouncementFiles` (array): Array of announcement files to be played as `welcomeMessage` greetings. These files are from the list of announcement files associated with this call queue. For `CUSTOM` announcement, a minimum of 1 file is mandatory, and the maximum is 4.
      - `id` (string): Unique identifier of the Announcement file.
      - `name` (string): Name of the announcement file. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
      - `mediaFileType` (string): Media file type of announcement file.
      - `level` (string): The level at which this announcement exists. Valores: LOCATION, ORGANIZATION, ENTITY.
  - `waitMessage` (object): Notify the caller with either their estimated wait time or position in the queue. If this option is enabled, it plays after the welcome message and before the comfort message. By default, it is not enabled.
    - `enabled` (boolean): If enabled play Wait Message.
    - `waitMode` (string) (**requerido**): Estimated wait message operating mode. Supported values `TIME` and `POSITION`.  * `TIME` - Announce the waiting time.  * `POSITION` - Announce queue position. Valores: TIME, POSITION.
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

### Ejemplo — petición
```json
{
  "name": "CallQueue-1",
  "phoneNumber": "+12225555309",
  "extension": "5309",
  "firstName": "Hakim",
  "lastName": "Smith",
  "callPolicies": {
    "policy": "CIRCULAR",
    "routingType": "SKILL_BASED",
    "waitingEnabled": false,
    "noAnswer": {
      "nextAgentEnabled": false,
      "nextAgentRings": 5,
      "forwardEnabled": false,
      "numberOfRings": 0,
      "destinationVoicemailEnabled": false
    },
    "businessContinuity": {
      "enabled": false,
      "destinationVoicemailEnabled": false
    }
  },
  "queueSettings": {
    "queueSize": 10,
    "callOfferToneEnabled": true,
    "resetCallStatisticsEnabled": true,
    "useEnterprisePlayToneToAgentSettingsEnabled": false,
    "playToneToAgentForBargeInEnabled": true,
    "playToneToAgentForSilentMonitoringEnabled": true,
    "playToneToAgentForSupervisorCoachingEnabled": true,
    "overflow": {
      "action": "PERFORM_BUSY_TREATMENT",
      "overflowAfterWaitEnabled": false,
      "overflowAfterWaitTime": 30,
      "playOverflowGreetingEnabled": false,
      "greeting": "DEFAULT",
      "audioAnnouncementFiles": [
        {
          "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9jZWRkODcwYS1lMTkzLTQxNmQtYmM3OS1mNzkyYmUyMzlhOGI",
          "fileName": "announcement.wav",
          "mediaFileType": "WAV",
          "level": "LOCATION"
        }
      ]
    },
    "welcomeMessage": {
      "enabled": true,
      "alwaysEnabled": false,
      "greeting": "DEFAULT",
      "audioAnnouncementFiles": [
       
  ... (truncado)
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/queues' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "callPolicies": {}, "queueSettings": {}, "agents": []}'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): ID of the newly created call queue.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0hVTlRfR1JPVVAvYUhaaFpUTjJNRzh5YjBBMk5EazBNVEk1Tnk1cGJuUXhNQzVpWTJ4a0xuZGxZbVY0TG1OdmJRPT0"
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs