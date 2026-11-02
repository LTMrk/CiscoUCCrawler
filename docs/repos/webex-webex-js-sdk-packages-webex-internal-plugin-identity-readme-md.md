---
doc_id: webex-webex-js-sdk-packages-webex-internal-plugin-identity-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/internal-plugin-identity/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/internal-plugin-identity/README.md
licencia: NOASSERTION
retrieved_at: 2026-11-02T12:35:59.829302+00:00
---

# webex-js-sdk — packages/@webex/internal-plugin-identity/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# @webex/internal-plugin-identity

Internal Webex SDK plugin for generating client identity credentials and obtaining signed
certificates from the Webex Certificate Authority. Credentials are cached per contact for the
lifetime of the Webex client instance.

The plugin self-registers when imported and is available as `webex.internal.identity`. Meetings
uses `getCredentials(contactId)` and `getTrustAnchors()` when joining E2EE meetings.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/internal-plugin-identity/README.md (licencia NOASSERTION)
