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
retrieved_at: 2026-11-16T14:22:47.298996+00:00
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
- `callPolicies` (object) (**requerido**): Policy controlling how calls are routed to `agents`.
- `queueSettings` (object) (**requerido**): Overall call queue settings.
- `agents` (array) (**requerido**): People, workspaces and virtual lines that are eligible to receive calls.
  - `id` (string) (**requerido**): ID of person, workspace or virtual line.
  - `weight` (string): Weight of person, workspace or virtual line. Only applied when call policy is `WEIGHTED`.
  - `skillLevel` (number): Skill level of person, workspace or virtual line. Only applied when call routing type is `SKILL_BASED`.
- `callingLineIdPolicy` (string): Which type of Calling Line ID Policy Selected for Call Queue.  * `DIRECT_LINE` - Calling Line ID Policy will show the caller's direct line number.  * `LOCATION_NUMBER` - Calling Line ID Policy will show the main number for the location.  * `CUSTOM` - Calling Line ID Policy will show the value from the `callingLineIdPhoneNumber` field. Valores: DIRECT_LINE, LOCATION_NUMBER, CUSTOM.
- `callingLineIdPhoneNumber` (string): Calling line ID Phone number which will be shown if CUSTOM is selected.
- `allowCallWaitingForAgentsEnabled` (boolean): Flag to indicate whether call waiting is enabled for agents.
- `allowAgentJoinEnabled` (boolean): Whether or not to allow agents to join or unjoin a queue.
- `phoneNumberForOutgoingCallsEnabled` (boolean): When `true`, indicates that the agent's configuration allows them to use the queue's Caller ID for outgoing calls.
- `directLineCallerIdName` (object): Settings for the direct line caller ID name to be shown for this call queue.
- `dialByName` (string): The name to be used for dial by name functions. Characters of `%`,  `+`, `\`, `"` and Unicode characters are not allowed.
- `digitalInboxEnabled` (boolean): Digital Inbox enabled for Queue. This field is applicable for queue which has `hasCxEssentials=true`.

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
    "callBounce": {
      "callBounceEnabled": true,
      "callBounceMaxRings": 5,
      "agentUnavailableEnabled": false,
      "alertAgentEnabled": false,
      "alertAgentMaxSeconds": 30,
      "callBounceOnHoldEnabled": false,
      "callBounceOnHoldMaxSeconds": 60
    },
    "distinctiveRing": {
      "enabled": false,
      "ringPattern": "NORMAL"
    },
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
          "id": "Y2lz
  ... (truncado)
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/queues' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "callPolicies": "<callPolicies>", "queueSettings": "<queueSettings>", "agents": []}'
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