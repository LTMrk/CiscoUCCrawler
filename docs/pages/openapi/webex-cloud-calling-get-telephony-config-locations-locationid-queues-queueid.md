---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-queues-queueid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/queues/{queueId}
operation_id: getCallQueueWithCustomerAssist
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.690740+00:00
---

# GET /telephony/config/locations/{locationId}/queues/{queueId}

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `getCallQueueWithCustomerAssist`

## Resumen
Get Details for a Call Queue or Customer Assist Queue

## Descripción
Retrieve Call Queue details.

Call queues temporarily hold calls in the cloud, when all agents assigned to receive calls from the queue are unavailable.
Queued calls are routed to an available agent, when not on an active call. Each call queue is assigned a lead number, which is a telephone
number that external callers can dial to reach the users assigned to the call queue. Call queues are also assigned an internal extension,
which can be dialed internally to reach the users assigned to the call queue.

Retrieving call queue details requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieves the details of a call queue in this location.
- `queueId` [path] (string) (**requerido**): Retrieves the details of call queue with this identifier.
- `orgId` [query] (string): Retrieves the details of a call queue in this organization.
- `hasCxEssentials` [query] (boolean): Must be set to `true`, to view the details of a call queue with Customer Assist license. This can otherwise be ommited or set to `false`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/queues/<queueId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for the call queue.
- `name` (string) (**requerido**): Unique name for the call queue.
- `hasCxEssentials` (boolean): Denotes if the call queue has Customer Assist license.
- `enabled` (boolean) (**requerido**): Whether or not the call queue is enabled.
- `language` (string): Language for call queue.
- `languageCode` (string): Language code for call queue.
- `firstName` (string): First name to be shown when calls are forwarded out of this call queue. Defaults to `.`. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `lastName` (string): Last name to be shown when calls are forwarded out of this call queue. Defaults to the `phoneNumber` if set, otherwise defaults to call group name. This field has been deprecated. Please use `directLineCallerIdName` and `dialByName` instead.
- `timeZone` (string): Time zone for the call queue.
- `phoneNumber` (string): Primary phone number of the call queue.
- `numberUsageType` (string): Number type of primary number assigned to queue.  * `PSTN_NUMBER` - Public Switched Telephone Network (PSTN) number.  * `MOBILE_NUMBER` - Mobile number.  * `SERVICE_NUMBER` - A number used in high-volume service.  * `ELIN` - Emergency Location Identification Number (ELIN), numbers can be used to place emergency calls from a location. Valores: PSTN_NUMBER, MOBILE_NUMBER, SERVICE_NUMBER, ELIN.
- `businessTextingEnabled` (boolean): Indicates whether business texting is enabled for the primary number assigned to the queue. This field is read-only and cannot be modified through the queue APIs.
- `extension` (string): Extension of the call queue.
- `routingPrefix` (string): Routing prefix of location.
- `esn` (string): Routing prefix + extension of the call queue.
- `tollFreeNumber` (boolean): Indicate if the number is toll free.
- `phoneNumberForOutgoingCallsEnabled` (boolean): When true, indicates that the agent's configuration allows them to use the queue's Caller ID for outgoing calls.
- `callingLineIdPolicy` (string): Which type of Calling Line ID Policy Selected for Call Queue.  * `DIRECT_LINE` - Calling Line ID Policy will show the caller's direct line number.  * `LOCATION_NUMBER` - Calling Line ID Policy will show the main number for the location.  * `CUSTOM` - Calling Line ID Policy will show the value from the `callingLineIdPhoneNumber` field. Valores: DIRECT_LINE, LOCATION_NUMBER, CUSTOM.
- `callingLineIdPhoneNumber` (string): Calling line ID Phone number which will be shown if CUSTOM is selected.
- `alternateNumberSettings` (object) (**requerido**): The alternate numbers feature allows you to assign multiple phone numbers or extensions to a call queue. Each number will reach the same greeting and each menu will function identically to the main number. The alternate numbers option enables you to have up to ten (10) phone numbers ring into the call queue.
  - `distinctiveRingEnabled` (boolean) (**requerido**): Distinctive Ringing selected for the alternate numbers in the call queue overrides the normal ringing patterns set for Alternate Number.
  - `alternateNumbers` (array) (**requerido**): Allows up to 10 numbers, each with an optional distinctive ring setting override.
    - `phoneNumber` (string) (**requerido**): Alternate phone number for the hunt group.
    - `ringPattern` (string): * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a short ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
