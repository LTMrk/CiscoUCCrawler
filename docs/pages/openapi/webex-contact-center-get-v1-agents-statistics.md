---
doc_id: webex-contact-center-get-v1-agents-statistics
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/agents/statistics
operation_id: getDocumentByQueryParam
tags: Agents
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.139271+00:00
---

# GET /v1/agents/statistics

**API:** Webex Contact Center
**Área:** Agents
**operationId:** `getDocumentByQueryParam`

## Resumen
Get Agent Statistics

## Descripción
Retrieve Agent statistics information for specified time duration and interval.
For this API, response compression using gzip can be enabled by including 'Accept-Encoding' header  in the request with its value as 'gzip'. 
The response will be compressed only if its size exceeds 1 MB.
If the header is not present in the request or if gzip is not listed as one of the encodings in the header's value (comma separated encodings), then API response will not be compressed and this can impact the latency as observed from clients.

## Parámetros
- `from` [query] (integer/int64) (**requerido**): Start time for the query (in epoch milliseconds). Any epoch time can be passed in the input, from date will be rounded down to nearest 15 minute window. For example, epoch time of 12:05 will be rounded down to 12:00.
- `to` [query] (integer/int64) (**requerido**): End time for the query (in epoch milliseconds). Any epoch time can be passed in the input, from date will be rounded down to nearest 15 minute window. For example, epoch time of 12:55 will be rounded down to 12:45.  The difference between to and from time must be less than 24 hours (86400000 milliseconds).
- `interval` [query] (integer/int32): Time interval (in minutes) to chunk statistics by i.e. break up the entire from-to timeframe by this interval amount so that statistics can be viewed incrementally. Supported values are 15, 30, or 60.
- `agentIds` [query] (array): Comma-separated list of agent IDs. A maximum of 100 values is permitted. If values are not provided, all agents of an organization are returned.
- `orgId` [query] (string): Organization ID to use for this operation. If unspecified, inferred from token. Token must have permission to interact with this organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes.

## Ejemplo de invocación
```bash
curl -X GET '/v1/agents/statistics?from=<from>&to=<to>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object) (**requerido**): Response metadata.
  - `orgId` (string): Organization ID to which resources belong.
- `data` (array) (**requerido**): List of Agent Statistics records retrieved according to query parameters.
  - `intervalStartTime` (integer/int64): Time in GMT
  - `agentId` (string): The ID of the agent.
  - `agentName` (string): The name of the agent
  - `teamId` (string): The ID of the team.
  - `teamName` (string): Name of the team to which agent belongs.
  - `channels` (array) (**requerido**): Channel-level statistics for the agent.
    - `channelType` (string): Channel Type
    - `totalAssignedTasks` (integer/int32): Number of tasks assigned within the channel during the agent session.
    - `totalOfferedTasks` (integer/int32): Number of offered tasks within this channel during the agent's session.
    - `totalAcceptedTasks` (integer/int32): Number of assigned tasks that were accepted by the agent.
    - `totalRejectedTasks` (integer/int32): Number of assigned tasks that were rejected by the agent.
    - `totalTransferredTasks` (integer/int32): Number of tasks that the agent transferred to another agent.
    - `totalEngagedDuration` (integer/int32): The amount of time the agent was engaged with a customer (in milliseconds). Note :- - Does not include wrap-up time and consult duration - Includes conferencing duration since the customer is involved
    - `totalHoldDuration` (integer/int64): The amount of time for which the customer(s) was put on hold (in milliseconds).
    - `totalWrapUpDuration` (integer/int64): The amount of time spent by the agent wrapping up customer interactions (in milliseconds). i.e Sum of all wrap-up time metric for a given agent
    - `totalAvailableTime` (integer/int64): Duration of time(in milliseconds) outside of the idle time when an agent was available and handling contacts after logging in.
    - `totalUnAvailableTime` (integer/int64): Amount of time the agent was unavailable (in milliseconds).
    - `averageHandledTime` (number/double): This is the average of the total handle time by an agent (in milliseconds) i.e avg(engagedDuration(connected state) + hold-duration  + wrap-up time)

## Respuestas de error
- **400**: Bad Request
- **401**: Unauthorized Operation
- **403**: Forbidden
- **422**: Unprocessable Entity
- **500**: An Unexpected Error Occurred
- **503**: The service is currently unavailable to serve the requests

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs