---
doc_id: ciscodevnet-xapi-samples-jsxapi-readme-md
source_url: https://github.com/CiscoDevNet/xapi-samples/blob/master/jsxapi/README.md
repo: CiscoDevNet/xapi-samples
ruta: jsxapi/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:12:04.550256+00:00
---

# xapi-samples — jsxapi/README.md

Repositorio: CiscoDevNet/xapi-samples
Descripcion del repositorio: Examples of UI Extensions, Macros and Node.js scripts for Webex devices and Cisco Collaboration Endpoints

# Example scripts using the Node.js jsxapi for Cisco Collaboration Devices

The [Node.js jsxapi](https://github.com/cisco-ce/jsxapi) lets you create applications that interact with Cisco Collaboration Devices (DX, SX, MX, RoomKit, any CE-powered in fact).

You'll find here scripts to learn the jsxapi through baby steps.

**New to Room Devices, Controls & Macros? check the [QuickStart Guide](../docs/QuickStart.md) to learn to connect to your Device's Web Interface, and load Controls & Macros to your device**

## Quickstart

Open a terminal and run the commands below:

```shell
git clone https://github.com/ObjectIsAdvantag/xapi-samples
cd xapi-samples
cd jsxapi
npm install

# Place your device ip-address and credentials
JSXAPI_DEVICE_URL='ssh://192.168.1.34' JSXAPI_USERNAME='integrator' JSXAPI_PASSWORD='integrator' node 8-rolling-messages
```

---
> Fuente: https://github.com/CiscoDevNet/xapi-samples/blob/master/jsxapi/README.md (licencia MIT)
