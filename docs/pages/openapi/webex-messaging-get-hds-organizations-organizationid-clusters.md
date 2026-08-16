---
doc_id: webex-messaging-get-hds-organizations-organizationid-clusters
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: GET
path: /hds/organizations/{organizationId}/clusters
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.510862+00:00
---

# GET /hds/organizations/{organizationId}/clusters

**API:** Webex Messaging
**Área:** Hybrid Data Security
**operationId:** `listHDSOrganizationClusters`

## Resumen
List clusters for an Hybrid Data Security organization

## Descripción
Retrieve a list of all clusters for a specific Hybrid Data Security organization, including cluster status, release channel, and upgrade schedule details.
To obtain the Organization ID needed for this API, use the [Organizations API](</docs/api/v1/organizations/list-organizations>)

## Parámetros
- `organizationId` [path] (string) **(requerido)**: Unique ID of the Hybrid Data Security organization.

## Respuestas
- **200**: OK
  - `clusters` (array): List of clusters in the organization.
    - `context` (object): Metadata information about the organization for which the cluster details are being retrieved.
      - `orgId` (string): Unique ID of the organization.
    - `clusterId` (string): Unique ID of the cluster.
    - `clusterName` (string): Name of the cluster.
    - `clusterStatus` (string): Current status of the cluster.
    - `releaseChannel` (string): Release channel of the cluster.
    - `upgradeSchedule` (object): Upgrade schedule details of the cluster.
      - `scheduleDays` (array): Days of the week when upgrades are scheduled.
      - `scheduleTime` (string): Time of the day when upgrades are scheduled.
      - `scheduleTimeZone` (string): Time zone for the scheduled upgrade time.
      - `nextUpgradeTime` (string): Next scheduled upgrade time.
- **400**: The request was invalid or could not be processed. An accompanying error message will provide more details.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
