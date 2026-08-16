---
doc_id: webex-cloud-calling-get-telephony-voicemessages
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/voiceMessages
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.646415+00:00
---

# GET /telephony/voiceMessages

**API:** Webex Cloud Calling
**Área:** User Call Settings (2/2)
**operationId:** `listMessages`

## Resumen
List Messages

## Descripción
Get the list of all voicemail messages for the user.

## Parámetros
- `lineOwnerId` [query] (string): The ID of a user, workspace, or virtual line for which there is a secondary line on a device owned by the user invoking the API.

## Respuestas
- **200**: OK
  - `items` (array) **(requerido)**:
    - `id` (string) **(requerido)**: The message identifier of the voicemail message.
    - `duration` (number): The duration (in seconds) of the voicemail message.  Duration is not present for a FAX message.
    - `callingParty` (object) **(requerido)**:
      - `name` (string): The party's name. Only present when the name is available and privacy is not enabled.
      - `number` (string): The party's number. Only present when the number is available and privacy is not enabled. The number can be digits or a URI. Some examples for number include: `1234`, `2223334444`, `+12223334444`, `*73`, and `user@company.domain`.
      - `personId` (string): The party's person ID. Only present when the person ID is available and privacy is not enabled.
      - `placeId` (string): The party's place ID. Only present when the place ID is available and privacy is not enabled.
      - `privacyEnabled` (boolean) **(requerido)**: if `true`, denotes privacy is enabled for the name, number and `personId`/`placeId`.
    - `urgent` (boolean): `true` if the voicemail message is urgent.
    - `confidential` (boolean): `true` if the voicemail message is confidential.
    - `read` (boolean): `true` if the voicemail message has been read.
    - `faxPageCount` (number): Number of pages for the FAX.  Only set for a FAX.
    - `created` (string) **(requerido)**: The date and time the voicemail message was created.
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
