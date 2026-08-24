---
doc_id: webex-webex-js-sdk-packages-webex-helper-html-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/helper-html/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/helper-html/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:07:07.928462+00:00
---

# webex-js-sdk — packages/@webex/helper-html/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# @webex/helper-html

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> HTML filter for the Cisco Webex JS SDK. See https://webex.github.io/webex-js-sdk/

Note: This package relies on DOM apis and largely returns noops in node environments.

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [Maintainers](#maintainers)
- [License](#license)

## Install

```bash
npm install --save @webex/helper-html
```

## Usage

### `filter(allowedTags, allowedStyles, html)`

Filters an html string such that it only includes the allowed tags and styles. Disallowed tags and styles are removed while their contents are kept.

`allowedTags` is an object keyed on tag name mapped to an array of attribuets allowed for that tag.
`allwedStyles` is an array of allowed style string.
`html` is a string.

Returns a promise that resolves with the new html string.

### `filterSync()`

See `filter()`

### `filterEscape(processCallback, allowedTags, allowedStyles, html)`

Filters an html string such that it only includes the allowed tags and styles. Disallowed tags and styles and their children are escaped.

`processCallback` synchronous callback that receives the body of the html fragment generated from `html`. Presents an opportunity to do preprocessing (e.g turn urls into links) without parsing html `mulitple` times
`allowedTags` is an object keyed on tag name mapped to an array of attribuets allowed for that tag.
`allwedStyles` is an array of allowed style string.
`html` is a string.

Returns a promise that resolves with the new html string.

### `filterEscapeSync()`

See `filterEscape()`

## Maintainers

This package is maintained by [Cisco Webex for Developers](https://developer.webex.com/).

## Contribute

Pull requests welcome. Please see [CONTRIBUTING.md](https://github.com/webex/webex-js-sdk/blob/master/CONTRIBUTING.md) for more details.

## License

© 2016-2020 Cisco and/or its affiliates. All Rights Reserved.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/helper-html/README.md (licencia NOASSERTION)
