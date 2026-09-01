---
doc_id: webex-contact-center-post-admin-v1-api-profile-view-template-workspace-id-workspaceid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /admin/v1/api/profile-view-template/workspace-id/{workspaceId}
operation_id: createTemplate
tags: Journey - Profile Creation & Insights API
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.768533+00:00
---

# POST /admin/v1/api/profile-view-template/workspace-id/{workspaceId}

**API:** Webex Contact Center
**Área:** Journey - Profile Creation & Insights API
**operationId:** `createTemplate`
**Autenticación:** bearerAuth

## Resumen
Create Template

## Descripción
Creates a Profile View Template in JDS. 

 **Role and Scope**: Requires id full admin or any role with cjp:config_write scope.

 **Template with single rule**: 
  ```
  {
    "name": "ClosedCaller",
    "attributes": [
      {
        "version": "0.1",
        "event": "Closed Queue",
        "metaDataType": "string",
        "metaData": "category",
        "limit": 100,
        "displayName": "ClosedCaller",
        "lookBackDurationType": "minutes",
        "lookBackPeriod": 5,
        "aggregationMode": "Count",
        "rules": {
          "logic": "SINGLE",
          "condition": "Closed Queue,category,string,Value EQ Closed"
        },
        "widgetAttributes": {
          "type": "table"
        },
        "verbose": false
      }
    ]
  }
 ```


 **Example Event:** 
  ```
  {
    "id": "{{$guid}}",
    "specversion": "1.0",
    "type": "Closed Queue",
    "source": "Voice%20Contact",
    "identity": "jes@gmail.com",
    "identitytype": "email",
    "datacontenttype": "application/json",
    "data": {
      "Email": "jes@gmail.com",
      "CallsQueuedNow": "Use GetQueueInfoNode Values",
      "OldestCallTime": "Use GetQueueInfoNode Values",
      "LoggedOnAgents": "Use GetQueueInfoNode Values",
      "PIQ": "Use GetQueueInfoNode Values",
      "EWT": "Use GetQueueInfoNode Values",
      "category": "Closed",
      "origin": "Past Due - 1st Notification",
      "channelType": "QueueCall",
      "channelBreakout": "voice"
    }
  }
  ```


 **Key components of the rule:** 
   * template.event: This refers to the specific event type you want to match (e.g., "Closed Queue").
   * event.type: This refers to the actual event type present in the event data.
   * event.data: This is the dictionary/object containing all the metadata associated with the event.
   * template.rules.condition - category: This is the specific metadata field you want to compare within event.data.
   * template.rules.condition - string: This indicates that the category metadata is a string type.
   * template.rules.condition - Value EQ Closed: This defines the condition: the value of the category field (as a string) must be equal to "Closed".


 **Evaluation process:** 
  1. The rule checks if template.event matches the event.type in the incoming event.
  2. If they match, the rule retrieves the value of the category field from event.data.
  3. It then compares the value of category (treated as a string) to "Closed" using an equality operator (EQ).
  4. If the values are equal, the condition evaluates to True and creates a progressive profile for the identity. Otherwise, it evaluates to False.
  
  The template has lookBackPeriod and lookBackDurationType which decide how long to look back for the calculation. In the above template, it fetches events triggered in the last 5 minutes and performs the aggregation mode on the data received from rules.
  
  * When the aggregation mode is Value, the profile result will have the value of the rule as the output.
  * When the aggregation mode is Count, the profile will have the count of events with category closed in the past 5 minutes.
  * When the aggregation mode is Distinct, the profile will have the value closed.
  * When aggregation mode is Sum, the data type should be Integer or double and it will be the sum of all matching values in the last 5 minutes.
  * When aggregation mode is Max, the data type should be Integer or double and it will be the max of all matching values in the last 5 minutes.
  * When aggregation mode is Min, the data type should be Integer or double and it will be the min of all matching values in the last 5 minutes.
  * When aggregation mode is Average, the data type should be Integer or double and it will be the average of all matching values in the last 5 minutes.


 **Example template with multiple rules :** 
  ```
1. {
2.   "name": "sample-template-multi-condition",
3.   "attributes": [
4.     {
5.       "version": "0.1",
6.       "event": "Quote",
7.       "metaDataType": "string",
8.       "metaData": "email",
9.       "limit": 1,
10.      "displayName": "Email",
11.      "lookBackDurationType": "days",
12.      "lookBackPeriod": 50,
13.      "aggregationMode": "Value",
14.      "rules": {
15.        "args": [
16.          "Quote,isEV,string,Value EQ Yes",
17.          "Quote,isEV,string,Value EQ No",
18.          {
19.            "args": [
20.              "Quote,make,string,Value EQ Honda",
21.              "Quote,model,string,Value EQ CR-V"
22.            ],
23.            "logic": "AND"
24.          }
25.        ],
26.        "logic": "OR"
27.      },
28.      "widgetAttributes": {
29.        "type": "table"
30.      },
31.      "verbose": false
32.    }
33.  ]
34. }
  ```
1. In the above template we have multiple rules.
2. The arguments in line 20 and 21 are evaluated with logical AND condition.
3. Then arguments in line 16 and 17 along with the result for 20 AND 21 are evaluated with logical OR (line 26).

## Parámetros
- `workspaceId` [path] (string) (**requerido**): Workspace ID

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Template Name
- `attributes` (array) (**requerido**):
  - `displayName` (string) (**requerido**): displayName
  - `version` (string) (**requerido**): version
  - `event` (string) (**requerido**): event
  - `metaDataType` (string) (**requerido**): metaDataType
  - `metaData` (string) (**requerido**): metaData
  - `limit` (integer/int32) (**requerido**): limit
  - `lookBackDurationType` (string) (**requerido**): lookBackDurationType
  - `lookBackPeriod` (integer/int32) (**requerido**): lookBackPeriod
  - `aggregationMode` (string) (**requerido**): aggregationMode
  - `verbose` (boolean) (**requerido**): verbose
  - `widgetAttributes` (object): Create or Update WidgetAttributes
    - `type` (string): type
  - `rules` (object): Configuration details of the Rules
    - `logic` (string): logic
    - `args` (array): Arguments

## Ejemplo de invocación
```bash
curl -X POST '/admin/v1/api/profile-view-template/workspace-id/<workspaceId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"attributes": [], "name": "<name>"}'
```

## Respuestas correctas
**201**: Created
- `meta` (object): Meta information of the response
  - `organizationId` (string): Organization ID
- `data` (object): Template Response Model
  - `createdAt` (string): Created Timestamp
  - `createdBy` (string): Created By
  - `updatedAt` (string): Updated Timestamp
  - `updatedBy` (string): Updated By
  - `id` (string): Profile View Template Id
  - `name` (string): Template Name
  - `workspaceId` (string): Workspace Id
  - `organizationId` (string): Organization Id
  - `attributes` (array):
    - `displayName` (string): displayName
    - `version` (string): version
    - `event` (string): event
    - `metaDataType` (string): metaDataType
    - `metaData` (string): metaData
    - `limit` (integer/int32): limit
    - `lookBackDurationType` (string): lookBackDurationType
    - `lookBackPeriod` (integer/int32): lookBackPeriod
    - `aggregationMode` (string): aggregationMode
    - `verbose` (boolean): verbose
    - `widgetAttributes` (object): WidgetAttributes
      - `type` (string): type
    - `rules` (object): Configuration details of the Rules based on which the Action will be triggered
      - `type` (string): type
      - `childrenRules` (object): childrenRules
        - `type` (string): type

## Respuestas de error
- **400**: Bad Request
- **404**: Resource not found
- **500**: Internal server error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs