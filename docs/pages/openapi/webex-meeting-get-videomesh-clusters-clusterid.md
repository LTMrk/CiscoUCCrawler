---
doc_id: webex-meeting-get-videomesh-clusters-clusterid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /videoMesh/clusters/{clusterId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.406434+00:00
---

# GET /videoMesh/clusters/{clusterId}

**API:** Webex Meetings
**Área:** Video Mesh
**operationId:** `Get Cluster Details`

## Resumen
Get Cluster Details

## Descripción
Returns the cluster details for a single Video Mesh cluster.

## Parámetros
- `clusterId` [path] (string) **(requerido)**: The unique Video Mesh Cluster ID.

## Respuestas
- **200**: OK
  - `items` (array):
    - `orgId` (string): The unique ID for the organization.
    - `items` (array): Details of the cluster.
      - `clusterId` (string): ID of the Video Mesh cluster.
      - `clusterName` (string): Name of the Video Mesh cluster.
      - `nodes` (array): The Video Mesh nodes in the cluster.
      - `releaseChannel` (string): Release Channel of the Video Mesh cluster.
      - `upgradeSchedule` (object):
        - `scheduleDays` (array): Days of the week when scheduled upgrades will occur for the Video Mesh cluster.
        - `scheduleTime` (string): Time when scheduled upgrade will occur for the Video Mesh cluster.
        - `scheduleTimeZone` (string): Timezone of the scheduled upgrade of Video Mesh cluster.
        - `upgradePending` (boolean): Upgrade Pending information.
        - `nextUpgradeTime` (string): Time when the next upgrade is scheduled for the Video Mesh cluster.
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
