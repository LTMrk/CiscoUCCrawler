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
retrieved_at: 2026-11-16T12:36:50.679379+00:00
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
    - `ringPattern` (object): Ring pattern for when this alternate number is called. Only available when `distinctiveRing` is enabled for the hunt group.
- `callPolicies` (object) (**requerido**): Policy controlling how calls are routed to agents.
- `queueSettings` (object) (**requerido**): Overall call queue settings.
- `allowCallWaitingForAgentsEnabled` (boolean): Flag to indicate whether call waiting is enabled for agents.
- `agents` (array) (**requerido**): People, workspaces and virtual lines that are eligible to receive calls.
  - `id` (string) (**requerido**): ID of person, workspace or virtual line.
  - `type` (string) (**requerido**): Type of the person, workspace or virtual line.  * `PEOPLE` - Indicates that this object is a user.  * `PLACE` - Indicates that this object is a place.  * `VIRTUAL_LINE` - Indicates that this object is a virtual line. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
  - `firstName` (string): First name of person, workspace or virtual line.
  - `lastName` (string): First name of person, workspace or virtual line.
  - `phoneNumber` (string): Phone number of person, workspace or virtual line.
  - `extension` (string): Extension of person, workspace or virtual line.
  - `routingPrefix` (string): Routing prefix of location.
  - `esn` (string): Routing prefix + extension of a person, workspace or virtual line.
  - `weight` (string): Weight of person, workspace or virtual line. Only applied when call policy is `WEIGHTED`.
  - `skillLevel` (number): Skill level of person, workspace or virtual line. Only applied when the call `routingType` is `SKILL_BASED`.
  - `joinEnabled` (boolean): Indicates the join status of the agent for this queue. The default value while creating call queue is `true`.
  - `location` (object): Location of the call queue.
  - `hasCxEssentials` (boolean): Person has the CX Essentials license.
- `allowAgentJoinEnabled` (boolean): Whether or not to allow agents to join or unjoin a queue.
- `department` (object): The department information.
  - `id` (string): Unique identifier of the department.
  - `name` (string): Name of the department.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this call queue.
- `dialByName` (string): The name to be used for dial by name functions.
- `digitalInboxEnabled` (boolean): Digital Inbox enabled for Queue. This field is applicable for queue which has `hasCxEssentials=true`.

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