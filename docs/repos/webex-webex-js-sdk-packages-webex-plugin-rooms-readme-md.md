---
doc_id: webex-webex-js-sdk-packages-webex-plugin-rooms-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/plugin-rooms/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/plugin-rooms/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:07:33.386415+00:00
---

# webex-js-sdk — packages/@webex/plugin-rooms/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# @webex/plugin-rooms

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Rooms plugin for the Cisco Webex JS SDK.

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [Maintainers](#maintainers)
- [License](#license)

## Install

```bash
npm install --save @webex/plugin-rooms
```

## Usage

This is a plugin for the Cisco Webex JS SDK. While most of the functionality of this plugin can be utilized using specific scopes, such as `spark:rooms_read` and `spark:rooms_write`, utilizing the `listen()` method of this plugin will require both `spark:all` and `spark:kms`. Please note that by toggling an application's `spark:all` scope via the portal will also toggle its `spark:kms` scope. Please see our [developer portal](https://developer.webex.com/) and the [API docs](https://webex.github.io/webex-js-sdk/api/) for full details.

## Install

```bash
npm install --save @webex/plugin-rooms
```

## Usage

```js
const Webex = require('webex');

const webex = Webex.init();
webex.rooms.get(id).then((room) => {
  console.log(room);
});
```

## Maintainers

This package is maintained by [Cisco Webex for Developers](https://developer.webex.com/).

## Contribute

Pull requests welcome. Please see [CONTRIBUTING.md](https://github.com/webex/webex-js-sdk/blob/master/CONTRIBUTING.md) for more details.

## License

© 2016-2020 Cisco and/or its affiliates. All Rights Reserved.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/plugin-rooms/README.md (licencia NOASSERTION)
