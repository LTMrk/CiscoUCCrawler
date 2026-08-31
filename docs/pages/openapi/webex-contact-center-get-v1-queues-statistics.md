---
doc_id: webex-contact-center-get-v1-queues-statistics
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/queues/statistics
operation_id: getDocumentByQueryParam_1
tags: Queues
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.742797+00:00
---

# GET /v1/queues/statistics

**API:** Webex Contact Center
**Área:** Queues
**operationId:** `getDocumentByQueryParam_1`

## Resumen
Get Queue Statistics

## Descripción
Retrieve Queue statistics for a given interval of time. 
An important thing to note is that each stat produced is for a specified time window (last 15, 30, or 60 minutes etc) and is not cumulative. 
Contacts that span across intervals will also have stats broken down across intervals. For example: A contact that starts at 12:05 and ends at 12:25 will have stats for Interval A (12:00-12:15) and Interval B (12:15-12:30) assuming the interval window is for 15 minutes. 
Stats that only require the start time of the contact like 'totalOfferedTasks' and 'totalAcceptedTasks' will be counted only once and it will be present in the interval where the contact started i.e. Interval A. 
Whereas, stats that require the end time as well for calculations like 'averageHandledTime', will be present in the interval where the contact ended i.e. interval B. 

For this API, response compression using gzip can be enabled by including 'Accept-Encoding' header  in the request with its value as 'gzip'. 
The response will be compressed only if its size exceeds 1 MB.
If the header is not present in the request or if gzip is not listed as one of the encodings in the header's value (comma separated encodings), then API response will not be compressed and this can impact the latency as observed from clients.

## Parámetros
- `from` [query] (integer/int64) (**requerido**): Start time for the query (in epoch milliseconds). Any epoch time can be passed in the input, from date will be rounded down to nearest 15 minute window. For example, epoch time of 12:05 will be rounded down to 12:00.
- `to` [query] (integer/int64) (**requerido**): End time for the query (in epoch milliseconds). Any epoch time can be passed in the input, from date will be rounded down to nearest 15 minute window. For example, epoch time of 12:55 will be rounded down to 12:45.  The difference between to and from time must be less than 24 hours (86400000 milliseconds).
- `interval` [query] (integer/int32): Time interval (in minutes) to chunk statistics by i.e. break up the entire from-to timeframe by this interval amount so that statistics can be viewed incrementally. Supported values are 15, 30, or 60.
- `queueIds` [query] (array): Comma-separated list of queue IDs. A maximum of 100 values is permitted. If values are not provided, all queues for an organization are returned.
- `orgId` [query] (string): Organization ID to use for this operation. If unspecified, inferred from token. Token must have permission to interact with this organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes.

## Ejemplo de invocación
```bash
curl -X GET '/v1/queues/statistics?from=<from>&to=<to>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object) (**requerido**): Response metadata.
  - `orgId` (string): Organization ID to which resources belong.
- `data` (array) (**requerido**): List of Queue statistics records retrieved according to query parameters.
  - `intervalStartTime` (integer/int64): Time in GMT (milliseconds)
  - `queueId` (string): The ID of the Queue.
  - `queueName` (string): Name of the queue.
  - `channelType` (string): The type of channel associated with this operation.
  - `totalOfferedTasks` (integer/int32): Number of times tasks were offered to the agents in the queue during the interval. This count includes the ones that are accepted or rejected by the agent.
  - `totalEnqueuedTasks` (integer/int32): Number of times tasks were parked in the queue during the interval. Tasks are not parked in queue if they are offered to an agent immediately since one is available.
  - `totalAssignedTasks` (integer/int32) (DEPRECADO): DEPRECATED FIELD, This field always returns 0
  - `totalAcceptedTasks` (integer/int32): Number of assigned tasks that were accepted in the queue.
  - `totalRejectedTasks` (integer/int32): Number of times tasks were rejected by the agents when they were offered during the interval.
  - `totalAbandonedTasks` (integer/int32): Number of assigned tasks that were abandoned in the queue.
  - `averageEnqueuedTime` (number/double): The Queue's average enqueue time in milli seconds. i.e total time in queue / number of calls that were queued
  - `averageHandledTime` (number/double): The Queue's average handle time in milli seconds. i.e total time the call was connected / number of calls that were handled. Note :- This does not include wrap-up time
  - `serviceLevelThresholdPercentage` (number/double): The Service Level threshold % is an aggregate percentage based on how many contacts out of the total handled have met the service level value and gives an indication of the timely pick-up of contacts by agents.

## Respuestas de error
- **400**: Validation Error
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