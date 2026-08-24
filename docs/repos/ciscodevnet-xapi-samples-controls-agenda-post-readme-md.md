---
doc_id: ciscodevnet-xapi-samples-controls-agenda-post-readme-md
source_url: https://github.com/CiscoDevNet/xapi-samples/blob/master/controls/agenda_post/README.md
repo: CiscoDevNet/xapi-samples
ruta: controls/agenda_post/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:11:59.797616+00:00
---

# xapi-samples — controls/agenda_post/README.md

Repositorio: CiscoDevNet/xapi-samples
Descripcion del repositorio: Examples of UI Extensions, Macros and Node.js scripts for Webex devices and Cisco Collaboration Endpoints

# Agenda with notifications (via Bot Account)

This agenda pushes session details to a Webex Teams space, via a Bot Account posting to the space.

![](img/touch10_snapshot.png)


## Quickstart

Deploy the [control](./agenda.xml) to your device

Create a [bot account](https://apphub.webex.com/categories/other/integrations/incoming-webhooks-cisco-systems) from Webex for Developers, and paste the bot token into the code below.

Run the JS script.

```shell
git clone https://github.com/ObjectIsAdvantag/xapi-samples
cd controls
cd agenda_post
npm install
JSXAPI_DEVICE_URL='ssh://192.168.1.34' JSXAPI_USERNAME='integrator' JSXAPI_PASSWORD='integrator' node agenda.js
```

Press 'push' and see messages poping up in Webex Teams.

![](img/push_to_teams.png)

---
> Fuente: https://github.com/CiscoDevNet/xapi-samples/blob/master/controls/agenda_post/README.md (licencia MIT)
