---
doc_id: webex-webex-js-sdk-packages-byods-demo-server-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/byods-demo-server/README.md
repo: webex/webex-js-sdk
ruta: packages/byods-demo-server/README.md
licencia: NOASSERTION
retrieved_at: 2026-11-02T12:36:01.291281+00:00
---

# webex-js-sdk — packages/byods-demo-server/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

## BYoDS Demo Server

Run the demo with Node.js 22.14:

```bash
yarn workspace byods-demo-server dev
# Or use the integration environment:
yarn workspace byods-demo-server dev:integration
```

Open `/config` and provide the Service App client ID, client secret, organization ID, and Service App refresh token. After authorization, the demo opens `/data-source` for that organization.

Configuration and tokens stay in memory. Configure again to replace the active instance and cancel its JWS refresh schedules. Use this server for local demos.

If bcrypt causes issues on macOS, run `yarn rebuild`.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/byods-demo-server/README.md (licencia NOASSERTION)
