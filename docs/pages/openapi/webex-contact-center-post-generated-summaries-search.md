---
doc_id: webex-contact-center-post-generated-summaries-search
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /generated-summaries/search
operation_id: listSummaries
tags: Agent Summaries
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.653284+00:00
---

# POST /generated-summaries/search

**API:** Webex Contact Center
**Área:** Agent Summaries
**operationId:** `listSummaries`

## Resumen
List summaries

## Descripción
Lists summaries based on the requested search type.

## Cuerpo de la petición (application/json)
- (uno de:)
  - `orgId` (string) (**requerido**): The unique identifier of the organization to which the summarized interactions belong.
  - `searchType` (string) (**requerido**): The type of search to be performed. Valores: ORGANIZATION.
  - `orgId` (string) (**requerido**): The unique identifier of the organization to which the summarized interactions belong.
  - `interactionId` (string) (**requerido**): The unique identifier of a specific interaction.
  - `searchType` (string) (**requerido**): The type of search to be performed. Valores: INTERACTION.
  - `orgId` (string) (**requerido**): The unique identifier of the organization to which the summarized interactions belong.
  - `agentCiUserId` (string) (**requerido**): The CI (Common Identity) user ID of the agent associated with the summaries.
  - `searchType` (string) (**requerido**): The type of search to be performed. Valores: AGENT.

### Case 1: List by organizationId — petición
```json
{
  "searchType": "ORGANIZATION",
  "orgId": "acc80d18-b1fb-4261-b44e-a46435eea1da"
}
```

### Case 2: List by interactionId — petición
```json
{
  "searchType": "INTERACTION",
  "orgId": "acc80d18-b1fb-4261-b44e-a46435eea1da",
  "interactionId": "9d2a7879-8957-4cd6-a39c-46d4f21eaea5"
}
```

### Case 3: List by agentCiUserId — petición
```json
{
  "searchType": "AGENT",
  "agentCiUserId": "77e70d79-64b1-402e-9b84-b113ad71b06d",
  "orgId": "acc80d18-b1fb-4261-b44e-a46435eea1da"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/generated-summaries/search' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: Successful operation
- `orgId` (string): The unique identifier of the organization to which the summarized interactions belong.
- `agentCiUserId` (string): The CI (Common Identity) user ID of the agent associated with the summaries. Present when searchType is AGENT; otherwise null.
- `interactionId` (string): The unique identifier of a specific interaction. Present when searchType is INTERACTION; otherwise null.
- `queueId` (string): The queue ID (reserved for future use).
- `searchType` (string): The type of search to be performed. Valores: ORGANIZATION, INTERACTION, AGENT.
- `summaries` (object): Map of summaries keyed by feature type (POST_CALL, MID_CALL). Each feature maps summary identifiers to their summary fields.
  - `POST_CALL` (object): Post-call summaries keyed by summary identifier.
  - `MID_CALL` (object): Mid-call summaries keyed by summary identifier.

### Case 1: List by organizationId — respuesta 200
```json
{
  "interactionId": null,
  "orgId": "acc80d18-b1fb-4261-b44e-a46435eea1da",
  "searchType": "ORGANIZATION",
  "agentCiUserId": null,
  "summaries": {
    "POST_CALL": {
      "acc80d18-b1fb-4261-b44e-a46435eea1da:1bf3bd99-633b-401a-a3d4-61157a446809:c47d7c08-0776-4e38-a6bb-751d933a0c5d": {
        "initialContactReason": "Broken tools appointment request",
        "additionalContext": "Customer mentioned they had previously tried to fix the tools themselves but were unsuccessful.",
        "additionalContactReasons": "Customer also asked about warranty coverage for the broken tools.",
        "keyActionsTaken": "Scheduled an appointment with Doctor Petrophe for the caller",
        "nextSteps": "Confirm appointment details via email and follow up on warranty inquiry.",
        "chosenWrapUpCode": "Appointment Scheduled",
        "proposedWrapUpCodes": [
          {
            "name": "Appointment Scheduled"
          },
          {
            "name": "Service Request"
          }
        ]
      }
    },
    "MID_CALL": {
      "acc80d18-b1fb-4261-b44e-a46435eea1da:9d2a7879-8957-4cd6-a39c-46d4f21eaea5:c47d7c08-0776-4e38-a6bb-751d933a0c5d": {
        "reasonForTransferOrConsult": "The caller wants to purchase fifteen tickets for an upcoming match but the current agent needs to check with teammates for ticket availability, requiring a transfer to another agent who can assist with ticket sales.",
        "additionalContext": "The match will take place next weekend at 6 PM, a
  ... (truncado)
```

### Case 2: List by interactionId — respuesta 200
```json
{
  "interactionId": "9d2a7879-8957-4cd6-a39c-46d4f21eaea5",
  "orgId": "acc80d18-b1fb-4261-b44e-a46435eea1da",
  "searchType": "INTERACTION",
  "agentCiUserId": null,
  "summaries": {
    "POST_CALL": {
      "acc80d18-b1fb-4261-b44e-a46435eea1da:9d2a7879-8957-4cd6-a39c-46d4f21eaea5:c47d7c08-0776-4e38-a6bb-751d933a0c5d": {
        "initialContactReason": "The caller wants to buy tickets for a match.",
        "additionalContext": "The match is next weekend and the caller represents a group looking for tickets.",
        "additionalContactReasons": "The caller also inquired about group discount options.",
        "keyActionsTaken": "The agent checked ticket availability with teammates.\\nThe agent engaged with the caller about their request.",
        "nextSteps": "Agent will confirm ticket availability for fifteen tickets and get back to the caller.",
        "chosenWrapUpCode": "Ticket Inquiry",
        "proposedWrapUpCodes": [
          {
            "name": "Ticket Inquiry"
          },
          {
            "name": "Group Booking"
          }
        ]
      }
    },
    "MID_CALL": {
      "acc80d18-b1fb-4261-b44e-a46435eea1da:9d2a7879-8957-4cd6-a39c-46d4f21eaea5:c47d7c08-0776-4e38-a6bb-751d933a0c5d": {
        "reasonForTransferOrConsult": "The caller wants to purchase fifteen tickets for an upcoming match but the current agent needs to check with teammates for ticket availability, requiring a transfer to another agent who can assist with ticket sales.",
        "add
  ... (truncado)
```

### Case 3: List by agentCiUserId — respuesta 200
```json
{
  "interactionId": null,
  "orgId": "acc80d18-b1fb-4261-b44e-a46435eea1da",
  "searchType": "AGENT",
  "agentCiUserId": "77e70d79-64b1-402e-9b84-b113ad71b06d",
  "summaries": {
    "POST_CALL": {
      "acc80d18-b1fb-4261-b44e-a46435eea1da:9d2a7879-8957-4cd6-a39c-46d4f21eaea5:77e70d79-64b1-402e-9b84-b113ad71b06d": {
        "initialContactReason": "Customer wants to buy tickets for an upcoming match.",
        "additionalContext": "Customer has a group of fifteen people and needs the tickets to be together.",
        "additionalContactReasons": "Customer asked about group seating arrangements.",
        "keyActionsTaken": "Checked availability of fifteen tickets for the match.\\nConfirmed grouped discount for the tickets.\\nProcessed the ticket purchase and confirmed ticket sending via email.",
        "nextSteps": "Send the tickets to the customer's email.",
        "chosenWrapUpCode": "Ticket Purchase",
        "proposedWrapUpCodes": [
          {
            "name": "Ticket Purchase"
          },
          {
            "name": "Group Booking"
          }
        ]
      }
    }
  },
  "queueId": null
}
```

## Respuestas de error
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs