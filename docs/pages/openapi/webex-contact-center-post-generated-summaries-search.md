---
doc_id: webex-contact-center-post-generated-summaries-search
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /generated-summaries/search
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.921203+00:00
---

# POST /generated-summaries/search

**API:** Webex Contact Center
**Área:** Agent Summaries
**operationId:** `listSummaries`

## Resumen
List summaries

## Descripción
Lists summaries based on the requested search type.

## Respuestas
- **200**: Successful operation
  - `orgId` (string): The unique identifier of the organization to which the summarized interactions belong.
  - `agentCiUserId` (string): The CI (Common Identity) user ID of the agent associated with the summaries. Present when searchType is AGENT; otherwise null.
  - `interactionId` (string): The unique identifier of a specific interaction. Present when searchType is INTERACTION; otherwise null.
  - `queueId` (string): The queue ID (reserved for future use).
  - `searchType` (string): The type of search to be performed. Valores: ORGANIZATION, INTERACTION, AGENT.
  - `summaries` (object): Map of summaries keyed by feature type (POST_CALL, MID_CALL). Each feature maps summary identifiers to their summary fields.
    - `POST_CALL` (object): Post-call summaries keyed by summary identifier.
    - `MID_CALL` (object): Mid-call summaries keyed by summary identifier.
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
