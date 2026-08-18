---
doc_id: webex-messaging-get-hds-nodes-nodeid-alarms
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: GET
path: /hds/nodes/{nodeId}/alarms
operation_id: getHDSNodeAlarms
tags: Hybrid Data Security
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.805711+00:00
---

# GET /hds/nodes/{nodeId}/alarms

**API:** Webex Messaging
**Área:** Hybrid Data Security
**operationId:** `getHDSNodeAlarms`

## Resumen
Get alarms for an Hybrid Data Security node

## Descripción
Returns the alarm details for a single Hybrid Data Security node for the provided time range (last 24 hours).
To obtain the Node ID needed for this API, use the [List nodes for an Hybrid Data Security cluster API](</docs/api/v1/hds/list-hds-cluster-nodes>)

## Parámetros
- `nodeId` [path] (string) (**requerido**): Unique ID of the Hybrid Data Security node.
- `from` [query] (string) (**requerido**): The start date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
- `to` [query] (string) (**requerido**): The end date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.

## Ejemplo de invocación
```bash
curl -X GET '/hds/nodes/<nodeId>/alarms?from=<from>&to=<to>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `context` (object): Metadata information about the node for which alarms are being retrieved.
  - `orgId` (string): Unique ID of the organization.
  - `clusterId` (string): Unique ID of the cluster.
  - `clusterName` (string): Name of the cluster.
  - `nodeId` (string): Unique ID of the node.
  - `host` (string): Host name or IP of the Hybrid Data Security node.
- `alarms` (array): List of alarms raised for the node.
  - `alarmId` (string): Unique identifier of the alarm.
  - `alarmName` (string): Name of the alarm.
  - `alarmSeverity` (string): Severity level of the alarm.
  - `alarmDetails` (string): Additional details about the alarm.
  - `possibleRemediation` (string): Suggested remediation steps for the alarm.
  - `currentStatus` (string): Current status of the alarm.
  - `occurrences` (object): Occurrence details of the alarm.
    - `total` (string): Total number of occurrences of the alarm.
    - `details` (array): List of individual alarm occurrence details.
      - `raisedAt` (string/date-time): Timestamp when the alarm was raised.
      - `clearedAt` (string/date-time): Timestamp when the alarm was cleared.
- `timeRange` (object): The time range for the alarms data.
  - `from` (string/date-time): Start time of the requested data range.
  - `to` (string/date-time): End time of the requested data range.

### Ejemplo — respuesta 200
```json
{
  "context": {
    "orgId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJVGNG",
    "clusterId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzFlYjY1ZmRmLTk2NDMtNDE3Zi05OTc0LWFkNzJjYWUwZTEwZjpiMzdmNTgzYy1kZGRjLTQyOGItODJlNS1jYmU2ODFkYjQ5xxx",
    "clusterName": "San Jose",
    "nodeId": "Y2lzY29zcGFyazovL3VzL0hZQlJJRF9DTFVTVEVSLzM2ZDg5NGY3LTJiNTctNDNjMS1hY2VlLWQ0N2U2Nzc2MTQxNDo0NjdiNGIxZC1jZWI2LTQwN2EtYWZmOC1mMjIxZmFiNzhjyyy",
    "host": "10.196.5.82"
  },
  "alarms": [
    {
      "alarmId": "AUTH_WARN.expiring-60",
      "alarmName": "Hybrid Data Security Machine Accounts Expiring in 60 days",
      "alarmSeverity": "Warning",
      "alarmDetails": "Expiration Details",
      "possibleRemediation": "Refresh Hybrid Data Security Machine Accounts using Hybrid Data Security Setup Tool",
      "currentStatus": "Active",
      "occurrences": {
        "total": "4",
        "details": [
          {
            "raisedAt": "2025-06-14T15:53:00Z",
            "clearedAt": "2025-06-15T15:53:00Z"
          },
          {
            "raisedAt": "2025-06-14T16:53:00Z",
            "clearedAt": "2025-06-15T17:53:00Z"
          }
        ]
      }
    }
  ],
  "timeRange": {
    "from": "2025-06-15T15:53:00Z",
    "to": "2025-06-16T15:53:00Z"
  }
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or could not be processed. An accompanying error message will provide more details.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request was understood, but it has been refused or access is not allowed.
- **404**: Not Found: The requested URI is invalid, or the resource requested (such as a user) does not exist. This response is also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type, or with a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present to indicate how many seconds you should wait before attempting the request again.
- **428**: Precondition Required: The file(s) cannot be scanned for malware and must be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given period of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, please contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond in time. If your query uses the max parameter, please try reducing its value.

## Contexto de la API
The Webex Messaging APIs offer robust programmatic access to messaging features within Webex, including sending and receiving messages, managing spaces, memberships, attachments, and moderating content. These APIs enable integration with bots, workflow automation, notification systems, and custom messaging solutions to enhance team collaboration and productivity. Use cases include building chatbots, integrating with ticketing or alerting platforms, automating onboarding flows, and creating custom collaboration experiences tailored to business needs.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs