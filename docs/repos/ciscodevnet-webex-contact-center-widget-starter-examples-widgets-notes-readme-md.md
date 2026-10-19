---
doc_id: ciscodevnet-webex-contact-center-widget-starter-examples-widgets-notes-readme-md
source_url: https://github.com/CiscoDevNet/webex-contact-center-widget-starter/blob/master/Examples/Widgets/Notes/README.md
repo: CiscoDevNet/webex-contact-center-widget-starter
ruta: Examples/Widgets/Notes/README.md
licencia: MIT
retrieved_at: 2026-10-19T09:48:50.924585+00:00
---

# webex-contact-center-widget-starter — Examples/Widgets/Notes/README.md

Repositorio: CiscoDevNet/webex-contact-center-widget-starter
Descripcion del repositorio: WebEx Contact Center widget starter

# WCC Notes Starter: Lit Element

## Development

Setting up your development environment:

1. Clone this repo
2. Run `yarn` from the root of the repo.
3. Run `yarn start` to start the playground app.

This widget is configured for demonstration purposes. For production usage, make edits according to the shape of your customer data for accurate results.

## Iframe shell / header placement

`notes-widget` is safe in a tall `navigation` / `panel` slot. `notes-header-widget` is a header trigger: inside the iframe shell it opens `notes-widget` with `Desktop.popover.open()` so the notes panel is not clipped to 64px. In-page and Storybook still use `md-menu-overlay`. After changing this source, run `yarn build` from `Examples/` to refresh `widgets/notes-widget.js`.

See [`../iframe-shell/`](../iframe-shell/) for the partner decision tree. 

![Notes Example Screenshot](./static/notes.png)

---
> Fuente: https://github.com/CiscoDevNet/webex-contact-center-widget-starter/blob/master/Examples/Widgets/Notes/README.md (licencia MIT)
