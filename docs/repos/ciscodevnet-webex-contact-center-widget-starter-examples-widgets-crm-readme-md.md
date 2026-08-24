---
doc_id: ciscodevnet-webex-contact-center-widget-starter-examples-widgets-crm-readme-md
source_url: https://github.com/CiscoDevNet/webex-contact-center-widget-starter/blob/master/Examples/Widgets/CRM/README.md
repo: CiscoDevNet/webex-contact-center-widget-starter
ruta: Examples/Widgets/CRM/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:11:45.126615+00:00
---

# webex-contact-center-widget-starter — Examples/Widgets/CRM/README.md

Repositorio: CiscoDevNet/webex-contact-center-widget-starter
Descripcion del repositorio: WebEx Contact Center widget starter

# WCC Widget Starter: Lit Element

## Development

Setting up your development environment:

1. Clone this repo
2. Run `yarn` from the root of the repo.
3. Run `yarn start` to start the playground app.

This widget is configured for demonstration purposes. For production usage, make edits according to the shape of your customer data for accurate results. 

The `./customer-data/mock-customer` file represents a demo customer info object that is imported directly into the widget.

As it currently exists, no additional API keys are needed to demonstrate this widget.

the `<customer-summary>` component's table is composable, simple add the table or table generating code needed between the tags and it will render within. Please note that the class names for "label" and "value" help the styles render correctly, like so: `<td class="title">`.

![Widget Example Screenshot](./static/crm.png)

---
> Fuente: https://github.com/CiscoDevNet/webex-contact-center-widget-starter/blob/master/Examples/Widgets/CRM/README.md (licencia MIT)
