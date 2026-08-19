---
doc_id: webex-cloud-calling-get-admin-convergedrecordings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /admin/convergedRecordings
operation_id: list_recordings_for_admin_or_compliance_officer
tags: Converged Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.988056+00:00
---

# GET /admin/convergedRecordings

**API:** Webex Cloud Calling
**Área:** Converged Recordings
**operationId:** `list_recordings_for_admin_or_compliance_officer`

## Resumen
List Recordings for Admin or Compliance officer

## Descripción
List recordings for an admin or compliance officer. You can specify a date range, and the maximum number of recordings to return.

The list returned is sorted in descending order by the date and time that the recordings were created.

Long result sets are split into [pages](/docs/basics#pagination).

List recordings requires the `spark-compliance:recordings_read` scope for compliance officer and `spark-admin:recordings_read` scope for admin.

#### Request Header

* `timezone`: *[Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.*

## Parámetros
- `max` [query] (number): Maximum number of recordings to return in a single page. `max` must be equal to or greater than `1` and equal to or less than `100`. Por defecto: 10.
- `from` [query] (string): Starting date and time (inclusive) for recordings to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`. The interval between `from` and `to` must be within 30 days. Por defecto: If only `to` is specified, the default `from` value is 7 days before `to`; if no `to` or `from` is specified, the default `from` value is 7 days before the current date and time..
- `to` [query] (string): Ending date and time (exclusive) for List recordings to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`. The interval between `from` and `to` must be within 30 days. Por defecto: If `from` is specified, the default value is 7 days after `from`; if `from` is not specified, the default value is the current date and time..
- `status` [query] (string): Recording's status. If not specified or `available`, retrieves recordings that are available. if specified as `purged`, retrieves recordings those are deleted but available to a compliance officer. Otherwise, if specified as `deleted`, retrieves recordings that have been moved into the recycle bin. Valores: available, deleted, purged. Por defecto: available.
- `serviceType` [query] (string): Recording's service-type. If specified, the API filters recordings by service-type. Valid values are `calling` and `customerAssist`. Valores: calling, customerAssist.
- `format` [query] (string): Recording's file format. If specified, the API filters recordings by format. Valid values are `MP3`. Valores: MP3.
- `ownerId` [query] (string): Webex user Id to fetch recordings for a particular user.
- `ownerEmail` [query] (string): Webex email address to fetch recordings for a particular user.
- `ownerType` [query] (string): Recording based on type of user. Valores: user, place, virtualLine, callQueue.
- `storageRegion` [query] (string): Recording stored in certain Webex locations. Valores: US, SG, GB, JP, DE, AU, IN, CA.
- `locationId` [query] (string): Fetch recordings for users in a particular Webex Calling location (as configured in Control Hub).
- `topic` [query] (string): Recording's topic. If specified, the API filters recordings by topic in a case-insensitive manner.
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/admin/convergedRecordings' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of recording objects.
  - `id` (string) (**requerido**): A unique identifier for the recording.
  - `topic` (string) (**requerido**): The recording's topic.
  - `createTime` (string) (**requerido**): The date and time recording was created in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. Please note that it's not the time the record button was clicked in meeting but the time the recording file was generated offline.
  - `timeRecorded` (string) (**requerido**): The date and time recording started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. It indicates when the record button was clicked in the meeting.
  - `format` (string) (**requerido**): * `MP3` - Recording file format is MP3. Valores: MP3.
  - `serviceType` (string) (**requerido**): * `calling` - Recording service type is Webex Call.  * `customerAssist` - Call Recordings of a Customer Assist Queue. Valores: calling, customerAssist.
  - `durationSeconds` (number) (**requerido**): The duration of the recording, in seconds.
  - `sizeBytes` (number) (**requerido**): The size of the recording file, in bytes.
  - `status` (string) (**requerido**): * `available` - Recording is available.  * `deleted` - Recording has been moved into recycle bin. Valores: available, deleted.
  - `ownerId` (string) (**requerido**): Webex UUID for recording owner/host.
  - `ownerEmail` (string) (**requerido**): Webex email for recording owner/host.
  - `ownerType` (string) (**requerido**): * `user` - Recording belongs to a user.  * `place` - Recording belongs to a workspace device.  * `virtualLine` - Recording belongs to a workspace device. Valores: user, place, virtualLine, callQueue.
  - `storageRegion` (string) (**requerido**): Storage location for recording within Webex datacenters.
  - `serviceData` (object): Fields relevant to each service Type.
    - `locationId` (string): Webex calling location for recording user.
    - `callSessionId` (string): Call ID for which recording was done.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "baa93e55c62e4663ae24f13fbfdb247f",
      "topic": "call with title",
      "createTime": "2023-10-31T16:24:12+08:00",
      "timeRecorded": "2023-10-31T10:41:28+08:00",
      "ownerId": "d7468402-e95f-42a9-92c8-dd65f45d40ba",
      "ownerType": "virtualLine",
      "ownerEmail": "Rbs_TA_Admin@wbxlab.us",
      "format": "MP3",
      "durationSeconds": 60,
      "sizeBytes": 244333,
      "serviceType": "calling",
      "storageRegion": "US",
      "status": "available",
      "serviceData": {
        "locationId": "US",
        "callSessionId": "7ba2967530164bf0af1966cf2854b000"
      }
    },
    {
      "id": "518cdca461c747dc840b29827d0cb62d",
      "topic": "call with title",
      "createTime": "2023-10-30T22:30:53+08:00",
      "timeRecorded": "2023-10-30T22:17:19+08:00",
      "ownerId": "d7468402-e95f-42a9-92c8-dd65f45d40ba",
      "ownerType": "virtualLine",
      "ownerEmail": "Rbs_TA_Admin@wbxlab.us",
      "format": "MP3",
      "durationSeconds": 60,
      "sizeBytes": 244326,
      "serviceType": "calling",
      "storageRegion": "US",
      "status": "available",
      "serviceData": {
        "locationId": "US",
        "callSessionId": "7ba2967530164bf0af1966cf2854b000"
      }
    }
  ]
}
```
- Cabecera `Link`: 

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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs