---
doc_id: webex-cloud-calling-get-people-personid-features-reception
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /people/{personId}/features/reception
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.640845+00:00
---

# GET /people/{personId}/features/reception

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `Read Receptionist Client Settings for a Person`

## Resumen
Read Receptionist Client Settings for a Person

## Descripción
Retrieve a person's Receptionist Client settings.

To help support the needs of your front-office personnel, you can set up people, workspaces or virtual lines as telephone attendants so that they can screen all incoming calls to certain numbers within your organization.

This API requires a full, user, or read-only administrator or location administrator auth token with a scope of `spark-admin:people_read`.

## Parámetros
- `personId` [path] (string) **(requerido)**: Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Respuestas
- **200**: OK
  - `receptionEnabled` (boolean) **(requerido)**: Set to `true` to enable the Receptionist Client feature.
  - `monitoredMembers` (array): List of people, workspaces or virtual lines to monitor.
    - `id` (string) **(requerido)**: Unique identifier of the person, workspace or virtual line to be monitored.
    - `lastName` (string): Last name of the monitored person, workspace or virtual line.
    - `firstName` (string): First name of the monitored person, workspace or virtual line.
    - `displayName` (string): Display name of the monitored person, workspace or virtual line.
    - `type` (string) **(requerido)**: * `PEOPLE` - Person or list of people.  * `PLACE` - Workspace that is not assigned to a specific person such as for a shared device in a common area.  * `VIRTUAL_LINE` - Virtual line or list of virtual lines. Valores: PEOPLE, PLACE, VIRTUAL_LINE.
    - `email` (string): Email address of the monitored person, workspace or virtual line.
    - `numbers` (array): List of phone numbers of the monitored person, workspace or virtual line.
      - `external` (string): External phone number of the monitored person, workspace or virtual line.
      - `extension` (string): Extension number of the monitored person, workspace or virtual line.
      - `routingPrefix` (string): Routing prefix of location.
      - `esn` (string): Routing prefix + extension of a person or workspace.
      - `primary` (boolean): Indicates whether phone number is a primary number.
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
