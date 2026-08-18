---
doc_id: webex-meeting-get-meetingpreferences-sites
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /meetingPreferences/sites
operation_id: Get Site List
tags: Preferences
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.471195+00:00
---

# GET /meetingPreferences/sites

**API:** Webex Meetings
**Área:** Preferences
**operationId:** `Get Site List`

## Resumen
Get Site List

## Descripción
Retrieves the list of Webex sites that the authenticated user is set up to use.
When the admin tries to get the site list via `userEmail`, if `siteUrl` is not specified, the API searches the user ID from the admin's default site. If `siteUrl` is specified, the API searches the user ID from the specified site.

## Parámetros
- `userEmail` [query] (string): Email address for the user. This parameter is only used if the user or application calling the API has the [admin-level scopes](/docs/meetings#adminorganization-level-authentication-and-scopes). If set, the admin may specify the email of a user and the API will return the list of Webex sites for that user.
- `siteUrl` [query] (string): URL of the Webex site to query. If `siteUrl` is not specified, the query will use the default site for the admin's authorization token used to make the call.

## Ejemplo de invocación
```bash
curl -X GET '/meetingPreferences/sites' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `sites` (array) (**requerido**): Array of sites for the user. Users can have one site or multiple sites. This concept is specific to Webex Meetings. Any `siteUrl` in the site list can be assigned as user's default site with the [Update Default Site](/docs/api/v1/meeting-preferences/update-default-site) API.
  - `siteUrl` (string) (**requerido**): Access URL for the site. ***Note***: This is a read-only attribute. The value can be assigned as user's default site with the [Update Default Site](/docs/api/v1/meeting-preferences/update-default-site) API.
  - `default` (boolean) (**requerido**): Flag identifying the site as the default site. Users can list meetings and recordings, and create meetings on the default site.

### Ejemplo — respuesta 200
```json
{
  "sites": [
    {
      "siteUrl": "site1-example.webex.com",
      "default": false
    },
    {
      "siteUrl": "site2-example.webex.com",
      "default": false
    },
    {
      "siteUrl": "site3-example.webex.com",
      "default": false
    },
    {
      "siteUrl": "site4-example.webex.com",
      "default": true
    }
  ]
}
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden
  Ejemplo:
```json
{
  "message": "The server understood the request, but refused to fulfill it because the access token is missing required scopes or the user is missing required roles or licenses.",
  "errors": [
    {
      "description": "Not permitted to view or change other user's preferences."
    }
  ],
  "trackingId": "4A78EB66D02E4C78B9955AA504ECFC3D_1572666592909"
}
```
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