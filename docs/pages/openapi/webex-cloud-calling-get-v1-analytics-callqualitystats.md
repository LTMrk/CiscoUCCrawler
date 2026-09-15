---
doc_id: webex-cloud-calling-get-v1-analytics-callqualitystats
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /v1/analytics/callQualityStats
operation_id: getCallQualityStats
tags: Calling Metrics
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-15T08:15:48.767840+00:00
---

# GET /v1/analytics/callQualityStats

**API:** Webex Cloud Calling
**Área:** Calling Metrics
**operationId:** `getCallQualityStats`

## Resumen
Webex Calling Call Quality Stats

## Descripción
Returns aggregated Webex Calling call and media-quality statistics for the authenticated organization. A call or media session is classified as good quality when all available audio and video quality measurements meet their defined thresholds. Missing individual quality measurements do not cause the call or session to be classified as poor quality.

You can query data for a time range of up to seven days within the previous 3 weeks. For older historical data, use the Webex Calling Media Quality dashboard or reports. For more information on Media Quality KPI definitions, [click here](https://help.webex.com/en-us/article/n0rlwxe/Analytics-for-Your-Cloud-Collaboration-Portfolio#Cisco_Concept.dita_7609f9dc-3b80-4c0f-9456-5aaa385c4e27).

This operation requires a Pro Pack for Control Hub license. The access token must include the analytics:read_all scope and represent either a full administrator or read-only administrator. The organization is derived from the access token.

<div><Callout type="error">The base URL for these APIs is **analytics.webexapis.com**, which does not work with the **Try It** feature.</Callout></div>

## Parámetros
- `from` [query] (string/date-time): Inclusive UTC start time in yyyy-MM-ddTHH:mm:ssZ format. If omitted while to is provided, it is seven days before the effective to time. If both times are omitted, it is seven days before the current time.
- `to` [query] (string/date-time): Exclusive UTC end time in yyyy-MM-ddTHH:mm:ssZ format. A value later than the current time is clamped to the current time. If omitted while from is provided, it is the earlier of seven days after from and the current time. If both times are omitted, it is the current time.
- `location` [query] (string): Exact Webex Calling location name. Omit it or provide an empty value to include all locations.

## Ejemplo de invocación
```bash
curl -X GET '/v1/analytics/callQualityStats' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `startTime` (string/date-time) (**requerido**): Start of the queried interval.
- `endTime` (string/date-time) (**requerido**): End of the queried interval.
- `location` (string): Selected location, or null when all locations are included.
- `metrics` (object) (**requerido**): Call and media-quality statistics.
  - `totalCalls` (integer/int64) (**requerido**): Total calls.
  - `totalCallsWithMedia` (integer/int64) (**requerido**): Total calls with media.
  - `totalGoodQualityCallsWithMedia` (integer/int64) (**requerido**): Total good-quality calls with media.
  - `totalMediaSessions` (integer/int64) (**requerido**): Total media sessions.
  - `totalGoodMediaSessions` (integer/int64) (**requerido**): Total good-quality media sessions.
  - `avgCallLegAudioJitter` (number/double) (**requerido**): Average call-leg audio jitter in milliseconds.
  - `avgCallLegAudioLatency` (number/double) (**requerido**): Average call-leg audio latency in milliseconds.
  - `avgCallLegAudioPacketLoss` (number/double) (**requerido**): Average call-leg audio packet loss percentage.

### Ejemplo — respuesta 200
```json
{
  "startTime": "2026-08-10T12:00:00Z",
  "endTime": "2026-08-16T12:00:00Z",
  "location": "Headquarters",
  "metrics": {
    "totalCalls": 12500,
    "totalCallsWithMedia": 12000,
    "totalGoodQualityCallsWithMedia": 11400,
    "totalMediaSessions": 24000,
    "totalGoodMediaSessions": 22800,
    "avgCallLegAudioJitter": 18.4,
    "avgCallLegAudioLatency": 132.7,
    "avgCallLegAudioPacketLoss": 0.8
  }
}
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs