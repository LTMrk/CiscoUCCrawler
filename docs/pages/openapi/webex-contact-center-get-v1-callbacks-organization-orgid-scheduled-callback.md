---
doc_id: webex-contact-center-get-v1-callbacks-organization-orgid-scheduled-callback
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v1/callbacks/organization/{orgId}/scheduled-callback
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.963147+00:00
---

# GET /v1/callbacks/organization/{orgId}/scheduled-callback

**API:** Webex Contact Center
**Área:** Callbacks
**operationId:** `GetScheduledCallbacks`

## Resumen
Get scheduled callbacks

## Descripción
Allows the user to list scheduled callbacks for a given customer number or assignee agent, excluding those whose scheduled trigger time has already passed. Requires 'cjp:user' scope for authorization.

## Parámetros
- `orgId` [path] (string) **(requerido)**: The organization ID for which the callback is being scheduled. This should be a valid UUID.
- `callbackNumber` [query] (string): The callback customer number to filter the scheduled callbacks. Only an exact match will yield the result. Allows an optional country code followed by digits (0-9) and the special characters: space, hyphen -, parentheses ( and ), and period ., ensuring the total length is between 7 and 15 characters.
- `assigneeAgent` [query] (string): The unique identifier of the agent assigned to handle the callback. Must be in UUID format. This parameter is optional, but at least one of assigneeAgent or callbackNumber must be provided.
- `page` [query] (integer): The page number to retrieve.
- `pageSize` [query] (integer): The number of items per page.
- `sortBy` [query] (string): The field to sort the results by. If `sortBy` is set to `assignedTime`, the `assigneeAgent` parameter must also be provided.
- `sortOrder` [query] (string): The order to sort the results in.

## Respuestas
- **200**: The get scheduled callback request was successfully processed.
  - `meta` (object):
    - `orgId` (string) **(requerido)**: Unique identifier for the organization.
    - `page` (integer) **(requerido)**: Current page number.
    - `pageSize` (integer) **(requerido)**: Number of items per page.
    - `totalPages` (integer) **(requerido)**: Total number of pages.
    - `totalRecords` (integer) **(requerido)**: Total number of items.
    - `links` (object) **(requerido)**:
      - `self` (string) **(requerido)**: Link to the current page.
      - `first` (string): Link to the first page.
      - `last` (string): Link to the last page.
      - `next` (string): Link to the next page.
      - `prev` (string): Link to the previous page.
  - `data` (array):
    - `id` (string) **(requerido)**: Unique identifier for the scheduled callback.
    - `customerName` (string) **(requerido)**: Name of the customer requesting the callback.
    - `callbackNumber` (string) **(requerido)**: Phone number provided for the callback.
    - `timezone` (string) **(requerido)**: Timezone in which the callback is scheduled.
    - `scheduleDate` (string) **(requerido)**: Date for the callback in ISO format (YYYY-MM-DD).
    - `startTime` (string) **(requerido)**: Scheduled start time in ISO 8601 format (HH:mm:ss), local to the specified timezone.
    - `endTime` (string) **(requerido)**: Scheduled end time in ISO 8601 format (HH:mm:ss), local to the specified timezone.
    - `queueId` (string) **(requerido)**: Identifier for the queue to route the callback request.
    - `callbackReason` (string): Reason provided for the callback request.
    - `sourceInteraction` (string): UUID of the source interaction.
    - `callbackOrigin` (string) **(requerido)**: Origin of the callback request, such as 'livecall' or 'api'.
    - `createdTimestamp` (integer) **(requerido)**: Unix timestamp in milliseconds when the callback was created.
    - `lastUpdatedTimestamp` (integer) **(requerido)**: Unix timestamp in milliseconds when the callback was last updated.
    - `assigneeAgent` (string): The unique identifier of the agent assigned to handle the callback.
    - `assignedTime` (integer): Unix timestamp in milliseconds when the assigneeAgent was last updated.
    - `orgId` (string) **(requerido)**: Unique identifier for the organization.
- **400**: Bad Request: Validation error. This can occur in the following cases: - Both `assigneeAgent` and `callbackNumber` are missing. - `assigneeAgent` is not in UUID format. - `sortBy` is set to `assignedTime` but `assigneeAgent` is not provided.
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **429**: Too Many Requests
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
