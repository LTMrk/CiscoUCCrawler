---
doc_id: webex-meeting-get-videomesh-testresults-networktest
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /videoMesh/testResults/networkTest
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.407015+00:00
---

# GET /videoMesh/testResults/networkTest

**API:** Webex Meetings
**Área:** Video Mesh
**operationId:** `List Network Test results`

## Resumen
List Network Test results

## Descripción
Returns the test results of the Network tests triggered for an organization. The tests listed below are run as a part of the Network Test execution on the node.

<b>Bandwidth Test</b> - Tests the bandwidth parameters of the Video Mesh node's network. The test is run between the Video Mesh node and cloud services.<br/>
<b>DNS Resolution Test</b> - Tests the resolution of IP addresses related to cloud services, against the DNS servers configured on the Video Mesh node's network.<br/>
<b>HTTPS Connectivity Test</b> - Tests whether the Video Mesh node is able to connect to cloud services via HTTPS protocol.<br/>
<b>Websocket Connectivity Test</b> - Tests whether the Video Mesh node is able to connect to Webex cloud services via Websocket.<br/>

## Parámetros
- `orgId` [query] (string) **(requerido)**: Unique ID of the organization.
- `triggerType` [query] (string) **(requerido)**: Trigger type.
- `from` [query] (string) **(requerido)**: The start date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. The `from` parameter cannot have date and time values that exceed `to`.
- `to` [query] (string) **(requerido)**: The end date and time of the requested data in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.

## Respuestas
- **200**: OK
  - `orgId` (string): Unique ID of the organization.
  - `from` (string): Start date and time (inclusive) of the Network Test data.
  - `to` (string): End date and time (inclusive) of the Network Test data.
  - `items` (array): Network test results.
    - `clusters` (array): List of Video Mesh clusters.
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
