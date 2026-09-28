---
doc_id: webex-webex-js-sdk-packages-webex-internal-plugin-conversation-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/internal-plugin-conversation/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/internal-plugin-conversation/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:07:11.806830+00:00
---

# webex-js-sdk — packages/@webex/internal-plugin-conversation/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# @webex/internal-plugin-conversation

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Plugin for the Conversation service

This is an internal Cisco Webex plugin. As such, it does not strictly adhere to semantic versioning. Use at your own risk. If you're not working on one of our first party clients, please look at our [developer api](https://developer.webex.com/) and stick to our public plugins.

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [Maintainers](#maintainers)
- [License](#license)

## Install

```bash
npm install --save @webex/internal-plugin-conversation
```

## Usage

```js
import '@webex/internal-plugin-conversation';

import WebexCore from '@webex/webex-core';

const webex = new WebexCore();
webex.internal.conversation.WHATEVER;
```

This is the list of environment variable used by this plugin:

- `WEBEX_CONVERSATION_DEFAULT_CLUSTER` - The name of the conversation cluster that contains all of the organizations and spaces prior to federation phase 2. This defaults to `urn:TEAM:us-east-2_a:identityLookup` for production but can be changed to `urn:TEAM:us-east-1_int13:identityLookup` for integration.
- `WEBEX_CONVERSATION_CLUSTER_SERVICE` - The name of the conversation cluster service used to lookup the host in the hostmap. Defaults to `identityLookup`, but if the service changes, will need to be updated.

## Maintainers

This package is maintained by [Cisco Webex for Developers](https://developer.webex.com/).

## Contribute

Pull requests welcome. Please see [CONTRIBUTING.md](https://github.com/webex/webex-js-sdk/blob/master/CONTRIBUTING.md) for more details.

## License

© 2016-2020 Cisco and/or its affiliates. All Rights Reserved.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/internal-plugin-conversation/README.md (licencia NOASSERTION)
