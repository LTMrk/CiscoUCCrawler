---
doc_id: webex-webex-js-sdk-packages-webex-common-timers-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/common-timers/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/common-timers/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:06:42.139368+00:00
---

# webex-js-sdk — packages/@webex/common-timers/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# @webex/common-timers

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Timer wrappers for the Cisco Webex JS SDK. See https://webex.github.io/webex-js-sdk/

- [@webex/common-timers](#webexcommon-timers)
  - [Install](#install)
  - [Usage](#usage)
  - [Maintainers](#maintainers)
  - [Contribute](#contribute)
  - [License](#license)

## Install

```bash
npm install --save @webex/common-timers
```

## Usage

Works just like `setTimeout` and `setInterval`, but doesn't wedge a node process open.

```js
import {safeSetTimeout, safeSetInterval} from '@webex/common-timers';

const timer = safeSetTimeout(() => {}, 1000);

const interval = safeSetInterval(() => {}, 1000);
```

## Maintainers

This package is maintained by [Cisco Webex for Developers](https://developer.webex.com/).

## Contribute

Pull requests welcome. Please see [CONTRIBUTING.md](https://github.com/webex/webex-js-sdk/blob/master/CONTRIBUTING.md) for more details.

## License

© 2016-2020 Cisco and/or its affiliates. All Rights Reserved.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/common-timers/README.md (licencia NOASSERTION)
