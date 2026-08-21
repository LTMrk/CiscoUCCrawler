---
doc_id: webex-contact-center-get-v1-tasks
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/tasks
operation_id: searchTasks
tags: Tasks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.800400+00:00
---

# GET /v1/tasks

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `searchTasks`

## Resumen
Get Tasks

## Descripción
Retrieve open and closed tasks. Sorted by createdTime ascending. Uses offset-based pagination.
For this API, response compression using gzip can be enabled by including 'Accept-Encoding' header  in the request with its value as 'gzip'. 
The response will be compressed only if its size exceeds 1 MB.
If the header is not present in the request or if gzip is not listed as one of the encodings in the header's value (comma separated encodings), then API response will not be compressed and this can impact the latency as observed from clients.

## Parámetros
- `channelTypes` [query] (array): Task channel type(s) permitted in response. Separate values with commas. Use lowercase. By default, there is no channelType filtering.
- `from` [query] (integer/int64) (**requerido**): Filters tasks created after the given epoch timestamp (in milliseconds).
- `to` [query] (integer/int64): Filters tasks created before the given epoch timestamp (in milliseconds); queries up to the present if timestamp is not specified.
- `pageSize` [query] (integer/int32): Maximum page size in the response. Maximum allowed value is 1000. Defaults to 100 items per page. Por defecto: 100.
- `orgId` [query] (string): Organization ID to use for this operation. If unspecified, inferred from token. Token must have permission to interact with this organization.
- `TrackingId` [header] (string): Tracking ID to use for this operation, for traceability, debugging, and error reporting purposes.

## Ejemplo de invocación
```bash
curl -X GET '/v1/tasks?from=<from>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object) (**requerido**): Response metadata.
  - `orgId` (string): Organization ID to which resources belong.
- `data` (array) (**requerido**): List of tasks retrieved according to query parameters.
  - `id` (string) (**requerido**): ID of the task.
  - `attributes` (object) (**requerido**): Attributes of the task.
    - `owner` (object) (**requerido**): The owner of the task.
      - `id` (string) (**requerido**): ID of the agent last assigned to this task.
      - `name` (string) (**requerido**): Name of the agent last assigned to this task.
    - `queue` (object) (**requerido**): The queue where the task belongs.
      - `id` (string) (**requerido**): ID of the last queue to which the task was assigned.
      - `name` (string) (**requerido**): Name of the last queue to which the task was assigned.
    - `channelType` (string) (**requerido**): Task channel type(s) permitted in the response. Must be lowercase. By default, there is no channel type filtering.
    - `status` (string) (**requerido**): Current status of the task. Valores: created, queued, offered, assigned, abandoned, completed.
    - `createdTime` (integer/int64) (**requerido**): Created time of the task (epoch milliseconds).
    - `lastUpdatedTime` (integer/int64) (**requerido**): Last updated time of the task (epoch milliseconds). Updates whenever the underlying data is modified, even if the Task view of the data is the same. May also update after task "closure", so not suitable for finding a task's "closed time"
    - `captureRequested` (boolean): Whether a capture has been requested for this Task. If this is true, a capture should eventually be available. False indicates no capture will be made available. If null, it is not yet known whether a capture has been requested.
    - `origin` (string): Customer's channel-specific identifier. For telephony, this is the phone number. For email and chat, this is the email address.
    - `destination` (string): Destination the customer contacted. For telephony, this is the number the contact called. For chat, this is the URL of the page where the chat takes place. For email, it is the email address contacted.
    - `direction` (string): Indicates which party initiated the Task. If "inbound", call was initiated by customer. If "outbound", was initiated by system as part of campaign. If "outdial", was initiated by an agent.
    - `reasonCode` (string): Reason code specified by customer to indicate main aim of the task

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