- `callPolicies` (object) (**requerido**):
  - `policy` (string) (**requerido**): * `CIRCULAR` - This option cycles through all agents after the last agent that took a call. It sends calls to the next available agent.  * `REGULAR` - Send the call through the queue of agents in order, starting from the top each time.  * `SIMULTANEOUS` - Sends calls to all agents at once  * `UNIFORM` - Sends calls to the agent that has been idle the longest. If they don't answer, proceed to the next agent who has been idle the second longest, and so on until the call is answered.  * `WEIGHTED` - Sends call to idle agents based on percentages you assign to each agent (up to 100%). Valores: CIRCULAR, REGULAR, SIMULTANEOUS, UNIFORM, WEIGHTED.
  - `callBounce` (object) (**requerido**): Settings for when the call into the call queue is not answered.
    - `callBounceEnabled` (boolean) (**requerido**): If enabled, bounce calls after the set number of rings.
    - `callBounceMaxRings` (number) (**requerido**): Number of rings after which to bounce call, if call bounce is enabled.
    - `agentUnavailableEnabled` (boolean) (**requerido**): Bounce if agent becomes unavailable.
    - `alertAgentEnabled` (boolean) (**requerido**): Alert agent if call on hold more than alertAgentMaxSeconds.
    - `alertAgentMaxSeconds` (number) (**requerido**): Number of second after which to alert agent if alertAgentEnabled.
    - `callBounceOnHoldEnabled` (boolean) (**requerido**): Bounce if call on hold more than callBounceMaxSeconds.
    - `callBounceOnHoldMaxSeconds` (number) (**requerido**): Number of second after which to bounce if callBounceEnabled.
  - `distinctiveRing` (object) (**requerido**): Whether or not the call queue has the distinctive ring option enabled.
    - `enabled` (boolean) (**requerido**): Whether or not the distinctive ring is enabled.
    - `ringPattern` (string): * `NORMAL` - Normal incoming ring pattern.  * `LONG_LONG` - Incoming ring pattern of two long rings.  * `SHORT_SHORT_LONG` - Incoming ring pattern of two short rings, followed by a short ring.  * `SHORT_LONG_SHORT` - Incoming ring pattern of a short ring, followed by a long ring, followed by a short ring. Valores: NORMAL, LONG_LONG, SHORT_SHORT_LONG, SHORT_LONG_SHORT.
  - `routingType` (string): * `PRIORITY_BASED` - Default routing type which directly uses the routing policy to dispatch calls to the agents.  * `SKILL_BASED` - This option uses skill level as the criteria to route calls to agents. When there is more than one agent with the same skill level, the selected `policy` helps dispatch the calls to the agents. Valores: PRIORITY_BASED, SKILL_BASED.
