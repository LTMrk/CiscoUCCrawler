---
doc_id: webex-webex-js-sdk-packages-webex-helper-image-readme-md
source_url: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/helper-image/README.md
repo: webex/webex-js-sdk
ruta: packages/@webex/helper-image/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:07:08.623250+00:00
---

# webex-js-sdk — packages/@webex/helper-image/README.md

Repositorio: webex/webex-js-sdk
Descripcion del repositorio: JavaScript SDK for Webex

# @webex/helper-image

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> Helpers for rotating images and creating their thumbnails. Mostly browser-only.

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [Maintainers](#maintainers)
- [License](#license)

## Install

```bash
npm install --save @webex/helper-image
```

## Usage

### `updateImageOrientation(file, options)`

Updates the image file with exif information, required to correctly rotate the image activity. Can specify `options.shouldNotAddExifData` to not add exif information. For example, clients may not need the exif data added if browsers already auto orient the image

### `readExifData(file, buf)`

Adds exif orientation information on the image file

### `orient(options, file)`

Rotates/flips the image on the canvas as per exif information

## Maintainers

This package is maintained by [Cisco Webex for Developers](https://developer.webex.com/).

## Contribute

Pull requests welcome. Please see [CONTRIBUTING.md](https://github.com/webex/webex-js-sdk/blob/master/CONTRIBUTING.md) for more details.

## License

© 2016-2020 Cisco and/or its affiliates. All Rights Reserved.

---
> Fuente: https://github.com/webex/webex-js-sdk/blob/next/packages/%40webex/helper-image/README.md (licencia NOASSERTION)
