---
doc_id: webex-webex-js-sdk-packages-webex-http-core-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/http-core/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/http-core/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:07:08.958120+00:00
---

# webex-js-sdk — packages/@webex/http-core/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# @webex/http-core

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Core HTTP library for the Cisco Webex JS SDK.

- [@webex/http-core](#webexhttp-core)
  - [Install](#install)
  - [Usage](#usage)
    - [Environment Variables](#environment-variables)
    - [`detect()`](#detect)
    - [request()](#request)
    - [`defaults()`](#defaults)
    - [`HttpError`](#httperror)
  - [Maintainers](#maintainers)
  - [Contribute](#contribute)
  - [License](#license)

## Install

```bash
npm install --save @webex/http-core
```

## Usage

### Environment Variables

This plugin utilizes the following environmental variables:

- `ENABLE_VERBOSE_NETWORK_LOGGING` [ *boolean* ]- Utilized to enable interceptor logging

### `detect()`

Detects the filetype of the specified file.

### request()

Same api as [request](https://github.com/request/request) with the following changes:

- Promise-based instead of nodeback based
- Adds an interceptors property to the options object for adding classes that intercept and modify each request
- 4XX and 5XX responses get rejected with the appropriate subclassed Error type
- Sensible defaults for our API (`{json:true}`, etc)

### `defaults()`

Curried version of `request()` that produces an http client with overridden defaults.

### `HttpError`

Child of `Error` (by way of `Exception` from `@webex/common`). Has subclassed errors for each [official HTTP status code](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) (and 429 Too Man Requests).

## Maintainers

This package is maintained by [Cisco Webex for Developers](https://developer.webex.com/).

## Contribute

Pull requests welcome. Please see [CONTRIBUTING.md](https://github.com/webex/webex-js-sdk/blob/master/CONTRIBUTING.md) for more details.

## License

© 2016-2020 Cisco and/or its affiliates. All Rights Reserved.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/http-core/README.md (licencia NOASSERTION)
