---
doc_id: webex-admin-get-hybrid-connectors
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: GET
path: /hybrid/connectors
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.151189+00:00
---

# GET /hybrid/connectors

**API:** Webex Admin
**Área:** Hybrid Connectors
**operationId:** `List Hybrid Connectors`

## Resumen
List Hybrid Connectors

## Descripción
List hybrid connectors for an organization. If no `orgId` is specified, the default is the organization of the authenticated user.

Only an admin auth token with the `spark-admin:hybrid_connectors_read` scope can list connectors.

## Parámetros
- `orgId` [query] (string): List hybrid connectors in this organization. If an organization is not specified, the organization of the caller will be used.

## Respuestas
- **200**: OK
  - `items` (array): An array of hybrid connector objects.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
