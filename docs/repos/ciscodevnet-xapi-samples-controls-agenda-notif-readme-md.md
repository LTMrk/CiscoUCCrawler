---
doc_id: ciscodevnet-xapi-samples-controls-agenda-notif-readme-md
source_url: https://github.com/CiscoDevNet/xapi-samples/blob/master/controls/agenda_notif/README.md
repo: CiscoDevNet/xapi-samples
ruta: controls/agenda_notif/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:11:59.419340+00:00
---

# xapi-samples — controls/agenda_notif/README.md

Repositorio: CiscoDevNet/xapi-samples
Descripcion del repositorio: Examples of UI Extensions, Macros and Node.js scripts for Webex devices and Cisco Collaboration Endpoints

# Agenda with notifications

This agenda pushes session details to a Webex Teams space (via an incoming Webhook)

![](img/touch10_snapshot.png)


## Quickstart

Deploy the [control](./agenda.xml) to your device

Create an [incoming webhook](https://apphub.webex.com/categories/other/integrations/incoming-webhooks-cisco-systems) from Webex App Hub Integrations

Run the JS script.
_Make sure to add an extra `INCOMING_WEBHOOK_ID` env variable filled with the identifier created earlier_

```shell
git clone https://github.com/ObjectIsAdvantag/xapi-samples
cd controls
cd agenda_notif
npm install
INCOMING_WEBHOOK_ID="XXXXX" JSXAPI_DEVICE_URL='ssh://192.168.1.34' JSXAPI_USERNAME='integrator' JSXAPI_PASSWORD='integrator' node agenda.js
```

Press 'push' and see messages poping up in Webex Teams.

![](img/push_to_teams.png)

---
> Fuente: https://github.com/CiscoDevNet/xapi-samples/blob/master/controls/agenda_notif/README.md (licencia MIT)
