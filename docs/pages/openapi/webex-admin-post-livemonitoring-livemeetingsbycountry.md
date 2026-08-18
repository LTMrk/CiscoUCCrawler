---
doc_id: webex-admin-post-livemonitoring-livemeetingsbycountry
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /livemonitoring/liveMeetingsByCountry
operation_id: getLiveMeetingMetricsByCountry
tags: Live Monitoring
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.567233+00:00
---

# POST /livemonitoring/liveMeetingsByCountry

**API:** Webex Admin
**Área:** Live Monitoring
**operationId:** `getLiveMeetingMetricsByCountry`

## Resumen
Get Live Meeting metrics categorized by Country

## Descripción
Retrieve live meeting metrics categorized by country for a specific meeting site or for all meeting sites owned by the customer. 

To retrieve live monitoring information, you must use an administrator token with the `analytics:read_all` [scope](/docs/integrations#scopes). The authenticated user must be a read-only or full administrator of the organization to which the meeting belongs and must not be an external administrator.

To use this endpoint, the org needs to be licensed for the Webex Pro Pack.

A rate limit of one API call per minute applies to each customer organization

## Cuerpo de la petición (application/json)
- `siteIds` (array): A list of meeting site Ids.
- `siteUrl` (string): A site URL.

## Ejemplo de invocación
```bash
curl -X POST '/livemonitoring/liveMeetingsByCountry' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `siteUrls` (array): A list of site URLs.
- `totalLiveMeetingCount` (integer): Total number of live meetings.
- `totalLiveParticipantCount` (integer): Total number of live participants.
- `totalGoodQualityLiveMeetingCount` (integer): Total number of good quality live meetings.
- `totalGoodQualityLiveParticipantCount` (integer): Total number of good quality live participants.
- `totalBadQualityMeetingCount` (integer): Total number of bad quality meetings.
- `totalBadQualityParticipantCount` (integer): Total number of bad quality participants.
- `locations` (array): Location breakdown of live meetings.
  - `badQualityLiveMeetingCount` (integer) (**requerido**): Bad quality live meeting count.
  - `badQualityLiveParticipantCount` (integer) (**requerido**): Bad quality live participant count.
  - `goodQualityLiveMeetingCount` (integer) (**requerido**): Good quality live meeting count.
  - `goodQualityLiveParticipantCount` (integer) (**requerido**): Good quality live participant count.
  - `country` (string) (**requerido**): Country name.
  - `countryLatitude` (number) (**requerido**): Country latitude.
  - `countryLongitude` (number) (**requerido**): Country longitude.
  - `liveMeetingCount` (integer) (**requerido**): Live meeting count.
  - `liveParticipantCount` (integer) (**requerido**): Live participant count.

### Ejemplo — respuesta 200
```json
{
  "siteUrls": [
    "cisco.webex.com"
  ],
  "totalLiveMeetingCount": 3,
  "totalLiveParticipantCount": 10,
  "totalGoodQualityLiveMeetingCount": 3,
  "totalGoodQualityLiveParticipantCount": 10,
  "totalBadQualityMeetingCount": 0,
  "totalBadQualityParticipantCount": 0,
  "locations": [
    {
      "badQualityLiveMeetingCount": 0,
      "badQualityLiveParticipantCount": 0,
      "goodQualityLiveMeetingCount": 1,
      "goodQualityLiveParticipantCount": 3,
      "country": "South Korea",
      "countryLatitude": 37.55,
      "countryLongitude": 126.98333,
      "liveMeetingCount": 1,
      "liveParticipantCount": 3
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
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs