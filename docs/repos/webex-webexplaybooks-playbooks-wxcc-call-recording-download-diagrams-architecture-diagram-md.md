---
doc_id: webex-webexplaybooks-playbooks-wxcc-call-recording-download-diagrams-architecture-diagram-md
source_url: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/wxcc-call-recording-download/diagrams/architecture-diagram.md
repo: webex/WebexPlaybooks
ruta: playbooks/wxcc-call-recording-download/diagrams/architecture-diagram.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:10:26.488431+00:00
---

# WebexPlaybooks — playbooks/wxcc-call-recording-download/diagrams/architecture-diagram.md

Repositorio: webex/WebexPlaybooks

# WxCC — Call recording download

```mermaid
sequenceDiagram
    participant Admin as AdminBrowser
    participant WxOAuth as WebexOAuth
    participant App as NodeServer
    participant WxCC as WxCC_API
    participant WxCCWH as WxCC_Webhooks

    Admin->>App: GET /login
    App->>WxOAuth: Redirect authorize
    WxOAuth->>App: GET callback with code
    App->>WxOAuth: POST access_token
    Note over App: Tokens in memory only

    WxCCWH->>App: POST /webhook capture:available
    App->>WxCC: POST captures/query Bearer token
    WxCC->>App: Recording URL metadata
    App->>WxCC: GET recording stream
    App->>App: Write file under recordings/
```

- **Trigger:** WxCC sends a `capture:available` webhook when a recording is ready.
- **Authentication:** An operator completes OAuth in a browser once so the Node process holds an access token for [Captures API](https://developer.webex.com/webex-contact-center/docs/api/v1/captures) query calls.
- **Download:** The app calls `POST /v1/captures/query` on the WxCC API base for your cluster, then streams the file from the returned storage URL to the local `recordings` directory.

---
> Fuente: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/wxcc-call-recording-download/diagrams/architecture-diagram.md (licencia NOASSERTION)
