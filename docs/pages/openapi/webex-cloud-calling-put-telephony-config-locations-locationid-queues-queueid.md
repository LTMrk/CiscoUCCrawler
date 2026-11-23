---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-queues-queueid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/queues/{queueId}
operation_id: updateCallQueue
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:15.838095+00:00
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
- `locationId` [path] (string) (**requerido**): Location in which this call queue exists.
- `queueId` [path] (string) (**requerido**): Update setting for the call queue with the matching ID.
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
    - `phoneNumber` (string) (**requerido**): Alternate phone number for the hunt group.
    - `ringPattern` (object): Ring pattern for when this alternate number is called. Only available when `distinctiveRing` is enabled for the hunt group.
- `callPolicies` (object): Policy controlling how calls are routed to agents.
- `callingLineIdPolicy` (string): Which type of Calling Line ID Policy Selected for Call Queue.  * `DIRECT_LINE` - Calling Line ID Policy will show the caller's direct line number.  * `LOCATION_NUMBER` - Calling Line ID Policy will show the main number for the location.  * `CUSTOM` - Calling Line ID Policy will show the value from the `callingLineIdPhoneNumber` field. Valores: DIRECT_LINE, LOCATION_NUMBER, CUSTOM.
- `callingLineIdPhoneNumber` (string): Calling line ID Phone number which will be shown if CUSTOM is selected.
- `queueSettings` (object) (**requerido**): Overall call queue settings.
- `allowCallWaitingForAgentsEnabled` (boolean): Flag to indicate whether call waiting is enabled for agents.
- `agents` (array): People, workspaces and virtual lines that are eligible to receive calls.
  - `id` (string) (**requerido**): ID of person, workspace or virtual line.
  - `weight` (string): Weight of person, workspace or virtual line. Only applied when call policy is `WEIGHTED`.
  - `skillLevel` (number): Skill level of person, workspace or virtual line. Only applied when call routing type is `SKILL_BASED`.
  - `joinEnabled` (boolean): Indicates the join status of the agent for this queue. The default value for newly added agents is `true`.
- `allowAgentJoinEnabled` (boolean): Whether or not to allow agents to join or unjoin a queue.
- `phoneNumberForOutgoingCallsEnabled` (boolean): When `true`, indicates that the agent's configuration allows them to use the queue's Caller ID for outgoing calls.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this call queue.
- `dialByName` (string): Sets or clears the name to be used for dial by name functions. To clear the `dialByName`, the attribute must be set to null or empty string. Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.
- `digitalInboxEnabled` (boolean): Digital Inbox enabled for Queue. This field is applicable for queue which has `hasCxEssentials=true`.

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/queues/<queueId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"queueSettings": "<queueSettings>"}'
```

## Respuestas correctas
**204**: No Content

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