- `queueSettings` (object) (**requerido**):
  - `queueSize` (number) (**requerido**): The maximum number of calls for this call queue. Once this number is reached, the overflow settings are triggered.
  - `callOfferToneEnabled` (boolean): Play ringing tone to callers when their call is set to an available agent.
  - `resetCallStatisticsEnabled` (boolean): Reset caller statistics upon queue entry.
  - `overflow` (object) (**requerido**): Settings for incoming calls exceed queueSize.
    - `action` (string) (**requerido**): Indicates how to handle new calls when the queue is full.  * `PERFORM_BUSY_TREATMENT` - The caller hears a fast-busy tone.  * `PLAY_RINGING_UNTIL_CALLER_HANGS_UP` - The caller hears ringing until they disconnect.  * `TRANSFER_TO_PHONE_NUMBER` - Number where you want to transfer overflow calls. Valores: PERFORM_BUSY_TREATMENT, PLAY_RINGING_UNTIL_CALLER_HANGS_UP, TRANSFER_TO_PHONE_NUMBER.
    - `sendToVoicemail` (boolean): When `true`, forwards all calls to a voicemail service of an internal number. This option is ignored when an external `transferNumber` is entered.
    - `transferNumber` (string): Destination number for overflow calls when `action` is set to `TRANSFER_TO_PHONE_NUMBER`.
    - `overflowAfterWaitEnabled` (boolean): After calls wait for the configured number of seconds and no agent is available, the overflow treatment is triggered.
    - `overflowAfterWaitTime` (number): Number of seconds to wait before the overflow treatment is triggered when no agent is available.
    - `playOverflowGreetingEnabled` (boolean): Indicate overflow audio to be played, otherwise callers will hear the hold music until the call is answered by a user.
    - `greeting` (string) (**requerido**): Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
    - `audioFiles` (array): Array of announcement file name strings to be played as overflow greetings. These files are from the list of announcements files associated with this call queue.
  - `welcomeMessage` (object): Play a message when callers first reach the queue. For example, “Thank you for calling. An agent will be with you shortly.” It can be set as mandatory. If the mandatory option is not selected and a caller reaches the call queue while there is an available agent, the caller will not hear this announcement and is transferred to an agent. The welcome message feature is enabled by default.
    - `enabled` (boolean): If enabled play entrance message. The default value is `true`.
    - `alwaysEnabled` (boolean): Mandatory entrance message. The default value is `false`.
    - `greeting` (string) (**requerido**): Indicates how to handle new calls when the queue is full.  * `CUSTOM` - Play the custom announcement specified by the `fileName` field.  * `DEFAULT` - Play default announcement. Valores: CUSTOM, DEFAULT.
    - `audioAnnouncementFiles` (array): Array of announcement files to be played as `welcomeMessage` greetings. These files are from the list of announcement files associated with this call queue. For `CUSTOM` announcement, a minimum of 1 file is mandatory, and the maximum is 4.
      - `id` (string) (**requerido**): Unique identifier of the Announcement file.
      - `name` (string) (**requerido**): Name of the announcement file.
      - `mediaFileType` (string) (**requerido**): Media file type of announcement file.
      - `level` (string) (**requerido**): The level at which this announcement exists. Valores: LOCATION, ORGANIZATION, ENTITY.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUVVFVUUvNTU1MzY4Y2QtZDg5Mi00YzFlLTk0YjYtNzdjNjRiYWQ3NWMx",
  "name": "CallQueue-1",
  "hasCxEssentials": true,
  "enabled": true,
  "language": "English",
  "languageCode": "en-US",
  "firstName": "Hakim",
  "lastName": "Smith",
  "timeZone": "Central/Chicago",
  "numberUsageType": "SERVICE_NUMBER",
  "businessTextingEnabled": true,
  "alternateNumberSettings": {
    "distinctiveRingEnabled": true,
    "alternateNumbers": [
      {
        "phoneNumber": "+9725554726",
        "ringPattern": "NORMAL"
      },
      {
        "phoneNumber": "+9725554729",
        "ringPattern": "NORMAL"
      }
    ]
  },
  "callPolicies": {
    "policy": "REGULAR",
    "callBounce": {
      "callBounceEnabled": true,
      "callBounceMaxRings": 8,
      "agentUnavailableEnabled": false,
      "alertAgentEnabled": false,
      "alertAgentMaxSeconds": 30,
      "callBounceOnHoldEnabled": false,
      "callBounceOnHoldMaxSeconds": 60
    },
    "distinctiveRing": {
      "enabled": false,
      "ringPattern": "NORMAL"
    }
  },
  "queueSettings": {
    "queueSize": 10,
    "callOfferToneEnabled": false,
    "resetCallStatisticsEnabled": false,
    "overflow": {
      "action": "PERFORM_BUSY_TREATMENT",
      "sendToVoicemail": false,
      "overflowAfterWaitEnabled": false,
      "overflowAfterWaitTime": 30,
      "playOverflowGreetingEnabled": false,
      "greeting": "DEFAULT",
      "isTransferNumberSet": false
    },
    "waitMessage": {
      "enabled
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