---
doc_id: webex-contact-center-get-v1-agents-statistics
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v1/agents/statistics
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.962052+00:00
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
- `from` [query] (integer) **(requerido)**: Start time for the query (in epoch milliseconds). Any epoch time can be passed in the input, from date will be rounded down to nearest 15 minute window. For example, epoch time of 12:05 will be rounded down to 12:00.
- `to` [query] (integer) **(requerido)**: End time for the query (in epoch milliseconds). Any epoch time can be passed in the input, from date will be rounded down to nearest 15 minute window. For example, epoch time of 12:55 will be rounded down to 12:45.  The difference between to and from time must be less than 24 hours (86400000 milliseconds).
- `interval` [query] (integer): Time interval (in minutes) to chunk statistics by i.e. break up the entire from-to timeframe by this interval amount so that statistics can be viewed incrementally. Supported values are 15, 30, or 60.
- `agentIds` [query] (array): Comma-separated list of agent IDs. A maximum of 100 values is permitted. If values are not provided, all agents of an organization are returned.
- `orgId` [query] (string): Organization ID to use for this operation. If unspecified, inferred from token. Token must have permission to interact with this organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes.

## Respuestas
- **200**: OK
  - `meta` (object) **(requerido)**: Response metadata.
    - `orgId` (string): Organization ID to which resources belong.
  - `data` (array) **(requerido)**: List of Agent Statistics records retrieved according to query parameters.
    - `intervalStartTime` (integer): Time in GMT
    - `agentId` (string): The ID of the agent.
    - `agentName` (string): The name of the agent
    - `teamId` (string): The ID of the team.
    - `teamName` (string): Name of the team to which agent belongs.
    - `channels` (array) **(requerido)**: Channel-level statistics for the agent.
      - `channelType` (string): Channel Type
      - `totalAssignedTasks` (integer): Number of tasks assigned within the channel during the agent session.
      - `totalOfferedTasks` (integer): Number of offered tasks within this channel during the agent's session.
      - `totalAcceptedTasks` (integer): Number of assigned tasks that were accepted by the agent.
      - `totalRejectedTasks` (integer): Number of assigned tasks that were rejected by the agent.
      - `totalTransferredTasks` (integer): Number of tasks that the agent transferred to another agent.
      - `totalEngagedDuration` (integer): The amount of time the agent was engaged with a customer (in milliseconds). Note :- - Does not include wrap-up time and consult duration - Includes conferencing duration since the customer is involved
      - `totalHoldDuration` (integer): The amount of time for which the customer(s) was put on hold (in milliseconds).
      - `totalWrapUpDuration` (integer): The amount of time spent by the agent wrapping up customer interactions (in milliseconds). i.e Sum of all wrap-up time metric for a given agent
      - `totalAvailableTime` (integer): Duration of time(in milliseconds) outside of the idle time when an agent was available and handling contacts after logging in.
      - `totalUnAvailableTime` (integer): Amount of time the agent was unavailable (in milliseconds).
      - `averageHandledTime` (number): This is the average of the total handle time by an agent (in milliseconds) i.e avg(engagedDuration(connected state) + hold-duration  + wrap-up time)
- **400**: Bad Request
- **401**: Unauthorized Operation
- **403**: Forbidden
- **422**: Unprocessable Entity
- **500**: An Unexpected Error Occurred
- **503**: The service is currently unavailable to serve the requests

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
