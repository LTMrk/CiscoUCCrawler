---
doc_id: webex-webex-js-sdk-packages-byods-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/byods/README.md
repo: webex/webex-js-sdk
ruta: packages/byods/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:07:45.561434+00:00
---

# webex-js-sdk — packages/byods/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

### Bring Your Own Data Source (BYoDS) Node.JS SDK

### Table of Contents

- [Getting Started](#getting-started)
- [Developing](#developing)
- [Building](#building)
- [Testing](#testing)
- [Samples](#samples)
- [Consuming SDK](#consuming-sdk)
  - [NPM](#npm)

---

## Getting Started

The BYoDS Node.js SDK makes it easy for developers to register their data sources to the BYoDS system. It allows developers to build data sources without needing to manage the complexities of integration. With features like customizable storage, service app token management, and auto refresh of JWS tokens. The BYoDS SDK provides a solid foundation for creating secure and reliable data sources.

## Developing

```bash
git clone https://github.com/\<your-fork\>/webex-js-sdk.git
cd web-js-sdk/
yarn install
```

## Building

If your project needs some additional steps for the developer to build the
project after some code changes, state them here:

```bash
yarn workspace @webex/byods run build:src
```

## Testing

```bash
 yarn workspace @webex/byods run test:unit
```

## Samples

```bash
  yarn workspace @webex/byods-demo-server dev:hot
```

## Consuming SDK

To consume the latest stable version of the BYoDS SDK, you can use NPM.

# NPM

```javascript
  npm install @webex/byods
```

(or)

```javascript
  yarn add @webex/byods
```

```javascript
  import BYoDS from '@webex/byods';
```

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/byods/README.md (licencia NOASSERTION)
