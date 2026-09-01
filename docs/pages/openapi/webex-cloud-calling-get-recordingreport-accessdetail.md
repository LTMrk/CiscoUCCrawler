---
doc_id: webex-cloud-calling-get-recordingreport-accessdetail
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /recordingReport/accessDetail
operation_id: Get Recording Audit Report Details
tags: Recording Report
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.746712+00:00
---

# GET /recordingReport/accessDetail

**API:** Webex Cloud Calling
**Área:** Recording Report
**operationId:** `Get Recording Audit Report Details`

## Resumen
Get Recording Audit Report Details

## Descripción
Retrieves details for a recording audit report with a specified recording ID.

Only recording audit report details of meetings hosted by or shared with the authenticated user may be retrieved.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.

## Parámetros
- `recordingId` [query] (string) (**requerido**): A unique identifier for the recording.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin on-behalf-of scopes. If set, the admin may specify the email of a user in a site they manage and the API will return recording details of that user.
- `max` [query] (number): Maximum number of recording audit report details to return in a single page. `max` must be equal to or greater than `1` and equal to or less than `100`. Por defecto: 10.
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/recordingReport/accessDetail?recordingId=<recordingId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of recording audit report objects.
  - `recordingId` (string): A unique identifier for the recording.
  - `topic` (string): The recording's topic.
  - `name` (string): The name of the person who accessed the recording.
  - `email` (string): The email address of the person who accessed the recording.
  - `accessTime` (string): The date and time the recording was accessed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
  - `viewed` (boolean): Whether or not the recording was viewed by the person.
  - `downloaded` (boolean): Whether or not the recording was downloaded by the person.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "recordingId": "4f914b1dfe3c4d11a61730f18c0f5387",
      "topic": "Example Topic",
      "name": "John Andersen",
      "email": "john.andersen@example.com",
      "accessTime": "2020-07-13T17:05:35Z",
      "viewed": true,
      "downloaded": false
    },
    {
      "recordingId": "4f914b1dfe3c4d11a61730f18c0f5387",
      "topic": "Example Topic",
      "name": "Brenda Song",
      "email": "brenda.song@example.com",
      "accessTime": "2020-07-18T19:05:35Z",
      "viewed": false,
      "downloaded": true
    },
    {
      "recordingId": "4f914b1dfe3c4d11a61730f18c0f5387",
      "topic": "Example Topic",
      "name": "Joe Doe",
      "email": "joeDoe@example.com",
      "accessTime": "2020-08-18T19:08:33Z",
      "viewed": true,
      "downloaded": true
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