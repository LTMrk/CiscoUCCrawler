---
doc_id: ciscodevnet-webex-contact-center-widget-starter-iframe-widget-allowedparams-md
source_url: https://github.com/CiscoDevNet/webex-contact-center-widget-starter/blob/master/Iframe_Widget_Allowedparams.md
repo: CiscoDevNet/webex-contact-center-widget-starter
ruta: Iframe_Widget_Allowedparams.md
licencia: MIT
retrieved_at: 2026-10-19T09:48:52.000563+00:00
---

# webex-contact-center-widget-starter — Iframe_Widget_Allowedparams.md

Repositorio: CiscoDevNet/webex-contact-center-widget-starter
Descripcion del repositorio: WebEx Contact Center widget starter

# `Iframe_Widget_Allowedparams.json` is not the host iframe shell

[`Iframe_Widget_Allowedparams.json`](./Iframe_Widget_Allowedparams.json) is a **full Desktop layout** that embeds a page with the built-in `agentx-wc-iframe` component and an `allowedParams` Permissions-Policy string.

That is **model 2** below. It does **not** wrap a partner custom element in the security iframe shell.

| Model | File / folder |
| --- | --- |
| Host iframe shell (partner custom element) | [`Examples/Widgets/iframe-shell/`](./Examples/Widgets/iframe-shell/) and [`Examples/Layouts/Iframe_Shell_Partner_Fixes.json`](./Examples/Layouts/Iframe_Shell_Partner_Fixes.json) |
| Built-in page iframe (`agentx-wc-iframe`) | This layout JSON |
| Partner wraps their own app iframe | [`Examples/Widgets/prebuild-app-widget/`](./Examples/Widgets/prebuild-app-widget/) |

---
> Fuente: https://github.com/CiscoDevNet/webex-contact-center-widget-starter/blob/master/Iframe_Widget_Allowedparams.md (licencia MIT)
