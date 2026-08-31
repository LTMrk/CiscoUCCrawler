---
doc_id: webex-contact-center-get-v1-agents-activities
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/agents/activities
operation_id: getAgentActivities
tags: Agents
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.747195+00:00
---

# GET /v1/agents/activities

**API:** Webex Contact Center
**Área:** Agents
**operationId:** `getAgentActivities`

## Resumen
Get Agent Activities

## Descripción
Retrieve agent activities. Sorted by start time ascending.
Maximum number of records that can be fetched for the given from and to is 10,000. 
For this API, response compression using gzip can be enabled by including 'Accept-Encoding' header  in the request with its value as 'gzip'. 
The response will be compressed only if its size exceeds 1 MB.
If the header is not present in the request or if gzip is not listed as one of the encodings in the header's value (comma separated encodings), then API response will not be compressed and this can impact the latency as observed from clients.

## Parámetros
- `agentIds` [query] (array): Filter agent activities by agent ids separated with commas if more than one value (max 100). By default, there is no agent filtering.
- `teamIds` [query] (array): Filter agent activities by team ids separated with commas if more than one value (max 100). By default, there is no team filtering.
- `channelTypes` [query] (array): Channel type(s) permitted in response. Separate values with commas. Must be lowercase. By default, there is no channelType filtering.
- `from` [query] (integer/int64) (**requerido**): Filter agent activities created after given epoch timestamp in UTC (in milliseconds).
- `to` [query] (integer/int64): Filter agent activities created before given epoch timestamp in UTC (in milliseconds). If unspecified, queries up to the present.  The difference between to and from timestamps must be less than 24 hours (86400000 milli seconds)
- `pageSize` [query] (integer/int32): Maximum page size in response. Maximum allowed value is 1000. Defaults to 100 items per page. Por defecto: 100.
- `page` [query] (integer/int32): Page number to be passed. Maximum number of records that can be fetched for the given from and to is 10,000. So maximum page number allowed is based on it. Defaults to 0. Por defecto: 0.
- `orgId` [query] (string): Organization ID to use for this operation. If unspecified, inferred from token. Token must have permission to interact with this organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes.

## Ejemplo de invocación
```bash
curl -X GET '/v1/agents/activities?from=<from>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object) (**requerido**): Response metadata.
  - `orgId` (string): Organization ID to which resources belong.
- `data` (array) (**requerido**): List of agent activities retrieved according to query parameters.
  - `active` (boolean) (**requerido**): Active indicates whether the activity is completed (false) or in progress (true).
  - `agentId` (string) (**requerido**): Unique identifier of an agent.
  - `agentDn` (string) (**requerido**): Dialed number for the agent.
  - `agentLogin` (string) (**requerido**): Login username of the agent.
  - `agentSessionId` (string) (**requerido**): Agent Session Id
  - `agentName` (string) (**requerido**): The name of the agent.
  - `currentState` (string) (**requerido**): The activity state (e.g. idle, available, connected, etc.).
  - `siteId` (string) (**requerido**): Unique identifier for a site.
  - `siteName` (string) (**requerido**): The name of the site.
  - `teamId` (string) (**requerido**): Unique identifier for a team.
  - `teamName` (string) (**requerido**): The name of the team.
  - `isLogin` (integer/int32) (**requerido**): Indicates whether the activity was the login event (1) or not (0).
  - `taskId` (string) (**requerido**): Unique identifier for a task.
  - `channelId` (string) (**requerido**): Unique identifier for the channel.
  - `channelType` (string) (**requerido**): Channel type for the activity (e.g. email, telephony, chat, etc.).
  - `subChannelType` (string) (**requerido**): SubChannel type for the activity.
  - `idleCodeName` (string) (**requerido**): In case of an idle activity, it will have an idle code attached with it (e.g. Break, Meeting, Lunch, etc.).
  - `idleCode` (string) (**requerido**): Unique identifier for the idle code.
  - `queueId` (string) (**requerido**): Unique identifier for the queue.
  - `queueName` (string) (**requerido**): The name of the Queue.
  - `wrapupCodeName` (string) (**requerido**): Selected wrapup code upon finished task.
  - `reason` (string) (**requerido**): Reason
  - `startTime` (integer/int64) (**requerido**): Epoch timestamp in milliseconds of the start of the activity.
  - `endTime` (integer/int64) (**requerido**): Epoch timestamp in milliseconds of the end of the activity. If active, it will be -1.
  - `mmProfileType` (string) (**requerido**): Multimedia profile type

## Respuestas de error
- **400**: Bad Request
- **401**: Unauthorized Operation
- **403**: Forbidden
- **413**: Content Too Large
- **422**: Unprocessable Entity
- **500**: An Unexpected Error Occurred
- **503**: The service is currently unavailable to serve the requests

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs