---
doc_id: webex-webex-js-sdk-packages-webex-jsdoctrinetest-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/jsdoctrinetest/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/jsdoctrinetest/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:07:22.281185+00:00
---

# webex-js-sdk — packages/@webex/jsdoctrinetest/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# @webex/jsdoctrinetest

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Mocha plugin which parses source code for doc blocks containing assertions and runs them as mocha specs.

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [Maintainers](#maintainers)
- [License](#license)

## Install

```bash
npm install --save @webex/jsdoctrinetest
```

## Usage

Assuming your source code is in `./src` and you've got code like

```js
/**
 * @example
 * fn();
 * //=> true
 * @returns {boolean}
 */
exports.fn = function fn() {
  return true;
};
```

The following command will create a run a mocha spec asserting the result of `fn()` is `true`.

```bash
mocha -r @webex/jsdoctrinetest ./src
```

## Maintainers

This package is maintained by [Cisco Webex for Developers](https://developer.webex.com/).

## Contribute

Pull requests welcome. Please see [CONTRIBUTING.md](https://github.com/webex/webex-js-sdk/blob/master/CONTRIBUTING.md) for more details.

## License

© 2016-2020 Cisco and/or its affiliates. All Rights Reserved.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/jsdoctrinetest/README.md (licencia NOASSERTION)
