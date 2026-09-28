---
doc_id: ciscodevnet-xapi-samples-controls-onair-readme-md
source_url: https://github.com/CiscoDevNet/xapi-samples/blob/master/controls/onair/README.md
repo: CiscoDevNet/xapi-samples
ruta: controls/onair/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:12:02.424301+00:00
---

# xapi-samples — controls/onair/README.md

Repositorio: CiscoDevNet/xapi-samples
Descripcion del repositorio: Examples of UI Extensions, Macros and Node.js scripts for Webex devices and Cisco Collaboration Endpoints

# OnAir - CanIBugDad?

an In-Room Control that toogles a Hue bulb color, depending on the room's state: free, occupied, busy, on air (call in progress)

![](img/onair_busy.png)



## Quickstart 

Deploy the [control](./onair.xml) to your device

Open the file `script.js` if you're planning to run/test/debug, or the `macro.js` if ready to deploy as a Macro.

> Note: the `multi.js` file targets both the Macro runtime AND standalone Node.js execution.

Update wih your Philipps Hue deployment settings.

Example to run as the script from a shell terminal:

```shell
git clone https://github.com/ObjectIsAdvantag/xapi-samples
cd controls
cd onair
npm install
JSXAPI_DEVICE_URL='ssh://192.168.1.32' JSXAPI_USERNAME='localadmin' JSXAPI_PASSWORD='ciscopsdt' node script.js
```

---
> Fuente: https://github.com/CiscoDevNet/xapi-samples/blob/master/controls/onair/README.md (licencia MIT)
