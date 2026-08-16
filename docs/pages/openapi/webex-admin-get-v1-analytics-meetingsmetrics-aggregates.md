---
doc_id: webex-admin-get-v1-analytics-meetingsmetrics-aggregates
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
method: GET
path: /v1/analytics/meetingsMetrics/aggregates
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.150786+00:00
---

# GET /v1/analytics/meetingsMetrics/aggregates

**API:** Webex Admin
**Área:** Historical Analytics APIs
**operationId:** `Historical Data related to Meetings`

## Resumen
Historical Data related to Meetings

## Descripción
Return aggregates of various metrics related to meetings for a given Webex site over a specified time range.

<div><Callout type="error">The base URL for these APIs is **analytics.webexapis.com**, which does not work with the **Try It** feature.</Callout></div>

## Parámetros
- `siteUrl` [query] (string) **(requerido)**: URL of the Webex site for which historical data is requested.
- `from` [query] (string): UTC Date starting from which the data needs to be returned
- `to` [query] (string): UTC Date up to which the data needs to be returned

## Respuestas
- **200**: OK
  - `siteUrl` (string): Site related to which the data is returned.
  - `startDate` (string): UTC start date of the data set.
  - `endDate` (string): UTC end date of the data set.
  - `metrics` (object):
    - `totalMeetings` (number): Total number of meetings held over the selected date range. includes Webex Meetings, Webex Events, Webex Support, and Webex Training sessions
    - `totalParticipants` (number): Total number of joins by participant and devices from all Webex meetings over the selected date range
    - `totalUniqueHosts` (number): Total number of unique hosts who started at least one webex meeting over the selected date range
    - `totalMeetingMinutes` (number): Total number of minutes for all meetings over selected date range
    - `totalAudioMinutes` (number): Total number of VoIP and telephony minutes used during meetings over the selected date range
    - `totalTelephoneMinutes` (number):
    - `totalVoIPMinutes` (number):
    - `videoMeetings` (number): Total number of meetings held where at least one participant enabled video for any amount of time
    - `sharingMeetings` (number): Total number of meetings held where at least one participant enabled sharing for any amount of time
    - `recordingMeetings` (number): Total number of meetings held where at least one participant enable recording for any amount of time
    - `participantsByJoinMethods` (object): Participant Count for each join/client type. This list is dynamic and can change
      - `webApp` (number):
      - `cloudVideoDevice` (number):
      - `mobileMeetingsApp` (number):
    - `participantsByRoles` (object): Participant Count for each Role
      - `host` (number):
      - `attendee` (number):
    - `participantsByLocation` (array): Participant Count for each Location. This is a json array of countries
      - `country` (string):
      - `totalParticipants` (number):
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
