---
doc_id: webex-meeting-get-meetings-templates-templateid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetings/templates/{templateId}
operation_id: getTemplateById
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:51.524638+00:00
---

# GET /meetings/templates/{templateId}

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `getTemplateById`

## Resumen
Get a Meeting Template

## Descripción
Retrieves details for a meeting template with a specified meeting template ID.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) for time stamps in response body, defined in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default value is `UTC` if not specified.

## Parámetros
- `templateId` [path] (string) (**requerido**): Unique identifier for the meeting template being requested.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will return the meeting template that is available for that user.
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/meetings/templates/<templateId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier for meeting template.
- `name` (string) (**requerido**): Meeting template name.
- `locale` (string) (**requerido**): Meeting template locale.
- `siteUrl` (string) (**requerido**): Site URL for the meeting template.
- `templateType` (string) (**requerido**): Meeting template type.  * `meeting` - Webex meeting.  * `webinar` - Webex webinar. Valores: meeting, webinar.
- `isDefault` (boolean) (**requerido**): Whether or not the meeting template is a default template.
- `isStandard` (boolean) (**requerido**): Whether or not the meeting template is a standard template.
- `meeting` (object) (**requerido**): Meeting object which is used to create a meeting by the meeting template. Please note that the meeting object should be used to create a meeting immediately after retrieval since the `start` and `end` may be invalid quickly after generation.

### Ejemplo — respuesta 200
```json
{
  "id": "N2Q3ZWE1ZjQyYjkyMWVhY2UwNTM4NmNhMjRhZDczMGU6VS0yMDA5NzItTUMtZW5fVVM",
  "name": "Meeting template 1",
  "locale": "en_US",
  "siteUrl": "site4-example.webex.com",
  "templateType": "meeting",
  "isDefault": false,
  "isStandard": false,
  "meeting": {
    "title": "My meeting template 1",
    "agenda": "My meeting template 1 agenda",
    "password": "gugUTMY4?25",
    "start": "2021-11-09T03:19:00Z",
    "end": "2021-11-09T03:39:00Z",
    "timezone": "UTC",
    "enabledJoinBeforeHost": false,
    "joinBeforeHostMinutes": 0,
    "enableConnectAudioBeforeHost": false,
    "hostEmail": "john.andersen@example.com",
    "sendEmail": true,
    "invitees": [
      {
        "email": "brenda.song@example.com",
        "displayName": "Brenda Song",
        "coHost": false,
        "panelist": false
      },
      {
        "email": "catherine.sinu@example.com",
        "displayName": "Catherine Sinu",
        "coHost": false,
        "panelist": false
      }
    ],
    "enabledAutoRecordMeeting": false,
    "allowAnyUserToBeCoHost": false,
    "allowFirstUserToBeCoHost": false,
    "allowAuthenticatedDevices": false,
    "meetingOptions": {
      "enabledChat": true,
      "enabledVideo": true,
      "enabledPolling": false,
      "enabledNote": true,
      "noteType": "allowAll",
      "enabledFileTransfer": false,
      "enabledUCFRichMedia": false
    },
    "attendeePrivileges": {
      "enabledShareContent": true,
      "enabledSaveDocument": false,
      "enabledPrin
  ... (truncado)
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
The Webex Meetings APIs enable developers to schedule, manage, and retrieve information about Webex meetings, webinars, and events. They provide endpoints for meeting creation, participant management, recordings, transcripts, in-meeting features such as chat and closed captions, and post-meeting analytics. Common use cases include integrating meeting scheduling into calendar apps, automating follow-ups with recordings and transcripts, embedding meeting controls in custom portals, and extracting insights for compliance or productivity analysis. The APIs support both real-time and asynchronous w...

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs