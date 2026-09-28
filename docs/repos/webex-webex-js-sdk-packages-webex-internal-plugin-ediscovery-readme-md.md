---
doc_id: webex-webex-js-sdk-packages-webex-internal-plugin-ediscovery-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/internal-plugin-ediscovery/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/internal-plugin-ediscovery/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:07:13.132237+00:00
---

# webex-js-sdk — packages/@webex/internal-plugin-ediscovery/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# @webex/internal-plugin-ediscovery

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Plugin for the ediscovery report client

This is an internal Cisco Webex plugin. As such, it does not strictly adhere to semantic versioning. Use at your own risk. If you're not working on one of our first party clients, please look at our [developer api](https://developer.webex.com/) and stick to our public plugins.

- [@webex/internal-plugin-ediscovery](#webexinternal-plugin-ediscovery)
  - [Install](#Install)
  - [Usage](#Usage)
  - [Tests](#Tests)
  - [Maintainers](#Maintainers)
  - [Contribute](#Contribute)
  - [License](#License)

## Install

```bash
npm install --save @webex/internal-plugin-ediscovery
```

## Usage

```js
import '@webex/internal-plugin-ediscovery';

import WebexCore from '@webex/webex-core';

const webex = new WebexCore();
webex.internal.plugin.ediscovery.WHATEVER;
```

## Tests

Run the ediscovery from the top level using

> yarn run test --packages @webex/internal-plugin-ediscovery

## Run some unit tests, for example: spaceInfo

Run the following command

> yarn run test --packages @webex/internal-plugin-ediscovery --grep "spaceInfo" --unit

## Debug Tests

Run the following command

> yarn run test --packages @webex/internal-plugin-ediscovery --grep "test name" --karmaDebug --browsers=Chrome

## Maintainers

This package is maintained by [Cisco Webex for Developers](https://developer.webex.com/).

## Contribute

Pull requests welcome. Please see [CONTRIBUTING.md](https://github.com/webex/webex-js-sdk/blob/master/CONTRIBUTING.md) for more details.

## License

© 2016-2020 Cisco and/or its affiliates. All Rights Reserved.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/internal-plugin-ediscovery/README.md (licencia NOASSERTION)
