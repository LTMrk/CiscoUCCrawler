---
doc_id: webex-webex-js-sdk-packages-webex-plugin-meetings-assets-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/plugin-meetings/assets/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/plugin-meetings/assets/README.md
licencia: NOASSERTION
retrieved_at: 2026-11-02T12:36:00.956721+00:00
---

# webex-js-sdk — packages/@webex/plugin-meetings/assets/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

<!--
  Copyright (c) 2015-2026 Cisco Systems, Inc. See LICENSE file.
-->

# plugin-meetings static assets

This folder contains files that plugin-meetings loads at runtime:

- `e2ee-x.x.x.js` and `e2ee-x.x.x.wasm` — the Emscripten loader and binary for MLS join to E2EE meetings. Filenames need to be unique for each version of the WASM module.

`yarn build` copies these files to `packages/@webex/plugin-meetings/dist/assets`. For UMD/CDN
distribution, `yarn build:script` copies them to
`packages/webex/umd/assets/plugin-meetings/`. Each plugin keeps its own source `assets/` folder;
the UMD build preserves that separation under `umd/assets/<plugin-name>/` to avoid filename
collisions (for example, internal-plugin-encryption ships `ios_union-<version>.p7b` under
`umd/assets/internal-plugin-encryption/`). The SDK does not serve them. Development builds and local builds without an injected SDK
version default to `/assets/plugin-meetings/`, which webpack-dev-server serves from this folder.
SDK release builds default to the matching UMD CDN directory
(`https://unpkg.com/webex@<sdk-version>/umd/assets/plugin-meetings/`). Standalone plugin npm releases
default to the plugin package's assets
(`https://unpkg.com/@webex/plugin-meetings@<plugin-version>/dist/assets/`). Applications
can override the URL to serve assets from their own origin or CDN.

Use a versioned URL so the JavaScript SDK and its static assets remain compatible. For a CDN URL,
allow the consuming application origin with CORS and serve `e2ee.js` with a
JavaScript MIME type.

`*.map` files are ignored and not copied.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/plugin-meetings/assets/README.md (licencia NOASSERTION)
