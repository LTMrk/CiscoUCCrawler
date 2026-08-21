---
doc_id: webex-contact-center-post-v1-monitor
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/monitor
operation_id: createMonitoringRequest
tags: Call Monitoring
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.798516+00:00
---

# POST /v1/monitor

**API:** Webex Contact Center
**Área:** Call Monitoring
**operationId:** `createMonitoringRequest`

## Resumen
Create Monitoring Request

## Descripción
Create a successful monitoring request. It can be done either on an on-going or next successful inbound/outbound call. Requires scope 'cloud-contact-center:pod_conv' and 'cjp.supervisor'.

## Cuerpo de la petición (application/json)
- `id` (string) (**requerido**): The id represents the unique request id with which the Monitoring Request will be created, maximum length 36 characters.
- `monitorType` (string) (**requerido**): It represents the type of the monitoring request. It can to be ```midcall```, ```adhoc``` and ```continuous```
- `taskId` (string/UUID): The unique ID representing the task that needs to be monitored. Mandatory for ```midcall``` type.
- `queueIds` (array): If the call is routed to an agent and the agent is assigned to a queue, the queueId can be entered here to initiate a successful call monitoring request for that particular queue, maximum length of each queue is 36 characters and maximum number of queueIds 250.
- `teams` (array): If the call is routed to an agent and the agent is assigned to a team, the teamId can be entered here to initiate a successful monitoring request for that particular team, maximum length of each team is 36 characters and maximum number of teams 100.
- `sites` (array): If the call is routed to an agent and the agent is assigned to a site, the siteId can be entered here to initiate a successful monitoring request for that particular site, maximum length of each site is 36 characters and the maximum number of sites 20.
- `agents` (array): Enter the agentId to monitor a particular agent to whom the call is being assigned, maximum length of each agent is 36 characters and the maximum number of agents is 500.
- `trackingId` (string/UUID): An unique id to keep a track of events occurring during the call
- `invisibleMode` (boolean): This allows the supervisor to obfuscate their details from Team Performance Widget panel. Set ```true``` inorder to activate this mode

## Ejemplo de invocación
```bash
curl -X POST '/v1/monitor' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"id": "<id>", "monitorType": "<monitorType>"}'
```

## Respuestas correctas
**202**: The create request was accepted for processing

## Respuestas de error
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **412**: Precondition Failed
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs