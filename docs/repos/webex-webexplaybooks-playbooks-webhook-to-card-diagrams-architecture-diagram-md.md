---
doc_id: webex-webexplaybooks-playbooks-webhook-to-card-diagrams-architecture-diagram-md
source_url: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/webhook-to-card/diagrams/architecture-diagram.md
repo: webex/WebexPlaybooks
ruta: playbooks/webhook-to-card/diagrams/architecture-diagram.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:10:18.563328+00:00
---

# WebexPlaybooks — playbooks/webhook-to-card/diagrams/architecture-diagram.md

Repositorio: webex/WebexPlaybooks

# Architecture — Incoming Webhook to Webex Messaging Adaptive Card

External systems can signal events with HTTP POSTs. This sample turns a structured JSON payload into a **Webex message** that includes an **Adaptive Card** attachment.

```mermaid
sequenceDiagram
  participant Ext as ExternalSystem
  participant App as FlaskWebhookApp
  participant Api as WebexMessagesAPI
  participant Space as WebexSpace
  Ext->>App: POST /webhook JSON payload
  App->>App: Validate body build AdaptiveCard
  App->>Api: POST /v1/messages Bearer bot token
  Api->>Space: Message with card attachment
```

Authentication: the **Webex bot token** is stored server-side (environment only). Callers of `/webhook` are **not** authenticated in this sample.

---
> Fuente: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/webhook-to-card/diagrams/architecture-diagram.md (licencia NOASSERTION)
