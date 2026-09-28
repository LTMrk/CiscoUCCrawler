---
doc_id: webex-webex-js-sdk-packages-webex-contact-center-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/contact-center/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/contact-center/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:06:43.731115+00:00
---

# webex-js-sdk — packages/@webex/contact-center/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

### Table of Contents

- [Getting Started](#getting-started)
- [Developing](#developing)
- [Building](#building)
- [Testing](#testing)
- [Samples](#samples)
- [Consuming SDK](#consuming-sdk)
  - [NPM](#npm)
  - [CDN](#cdn)
- [Kitchen Sink App](#kitchen-sink-app)

---

## Getting Started

The `ContactCenter` package is designed to provide a set of APIs to perform various operations for the Agent flow within Webex Contact Center.

- [Introduction to the Webex Web Calling SDK]()
- [Quickstart guide]().

## Developing

```bash
git clone https://github.com/\<your-fork\>/webex-js-sdk.git
cd webex-js-sdk/
yarn install
```

## Building

If your project needs some additional steps for the developer to build the
project after some code changes, state them here:

```bash
yarn workspaces foreach --parallel --verbose run build:src

yarn build:local
```

## Testing

```bash
 yarn workspace @webex/contact-center run test:unit
```

## Samples

```bash
  yarn run samples:serve
```

## Consuming SDK

To consume the latest stable version of the Calling SDK one can use NPM or CDN.

# NPM

```javascript
  npm install @webex/contact-center
```

(or)

```javascript
  yarn add @webex/contact-center
```

```javascript
import ContactCenter from '@webex/contact-center';
```

# CDN

```javascript
<script src="../contact-center.min.js"></script>
```

### Kitchen Sink App

To test Contact Center SDK API, use this Kitchen Sink app: https://webex.github.io/webex-js-sdk/samples/contact-center/

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/contact-center/README.md (licencia NOASSERTION)
