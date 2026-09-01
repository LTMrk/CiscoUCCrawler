---
doc_id: webex-contact-center-post-admin-v1-api-journey-actions-workspace-id-workspaceid-template-id-templateid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /admin/v1/api/journey-actions/workspace-id/{workspaceId}/template-id/{templateId}
operation_id: createJourneyActionConfiguration
tags: Journey - Trigger Actions API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.770813+00:00
---

# POST /admin/v1/api/journey-actions/workspace-id/{workspaceId}/template-id/{templateId}

**API:** Webex Contact Center
**Área:** Journey - Trigger Actions API
**operationId:** `createJourneyActionConfiguration`
**Autenticación:** bearerAuth

## Resumen
Create a new  Journey Action

## Descripción
Create a new Journey Action in JDS. 

 **Role and Scope**: It requires id full admin or any role with cjp:config_write scope.

 **Sample Input for Creating new Journey action**: 
  ```
  {
    "name": "Closed Queue Action",
    "cooldownPeriodInMinutes": 1,
    "rules": {
      "logic": "SINGLE",
      "condition": "Closed Queue,category,string,Value GTE 2"
    },
    "actionTriggers": [
      {
        "type": "Webhook",
        "webhookURL": "https://hooks.us.webexconnect.io/events/6M347NJ6",
        "attributes": {
          "httpverb": "post",
          "requestbody": "{\"SMS\":\"12263762551\",\"callID\":\"\",\"MessageToSend\":\"Hello there!\"}"
        }
      }
    ],
    "isActive": true
  }
 ```
The action trigger's evaluation process is predicated on the progressive profile that has been established. 
In this specific action trigger, the rule assessment verifies whether the progressive profile value from the prior template evaluation was in excess of 2. 
If this condition is met, the webhook is subsequently activated.


Prior to rule evaluation for actions, several conditions must be satisfied. 
Firstly, the event associated with the template must align with the rule event, which, in this case, is 'Closed Queue'. 
Secondly, the metadata assigned to the template must correspond with the metadata set by the rules, which in this context, is 'category'. 
Thirdly, the aggregation mode of the template must be equivalent to the rules' aggregation mode, which is 'value' in this instance. 
Finally, the operator of the template's aggregation mode must match those defined for 'value'. 
In this scenario, it is 'GTE' (greater than or equal), which is an accepted value for 'value'.

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID
- `templateId` [path] (string) (**requerido**): Template ID

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Name
- `cooldownPeriodInMinutes` (integer/int32): Cooldown Period In Minutes
- `rules` (object) (**requerido**): Configuration details of the Rules
  - `logic` (string): logic
  - `args` (array): Arguments
- `actionTriggers` (array):
  - `type` (string) (**requerido**): Type
- `isActive` (boolean): Is Journey Action Configuration Active

## Ejemplo de invocación
```bash
curl -X POST '/admin/v1/api/journey-actions/workspace-id/<workspaceId>/template-id/<templateId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "rules": {}}'
```

## Respuestas correctas
**201**: Accepted
- `meta` (object): Meta information of the response
  - `organizationId` (string): Organization ID
- `data` (object): Journey Action Configuration Response Model
  - `createdAt` (string): Created Timestamp
  - `createdBy` (string): Created By
  - `updatedAt` (string): Updated Timestamp
  - `updatedBy` (string): Updated By
  - `id` (string): Journey Action Id
  - `name` (string): Journey Action Name
  - `organizationId` (string): Organization Id
  - `workspaceId` (string): Workspace Id
  - `isActive` (boolean): Is Journey Action Configuration Active
  - `templateId` (string): Profile View Template ID
  - `cooldownPeriodInMinutes` (integer/int32): Cooldown Period In Minutes
  - `rules` (object): Configuration details of the Rules based on which the Action will be triggered
    - `type` (string): type
    - `childrenRules` (object): childrenRules
      - `type` (string): type
  - `actionTriggers` (array):
    - `type` (string) (**requerido**): Type

## Respuestas de error
- **400**: Bad Request
- **500**: Internal server error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs