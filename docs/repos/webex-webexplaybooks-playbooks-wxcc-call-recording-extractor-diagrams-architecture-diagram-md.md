---
doc_id: webex-webexplaybooks-playbooks-wxcc-call-recording-extractor-diagrams-architecture-diagram-md
source_url: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/wxcc-call-recording-extractor/diagrams/architecture-diagram.md
repo: webex/WebexPlaybooks
ruta: playbooks/wxcc-call-recording-extractor/diagrams/architecture-diagram.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:10:27.180657+00:00
---

# WebexPlaybooks — playbooks/wxcc-call-recording-extractor/diagrams/architecture-diagram.md

Repositorio: webex/WebexPlaybooks

# Webex Contact Center call recording export

This diagram summarizes how the Spring Boot sample authenticates with Webex Contact Center, calls the Capture API for call recording metadata and URLs, and writes audio to a configured storage backend.

```mermaid
sequenceDiagram
  participant Operator as Operator
  participant App as SpringBootApp
  participant WebexCC_OAuth as WebexCC_OAuth
  participant WxCC_Capture_API as WxCC_Capture_API
  participant Storage as Storage

  Operator->>App: Open UI and select date range
  App->>WebexCC_OAuth: Authorization code and token exchange
  WebexCC_OAuth-->>App: Access token
  App->>WxCC_Capture_API: Organization and Capture API requests
  WxCC_Capture_API-->>App: Recording metadata and media URLs
  App->>Storage: Persist WAV files or objects
  App-->>Operator: HTML summary and downloads
```

---
> Fuente: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/wxcc-call-recording-extractor/diagrams/architecture-diagram.md (licencia NOASSERTION)
