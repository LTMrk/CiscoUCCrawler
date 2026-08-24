---
doc_id: ciscodevnet-xapi-samples-jsxapi-httpfeedback-readme-md
source_url: https://github.com/CiscoDevNet/xapi-samples/blob/master/jsxapi/httpfeedback/README.md
repo: CiscoDevNet/xapi-samples
ruta: jsxapi/httpfeedback/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:12:05.430086+00:00
---

# xapi-samples — jsxapi/httpfeedback/README.md

Repositorio: CiscoDevNet/xapi-samples
Descripcion del repositorio: Examples of UI Extensions, Macros and Node.js scripts for Webex devices and Cisco Collaboration Endpoints

# Service to follow people count metrics in real time

Start an HTTP Server that registers as a Webhook to your Room Device (via xAPI 's HttpFeedback)

Open a terminal and run the commands as described below: 

```shell
git clone <repo>
cd <repo>
cd jsxapi
cd httpfeedback
npm install

JSXAPI_DEVICE_URL='ssh://192.168.1.34' JSXAPI_USERNAME='admin' JSXAPI_PASSWORD='' WEBHOOK_URL="http://192.168.1.34:8080" node server.js
```

Check the service is running by hitting its healthcheck at http://localhost:8080 and http://192.168.1.34:8080 in the example above.

---
> Fuente: https://github.com/CiscoDevNet/xapi-samples/blob/master/jsxapi/httpfeedback/README.md (licencia MIT)
