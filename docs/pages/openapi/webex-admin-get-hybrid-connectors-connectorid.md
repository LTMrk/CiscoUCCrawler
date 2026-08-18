---
doc_id: webex-admin-get-hybrid-connectors-connectorid
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: GET
path: /hybrid/connectors/{connectorId}
operation_id: Get Hybrid Connector Details
tags: Hybrid Connectors
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.566384+00:00
---

# GET /hybrid/connectors/{connectorId}

**API:** Webex Admin
**Área:** Hybrid Connectors
**operationId:** `Get Hybrid Connector Details`

## Resumen
Get Hybrid Connector Details

## Descripción
Shows details for a hybrid connector, by ID.

Only an admin auth token with the `spark-admin:hybrid_connectors_read` scope can see connector details.

## Parámetros
- `connectorId` [path] (string) (**requerido**): The ID of the connector.

## Ejemplo de invocación
```bash
curl -X GET '/hybrid/connectors/<connectorId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string): A unique identifier for the connector.
- `orgId` (string): The ID of the organization to which this hybrid connector belongs.
- `hybridClusterId` (string): The ID of the cluster this connector belongs to.
- `hostname` (string): The hostname of the system the connector is running on.
- `status` (string):  Valores: operational, impaired, outage, maintenanceMode.
- `created` (string): The date and time the connector was created.
- `type` (string):  Valores: expresswayManagement, calendar, call, message, expresswayServiceability, ecpServiceability, videoMesh, dataSecurity, care, careManagement.
- `version` (string): The version of the software installed.
- `alarms` (array): A list of alarms raised on the connector.
  - `id` (string): A unique identifier for the alarm.
  - `created` (string): The date and time the alarm was raised.
  - `severity` (string):  Valores: critical, warning, alert, error.
  - `title` (string): The title of the alarm.
  - `description` (string): A description of the alarm.
  - `hybridConnectorId` (string): The ID of the connector the alarm is raised on.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lZY76123",
  "orgId": "Y2lzY29zcGFyazovL3",
  "hybridClusterId": "Y2lZY76123abbb",
  "hostname": "foo.example.org",
  "status": "operational",
  "created": "2017-09-15T15:53:00Z",
  "type": "calendar",
  "version": "1.9_foo_zz",
  "alarms": [
    {
      "id": "Y2lZY76123af234bbYY",
      "created": "2017-09-15T15:53:00Z",
      "severity": "warning",
      "title": "Something is wrong",
      "description": "More detail about something being wrong",
      "hybridConnectorId": "Y2lZY76123af234bb"
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs